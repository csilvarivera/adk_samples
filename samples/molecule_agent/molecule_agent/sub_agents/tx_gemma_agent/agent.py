from google.genai import types
from google.adk.agents import Agent
from .tools import get_tx_gemma_toxicity
from .prompts import return_tx_gemma_agent_instructions

root_agent = Agent(
    model='gemini-2.5-pro',
    name='tx_gemma_agent',
    instruction=return_tx_gemma_agent_instructions(),
    tools=[get_tx_gemma_toxicity],
    generate_content_config=types.GenerateContentConfig(temperature=0.01),
)
