# Molecule Agent

## Overview
This project demonstrates a molecular agent designed to investigate drug or molecule properties, specifically focusing on toxicity prediction using Tx-Gemma. It leverages the latest Gemini models and integrates with Vertex AI endpoints for specialized predictions.

### Prerequisites

*   **Google Cloud Account:** You need a Google Cloud account with Vertex AI enabled.
*   **Python 3.11+:** Ensure you have Python 3.11 or a later version installed.

## Project Setup

1.  **Clone the Repository:**

    ```bash
    # Clone the repository
    ```

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

### Alternative: Install with uv (Recommended)
You can also use [uv](https://docs.astral.sh/uv/) for faster installation:

1. Install uv:
   ```bash
   pip install uv
   ```
2. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   # or if you have a pyproject.toml
   # uv pip install .
   ```
4.  **Execute the developer environment:**

    ```
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

    # Molecule Agent Configuration
    TX_GEMMA_ENDPOINT_ID='YOUR_ENDPOINT_ID'
    TX_GEMMA_ENDPOINT_REGION='us-central1'
    TX_GEMMA_PROJECT_ID='YOUR_PROJECT_ID'

    MED_GEMMA_ENDPOINT_ID='YOUR_ENDPOINT_ID'
    MED_GEMMA_ENDPOINT_REGION='us-central1'
    MED_GEMMA_PROJECT_ID='YOUR_PROJECT_ID'
    ```


6.  **Deploy to Agent engine:**

    From the root project execute 
    ```
    python -m deploy
    
    ```
    Make sure your environment variables are set. For now, the deploy.py is pointing to always create a new Agent Engine. However, you can modify the ```main``` method to either list Agent Engines or test it locally.
    TODO: Add the ability to add flags for testing 

7.  **Deploy to Gemini Enterprise:**

    Modify the environment variables in the deploy_as.sh bash file with your data:

    -  Gemini Enterprise app Id
    -  Reasoning Engine Id
    -  Agent Id 

    From the root project execute 
    ```
    sh deploy_as.sh
    
    ```
    IMPORTANT: Your prpoject needs to be allowlisted for this command to work. This functionality is still in private preview and should be use for demo purposes only