import os
from google.adk.agents import LlmAgent
from google.adk.tools import ToolContext
from google.adk.tools.load_artifacts_tool import load_artifacts_tool
from google.cloud import storage
import google.genai.types as types
from markdown_pdf import MarkdownPdf, Section

async def save_pdf_artifact_tool(summary_text:str, tool_context: ToolContext):
    file_name = "output_summary.pdf"
    pdf = MarkdownPdf()
    pdf.add_section(Section(summary_text))
    pdf.save(file_name)

    report_bytes = open(file_name, "rb").read()
    report_artifact = types.Part.from_bytes(
        data=report_bytes,
        mime_type="application/pdf"
    )
    # Create the artifacts
    version = await tool_context.save_artifact(filename=file_name, artifact=report_artifact)
   
    # Save to GCS bucket
    bucket_name = "csr-demo-bucket"
    gcs_uri = save_to_gcs(
        content=report_bytes,
        filename=file_name,
        bucket_name=bucket_name
    )
   
    if gcs_uri:
        # TODO: Generate signed URL instead of access url
        # signed_url = generate_signed_url(gcs_uri, service_account_key_path=DEFAULT_SERVICE_ACCOUNT_KEY_PATH)
        signed_url = generate_access_url(bucket_name,file_name)
        return {
            "status": "success",
            "message": f"Saved to file to GCS as '{file_name}' under signed_url {signed_url}",
            "filename": file_name,
            # "version": version,
            "signed_url": signed_url
        }
   

    return {"status": 'success',
        "detail": 'Summary PDF generated.',
        "filename": f"{file_name}"
    }
def save_to_gcs(content: bytes, filename: str, bucket_name: str) -> str:
    """
    Saves the file in a GCS bucket and returns the URL
    """
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(filename)
    blob.upload_from_string(content,  content_type='application/pdf')
    return f"https://storage.googleapis.com/{bucket_name}/{filename}"



def generate_access_url(filename: str, bucket_name: str) -> str:
    """
    Returns a signed URL
    """
    # Make sure you haev added the correct signed url prefix!!
    prefix = "storage.cloud.google.com"
    return f"https://{prefix}/{bucket_name}/{filename}"


root_agent = LlmAgent(
    model='gemini-2.5-pro',
    name="root_agent",
    description = "Agent for summarizing user documents", 
    instruction = """
    ## Persona ##
    You are an helpful agent that helps to cater user queries

    ## Instruction ##
    **Follow the steps mentioned as-it is**

    **Steps to be followed**
    - STEP 1 - Generate a summary text for the user provided document. The output will be a markdown text. with the following sections:
        ** Title
        ** Summary
        ** Table of Contents
        ** Body
        ** Concluston 
        You will call the `load_artifacts_tool` to load the file the user is uploading
    - STEP 2 - Call the `save_pdf_artifact_tool` with the generated summary text.
    - STEP 3 - Call the `load_artifacts_tool` once the `save_pdf_artifact_tool` gets completed to display all the files created in the session.
    - STEP 4 - Show the signed URL for the end user to be able to see the saved filed on GCS
    """,
    tools = [ save_pdf_artifact_tool, load_artifacts_tool ]
)