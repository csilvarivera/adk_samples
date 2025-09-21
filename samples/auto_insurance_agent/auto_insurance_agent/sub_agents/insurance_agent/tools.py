import json
import uuid

from google.adk.tools.tool_context import ToolContext


def file_claim(
    email: str,
    customerId: str,
    accidentDetails: str,
    tool_context: ToolContext,
) -> str:
  """Create customer ID."""
  claim_id = str(uuid.uuid4())  # Replace with actual ID generation
  tool_context.state["claimId"] = claim_id
  tool_context.state["accidentDetails"] = accidentDetails

  return json.dumps({"claimId": claim_id})