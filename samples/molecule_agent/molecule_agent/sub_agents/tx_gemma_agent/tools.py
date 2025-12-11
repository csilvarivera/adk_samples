import json
import os
from google.cloud import aiplatform
from google.adk.tools.tool_context import ToolContext
from dotenv import load_dotenv


# load the environment
load_dotenv()

def get_tx_gemma_toxicity(
    question:str,
    smiles: str,
    tool_context: ToolContext,
):
  print (f" question : {question}")
  print (f" smiles : {smiles}")
  TDC_PROMPT = """
    Instructions: Answer the following question about drug properties. Context: As a membrane separating circulating blood and brain extracellular fluid, the blood-brain barrier (BBB) is the protection layer that blocks most foreign drugs. Thus the ability of a drug to penetrate the barrier to deliver to the site of action forms a crucial challenge in development of drugs for central nervous system. Question: Given a drug SMILES string, predict whether it (A) does not cross the BBB (B) crosses the BBB Drug
    Drug SMILES: {smiles}
    Answer:
    """
  
  TX_GEMMA_PROJECT_ID = os.getenv("TX_GEMMA_PROJECT_ID","YOUR_PROJECT_ID")
  TX_GEMMA_ENDPOINT_ID = os.getenv("TX_GEMMA_ENDPOINT_ID","YOUR_ENDPOINT_ID")
  TX_GEMMA_ENDPOINT_REGION = os.getenv("TX_GEMMA_ENDPOINT_REGION","YOUR_ENDPOINT_REGION")

  endpoints = {}
  endpoints["endpoint"] = aiplatform.Endpoint(
    endpoint_name=TX_GEMMA_ENDPOINT_ID,
    project=TX_GEMMA_PROJECT_ID,
    location=TX_GEMMA_ENDPOINT_REGION,
  )
  # print (endpoints)
  instances = [
    {
        "prompt": TDC_PROMPT,
        "max_tokens": 8,
        "temperature": 0
    },
  ]
  response = endpoints["endpoint"].predict(instances=instances)
  predictions = response.predictions
  gemma_response = predictions[0]
  print (f" GEMA RESPONSE!!!!!!!!: {gemma_response} PREDICTONS!!! {predictions}" )
  return  json.dumps({"response": gemma_response})
