
from google.adk.tools.tool_context import ToolContext
from .common_utils.utils_bigquery import bq_get_open_complaints, bq_get_count_by_status, bq_get_complaints_by_customer, bq_update_complaint_status, bq_get_single_complaint
from typing import Any, Dict, List

import os 
from dotenv import load_dotenv
load_dotenv()

BIGQUERY_PROJECT = os.environ.get("BIGQUERY_PROJECT_ID", "your_project_id")
BIGQUERY_DATASET = os.environ.get("BIGQUERY_DATASET_NAME", "sample")
BIGQUERY_TABLE = os.environ.get("BIGQUERY_TABLE_NAME", "complaints")
GOOGLE_CLOUD_PROJECT = os.environ.get("GOOGLE_CLOUD_PROJECT", "your_project_id")

# --- Tool Functions for Gemini Agent ---

def get_open_complaints_last_7_days() -> List[Dict[str, Any]]:
    """
    Fetches all complaints with 'Open' status from the last 7 days.
    
    Returns:
        A list of dictionaries, where each dictionary is a complaint.
    """
    print("Tool 'get_open_complaints_last_7_days' called.")
    response = bq_get_open_complaints(
        BIGQUERY_PROJECT, 
        BIGQUERY_DATASET, 
        BIGQUERY_TABLE
    )
    return response

def get_total_complaints_by_status(status: str) -> int:
    """
    Gets the total count of complaints for a specific status.

    Args:
        status: The status to filter by (e.g., "Open", "Closed").

    Returns:
        The total count as an integer.
    """
    print(f"Tool 'get_total_complaints_by_status' called with status: {status}")
    # You might add validation for the 'status' parameter here
    valid_statuses = {"Open", "In-Progress", "Closed", "Cancelled"}
    if status not in valid_statuses:
        # In a real app, you might raise a ValueError
        return f"Error: Invalid status '{status}'. Must be one of {valid_statuses}"

    response = bq_get_count_by_status(
        BIGQUERY_PROJECT, 
        BIGQUERY_DATASET, 
        BIGQUERY_TABLE, 
        status
    )
    return response

def get_complaints_by_customer_id(user_id: str, date: str) -> int:
    """
    Gets the complaints filed by a specific customer up to a
    given date. The date will be used as starting date to query the database

    Args:
        user_id: The customer's ID (e.g., 'sallyJones').
        date: A date in format "yyyy-MM-dd" (e.g., '2025-10-21').

    Returns:
        A List of complaints raised by the customer 
    """
    print(f"Tool 'get_complaints_by_customer_id' called for user: {user_id}, date: {date}")
    response = bq_get_complaints_by_customer(
        BIGQUERY_PROJECT,
        BIGQUERY_DATASET,
        BIGQUERY_TABLE,
        user_id,
        date
    )
    return response

def get_complaint_details(GUID: str) -> Dict[str, Any]:
    """
    Retrieves all details for a single complaint using its GUID.

    Args:
        GUID: The unique identifier for the complaint.

    Returns:
        A dictionary containing the complaint's details.
    """
    print(f"Tool 'get_complaint_details' called for GUID: {GUID}")
    response = bq_get_single_complaint(
        BIGQUERY_PROJECT, 
        BIGQUERY_DATASET, 
        BIGQUERY_TABLE, 
        GUID
    )
    return response

def update_complaint_details(GUID: str, status: str) -> Dict[str, Any]:
    """
    Updates the status of a specific complaint.

    Args:
        GUID: The unique identifier of the complaint to update.
        status: The new status to set (e.g., "Closed", "In-Progress").

    Returns:
        A dictionary of the *updated* complaint.
    """
    print(f"Tool 'update_complaint_details' called for GUID: {GUID}, new status: {status}")
    # You can add validation for the 'status' here as well
    valid_update_statuses = {"In-Progress", "Closed", "Cancelled"}
    if status not in valid_update_statuses:
         return f"Error: Invalid update status '{status}'. Must be one of {valid_update_statuses}"

    response = bq_update_complaint_status(
        BIGQUERY_PROJECT, 
        BIGQUERY_DATASET, 
        BIGQUERY_TABLE, 
        GUID, 
        status
    )
    return response