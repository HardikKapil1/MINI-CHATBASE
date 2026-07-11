from fastapi import APIRouter

router = APIRouter()

router = APIRouter(
    prefix="/system",
    tags=["System"],
)

@router.get("/")
async def root():
    return {
        "success": True,
        "message": "Welcome to Mini Chatbase"
    }


@router.get("/health")
async def health():
    return {
        "success": True,
        "data": {
            "status": "healthy"
        }
    }


@router.get("/version")
async def version():
    return {
        "success": True,
        "data": {
            "version": "1.0.0"
        }
    }


@router.get("/about")
async def about():
    return {
        "success": True,
        "data": {
            "project": "Mini Chatbase",
            "framework": "FastAPI",
            "version": "1.0.0"
        }
    }