
from google.adk.agents import Agent
from .prompts import return_risk_mitigation_agent_instructions
from google.adk.agents.callback_context import CallbackContext
from google.adk.tools import google_search
from google.genai import types 
from typing import Optional
from tariff_agent.common_utils.utils_bigquery import get_valid_countries_by_material_list


BIGQUERY_DATASET="tariffs_dataset"
BIGQUERY_PROJECT="matt-ai"
BIGQUERY_TABLE="materials_by_country"


def set_valid_countries_list(callback_context: CallbackContext) -> Optional[types.Content]:
    """
    Sets the countries and materials and adds them to the context.

    This function is used as a callback (e.g., a `before_agent_callback`)
    to fetch necessary data (valid countries and materials) and store it in the conversational context
    (`callback_context.state`) before the agent processes a turn.
    Args:
        callback_context: The context object provided by the framework,
                          containing conversation state and other relevant info.
    Returns:
        Optional[types.Content]: This function modifies the context in place
                                 and typically returns None, as its primary
                                 purpose is side effects (updating state).
                                 The return type hint suggests it *could*
                                 return content, but the current implementation
                                 returns None.
    """
    print ("!! In before agent callback RISK!!")
    #get the valid list of countries and materials
    countries = get_valid_countries_by_material_list(BIGQUERY_PROJECT, BIGQUERY_DATASET, BIGQUERY_TABLE,callback_context.state.get("material"))
    
    # add the list of valid countries to the context
    callback_context.state["VALID_COUNTRIES_LIST"] = countries

    # add the BQ variables after successful execution
    callback_context.state["BIGQUERY_DATASET"] = BIGQUERY_DATASET
    callback_context.state["BIGQUERY_TABLE"] = BIGQUERY_TABLE
    callback_context.state["BIGQUERY_PROJECT"] = BIGQUERY_PROJECT
    return None

root_agent = Agent(
    model='gemini-2.5-flash-preview-04-17',
    name="risk_mitigation_agent",
    instruction=return_risk_mitigation_agent_instructions(),
    before_agent_callback=set_valid_countries_list,
    tools=[google_search],
    generate_content_config=types.GenerateContentConfig(temperature=0.01), 
)
