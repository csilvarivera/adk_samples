
from google.adk.agents import Agent
from .prompts import return_rewards_agent_instructions
from .tools import find_rewards




root_agent = Agent(
    model='gemini-2.0-flash-001',
    name="rewards_agent",
    instruction=return_rewards_agent_instructions(),
    tools=[find_rewards],
)
