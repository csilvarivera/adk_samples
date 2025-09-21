import google.cloud.bigquery.client as bigquery
import pandas as pd

def get_valid_countries_list(project_id:str, bq_dataset:str, bq_table:str):
    """ 
    Obtains the valid list of countries for Gemini to calculate a scenario.
    This function connects to Google BigQuery, executes a query to find
    all unique values in the 'origin' column of the given table, and
    returns the results as a JSON string.

    Args:
        project_id (str): The Google Cloud project ID where the BigQuery dataset and table reside.
        bq_dataset (str): The name of the BigQuery dataset.
        bq_table (str): The name of the BigQuery table containing the 'origin' column.

    Returns:
        str: A JSON string representing a list of distinct values from the 'origin' column.
             Returns an empty list in JSON format if the table is empty or the column has no distinct values.
   
"""
    
    client = bigquery.Client(project=project_id) 

    # validate that we got a material
    query = ("""
    SELECT DISTINCT (origin)
    FROM `{0}.{1}.{2}`
    """).format(project_id,bq_dataset, bq_table)
    print (query)
    query_job = client.query(query)
    rows = query_job.result()
    pd = rows.to_dataframe()
    return pd.to_json() 

def get_valid_materials_list(project_id:str, bq_dataset:str, bq_table:str,country_origin:str=None):
    """ 
    Obtains the valid list of materials for Gemini to calculate a scenario.
    This function connects to Google BigQuery, executes a query to find
    all unique values in the 'origin' column of the given table, and
    returns the results as a JSON string.

    Args:
        project_id (str): The Google Cloud project ID where the BigQuery dataset and table reside.
        bq_dataset (str): The name of the BigQuery dataset.
        bq_table (str): The name of the BigQuery table containing the 'origin' column.
        country_origin (str): Optional - a country of origin to filter down the materials

    Returns:
        str: A JSON string representing a list of distinct values from the 'origin' column.
             Returns an empty list in JSON format if the table is empty or the column has no distinct values.
   
    """
    client = bigquery.Client(project=project_id) 
    if country_origin is None:
        country_origin = "NULL"
        
    query = ("""
    SELECT DISTINCT (materials)
    FROM `{0}.{1}.{2}`
    WHERE ( '{3}' = 'NULL' OR origin = '{3}')
    """).format(project_id,bq_dataset, bq_table,country_origin)

    print (f"{query} !!!!!!!!!!!")
    query_job = client.query(query)
    rows = query_job.result()
    pd = rows.to_dataframe()
    return pd.to_json() 


def get_valid_countries_by_material_list(project_id:str, bq_dataset:str, bq_table:str, materials:str=None):
    """ 
    Obtains the valid list of countries for Gemini to calculate a risk mitigation scenario based on a material.
    This function connects to Google BigQuery, executes a query to find
    all unique values in the 'origin' column of the given table, and
    returns the results as a JSON string.

    Args:
        project_id (str): The Google Cloud project ID where the BigQuery dataset and table reside.
        bq_dataset (str): The name of the BigQuery dataset.
        bq_table (str): The name of the BigQuery table containing the 'origin' column.
        materials (str): Optional - a material to filter down the countries


    Returns:
        str: A JSON string representing a list of distinct values from the 'origin' column.
             Returns an empty list in JSON format if the table is empty or the column has no distinct values.
   
"""
    
    client = bigquery.Client(project=project_id) 

    # validate that we got a material
    if materials is None:
        materials = "NULL"
    
    query = ("""
    SELECT DISTINCT (origin)
    FROM `{0}.{1}.{2}`
    WHERE ( '{3}' = 'NULL' OR materials = '{3}')         
    """).format(project_id,bq_dataset, bq_table,materials)
    print (query)
    query_job = client.query(query)
    rows = query_job.result()
    pd = rows.to_dataframe()
    return pd.to_json() 


def calculate_impact(project_id:str, bq_dataset:str, bq_table:str, country_origin:str, material:str, impact_percentage:float):
    """
     Calculates the financial impact of a percentage change on spend for a specific
    country and material based on data in a BigQuery table.

    This function queries a BigQuery table to find the total current spend for a
    given country and material. It then calculates the absolute increase in spend
    and the new total spend based on the provided impact percentage. The results
    are returned as a JSON string.

    Args:
        project_id (str): The Google Cloud project ID where the BigQuery dataset and table reside.
        bq_dataset (str): The name of the BigQuery dataset.
        bq_table (str): The name of the BigQuery table containing 'origin', 'materials', and 'spend' columns.
        country_origin (str): The specific country ('origin') to filter the data by.
        material (str): The specific material ('materials') to filter the data by.
        impact_percentage (float): The percentage increase or decrease (e.g., 0.10 for a 10% increase,
                                     -0.05 for a 5% decrease). This value is treated as a multiplier
                                     (e.g., 10% increase means multiplying by 0.10, not 1.10).

    Returns:
        str: A JSON string representing the calculation results. The JSON will contain
             the original 'origin', 'materials', 'current_spend', the applied '_increase_percentage',
             the calculated 'total_increase_usd', and the calculated 'total_impact_usd'.
             Returns an empty list in JSON format if no data is found for the specified
             country and material. The JSON format will be a list of objects.
    """
    client = bigquery.Client(project=project_id)
    query = ("""
        WITH tmp_tariff as (
        SELECT origin,materials, SUM(spend) as current_spend
        FROM `{0}.{1}.{2}` 
        WHERE origin='{3}'
        AND materials ='{4}'
        GROUP BY ALL 
        ) 
        SELECT t.*, {5} AS _increase_percentage,
        (t.current_spend * ({5})) AS total_increase_usd,
        (t.current_spend * ({5} + 1)) as total_impact_usd
        FROM tmp_tariff t
        """).format(project_id, bq_dataset, bq_table,country_origin, material, impact_percentage)
    query_job = client.query(query)
    rows = query_job.result()
    pd = rows.to_dataframe()
    return pd.to_json() 
    