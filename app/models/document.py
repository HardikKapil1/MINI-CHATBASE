from datetime import datetime, UTC

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
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.chat import Chat


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

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(UTC),
    )

    chat: Mapped["Chat"] = relationship(
        back_populates="documents",
    )
