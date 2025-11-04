"""Deployment script for MRNA."""

import os
import sys

# Now use an absolute import from the project root
import vertexai
from vertexai import agent_engines
from vertexai.preview import reasoning_engines
from dotenv import load_dotenv
from pdf_summary_agent.agent import root_agent


# load the environment
load_dotenv()

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION")
GOOGLE_CLOUD_STORAGE_BUCKET = os.getenv("GOOGLE_CLOUD_STORAGE_BUCKET")


print("Project ID:", PROJECT_ID)
print("Location:", LOCATION)
print("Staging bucket:", GOOGLE_CLOUD_STORAGE_BUCKET)
if not PROJECT_ID or not LOCATION or not GOOGLE_CLOUD_STORAGE_BUCKET:
  print(
      "Missing GOOGLE_CLOUD_PROJECT, GOOGLE_CLOUD_LOCATION, or STAGING_BUCKET",
      file=sys.stderr,
  )
  sys.exit(1)

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=GOOGLE_CLOUD_STORAGE_BUCKET,
)

def test_local_agent():
  
  # create a local version of your root agent
  app = reasoning_engines.AdkApp(
    agent=root_agent,
    enable_tracing=True,
  )

  
  session = app.create_session(user_id="u_123")
  session
  for event in app.stream_query(
    user_id="u_123",
    session_id=session.id,
    message="whats the weather in new york",
  ):
    print(event)

def deploy_agent():
  # Deploy to AgentEngine - Check Cloud Logging for detailed issues.
  remote_agent = agent_engines.create(
      root_agent,
          requirements=[
        "google-cloud-aiplatform[agent_engines]",
        "google-adk(>=1.14.1, <1.15.0)",
        "google-cloud-storage",
        "pandas",
        "db_dtypes",
        "cloudpickle",
        "pydantic",
        "dotenv",
        "markdown-pdf"
      ],
       extra_packages= ["pdf_summary_agent/agent.py", 
      ],
      display_name="pdf_summarisation_agent "
  )
  print(f"\nSuccessfully created agent: {remote_agent.resource_name}")

def update_agent():
   # Change to your agent engine ID
    agent_engines.update(
    resource_name="projects/774298971519/locations/us-central1/reasoningEngines/233329561553600512",                    # Required.
    requirements=[
        "google-cloud-aiplatform[agent_engines]",
        "google-adk(>=1.14.1, <1.15.0)",
        "google-cloud-storage",
        "pandas",
        "db_dtypes",
        "cloudpickle",
        "pydantic",
        "dotenv",
        "markdown-pdf"
      ],
       extra_packages= ["smd_resistor_abtester_agent/agent.py",
                        "smd_resistor_abtester_agent/tools/" 
      ],
      display_name="pdf_summarisation_agent "
)
  
  
def list_agents():
  for agent in agent_engines.list():
    print(agent.display_name)

def call_agent():
  # Change to your agent engine ID
  AGENT_ENGINE_ID="projects/774298971519/locations/us-central1/reasoningEngines/2881674840866029568"
  agent = agent_engines.get(AGENT_ENGINE_ID)

  remote_session = agent.create_session(user_id="u_123")
  print (f" calling agent {AGENT_ENGINE_ID} with session {remote_session['id']}")
  for event in agent.stream_query(
    user_id="u_123",
    session_id=remote_session['id'],
    # session_id="5286711940846977024",
    message="Give me the details of an invoice",
  ):
    print(event)

  # print (agent.operation_schemas())
if __name__ == "__main__":
    try:
        
        # Call the deployment function with the obtained values
        deploy_agent()
        # update_agent()
        print("\nDeployment script finished.")
        #call_agent()

    except (ValueError, FileNotFoundError) as e: # Catch specific known errors
         print(f"Configuration Error: {e}", file=sys.stderr)
         sys.exit(1)
    except Exception as e: # Catch any other unexpected errors during the process
        print(f"Script execution failed: {e}", file=sys.stderr)
        sys.exit(1)
