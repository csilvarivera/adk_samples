"""Deployment script for bq_agent."""

import os
import sys

# Now use an absolute import from the project root
import vertexai
from vertexai import agent_engines
from vertexai.preview import reasoning_engines
from dotenv import load_dotenv
from bq_agent.agent import root_agent


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

def deploy_agent():
  # Deploy to AgentEngine - Check Cloud Logging for detailed issues.
  remote_agent = agent_engines.create(
      root_agent,
        requirements=[
        "google-cloud-aiplatform[agent_engines]",
        "google-adk(>=1.18.1, <1.19.0)",
        "db_dtypes",
        "cloudpickle",
        "pydantic",
        "dotenv"
      ],
      display_name="bq_agent"
  )
  print(f"\nSuccessfully created agent: {remote_agent.resource_name}")

  
  # print (agent.operation_schemas())
if __name__ == "__main__":
    try:
        
        # Call the deployment function with the obtained values
        deploy_agent()
        print("\nDeployment script finished.")

    except (ValueError, FileNotFoundError) as e: # Catch specific known errors
         print(f"Configuration Error: {e}", file=sys.stderr)
         sys.exit(1)
    except Exception as e: # Catch any other unexpected errors during the process
        print(f"Script execution failed: {e}", file=sys.stderr)
        sys.exit(1)
