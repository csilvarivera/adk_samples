
from google.adk.agents import Agent
from .prompts import return_membership_agent_instructions
from .tools import create_customer_id,update_user_info


root_agent = Agent(
    model='gemini-2.5-flash',
    name="membership_agent",
    instruction=return_membership_agent_instructions(),
    tools=[create_customer_id],
    
)
