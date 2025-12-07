import base64
import logging
import os
import httpx
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import JSONResponse

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("notion-proxy")

app = FastAPI()

@app.get("/")
def health_check():
    """Simple health check to ensure container is running."""
    return {"status": "Notion Proxy Active"}

@app.post("/oauth/token")
async def proxy_token(request: Request):
    """
    The Bridge:
    1. Receives 'application/x-www-form-urlencoded' from Google.
    2. Extracts client_id/secret from the BODY.
    3. Moves them to the HEADER (Basic Auth).
    4. Forwards to Notion.
    """
    try:
        # 1. Parse Form Data (Google sends this format)
        form_data = await request.form()
        
        # Log (Sanitized)
        logger.info(f"Received token request. Grant Type: {form_data.get('grant_type')}")

        # 2. Extract Data
        code = form_data.get("code")
        redirect_uri = form_data.get("redirect_uri")
        client_id = form_data.get("client_id")
        client_secret = form_data.get("client_secret")
        grant_type = form_data.get("grant_type")

        # Validation: Ensure we have what we need
        if not all([code, redirect_uri, client_id, client_secret]):
            logger.error("Missing required OAuth parameters in request body.")
            raise HTTPException(status_code=400, detail="Missing parameters (code, client_id, etc.)")

        # 3. The Transformation (Body -> Header)
        # Notion requires Basic Auth: Base64(client_id:client_secret)
        auth_str = f"{client_id}:{client_secret}"
        b64_auth = base64.b64encode(auth_str.encode()).decode()

        notion_headers = {
            "Authorization": f"Basic {b64_auth}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }

        notion_payload = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": redirect_uri
        }

        # 4. Proxy Request to Notion
        logger.info("Forwarding request to Notion API...")
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.notion.com/v1/oauth/token",
                json=notion_payload,
                headers=notion_headers
            )
            
            # Log the result status
            logger.info(f"Notion responded with status: {response.status_code}")

            # Return Notion's response EXACTLY as is
            # (If Notion errors, we want Google to see that error)
            return JSONResponse(content=response.json(), status_code=response.status_code)

    except Exception as e:
        logger.exception("Internal Server Error in Proxy")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)