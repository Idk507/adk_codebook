Sessions and State Management in ADK
This example demonstrates how to create and manage stateful sessions in the Agent Development Kit (ADK), enabling your agents to maintain context and remember user information across interactions.

What Are Sessions in ADK?
Sessions in ADK provide a way to:

Maintain State: Store and access user data, preferences, and other information between interactions
Track Conversation History: Automatically record and retrieve message history
Personalize Responses: Use stored information to create more contextual and personalized agent experiences
Unlike simple conversational agents that forget previous interactions, stateful agents can build relationships with users over time by remembering important details and preferences.

Example Overview
This directory contains a basic stateful session example that demonstrates:

Creating a session with user preferences
Using template variables to access session state in agent instructions
Running the agent with a session to maintain context
The example uses a simple question-answering agent that responds based on stored user information in the session state.

Project Structure
5-sessions-and-state/
│
├── basic_stateful_session.py      # Main example script
│
└── question_answering_agent/      # Agent implementation
    ├── __init__.py
    └── agent.py                   # Agent definition with template variables