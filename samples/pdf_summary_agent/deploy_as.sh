export AGENT_DISPLAY_NAME="PDF Creator - V2"
export AGENT_DESCRIPTION="Agent that creates PDF summay or another PDF"
export AGENT_ID="PDF Creator - V2"
export AS_APP="oem_1746532905481"
export PROJECT_ID="csilvariverademo"
export PROJECT_NUMBER="774298971519"

export REASONING_ENGINE="projects/774298971519/locations/us-central1/reasoningEngines/4315279673811533824"

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


