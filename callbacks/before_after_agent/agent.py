from datetime import datetime 
from typing import Optional

from google.adk.agents import LlmAgent 
from google.adk.agents.callback_context import CallbackContext 
from google.genai import types


def before_agent_callback(callback_context : CallbackContext) -> Optional[types.Content] :

    state = callback_context.state  #session state 
    timestamp = datetime.now() #record timestamp 
    if "agent_name" not in state :
        state["agent_name"] = "Simplechatbot" #set agent name 
    
    if "request_counter" not in state : 
        state["request_counter"] = 1
    else : 
        state["request_counter"] += 1

    state["request_start_time"] = timestamp 

    print("Agent execution started")
    print(f"Request: {state['request_counter']}")
    print(f"Timestamp : {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

    print(f"Before Callback ,Agent processing request {state['request_counter']}")


def after_agent_callback(callback_context : CallbackContext) -> Optional[types.Content] : 
    state = callback_context.state 


    timestamp = datetime.now()  # record timestamp
    duration = None 
    if "request_start_time" in state :
        duration = (timestamp - state['request_start_time']).total_seconds()
    
    print("Agent execution completed")
    print(f"Request: {state.get('request_start_time','Unknown')}")

    if duration is not None :
        print(f"After callback processing took {duration: .2f} seconds")

    return None 

root_agent = LlmAgent(
    name = "before_after_agent",
    model = "gemini-2.0-flash",
    description = "A basic agent that demostrates before and after agent callbacks",
    instructions = """
      You are a friendly greeting agent. Your name is {agent_name}.
    
    Your job is to:
    - Greet users politely
    - Respond to basic questions
    - Keep your responses friendly and concise
    """,
    before_agent_callback=before_agent_callback,
    after_agent_callback=after_agent_callback,
)