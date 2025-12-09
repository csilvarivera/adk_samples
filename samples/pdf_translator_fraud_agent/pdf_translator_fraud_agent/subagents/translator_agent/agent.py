import os
from google.adk.agents import LlmAgent
from google.adk.tools import ToolContext
from google.adk.tools.load_artifacts_tool import load_artifacts_tool


root_agent = LlmAgent(
    model='gemini-2.5-pro',
    name="translator_agent",
    
    description = "Translator Agent for Bupa's Cross-Border Claims Fraud System.", 
    instruction = """
    ## Persona ##
    You are the Translator Agent for Bupa's Cross-Border Claims Fraud System.

    ## Instruction ##
    **Follow the steps mentioned as-it is**

    **Steps to be followed**
    - STEP 1 - call the `load_artifacts_tool` to load the file the user has uploaded
    - STEP 2 - Translate the document to English 
    
    """,
    tools = [load_artifacts_tool]
)