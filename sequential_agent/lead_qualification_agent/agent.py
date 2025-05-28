from google.adk.agents import SequentialAgent

from .subagents.recommender import action_recommender_agent
from .subagents.scorer import lead_scorer_agent

# Import the subagents
from .subagents.validator import lead_validator_agent

# Create the sequential agent with minimal callback
root_agent = SequentialAgent(
    name="LeadQualificationPipeline",
    sub_agents=[lead_validator_agent, lead_scorer_agent, action_recommender_agent],
    description="A pipeline that validates, scores, and recommends actions for sales leads",
)

