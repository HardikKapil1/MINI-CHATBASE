from collections.abc import Generator

from sqlalchemy.orm import Session

from app.core.database import SessionLocal


def get_db() -> Generator[Session, None, None]:
    """
    Creates a database session for a single request.

    FastAPI will:
    1. Open a session.
    2. Yield it to the endpoint.
    3. Close it after the request finishes.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
