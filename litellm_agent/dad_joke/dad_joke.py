import os 
import random 

from google.adk.agents import Agent 
from google.adk.models.lite_llm import LiteLlm

model = LiteLlm(
    model = "openrouter/openai/gpt-4.1",
    api_key = os.getenv("OPENROUTER_API_KEY")
)

def get_dad_joke():
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I used to play piano by ear, but now I use my hands.",
        "What do you call fake spaghetti? An impasta!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call cheese that isn't yours? Nacho cheese!"
    ]
    return random.choice(jokes)

root_agent = Agent(
    name = "dad_joke",
    model = model,
    description = "A helpful assistant that can tell dad jokes.",
    tools = [get_dad_joke],
    instruction = """
    You are a helpful assistant that can tell dad jokes.only use the tool get_dad_joke to tell jokes
    """
)
