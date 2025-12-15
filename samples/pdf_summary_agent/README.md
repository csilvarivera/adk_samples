# PDF Summary Agent

## Overview

This project demonstrates a PDF Summary Agent designed to summarize user documents. It leverages Gemini models to generate a comprehensive summary including Title, Summary, Table of Contents, Body, and Conclusion.

**Key Feature:** This project highlights how to upload files into Gemini Enterprise using the `load_artifacts` tool provided by the Agent Development Kit (ADK). This tool allows the agent to ingest and process user-provided files seamlessly.

### Prerequisites

*   **Google Cloud Account:** You need a Google Cloud account with Vertex AI enabled.
*   **Python 3.11+:** Ensure you have Python 3.11 or a later version installed.

## Project Setup

1.  **Clone the Repository:**
    (You are already in the repository)

### Option 1: Using uv (Recommended)

2.  **Install uv:**

    If you haven't installed `uv` yet, follow the instructions [here](https://github.com/astral-sh/uv).

3.  **Sync dependencies:**

    ```bash
    uv sync
    ```

    This command will create a virtual environment and install all dependencies defined in `pyproject.toml`.

### Option 2: Using pip

2.  **Create a virtual environment:**

    ```bash
    python3.11 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute the developer environment:**

    ```bash
    adk web
    ```

## Configuration

1.  **Set up Environment Variables:**

    Rename the file ".env-example" (if available) or create a ".env" file.
    Fill the below values:

    ```bash
    # Choose Model Backend: 0 -> ML Dev, 1 -> Vertex
    GOOGLE_GENAI_USE_VERTEXAI=1

    # Vertex backend config
    GOOGLE_CLOUD_PROJECT='YOUR_VALUE_HERE'
    GOOGLE_CLOUD_LOCATION='us-central1'

    # Agent Engine backend config - bucket for agent engine
    GOOGLE_CLOUD_STORAGE_BUCKET='YOUR_BUCKET_HERE'
    ```

2.  **Deploy to Agent engine:**

    From the root project execute 
    ```bash
    python -m deploy
    ```
    Make sure your environment variables are set. For now, the deploy.py is pointing to always create a new Agent Engine. However, you can modify the `main` method to either list Agent Engines or test it locally.

3.  **Deploy to Gemini Enterprise:**

    Modify the environment variables in the deploy_as.sh bash file with your data:

    -  Gemini Enterprise app Id
    -  Reasoning Engine Id
    -  Agent Id 

    From the root project execute 
    ```bash
    sh deploy_as.sh
    ```
    IMPORTANT: Your project needs to be allowlisted for this command to work. This functionality is still in private preview and should be use for demo purposes only.
