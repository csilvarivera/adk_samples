
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from .prompts import return_auto_agent_instructions
from .tools import create_tow_id, check_tow_status
from auto_insurance_agent.sub_agents.membership_agent.agent import root_agent as membership_agent



root_agent = Agent(
    model='gemini-2.5-flash',
    name="auto_agent",
    instruction=return_auto_agent_instructions(),
    tools=[create_tow_id, check_tow_status, AgentTool(membership_agent)],
)
