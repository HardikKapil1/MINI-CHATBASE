from datetime import UTC, datetime

from sqlalchemy import (
    String,
    Integer,
    ForeignKey,
    DateTime,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.core.database import Base
from app.enums.document_status import DocumentStatus

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.chat import Chat
    from app.models.document_chunk import DocumentChunk


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    original_filename: Mapped[str] = mapped_column(
        String(255),
    )

    stored_filename: Mapped[str] = mapped_column(
        String(255),
        unique=True,
    )

    content_type: Mapped[str] = mapped_column(
        String(100),
    )

    file_size: Mapped[int] = mapped_column(
        Integer,
    )

    chat_id: Mapped[int] = mapped_column(
        ForeignKey("chats.id"),
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default=DocumentStatus.UPLOADED.value,
    )

    error_message: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
    )

    chat: Mapped["Chat"] = relationship(
        back_populates="documents",
    )
    chunks: Mapped[list["DocumentChunk"]] = relationship(
        back_populates="document",
        cascade="all, delete-orphan",
    )
