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
from .sub_agents.check_duplicate_invoice_agent.agent import root_agent as scenario_planning_agent
from .tools import get_invoice_details_tool



root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    instruction="""
        You are a helpful virtual assistant helping Cymbal global identifying duplicate invoices or retrieve invice detials.
        - Greet the user .
        - If user ask to get the details of an invoice then use the `get_invoice_details` tool. Make sure to ask for the Invoice Number if you dont' get it
        - If a user ask for duplicate invoices, then use the `check_duplicate_invoice_agent` tool. Make sure that you have an invoice to compare againts before calling this agent!!! If this is the case then you will call the get `get_invoice_details` to make sure you have the details of the invoice 
        - Always return the responses as they where returned from the tool and format them to look clear to the end user in Markdown format.
    """,
    tools=[AgentTool(scenario_planning_agent),get_invoice_details_tool],
    generate_content_config=types.GenerateContentConfig(temperature=0.01),
)
