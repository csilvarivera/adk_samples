# Agent Development Kit (ADK) Samples

Welcome to the ADK samples directory! This directory contains a collection of sample applications built using the Agent Development Kit. Each sample is a self-contained project designed to demonstrate a specific capability or use case of the ADK, particularly for building generative AI agents on Google Cloud.

## 📂 Available Samples

*   **`mcp_sample`**: A "Material Cost Projection" agent that integrates with Vertex AI, BigQuery, and Cloud Storage to answer questions about material costs.
*   **`tariff_agent`**: An intelligent agent that monitors, analyzes, and provides insights on tariffs using specialized sub-agents for news monitoring and scenario planning.

*(Add more samples to this list as they are created!)*

## 🚀 Getting Started with a Sample

Each sample is a standalone project. To run a sample, follow these general steps.

### 1. Navigate to the Sample Directory

Change your directory to the specific sample you want to run. For example:

```sh
cd mcp_sample
```

### 2. Set Up the Environment

It is highly recommended to use a Python virtual environment to manage dependencies for each sample.

```sh
# Create a virtual environment
python -m venv venv

# Activate the environment
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

Each sample includes its own `requirements.txt` file. Install the necessary packages using pip:

```sh
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Most samples require you to set up environment variables for things like API keys and cloud project configuration.

1.  Look for an `.env-example` file in the sample's directory.
2.  Create a copy of this file and name it `.env`.
    ```sh
    cp .env-example .env
    ```
3.  Open the new `.env` file and fill in the required values (e.g., your Google Cloud Project ID, BigQuery dataset, etc.).

### 5. Run the Sample

Each sample will have its own main script to execute. Please refer to the specific `README.md` inside each sample's folder for detailed instructions on how to run it.

---

We hope these samples help you get started with building your own powerful agents with the ADK!
