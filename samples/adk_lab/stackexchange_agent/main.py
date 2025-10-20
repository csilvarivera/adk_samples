# file: adk_lab/stackexchange_agent/main.py

import logging
import os

import uvicorn
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCapabilities, AgentCard, AgentSkill

# Make sure the imports point to your project structure
from adk_lab.stackexchange_agent.agent import StackExchangeAgent
from adk_lab.stackexchange_agent.agent_executor import StackExchangeExecutor
from adk_lab.utils.proxy import STACKEXCHANGE_AGENT_URL, logger

from adk_lab.utils.proxy import cepf_log_client

# Create a custom logger for activity tracking
cepf_logger = cepf_log_client.logger("cepf-stackexchange-agent") 


def main():
    """Starts the StackExchange Agent A2A server, configured for Cloud Run."""

    # Read port from environment variable, default to 8080 for local testing
    port = int(os.environ.get("PORT", 8080))
    
    # In a container, listen on all interfaces
    public_url = STACKEXCHANGE_AGENT_URL

    logger.info(f"Using public URL for Agent Card: {public_url}")

    logger.info("Defining Agent Card...")
    
    # The URL will be dynamically provided by Cloud Run,
    # so we use a placeholder or leave it generic.
    # A controller service would typically update this upon discovery.
    search_stackExchange_skills = AgentSkill(
        id='search_stackExchange',
        name='Search StackExchange',
        description='returns stackExchange answer',
        tags=['Search stackExchange'],
        examples=['Search repository 123', 'Give me the details of repository 456'],
    )
    
    agent_card = AgentCard(
        name="StackExchangeAgent-A2A",
            description="An agent that uses MCP to interact with Stack Exchange.",
            url=public_url,
            version="1.0.0",
            default_input_modes=StackExchangeAgent.SUPPORTED_CONTENT_TYPES,
            default_output_modes=StackExchangeAgent.SUPPORTED_CONTENT_TYPES,
            capabilities=AgentCapabilities(streaming=False),
            skills=[
                 search_stackExchange_skills,
        ],
    )


    # Do not change — used for activity tracking.
    cepf_logger.log_text(
        f"agent_card.skills: {agent_card.skills}"        
    )  

    # Assemble the A2A server components
    logger.info("Initializing A2A request handler...")
    request_handler = DefaultRequestHandler(
        agent_executor=StackExchangeExecutor(),
        task_store=InMemoryTaskStore(),
    )

    # The server still listens on 0.0.0.0 inside the container
    listen_host = "0.0.0.0"
    server = A2AStarletteApplication(agent_card=agent_card, http_handler=request_handler)

    logger.info(f"Starting Uvicorn server on {listen_host}:{port}")
    uvicorn.run(server.build(), host=listen_host, port=port)


if __name__ == "__main__":
    main()
