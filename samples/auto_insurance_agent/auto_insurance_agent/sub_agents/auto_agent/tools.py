
import json
import uuid
import datetime
import pytz

from google.adk.tools.tool_context import ToolContext

def create_tow_id(
    customerId: str,
    email: str,
    tool_context: ToolContext,
):
  """
  Create a new customer and generate a unique customer ID.
  """

  # And store the customer data.
  tow_id = str(uuid.uuid4())  # Replace with actual ID generation

  # Get the current datetime
  pacific_tz = pytz.timezone("US/Pacific")
  current_datetime = datetime.datetime.now(pacific_tz)

  # Add one hour
  hours = 1
  new_datetime = current_datetime + datetime.timedelta(hours=hours)

  # Format the output
  formatted_time = new_datetime.strftime("%I:%M %p, %Y-%m-%d")
  minutes = hours * 60
  if customerId == "":
    return "please join the club, and get a customer ID first."
  else:
    tool_context.state["customerId"] = customerId
    tool_context.state["towId"] = tow_id
    tool_context.state["towETA"] = formatted_time
    tool_context.state["towStatus"] = "Active"
    return json.dumps(
        {"towId": tow_id, "towETA": formatted_time, "towETAMinutes": minutes}
    )


def check_tow_status(
    towId: str,
    towETA: str,
    tool_context: ToolContext,
):
  """
  Create a new customer and generate a unique customer ID.
  """

  # and store the customer data.
  tow_id = str(uuid.uuid4())  # Replace with actual ID generation

  # Get the current datetime
  pacific_tz = pytz.timezone("US/Pacific")
  current_datetime = datetime.datetime.now(pacific_tz)
  current_time = current_datetime.strftime("%I:%M %p, %Y-%m-%d")

  eta = towETA
  eta_datetime = datetime.datetime.strptime(eta, "%I:%M %p, %Y-%m-%d")

  # Calculate the difference in minutes
  time_difference = eta_datetime - datetime.datetime.strptime(
      current_time, "%I:%M %p, %Y-%m-%d"
  )
  minutes_difference = time_difference.total_seconds() / 60
  tool_context.state["towETAMinutes"] = minutes_difference

  return json.dumps({
      "towId": tow_id,
      "towETA": eta,
      "towETAMinutes": minutes_difference,
      "towStatus": "Active",
  })

def create_customer_id(
    first_name: str,
    last_name: str,
    email: str,
    tool_context: ToolContext,
) -> str:
  """Create customer ID."""
  customer_id = str(uuid.uuid4())
  tool_context.state["first_name"] = first_name
  tool_context.state["last_name"] = last_name
  tool_context.state["email"] = email
  tool_context.state["customerId"] = customer_id
  return json.dumps([{"customerId": customer_id}])



def update_user_info(
    email: str,
    tool_context: ToolContext,
) -> None:
  """Update user's  email in the context.
  Args:
  email: The user's email.
  """
  tool_context.state["email"] = email

