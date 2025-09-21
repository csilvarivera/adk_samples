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

from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from google.adk.agents import RunConfig
from google.genai import types as genai_types


voice_config = genai_types.VoiceConfig(
    prebuilt_voice_config=genai_types.PrebuiltVoiceConfigDict(
        voice_name='Aoede'
    )
)
speech_config = genai_types.SpeechConfig(voice_config=voice_config)
run_config = RunConfig(
    speech_config=speech_config,
    response_modalities=['AUDIO','TEXT'],
)


root_agent = LlmAgent(
   name="basic_search_agent",
   model="gemini-2.0-flash-live-preview-04-09", ### model that supports live streaming
   description="Agent to answer questions using Google Search.",
   instruction="You are an expert researcher. You always stick to the facts.",
   tools=[google_search],

)

