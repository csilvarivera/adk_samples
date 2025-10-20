from google.adk.sessions import VertexAiSessionService
from google.genai import types
from ..financial_advisor.agent import root_agent
from dotenv import load_dotenv
import google.adk as adk
import os


app_name="projects/774298971519/locations/us-central1/reasoningEngines/1946210347954208768"
user_id="csilva@google.com"
# load the environment
load_dotenv()

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION")

# Create the ADK runner with VertexAiSessionService
session_service = VertexAiSessionService(
       PROJECT_ID, LOCATION)
runner = adk.Runner(
    agent=root_agent,
    app_name=app_name,
    session_service=session_service)

# Helper method to send query to the runner
def call_agent(query, session_id, user_id):
  content = types.Content(role='user', parts=[types.Part(text=query)])
  events = runner.run(
      user_id=user_id, session_id=session_id, new_message=content)

  for event in events:
      if event.is_final_response():
          final_response = event.content.parts[0].text
          print("Agent Response: ", final_response)


