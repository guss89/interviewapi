from fastapi import APIRouter
from pydantic import BaseModel
from app.services.chatBot import generar_respuesta_openai

router = APIRouter(tags=["Chat-OpenIA"])

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        respuesta = await generar_respuesta_openai(request.message)
        return {"response": respuesta}
    except Exception as e:
        return {"error": str(e)}