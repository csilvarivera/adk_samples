# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Top level agent for data agent multi-agents.

-- it get data from database (e.g., BQ) using NL2SQL
-- then, it use NL2Py to do further data analysis as needed
"""

from google.genai import types
from google.adk.agents import Agent
from google.adk.agents import LlmAgent
from google.adk.tools import load_artifacts
from google.adk.tools.tool_context import ToolContext
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.load_artifacts_tool import load_artifacts_tool
from molecule_agent.tools import get_similar_molecules
from molecule_agent.sub_agents.tx_gemma_agent.agent import root_agent as tx_gemma_agent
from molecule_agent.sub_agents.symptom_agent.agent import root_agent as symptom_agent
from molecule_agent.prompts import return_agent_instructions


from dotenv import load_dotenv
import os

# load the environment
load_dotenv()

root_agent = Agent(
    model='gemini-2.5-pro',
    name='root_agent',
    instruction=return_agent_instructions(),
    tools=[get_similar_molecules, AgentTool(tx_gemma_agent), AgentTool(symptom_agent), load_artifacts_tool],
    generate_content_config=types.GenerateContentConfig(temperature=0.01),
)
