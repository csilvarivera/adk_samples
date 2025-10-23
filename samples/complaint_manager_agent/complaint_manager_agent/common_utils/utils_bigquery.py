import google.cloud.bigquery.client as bigquery
import pandas as pd

def bq_get_open_complaints(project_id:str, bq_dataset:str, bq_table:str):
    """
     
    """
    client = bigquery.Client(project=project_id, location="US")
    query = ("""
        SELECT guid, complaint_date, product,Narrative,Customer_Id,Status
        FROM `{0}.{1}.{2}` 
        WHERE status = "Open"
        AND complaint_date >= CURRENT_DATE - 3
        and product = "credit_card"
        and Customer_Id in ("oliverSmith","sallyJones","williamBrown")        
    """).format(project_id, bq_dataset, bq_table)
    query_job = client.query(query)
    rows = query_job.result()
    pd = rows.to_dataframe()
    return pd.to_json() 


def bq_get_count_by_status(project_id:str, bq_dataset:str, bq_table:str, status:str):
    """
     
    """
    client = bigquery.Client(project=project_id, location="US")
    query = ("""
        SELECT COUNT(1) as total
        FROM `{0}.{1}.{2}` 
        WHERE UPPER(status) = UPPER("{3}")
        AND complaint_date >= CURRENT_DATE - 30
        AND product = "credit_card"
    """).format(project_id, bq_dataset, bq_table, status)
    query_job = client.query(query)
    rows = query_job.result()
    pd = rows.to_dataframe()
    return pd.to_json() 



def bq_get_complaints_by_customer(project_id:str, bq_dataset:str, bq_table:str, customerId:str, date:str):
    """
     
    """
    client = bigquery.Client(project=project_id, location="US")
    query = ("""
        SELECT guid, complaint_date, product,Narrative,Customer_Id,Status
        FROM `{0}.{1}.{2}` 
        WHERE complaint_date >= "{3}" 
        AND Customer_Id = "{4}"
        and product = "credit_card"
    """).format(project_id, bq_dataset, bq_table, date, customerId)
    query_job = client.query(query)
    rows = query_job.result()
    pd = rows.to_dataframe()
    return pd.to_json() 


def bq_get_single_complaint(project_id:str, bq_dataset:str, bq_table:str, guid:str):
    """
     
    """
    client = bigquery.Client(project=project_id, location="US")
    query = ("""
        SELECT guid, complaint_date, product,Narrative,Customer_Id,Status
        FROM `{0}.{1}.{2}` 
        WHERE guid = "{3}" 

    """).format(project_id, bq_dataset, bq_table, guid)
    query_job = client.query(query)
    rows = query_job.result()
    pd = rows.to_dataframe()
    return pd.to_json() 


def bq_update_complaint_status(project_id:str, bq_dataset:str, bq_table:str, status:str, guid:str):
    """
     
    """
    client = bigquery.Client(project=project_id, location="US")
    query = ("""
        UPDATE `{0}.{1}.{2}` 
        SET STATUS = {3}
        WHERE guid = "{4}" 

    """).format(project_id, bq_dataset, bq_table, status, guid)
    query_job = client.query(query)
    rows = query_job.result()
    pd = rows.to_dataframe()
    return pd.to_json() 
    