from datetime import datetime

from pydantic import BaseModel


class DocumentResponse(BaseModel):

    id: int
    original_filename: str
    stored_filename: str
    content_type: str
    file_size: int
    chat_id: int
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }