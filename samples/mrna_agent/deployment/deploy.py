"""Deployment script for MRNA."""

import os
import sys

from dotenv import load_dotenv
from agent import root_agent
import vertexai
from vertexai import agent_engines
from vertexai.preview.reasoning_engines import ADKApp


RELEASE_VERSION="google_adk-0.0.2.dev20250404+nightly743987168"
WHL_FILE = f"{RELEASE_VERSION}-py3-none-any.whl"

load_dotenv()

PROJECT_ID = "csilvariverademo"
LOCATION="us-central1"
STAGING_BUCKET="gs://csr-demo-bucket-agents"
# PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
# LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION")
# STAGING_BUCKET = os.getenv("STAGING_BUCKET")
print("Project ID:", PROJECT_ID)
print("Location:", LOCATION)
print("Staging bucket:", STAGING_BUCKET)
if not PROJECT_ID or not LOCATION or not STAGING_BUCKET:
  print(
      "Missing GOOGLE_CLOUD_PROJECT, GOOGLE_CLOUD_LOCATION, or STAGING_BUCKET",
      file=sys.stderr,
  )
  sys.exit(1)

vertexai.init(
  project=PROJECT_ID,
  location=LOCATION,
  staging_bucket=STAGING_BUCKET,
)

app = ADKApp(
    agent=root_agent, enable_tracing=True
)

# A local test run before deploy
session = app.create_session(user_id="test_user")
for event in app.stream_query(
    user_id=session.user_id,
    session_id=session.id,
    message="Double check this: Earth is closer to the Sun than Venus.",
):
  print(event)

# Deploy to AgentEngine - Check Cloud Logging for detailed issues.
remote_app = agent_engines.create(
    root_agent,
    requirements=[
        WHL_FILE,
        "google-cloud-aiplatform[agent_engines] @ git+https://github.com/googleapis/python-aiplatform.git@copybara_738852226",
    ],
    extra_packages=[
        WHL_FILE   ],
)
