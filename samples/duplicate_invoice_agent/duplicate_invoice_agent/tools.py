
from google.adk.tools.tool_context import ToolContext
from .common_utils.utils_bigquery import get_invoice_details
from google.adk.tools.application_integration_tool.application_integration_toolset import ApplicationIntegrationToolset


import os 
from dotenv import load_dotenv
load_dotenv()

# BIGQUERY_PROJECT = os.getenv("BIGQUERY_PROJECT")
# BIGQUERY_DATASET = os.getenv("BIGQUERY_DATASET")
# BIGQUERY_TABLE = os.getenv("BIGQUERY_TABLE")    
# GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")    
# APPLICATION_INTEGRATION_LOCATION= os.getenv("APPLICATION_INTEGRATION_LOCATION")
# APPLICATION_INTEGRATION_ID = os.getenv("APPLICATION_INTEGRATION_ID")

BIGQUERY_PROJECT = "csilvariverademo"
BIGQUERY_DATASET = "eu_samples"
BIGQUERY_TABLE = "sap_invoices"
GOOGLE_CLOUD_PROJECT = "csilvariverademo"
APPLICATION_INTEGRATION_LOCATION= "europe-west4"
APPLICATION_INTEGRATION_ID = "sap-demo-supplier-invoice"




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

def reverse_invoice_tool(
    invoice_number: str,
    tool_context: ToolContext,):

    sap_invoice_toolset = ApplicationIntegrationToolset(
        project=GOOGLE_CLOUD_PROJECT,
        location=APPLICATION_INTEGRATION_LOCATION,
        connection=APPLICATION_INTEGRATION_ID,
        actions={"A_SupplierInvoice":["CANCEL"]},
        tool_instructions="""
         **Tool Definition: Tool for SAP Supplier Connector via Apigee Integration**

        This tool interacts with Invoices using an Apigee Integration Connector.
        It supports CANCEL operations as defined for the A_SupplierInvoice entity.

        When cancelling the Invoice use the following constants:

            FiscalYear: 2024,
            ReversalReason": 02,
            SupplierInvoice: 5100001398,
            PostingDate: 2024-11-20 00:00:00
        """
    )


def list_open_items_tool(
    invoice_number: str,
    tool_context: ToolContext,):

    sap_invoice_toolset = ApplicationIntegrationToolset(
        project=GOOGLE_CLOUD_PROJECT,
        location=APPLICATION_INTEGRATION_LOCATION,
        connection=APPLICATION_INTEGRATION_ID,
        actions={"A_SupplierInvoice":["LIST"]},
        filter="SupplierInvoiceStatus = '5' and PaymentReference = ''",
        tool_instructions="""
         **Tool Definition: Tool for SAP Supplier Connector via Apigee Integration**

        This tool List Invoices using an Apigee Integration Connector.
        It supports LIST operations as defined for the A_SupplierInvoice entity.
        """
    )
