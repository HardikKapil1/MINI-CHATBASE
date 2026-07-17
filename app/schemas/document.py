from datetime import datetime

from pydantic import BaseModel

from app.enums.document_status import DocumentStatus


class DocumentResponse(BaseModel):
    id: int
    original_filename: str
    stored_filename: str
    content_type: str
    file_size: int
    chat_id: int
    status: DocumentStatus
    error_message: str
    created_at: datetime
    updated_at: datetime
    model_config = {
        "from_attributes": True,
    }
