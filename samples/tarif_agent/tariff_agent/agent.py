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
from .sub_agents.risk_mitigation_agent.agent import root_agent as risk_mitigation_agent
from .sub_agents.scenario_planning_agent.agent import root_agent as scenario_planning_agent
from .sub_agents.tariff_news_agent.agent import root_agent as tariff_news_agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    instruction="""
        You are a helpful virtual assistant helping Cymbal Retail a global retail company to understand the impact on tariffs imposed to countries in the US.
        - Greet the user .
        - If a user asks for the latest news in tariffs, use the `tariff_news_agent` to get the latest news.
        - Use the `scenario_planning_agent` tool  to understand the impact the tariffs will bring into the business and plan scenarios.
        - If a user asks for a risk mitigation strategy, then use the `risk_mitigation_agent` tool
        - Always return the responses as they where returned from the tool and format them to look clear to the end user in Markdown format. Specially tables and web citations
    """,
    tools=[AgentTool(tariff_news_agent), AgentTool(risk_mitigation_agent),AgentTool(scenario_planning_agent)],
    generate_content_config=types.GenerateContentConfig(temperature=0.01),
)
