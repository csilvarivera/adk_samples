import os
from flask import Flask, render_template, request, jsonify
from google.cloud import aiplatform
from google.cloud.aiplatform_v1.services.prediction_service import PredictionServiceClient
from google.cloud.aiplatform_v1.types import prediction_service as gca_prediction_service
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value

app = Flask(__name__)

AGENT_ID = "projects/774298971519/locations/us-central1/reasoningEngines/1946210347954208768"

# Initialize the Vertex AI client
aiplatform.init(project="774298971519", location="us-central1")

# The AI Platform services require regional API endpoints.
client_options = {"api_endpoint": f"us-central1-aiplatform.googleapis.com"}
# Initialize client that will be used to create and send requests.
# This client only needs to be created once, and can be reused for multiple requests.
client = PredictionServiceClient(client_options=client_options)


# In-memory session storage (for demonstration purposes)
sessions = {
    "default-user": []
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sessions', methods=['GET'])
def get_sessions():
    return jsonify(list(sessions.keys()))

@app.route('/sessions/<session_id>', methods=['GET'])
def get_session_history(session_id):
    return jsonify(sessions.get(session_id, []))

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    session_id = data.get('session_id', 'default-user')
    message = data.get('message')

    if not message:
        return jsonify({'error': 'Message is required'}), 400

    # Add user message to history
    if session_id not in sessions:
        sessions[session_id] = []
    sessions[session_id].append({'author': 'user', 'text': message})

    # The session ID.
    session = f"{AGENT_ID}/sessions/{session_id}"
    # The instruction to send to the agent.
    instruction = gca_prediction_service.Instruction(prompt=message)
    # The request to send to the agent.
    request = gca_prediction_service.RunAgentRequest(
        session=session,
        instruction=instruction,
    )
    # Make the request to the agent.
    resp = client.run_agent(request=request)
    agent_response = json_format.MessageToDict(resp._pb)

    # Add agent response to history
    response_text = agent_response.get('output', 'Sorry, I could not understand your request.')
    sessions[session_id].append({'author': 'agent', 'text': response_text})

    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True, port=8080)