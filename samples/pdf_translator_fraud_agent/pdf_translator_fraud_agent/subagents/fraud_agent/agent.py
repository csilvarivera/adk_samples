import os
from google.adk.agents import LlmAgent
from google.adk.tools import ToolContext
from google.adk.tools.load_artifacts_tool import load_artifacts_tool
from .prompts import return_fraud_agent_instructions

root_agent = LlmAgent(
    model='gemini-2.5-pro',
    name="fraud_agent",
    
    description = "Fraud Agent for Bupa's Cross-Border Claims Fraud System.", 
    instruction =  return_fraud_agent_instructions(),

    tools = [load_artifacts_tool]
)