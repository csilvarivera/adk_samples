import google.cloud.bigquery.client as bigquery
import pandas as pd


def get_full_invoice_list(project_id:str, bq_dataset:str, bq_table:str):
    """
     
    """
    client = bigquery.Client(project=project_id)
    query = ("""
        SELECT  Company_Code,Invoice_Number,GIN,Doc_No,
                    Vendor_Number, Invoice_Value,Invoice_Value__Converted_,Fiscal_year,
                    Invoice_Date,comment
        FROM ( 
            SELECT   Company_Code,Invoice_Number,GIN,Doc_No,
                        Vendor_Number, Invoice_Value,Invoice_Value__Converted_,Fiscal_year,
                        Invoice_Date,comment,COUNT (_Case_Key) AS _case_key_count
            FROM `{0}.{1}.{2}` 
            GROUP BY Company_Code,Invoice_Number,GIN,Doc_No,
                        Vendor_Number, Invoice_Value,Invoice_Value__Converted_,Fiscal_year,
                        Invoice_Date,comment, _Case_Key
            HAVING COUNT (_Case_Key) < 2
        )          
    """).format(project_id, bq_dataset, bq_table)
    query_job = client.query(query)
    rows = query_job.result()
    pd = rows.to_dataframe()
    return pd.to_json() 
    
def get_invoice_details(project_id:str, bq_dataset:str, bq_table:str, invoice_number:str):
    """
     
    """
    client = bigquery.Client(project=project_id, location="EU")
    query = ("""
       SELECT Source_System_ID,Company_Code,Doc_No,Invoice_Number,Fiscal_year, Group_id,Vendor_Number, 
              Vendor_Name, GIN, Invoice_Value,Transaction_Currency, Invoice_Value__Converted_, InvoiceEntryDate,
              Invoice_Date, Payment_Date, Payment_Number, Due_Date Sequence_Number,Comment
        FROM `{0}.{1}.{2}` 
        WHERE Invoice_Number = '{3}'
        ORDER BY 1,5,4,6
        LIMIT 1
    """).format(project_id, bq_dataset, bq_table,invoice_number)
    query_job = client.query(query)
    rows = query_job.result()
    pd = rows.to_dataframe()
    return pd.to_json() 
    