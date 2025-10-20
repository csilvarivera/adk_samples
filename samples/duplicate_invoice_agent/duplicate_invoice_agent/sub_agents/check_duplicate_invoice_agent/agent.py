
from google.adk.agents import Agent
from .prompts import return_check_duplicate_invoice_agent_instructions
from google.adk.agents.callback_context import CallbackContext
from google.genai import types 
from typing import Optional
from duplicate_invoice_agent.common_utils.utils_bigquery import get_full_invoice_list

import os
from dotenv import load_dotenv
load_dotenv()

# BIGQUERY_PROJECT = os.getenv("BIGQUERY_PROJECT")
# BIGQUERY_DATASET = os.getenv("BIGQUERY_DATASET")
# BIGQUERY_TABLE = os.getenv("BIGQUERY_TABLE")    

BIGQUERY_PROJECT = "csilvariverademo"
BIGQUERY_DATASET = "eu_samples"
BIGQUERY_TABLE = "sap_invoices"


def get_invoice_list(callback_context: CallbackContext) -> Optional[types.Content]:
    """
    
    """
    print ("!! In before agent get invoices!!")
    #get the valid list of countries and materials
    project_id = BIGQUERY_PROJECT
    bq_dataset = BIGQUERY_DATASET
    bq_table = BIGQUERY_TABLE
    invoices = get_full_invoice_list(project_id, bq_dataset, bq_table)
    
    # add the list of valid countries to the context
    callback_context.state["INVOICES_JSON"] = invoices
    return None

root_agent = Agent(
    model='gemini-2.5-pro',
    name="check_duplicate_invoice",
    instruction=return_check_duplicate_invoice_agent_instructions(),
    generate_content_config=types.GenerateContentConfig(temperature=0.01), 
    before_agent_callback=get_invoice_list
)
