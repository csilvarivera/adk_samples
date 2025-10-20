document.addEventListener('DOMContentLoaded', () => {
    const sessionList = document.getElementById('session-list');
    const newSessionBtn = document.getElementById('new-session-btn');
    const chatHistory = document.getElementById('chat-history');
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');

    let currentSessionId = null;

    const addSessionToList = (session) => {
        const li = document.createElement('li');
        li.textContent = session;
        li.addEventListener('click', () => {
            currentSessionId = session;
            loadSessionHistory(session);
        });
        sessionList.appendChild(li);
    };

    // Function to load sessions
    const loadSessions = async () => {
        const response = await fetch('/sessions');
        const sessions = await response.json();
        sessionList.innerHTML = '';
        sessions.forEach(session => {
            addSessionToList(session);
        });
    };

    // Function to load session history
    const loadSessionHistory = async (sessionId) => {
        const response = await fetch(`/sessions/${sessionId}`);
        const history = await response.json();
        chatHistory.innerHTML = '';
        history.forEach(message => {
            const messageElement = document.createElement('div');
            messageElement.textContent = `${message.author}: ${message.text}`;
            chatHistory.appendChild(messageElement);
        });
    };

    // Function to create a new session
    const createNewSession = async () => {
        currentSessionId = `session-${Date.now()}`;
        addSessionToList(currentSessionId);
        loadSessionHistory(currentSessionId);
    };

    // Function to send a message
    const sendMessage = async (e) => {
        e.preventDefault();
        const message = userInput.value;
        userInput.value = '';

        if (!currentSessionId) {
            createNewSession();
        }

        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 
                session_id: currentSessionId, 
                message: message 
            })
        });

        const data = await response.json();
        loadSessionHistory(currentSessionId);
    };

    // Event listeners
    newSessionBtn.addEventListener('click', createNewSession);
    chatForm.addEventListener('submit', sendMessage);

    // Initial load
    loadSessions();
});