
from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext

from .prompts import return_scenario_planning_agent_instructions
from .tools import calculate_tariff_scenario
from typing import Optional
from tariff_agent.common_utils.utils_bigquery import get_valid_countries_list, get_valid_materials_list
from google.genai import types 
from dotenv import load_dotenv
import os

# load the environment
load_dotenv()

BIGQUERY_DATASET = os.getenv("BIGQUERY_DATASET")
BIGQUERY_PROJECT = os.getenv("BIGQUERY_PROJECT")
BIGQUERY_TABLE = os.getenv("BIGQUERY_TABLE")


def set_materials_and_countries(callback_context: CallbackContext) -> Optional[types.Content]:
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
    print ("!! In before agent callback !!")
    #get the valid list of countries and materials
    countries = get_valid_countries_list(BIGQUERY_PROJECT, BIGQUERY_DATASET, BIGQUERY_TABLE)
    materials = get_valid_materials_list(BIGQUERY_PROJECT, BIGQUERY_DATASET, BIGQUERY_TABLE, callback_context.state.get("country_origin"))

    # add the list of valid countries and materials to the co   ntext
    callback_context.state["COUNTRIES"] = countries
    callback_context.state["MATERIALS"] = materials

    # add the BQ variables after successful execution
    callback_context.state["BIGQUERY_DATASET"] = BIGQUERY_DATASET
    callback_context.state["BIGQUERY_TABLE"] = BIGQUERY_TABLE
    callback_context.state["BIGQUERY_PROJECT"] = BIGQUERY_PROJECT
    return None


root_agent = Agent(
    model='gemini-2.5-flash',
    name="scenario_planning_agent",
    instruction=return_scenario_planning_agent_instructions(),
    tools=[calculate_tariff_scenario],
    before_agent_callback=set_materials_and_countries,
    generate_content_config=types.GenerateContentConfig(temperature=0.01),
)
