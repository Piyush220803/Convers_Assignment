from fastapi import FastAPI
from routes.agent import router as agent_router
from services.retell import create_retell_agent

app = FastAPI()

app.include_router(agent_router, prefix="/agent", tags=["Agent"])

create_retell_agent()