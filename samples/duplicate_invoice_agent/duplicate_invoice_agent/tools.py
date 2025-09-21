
from google.adk.tools.tool_context import ToolContext
from .common_utils.utils_bigquery import get_invoice_details

BIGQUERY_PROJECT="csilvariverademo"
BIGQUERY_DATASET="sample"
BIGQUERY_TABLE="duplicate_invoice"

def get_invoice_details_tool(
    invoice_number: str,
    tool_context: ToolContext,):

    print (f" in tool with values {invoice_number}")
    response = get_invoice_details(BIGQUERY_PROJECT, BIGQUERY_DATASET, BIGQUERY_TABLE, invoice_number)
    print (f"obtained tool response {response}")
    
    tool_context.state["BASE_INVOICE"] = response
    tool_context.state["INVOICE_NUMBER"] = invoice_number

     # add the BQ variables after successful execution
    tool_context.state["BIGQUERY_DATASET"] = BIGQUERY_DATASET
    tool_context.state["BIGQUERY_TABLE"] = BIGQUERY_TABLE
    tool_context.state["BIGQUERY_PROJECT"] = BIGQUERY_PROJECT
    return response