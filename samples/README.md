# Agent Development Kit (ADK) Samples

Welcome to the ADK samples directory! This directory contains a collection of sample applications built using the Agent Development Kit. Each sample is a self-contained project designed to demonstrate a specific capability or use case of the ADK, particularly for building generative AI agents on Google Cloud.

## 📂 Available Samples

| Agent Name | Description |
| :--- | :--- |
| [adk_lab](./adk_lab) | Lab environment for ADK. |
| [auto_insurance_agent](./auto_insurance_agent) | Agent for handling auto insurance claims or queries. |
| [bq_agent](./bq_agent) | Agent interacting with BigQuery. |
| [complaint_manager_agent](./complaint_manager_agent) | Agent for managing customer complaints. |
| [duplicate_invoice_agent](./duplicate_invoice_agent) | Agent for detecting or handling duplicate invoices. |
| [financial-advisor](./financial-advisor) | Team of specialized AI agents that assists human financial advisors with market analysis and trading strategies. |
| [lab_analysis](./lab_analysis) | Agent for analyzing lab data. |
| [mcp_bq_agent](./mcp_bq_agent) | Material Cost Projection agent using BigQuery. |
| [mcp_sample](./mcp_sample) | Material Cost Projection sample agent that integrates with Vertex AI, BigQuery, and Cloud Storage. |
| [medical_agent](./medical_agent) | General medical assistant agent. |
| [medical_pre_autorization](./medical_pre_autorization) | Agent for medical pre-authorization processes. |
| [molecule_agent](./molecule_agent) | Molecular agent designed to investigate drug or molecule properties, focusing on toxicity prediction. |
| [mrna_agent](./mrna_agent) | Agent for mRNA related analysis or queries. |
| [pdf_summary_agent](./pdf_summary_agent) | Agent for summarizing PDF documents. |
| [tarif_agent](./tarif_agent) | Intelligent agent that monitors, analyzes, and provides insights on tariffs. |

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
