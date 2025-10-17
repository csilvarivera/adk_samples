# Duplicate Invoice Agent with ADK!


## Overview
This project demonstrates a multi-agent system designed to retrieve invoice detials and performs duplicate invoice checks. The system is built to interact with BigQuery & Google Search and it leverages the latest Gemini 2.5 pro.


### Prerequisites

*   **Google Cloud Account:** You need a Google Cloud account with BigQuery enabled.
*   **Python 3.9+:** Ensure you have Python 3.9 or a later version installed.


## Project Setup with Poetry

1.  **Clone the Repository:**

    ```bash
   
    ```

1.  **Create a virtual environment**

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

4.  **Install dependencies:**
    ```
    pip install -r requirements.txt
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

    # BigQuery config
    BIGQUERY_DATASET='YOUR_VALUE_HERE'
    BIGQUERY_PROJECT='YOUR_VALUE_HERE'
    BIGQUERY_TABLE='YOUR_VALUE_HERE'
    ```
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
    IMPORTANT: Your prpoject needs to be allowlisted for this command to work. This functionality is still in private preview and should be use for demo purposes only