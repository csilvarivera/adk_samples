import json
import os
from google.cloud import aiplatform
from google.adk.tools.tool_context import ToolContext
from dotenv import load_dotenv


# load the environment
load_dotenv()

def get_med_gemma_response(
    question:str,
    tool_context: ToolContext,):
    print (f" question : {question}")
    system_instruction = """
    You are an expert medical assistant specializing in analyzing symptoms caused by chemical compounds and drugs.
    Your goal is to explain the potential symptoms and side effects associated with specific compounds provided by the user.
    Provide detailed, medically accurate information about how these compounds affect the human body and what symptoms might manifest.

    """

    MED_GEMMA_PROJECT_ID = os.getenv("MED_GEMMA_PROJECT_ID","YOUR_PROJECT_ID")
    MED_GEMMA_ENDPOINT_ID = os.getenv("MED_GEMMA_ENDPOINT_ID","YOUR_ENDPOINT_ID")
    MED_GEMMA_ENDPOINT_REGION = os.getenv("MED_GEMMA_ENDPOINT_REGION","YOUR_ENDPOINT_REGION")

    endpoints = {}
    endpoints["endpoint"] = aiplatform.Endpoint(
    endpoint_name=MED_GEMMA_ENDPOINT_ID,
    project=MED_GEMMA_PROJECT_ID,
    location=MED_GEMMA_ENDPOINT_REGION,
    )
    max_tokens = 1500
    print (endpoints)
    messages = [
    {
        "role": "system",
        "content": [{"type": "text", "text": system_instruction}]
    },
    {
        "role": "user",
        "content": [
            {"type": "text", "text": question},
        ]
    }
    ]
    instances = [
        {
            "@requestFormat": "chatCompletions",
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": 0
        },
    ]
    response = endpoints["endpoint"].predict(
        instances=instances, use_dedicated_endpoint=False)
    print (f" GEMMA RESPONSE!!!!!!!! PREDICTONS!!! {response}" )

    predictions = response.predictions
    # response = endpoints["endpoint"].predict(instances=instances)
    # predictions = response.predictions
    gemma_response =  response.predictions
    print (f" GEMMA RESPONSE!!!!!!!!: {gemma_response} PREDICTONS!!! {predictions}" )
    return  json.dumps({"response": gemma_response})
