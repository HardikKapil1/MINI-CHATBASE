from datetime import datetime, UTC
from typing import TYPE_CHECKING

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.core.database import Base

if TYPE_CHECKING:
    from app.models.document import Document


class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    __table_args__ = (
        UniqueConstraint(
            "document_id",
            "chunk_index",
            name="uq_document_chunk_index",
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    document_id: Mapped[int] = mapped_column(
        ForeignKey("documents.id"),
    )

    chunk_index: Mapped[int] = mapped_column(
        Integer,
    )

    text: Mapped[str] = mapped_column(
        Text,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )

    document: Mapped["Document"] = relationship(
        back_populates="chunks",
    )
