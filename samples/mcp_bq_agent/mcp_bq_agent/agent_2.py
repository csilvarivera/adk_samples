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

from datetime import date

from google.genai import types

from google.adk.agents import Agent
from google.adk.tools import load_artifacts

date_today = date.today()

the_mirror_agent = Agent(
    name="the_mirror_agent",
    description="translate",
    model="gemini-2.0-flash-001",
    instruction="""
     You are translating headlines to spanish for the Mirror publication.
     - Don't greet the user
     - Ask for the headline to translate
     - Once you have the headline ask to what flavour of Spanish you want to translate to
     - Keep the tone as in the original headline and make it expressive to represent the Express publication

""",
)

the_express_agent = Agent(
    name="the_express_agent",
    description="get license details",
    model="gemini-2.0-flash-001",
    instruction="""
     You are translating headlines to spanish for the Express publication.
     - Don't greet the user
     - Ask for the headline to translate
     - Once you have the headline ask to what flavour of Spanish you want to translate to
     - Keep the tone as in the original headline and make it expressive to represent the Express publication
""",
)

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='root_agent',
    instruction="""
    You are an expert translator of news headlines
        - Greet the customer
        - Ask which publication are we talking to. The only valid options are [The Mirror, The express]. Don't answer fo any other publication
        - Use `the_mirror_agent` or `the_express_agent` to translate the headline depending on the publication.
        
    """,
    sub_agents=[the_mirror_agent, the_express_agent],
    generate_content_config=types.GenerateContentConfig(temperature=0.01),
)
