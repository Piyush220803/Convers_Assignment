import requests
import os

VAPI_API_KEY = os.getenv("e94aa2f4-323c-4276-9426-ef86869ae0e9")

def create_vapi_agent(name: str, description: str, voice: str):
    url = "https://api.vapi.ai/assistant"
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "name": name,
        "description": description,
        "voice": voice
    }

    response = requests.post(url, headers=headers, json=payload)

    try:
        return response.json()
    except ValueError:
        return {
            "error": "Failed to decode JSON from VAPI",
            "status_code": response.status_code,
            "text": response.text
        }
