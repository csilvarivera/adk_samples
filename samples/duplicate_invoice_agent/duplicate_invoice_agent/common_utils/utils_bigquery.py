import google.cloud.bigquery.client as bigquery
import pandas as pd


def get_full_invoice_list(project_id:str, bq_dataset:str, bq_table:str, invoice_number:str):
    """
     
    """
    client = bigquery.Client(project=project_id)
    query = ("""
       SELECT Company_Code, Accounting_Document_Number, Vendor_id, Document_Number, Date, User_id, Amount_USD
        FROM `{0}.{1}.{2}` 
        ORDER BY 1,5,4,6
    """).format(project_id, bq_dataset, bq_table)
    query_job = client.query(query)
    rows = query_job.result()
    pd = rows.to_dataframe()
    return pd.to_json() 
    


def get_invoice_details(project_id:str, bq_dataset:str, bq_table:str, invoice_number:str):
    """
     
    """
    client = bigquery.Client(project=project_id)
    query = ("""
       SELECT Company_Code, Accounting_Document_Number, Vendor_id, Document_Number, Date, User_id, Amount_USD
        FROM `{0}.{1}.{2}` 
        WHERE Document_Number = '{3}'
        ORDER BY 1,5,4,6
        LIMIT 1
    """).format(project_id, bq_dataset, bq_table,invoice_number)
    query_job = client.query(query)
    rows = query_job.result()
    pd = rows.to_dataframe()
    return pd.to_json() 
    