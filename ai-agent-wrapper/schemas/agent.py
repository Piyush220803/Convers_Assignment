from pydantic import BaseModel
from typing import Optional

class AgentInput(BaseModel):
    provider: str              # 'vapi' or 'retell'
    name: str
    description: Optional[str] = None
    voice: Optional[str] = None
    