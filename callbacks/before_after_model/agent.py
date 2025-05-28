import copy 
from datetime import datetime 
from typing import Optional
from google.adk.agents import LlmAgent
from google.adk.agents.callback_context import CallbackContext 
from google.adk.models import LlmRequest,LlmResponse 
from google.genai import types

def before_model_callback(callback_context : CallbackContext,llm_request : LlmResponse) -> Optional[LlmResponse]:
    state = callback_context.state #session state 
    agent_name = callback_context.agent_name 

    #extract the last user message 
    last_user_message = ""
    if llm_request.contents and len(llm_request.contents) > 0:
        for content in reversed(llm_request.contents):
            if content.role == "user" and content.parts and len(content.parts) > 0:
                if hasattr(content.parts[0], "text") and content.parts[0].text:
                    last_user_message = content.parts[0].text
                    break
    print("Model request started")
    print(f"Agent : {agent_name}")
    if last_user_message : 
        print(f"User Message : {last_user_message}") 
    else: 
        print("User message : Emptty") 

    #check for inappropriate content 
    if last_user_message and "sucks" or "fuck" in last_user_message.lower():
        print("Before model ,Request blocked due to inappropriate content")
        return LlmResponse(
            content = types.Content(
                role = "model",
                parts = [
                    types.Part(
                        text = "I cannot respond to the messages containing inappropriate language"
                        "Please rephrase your request without using such words"
                    )
                ],
            )
        )          
    print("Before model callback processing request")
    state["model_start_time"] = datetime.now()  # record start time
    print(f"Request start time: {state['model_start_time'].strftime('%Y-%m-%d %H:%M:%S')}")
    return None


def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    if not llm_response or not llm_response.content or not llm_response.content.parts:
        return None

    # Extract text from the response
    response_text = ""
    for part in llm_response.content.parts:
        if hasattr(part, "text") and part.text:
            response_text += part.text

    if not response_text:
        return None

    # Simple word replacements
    replacements = {
        "problem": "challenge",
        "difficult": "complex",
    }

    # Perform replacements
    modified_text = response_text
    modified = False

    for original, replacement in replacements.items():
        if original in modified_text.lower():
            modified_text = modified_text.replace(original, replacement)
            modified_text = modified_text.replace(
                original.capitalize(), replacement.capitalize()
            )
            modified = True

    # Return modified response if changes were made
    if modified:
        print("[AFTER MODEL] ↺ Modified response text")

        modified_parts = [copy.deepcopy(part) for part in llm_response.content.parts]
        for i, part in enumerate(modified_parts):
            if hasattr(part, "text") and part.text:
                modified_parts[i].text = modified_text

        return LlmResponse(content=types.Content(role="model", parts=modified_parts))

    # Return None to use the original response
    return None


root_agent = LlmAgent(
    name="content_filter_agent",
    model="gemini-2.0-flash",
    description="An agent that demonstrates model callbacks for content filtering and logging",
    instruction="""
    You are a helpful assistant.
    
    Your job is to:
    - Answer user questions concisely
    - Provide factual information
    - Be friendly and respectful
    """,
    before_model_callback=before_model_callback,
    after_model_callback=after_model_callback,
)   