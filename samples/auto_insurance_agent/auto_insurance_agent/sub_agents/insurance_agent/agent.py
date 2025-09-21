
from google.adk.agents import Agent
from .prompts import return_insurance_agent_instructions
from .tools import file_claim




root_agent = Agent(
    model='gemini-2.5-pro',
    name="insurance_agent",
    instruction=return_insurance_agent_instructions(),
    tools=[file_claim],
)
