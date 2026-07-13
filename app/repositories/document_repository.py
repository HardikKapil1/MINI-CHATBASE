from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        document: Document,
    ) -> Document:

        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)

        return document

    def get_by_chat(
        self,
        chat_id: int,
    ) -> list[Document]:

        return list(
            self.db.scalars(
                select(Document).where(
                    Document.chat_id == chat_id
                )
            )
        )

    def get_by_id(
        self,
        document_id: int,
    ) -> Document | None:

        return self.db.scalar(
            select(Document).where(
                Document.id == document_id
            )
        )