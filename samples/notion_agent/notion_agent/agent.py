import os
from google.adk.agents import Agent
from google.adk.tools import ToolContext

# for using the token to retrieve the email
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build	

def get_email_from_token(access_token):
    """Get user info from access token"""
    credentials = Credentials(token=access_token)
    service = build('oauth2', 'v2', credentials=credentials)
    user_info = service.userinfo().get().execute()
    user_email = user_info.get('email')
    
    return user_email

def lazy_mask_token(access_token):
    """Mask access token for printing"""
    start_mask = access_token[:4]
    end_mask = access_token[-4:]
    
    return f"{start_mask}...{end_mask}"

def print_tool_context(tool_context: ToolContext):
    """ADK Tool to get email and masked token from Gemini Enterprise"""
    auth_id = os.getenv("AUTH_ID")
    
    # get access token using tool context
    access_token = tool_context.state[f"temp:{auth_id}"]
    
    # mask the token to be returned to the agent
    masked_token = lazy_mask_token(access_token)

    # get the user email using the token
    user_email = get_email_from_token(access_token)
    
    # store email in tool context in case you want to keep referring to it
    tool_context.state["user_email"] = user_email
    
    return {
        f"temp:{auth_id}": lazy_mask_token(access_token),
        "user_email": user_email
    }
    
root_agent = Agent(
    model='gemini-2.5-pro',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Greet the user first before you respond.Return the exact response of `print_tool_context` when asked to print     the tool context.',
    tools=[print_tool_context],
)
