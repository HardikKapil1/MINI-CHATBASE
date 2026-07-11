from fastapi import APIRouter

from app.schemas.chatbot import ChatRequest

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("/")
async def chat(request: ChatRequest):
    return {
        "success": True,
        "data": {
            "user_message": request.message,
            "ai_response": "This is a dummy AI response.",
            "temperature": request.temperature,
        },
    }
