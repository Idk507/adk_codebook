from google.adk.agents import LlmAgent 

GEMINI_MODEL = "gemini-2.0-flash"

#recommender agent 
action_recommender_agent = LlmAgent(
    name = "ACtionRecommenderAgent",
    model = GEMINI_MODEL,
    instruction = """
     Based on the lead information and scoring:
    
    - For invalid leads: Suggest what additional information is needed
    - For leads scored 1-3: Suggest nurturing actions (educational content, etc.)
    - For leads scored 4-7: Suggest qualifying actions (discovery call, needs assessment)
    - For leads scored 8-10: Suggest sales actions (demo, proposal, etc.)
    
    Format your response as a complete recommendation to the sales team.
    
    Lead Score:
    {lead_score}

    Lead Validation Status:
    {validation_status}
    """,
    description="Recommends next actions based on lead qualification.",
    output_key="action_recommendation",
)