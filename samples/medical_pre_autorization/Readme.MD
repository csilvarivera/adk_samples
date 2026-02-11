# Medical Pre-Authorization Agent with ADK!


## Overview
This project demonstrates a multi-agent system designed to streamline the medical pre-authorization process. The system extracts relevant clinical data from medical records and insurance policy documents to determine if a requested medical procedure meets specific coverage criteria. It leverages the latest Gemini models and Google ADK for orchestration.


### Prerequisites

*   **Google Cloud Account:** You need a Google Cloud account with a project and billing enabled.
*   **Vertex AI Search:** Ensure you have the necessary Vertex AI Search and Conversation APIs enabled if using RAG features.
*   **Python 3.9+:** Ensure you have Python 3.9 or a later version installed.
*   **UV (Recommended):** We recommend using [uv](https://github.com/astral-sh/uv) for fast and reliable dependency management.


## Project Setup

We recommend using `uv` for easy setup and fast dependency management.

1.  **Install uv (if not already installed):**
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
    Alternatively, on macOS: `brew install uv`

2.  **Create a Virtual Environment and Install Dependencies:**
    ```bash
    uv venv
    source .venv/bin/activate
    uv pip install -e .
    ```

### Alternative: Standard Python venv

If you prefer not to use `uv`, you can use the standard `venv` module:

1.  **Create a virtual environment:**
    ```bash
    python3 -m venv .venv
    ```

2.  **Activate the Virtual Environment:**
    ```bash
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -e .
    ```
5.  **Set up Environment Variables:**

    Rename the file ".env-example" to ".env"
    Fill the below values:

    ```bash
    # Choose Model Backend: 0 -> ML Dev, 1 -> Vertex
    GOOGLE_GENAI_USE_VERTEXAI=1

    # ML Dev backend config. Fill if using Ml Dev backend.
    GOOGLE_API_KEY='YOUR_VALUE_HERE'

    # Vertex backend config
    GOOGLE_CLOUD_PROJECT='YOUR_VALUE_HERE'
    GOOGLE_CLOUD_LOCATION='YOUR_VALUE_HERE'

    # Agent Engine backend config - bucket for agent engine
    GOOGLE_CLOUD_STORAGE_BUCKET='YOUR_VALUE_HERE'
    
6.  **Execute the developer environment:**

    ```
    adk web
    
    ```

7.  **Deploy to Agent engine:**

    From the root project execute 
    ```
    python -m deploy
    
    ```
    Make sure your environment variables are set. For now, the deploy.py is pointing to always create a new Agent Engine. However, you can modify the ```main``` method to either list Agent Engines or test it locally.
    TODO: Add the ability to add flags for testing 

8.  **Deploy to Agentspace:**

    Modify the environment variables in the deploy_as.sh bash file with your data:

    -  Agentspace app Id
    -  Reasoning Engine Id
    -  Agent Id 

    From the root project execute 
    ```
    sh deploy_as.sh
    
    ```
    IMPORTANT: This functionality is still in  preview and should be use for test purposes only