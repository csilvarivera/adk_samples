export AGENT_DISPLAY_NAME="Tariff Agent Demo-2"
export AGENT_DESCRIPTION="Tariff agent Demo for Cymbal Retail"
export AGENT_ID="Tariff_agent_Demo-1"
export AS_APP="test_1754474283170"
export REASONING_ENGINE="projects/1084188996181/locations/us-central1/reasoningEngines/4642863770144604160"

export PROJECT_ID="matt-ai"
export PROJECT_NUMBER="1084188996181"


echo "REASONING_ENGINE: $REASONING_ENGINE"
echo "PROJECT_NUMBER: $PROJECT_NUMBER"
echo "PROJECT_ID: $PROJECT_ID"

echo "https://discoveryengine.googleapis.com/v1alpha/projects/${PROJECT_ID}/locations/global/collections/default_collection/engines/${AS_APP}/assistants/default_assistant/agents" \
  -d '{
        "id": "'"${AGENT_ID}"'"
        "displayName": "'"${AGENT_DISPLAY_NAME}"'",
        "description": "'""${AGENT_DESCRIPTION}""'",
        "icon": {
          "uri": "https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/corporate_fare/default/24px.svg"
          },
      },
      "adk_agent_definition": {
          "tool_settings": {
            "tool_description": "give me the latest on Tariffs"
          },
          "provisioned_reasoning_engine": {
            "reasoning_engine":"'"${REASONING_ENGINE}"'"
          },
      },
    }'

curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "x-goog-user-project: ${PROJECT_ID}" \
https://discoveryengine.googleapis.com/v1alpha/projects/${PROJECT_NUMBER}/locations/global/collections/default_collection/engines/${AS_APP}/assistants/default_assistant?updateMask=agent_configs -d '{
    "name": "projects/${PROJECT_NUMBER}/locations/global/collections/default_collection/engines/${AS_APP}/assistants/default_assistant",
    "displayName": "Default Assistant",
    "agentConfigs": [{
      "displayName": "'"${AGENT_DISPLAY_NAME}"'",
      "vertexAiSdkAgentConnectionInfo": {
        "reasoningEngine": "'"${REASONING_ENGINE}"'"
      },
      "toolDescription": "'"${AGENT_DESCRIPTION}"'",
      "icon": {
        "uri": "https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/corporate_fare/default/24px.svg"
      },
      "id": "'"${AGENT_ID}"'"
    }]
  }'
