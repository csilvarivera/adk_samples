# ADK Lab: Code Assistant Agent

This sample demonstrates a multi-agent system built using the Google Agent Development Kit (ADK). The core component is the **Code Assistant Agent**, designed to help developers debug code errors by leveraging a variety of specialized tools and sub-agents.

## Architecture

The system follows a hierarchical agent architecture where a root agent (`code_assist_agent`) orchestrates several specialized components:

![ADK Lab Architecture](adk_lab_arch.png)

### Components

1.  **Code Assistant Agent (Root Agent)**: The main interface for users. It analyzes queries, manages context from uploaded files, and delegates tasks to specialized tools.
2.  **Specialized Tools & Agents**:
    *   **Bug Database Tool**: Searches a BigQuery database for known bug patterns and solutions.
    *   **Code Manual Tool**: Uses Vertex AI Search to consult documentation and manuals.
    *   **Stack Exchange Agent (Sub-agent)**: An A2A (Agent-to-Agent) component that retrieves relevant logs and discussions from Stack Overflow and Stack Exchange.
    *   **GitHub Agent (Sub-agent)**: An A2A component that can query repositories, issues, and pull requests.
    *   **Google Drive Upload Tool**: Saves the session information and combined user context to Google Drive.
    *   **Load Artifacts**: Integrated ADK tool to obtain the content of any uploaded files (text or images) for enhanced context.

## Setup

### 1. Prerequisites
- A Google Cloud Project with the following APIs enabled:
    - Vertex AI API
    - BigQuery API
    - Google Drive API
    - Cloud Storage API
- Python 3.10+ installed.

### 2. Environment Variables
Create a `.env` file in the `samples/adk_lab` directory with the following variables:

```env
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
GOOGLE_CLOUD_STORAGE_BUCKET=your-bucket-name
MAIN_MODEL=gemini-2.5-pro
GITHUB_AGENT_URL=https://... (URL of your GitHub A2A agent)
STACKEXCHANGE_AGENT_URL=https://... (URL of your StackExchange A2A agent)
```

### 3. Install Dependencies
Install the required packages using pip:

```bash
pip install -e .
```

Alternatively, if you are in the `samples/` directory, you can run:
```bash
pip install -r adk_lab/requirements_cloudrun.txt
```

## Running the Agent

### Local Execution
To run the agent locally with a test query:

```bash
python -m adk_lab
```

This will trigger the default query defined in `__main__.py`, which demonstrates the interaction with the Stack Exchange tool.

### Deployment to Vertex AI
To deploy the agent to the Vertex AI Agent Engine:

```bash
python adk_lab/deploy.py
```

This script will package the agent, upload dependencies, and create a Reasoning Engine instance in your Google Cloud Project.

## Project Structure

- `__main__.py`: Local entry point for testing the agent.
- `deploy.py`: Script to deploy the agent to Vertex AI.
- `code_assistant/agent.py`: Definition of the root `code_assist_agent`.
- `tools/`: Implementations of the various tools (Bug DB, GDrive, etc.).
- `github_call.py` / `stack_exchange_call.py`: A2A wrappers for the sub-agents.
- `adk_lab_arch.png`: Architecture diagram.
