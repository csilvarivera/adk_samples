from google.adk.agents import Agent
from .prompts import return_symptom_agent_instructions
from .tools import get_med_gemma_response



root_agent = Agent(
    model='gemini-2.5-pro',
    name="symptom_agent",
    instruction=return_symptom_agent_instructions(),
    tools=[get_med_gemma_response]
)
