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
"""
from google.genai import types

from google.adk.agents import Agent
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from .prompts import return_duplicate_invoice_agent_instructions
from .sub_agents.check_duplicate_invoice_agent.agent import root_agent as duplicate_invoice_check
from .tools import get_invoice_details_tool
from .tools import reverse_invoice_tool




root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    instruction=return_duplicate_invoice_agent_instructions(),
    
    tools=[AgentTool(duplicate_invoice_check),
           get_invoice_details_tool,
           reverse_invoice_tool],
    generate_content_config=types.GenerateContentConfig(temperature=0.01),
)
