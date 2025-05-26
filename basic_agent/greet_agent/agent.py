from google.adk.agents import Agent 

root_agent = Agent(
    name= "greet_agent",
    model = "gemini-2.0-flash",
    description = "greet agent",
    instruction = """
    You are a friendly agent that greets users warmly.
    Ask for the user's name and greet them by name.
    """,
)
