export AGENT_DISPLAY_NAME="Complaint Manager"
export AGENT_DESCRIPTION="Complaint Manager for Cymbal Bank"
export AGENT_ID="Complaint Manager"
export AS_APP="your_GE_app"
export PROJECT_ID="<Your_Project>"
export PROJECT_NUMBER="<Your_Project_Number>"

export REASONING_ENGINE="projects/${PROJECT_NUMBER}/locations/us-central1/reasoningEngines/1946210347954208768"

echo "REASONING_ENGINE: $REASONING_ENGINE"
echo "PROJECT_NUMBER: $PROJECT_NUMBER"
echo "PROJECT_ID: $PROJECT_ID"

curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: ${PROJECT_ID}" \
  "https://discoveryengine.googleapis.com/v1alpha/projects/${PROJECT_NUMBER}/locations/global/collections/default_collection/engines/${AS_APP}/assistants/default_assistant/agents" \
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


