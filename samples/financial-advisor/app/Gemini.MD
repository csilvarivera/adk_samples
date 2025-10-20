AI Collaboration Guide for Lloyds Bank Chatbot
This document provides instructions for Gemini to assist in the development of a Python-based chatbot prototype for Lloyds Bank. The application uses the Vertex AI Agent Engine for its reasoning capabilities.

1. Project Overview
Project Name: Lloyds Bank AI Chatbot Prototype

Objective: To create a mobile-first chatbot interface that interacts with a deployed Vertex AI agent. This is a prototype and does not require user authentication.

User Interface: The frontend should have a clean, modern design with the branding and color scheme of Lloyds Bank.

2. Technology Stack
Frontend: HTML, CSS (Tailwind CSS for styling), and vanilla JavaScript.

Backend Interaction: The frontend will make asynchronous fetch requests to a specific Vertex AI Agent Engine endpoint.

Core Logic: All reasoning and response generation is handled by the deployed Vertex AI agent.

3. Architectural Patterns
Frontend Architecture: A single-page HTML application. All logic for UI updates and API calls is contained within a <script> tag in the Gem-AI-Chat.html file.

API Interaction:

Endpoint: The application sends POST requests to an endpoint with the following structure:
https://{REGION}-aiplatform.googleapis.com/v1beta1/projects/{PROJECT_ID}/locations/{REGION}/agents/{AGENT_ID}/sessions/{SESSION_ID}:run

Request Body: The JSON body sent with the POST request must contain an instruction object with a prompt field.

{
  "instruction": {
    "prompt": "The user's input text goes here."
  }
}


Response Body: The response from the agent is a JSON object that includes the agent's output text within an output field.

Session Management:

To maintain a persistent conversation, the application will use a fixed SESSION_ID (e.g., "default-user") for all interactions.

On application load, the app will make a GET request to the session URL (.../sessions/{SESSION_ID}) to fetch the existing message history and display it in the chat window.

4. Coding Conventions & Style Guide
HTML: Use semantic HTML5 tags where appropriate.

CSS: Use the Lloyds Bank official color palette for styling. The design should be mobile-responsive.

JavaScript:

Use modern JavaScript (ES6+ features like async/await and const/let).

Code should be well-commented, especially the API call logic.

Implement error handling for the API call to gracefully manage network issues or errors from the Vertex AI endpoint.

5. Unit Testing
Framework: Use Jest as the primary testing framework. Configure it with jsdom to simulate a browser environment for DOM manipulation testing.

Mocking API Calls: All fetch requests to the Vertex AI Agent Engine must be mocked using jest.fn() or jest.spyOn(). This prevents actual network requests during test runs and allows for simulating various API responses (e.g., success, failure, different data).

Test Coverage:

API Functions: Test the functions responsible for sending prompts and fetching session history. Verify that they construct the correct request body and call fetch with the appropriate URL, method, and headers.

UI Manipulation: Write tests to confirm that functions correctly add new messages (both user and agent) to the chat display. Simulate API responses and assert that the DOM is updated as expected.

Session Loading: Test the initial application load logic. Ensure it calls the session history endpoint and correctly renders the conversation history.

Error Handling: Create tests for API failure scenarios. Verify that if a fetch call fails, a user-friendly error message is displayed in the UI.

6. Key Instructions for Gemini
Consult Documentation: When providing assistance, refer to the official Google Cloud documentation for the Vertex AI Agent Engine, particularly the sections on using the Agent Development Kit (ADK) and managing sessions.

ADK Usage: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/use/adk

Session Management: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/sessions/manage-sessions-api#vertex-ai-sdk-for-python
2
Focus on Frontend: Since the core logic is handled by the deployed agent, focus on generating clean, efficient, and well-styled frontend code.

No Authentication: Do not suggest or implement any user login, authentication, or session management logic beyond the session ID mechanism. This is a public-facing prototype.

Prototyping: Remember that this is a prototype. Avoid over-engineering solutions. The primary goal is a functional and visually appealing user interfac