from fastapi import APIRouter
from services.retell import create_retell_agent
from pydantic import BaseModel

router = APIRouter()

class AgentRequest(BaseModel):
    api_key: str
    llm_id: str
    voice_id: str

@router.post("/create")
def create_agent(request: AgentRequest):
    try:
        agent_response = create_retell_agent(
            api_key=request.api_key,
            llm_id=request.llm_id,
            voice_id=request.voice_id
        )
        return {"success": True, "agent_id": agent_response.agent_id}
    except Exception as e:
        return {"success": False, "error": str(e)}
