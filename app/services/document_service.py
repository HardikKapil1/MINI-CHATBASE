from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile
from sqlalchemy.orm import Session
from app.models.document import Document
from app.models.user import User
from app.repositories.chat_repository import ChatRepository
from app.repositories.document_repository import DocumentRepository
from app.exceptions.chat import (
    ChatNotFoundError,
    ChatAccessDeniedError,
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


class DocumentService:
    def __init__(self, db: Session):
        self.document_repository = DocumentRepository(db)
        self.chat_repository = ChatRepository(db)

    def upload_document(
        self,
        chat_id: int,
        file: UploadFile,
        current_user: User,
    ) -> Document:
        # 1. Fetch and Validate Chat Existence First
        chat = self.chat_repository.get_by_id(chat_id)
        if not chat:
            raise ChatNotFoundError()

        # 2. Validate Permissions Second
        if chat.user_id != current_user.id:
            raise ChatAccessDeniedError()

        # 3. Handle File Upload Safely
        file_extension = Path(file.filename).suffix
        stored_filename = f"{uuid4()}{file_extension}"
        file_path = UPLOAD_DIR / stored_filename

        with open(file_path, "wb") as buffer:
            while chunk := file.file.read(1024 * 1024):
                buffer.write(chunk)

        # 4. Create and Persist Database Record
        document = Document(
            original_filename=file.filename,
            stored_filename=stored_filename,
            content_type=file.content_type,
            file_size=file.size,
            chat_id=chat.id,
        )
        return self.document_repository.create(document)
