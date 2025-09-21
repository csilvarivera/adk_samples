import json
import uuid

from google.adk.tools.tool_context import ToolContext


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
  return None


