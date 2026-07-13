from fastapi import (
    APIRouter,
    Depends,
    File,
    UploadFile,
    status,
)

from app.api.deps import (
    DBSession,
    get_current_user,
)

from app.models.user import User
from app.schemas.document import DocumentResponse
from app.services.document_service import DocumentService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post(
    "/{chat_id}/upload",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED,
)
def upload_document(
    chat_id: int,
    db: DBSession,
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
):
    return DocumentService(db).upload_document(
        chat_id,
        file,
        current_user,
    )
