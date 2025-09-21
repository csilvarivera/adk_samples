
from google.adk.tools.tool_context import ToolContext
from tariff_agent.common_utils.utils_bigquery import calculate_impact


def calculate_tariff_scenario(
    country_origin: str,
    material: str,
    percentage_increase: float,
    tool_context: ToolContext,):

    print (f" in tool with values {country_origin}, {material}, {percentage_increase}")
    project_id = tool_context.state["BIGQUERY_PROJECT"]
    bq_dataset = tool_context.state["BIGQUERY_DATASET"]
    bq_table = tool_context.state["BIGQUERY_TABLE"]
    response = calculate_impact(project_id, bq_dataset, bq_table, country_origin, material, percentage_increase)
    print (f"obtained tool response {response}")

    tool_context.state["material"] = material
    tool_context.state["country_origin"] = country_origin
    tool_context.state["percentage_increase"] = percentage_increase
    return response