
from google.adk.agents import Agent
from .prompts import return_tariffs_news_agent_instructions
from google.adk.tools import google_search

root_agent = Agent(
    model='gemini-2.5-flash',
    name="tariff_news_agent",
    instruction=return_tariffs_news_agent_instructions(),
    tools=[google_search],
)
