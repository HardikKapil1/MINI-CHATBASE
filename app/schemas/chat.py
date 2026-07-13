from datetime import datetime

from pydantic import BaseModel, Field


class ChatCreate(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=255,
    )

    description: str | None = None


class ChatUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=255,
    )

    description: str | None = None


class ChatResponse(BaseModel):
    id: int
    name: str
    description: str | None
    user_id: int
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }