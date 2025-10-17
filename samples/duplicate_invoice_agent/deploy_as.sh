export AGENT_DISPLAY_NAME="Duplicate Invoice SAP"
export AGENT_DESCRIPTION="Duplicate Invoice Demo for Cymbal "
export AGENT_ID="Duplicate_Invoice SAP"
export AS_APP="agentspace_1760016997278"
export REASONING_ENGINE="projects/774298971519/locations/us-central1/reasoningEngines/2370107264833945600"

export PROJECT_ID="your-project-id"
export PROJECT_NUMBER="your-number-id"


echo "REASONING_ENGINE: $REASONING_ENGINE"
echo "PROJECT_NUMBER: $PROJECT_NUMBER"
echo "PROJECT_ID: $PROJECT_ID"

curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: ${PROJECT_ID}" \
  "https://us-discoveryengine.googleapis.com/v1alpha/projects/${PROJECT_NUMBER}/locations/us/collections/default_collection/engines/${AS_APP}/assistants/default_assistant/agents" \
-d '{
      "displayName": "'"${AGENT_DISPLAY_NAME}"'",
      "description": "'"${AGENT_DESCRIPTION}"'",
      "icon": {
        "uri": "https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/corporate_fare/default/24px.svg"
      },
      "adk_agent_definition": {
        "tool_settings": {
          "tool_description": "'"${AGENT_DESCRIPTION}"'",
        },
        "provisioned_reasoning_engine": {
        "reasoning_engine":"'"${REASONING_ENGINE}"'"
        }
      },    
}'