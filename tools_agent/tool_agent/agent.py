from google.adk.agents import Agent 
from google.adk.tools import google_search 

#builtin tools
root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - google_search
    """,
    tools=[google_search],
    # tools=[get_current_time],
   
)

# #function calling 
# from datetime import datetime

# def get_current_time() :
#     return { 
#         " current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
#         }

# root_agent = Agent(
#     name = "tool_agent",
#     model = "gpt-4",
#     description = "Tool agent that can use get_current_time to answer questions.",
#     tools = [get_current_time],
#     instruction = """
#     You are helpful assistant that can use the following tools :
#     -get_current_time
#     """
# )