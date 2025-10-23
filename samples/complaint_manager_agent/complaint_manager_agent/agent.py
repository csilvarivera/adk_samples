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
from .prompts import return_complaint_manager_agent_instructions
from .tools import get_open_complaints_last_7_days
from .tools import get_total_complaints_by_status
from .tools import get_complaints_by_customer_id
from .tools import get_complaint_details
from .tools import update_complaint_details


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    instruction=return_complaint_manager_agent_instructions(),
    tools=[
           get_open_complaints_last_7_days,
           get_total_complaints_by_status,
           get_complaints_by_customer_id,
           get_complaint_details,
           update_complaint_details],
    generate_content_config=types.GenerateContentConfig(temperature=0.01),
)
