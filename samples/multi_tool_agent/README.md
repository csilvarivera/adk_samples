# Multi Tool Agent

This sample demonstrates a multi-tool agent built using the Agent Development Kit (ADK). The agent has access to a weather lookup tool and a calculator tool.

## Features

- **Weather Lookup**: Retrieves weather information for a given location.
- **Calculator**: Performs basic mathematical calculations.

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment**:
   Copy `.env-example` to `.env` and fill in your Google Cloud project details.

## Running the Agent

To run the agent locally and test the tools:
```bash
python -m multi_tool_agent
```
