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

from google.adk.agents import LlmAgent
from google.adk.tools import load_artifacts

date_today = date.today()

# x_ray_agent = Agent(
#     name="x_ray_agent",
#     description="Understand X-Ray to help practicioners identifying torax condition like pulmonar cancer",
#     model="gemini-2.0-flash-001",
#     instruction="""
#         You are a specialized medical assistant that understand X-Ray and can assess conditions like pulmonar cancer. You are working at Cymbal Health helping practictioners.
#         - Do not greet user.
#         - Collect the patient X-Ray by asking the end user to upload a picture of the X-Ray they need help with. You will use this picture to the patient condition.
#         - Analyse the image and give your expert opinion and always be helful
#         - Always provide the user with answers 
#         - If user asks for causes for disease then check with other child agents,
#             - After you addressed questions, ask user if continue to something else?

# """,
# )

# root_agent = Agent(
#     model='gemini-2.5-flash',
#     name='root_agent',
#     instruction="""
#    You are a helpful assistant working for Cymbal Health helping doctors and pracitioners to better understand symptoms and chest X-Rays 
#     If user ask to know about or need help with a X-Ray then use the "x_ray_agent"
#     Never greet user again if you already did previously.
#     """,
#     generate_content_config=types.GenerateContentConfig(temperature=0.01),
# )
# Replace with your actual Vertex AI Endpoint resource name
med_gemma_endpoint = "projects/cloud-llm-preview2/locations/us-central1/endpoints/8692583898057539584"

root_agent = LlmAgent(
    model=med_gemma_endpoint,
    name="med_gemma_agent",
    instruction="You are an expert radiologist..",
)