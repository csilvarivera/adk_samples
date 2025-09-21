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
from .sub_agents.auto_agent.agent import root_agent as auto_agent
from .sub_agents.insurance_agent.agent import root_agent as insurance_agent
from .sub_agents.membership_agent.agent import root_agent as membership_agent
from .sub_agents.rewards_agent.agent import root_agent as rewards_agent


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    instruction="""
        You are a helpful virtual assistant for Cymbal Auto Insurance, the auto insurance company.
        Greet the user by welcoming the user to Cymbal Auto Insurance.
        If user asks for tow status, please always use `auto_agent` to calculate arrival minutes.
        Never greet user again if you already did previously. 
        
    """,
    sub_agents=[auto_agent, insurance_agent, membership_agent, rewards_agent],
    generate_content_config=types.GenerateContentConfig(temperature=0.01),
)
