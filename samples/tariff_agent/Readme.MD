# Tariff Agent with ADK!


## Overview
This project demonstrates a multi-agent system designed to understand the impact of the newly imposed US tariffs as well as the latest news and scenario planning. The system is built to interact with BigQuery & Google Search and it leverages the latest Gemini 2.5 pro.


### Prerequisites

*   **Google Cloud Account:** You need a Google Cloud account with BigQuery enabled.
*   **Python 3.9+:** Ensure you have Python 3.9 or a later version installed.


## Project Setup with Poetry

1.  **Clone the Repository:**

    ```bash
    git clone https://gitlab.com/google-cloud-ce/communities/uki-ai-ml-ce/tariff_agent_adk.git
    cd tariff_agent_adk
    ```

2.  **Create a virtual environment**

    ```
    python3.11 -m venv .venv
    ```

    This command assumes you have python 3.11 installed in your system

3.  **Activate the Virtual Environment:**

    ```
    source .venv/bin/activate
    ```

    This activates the virtual environment, allowing you to run commands within the project's environment.
    Make sure the environment is active.

### Option 1: Using uv (Recommended)

1.  **Install uv:**

    If you haven't installed `uv` yet, follow the instructions [here](https://github.com/astral-sh/uv).

2.  **Sync dependencies:**

    ```bash
    uv sync
    ```

    This command will create a virtual environment and install all dependencies defined in `pyproject.toml`.


### Option 2: Using pip

1.  **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables:**

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
    ```
5.  **Execute the developer environment:**

    ```
    adk web
    
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