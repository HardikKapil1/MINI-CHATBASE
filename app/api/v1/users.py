from fastapi import APIRouter, HTTPException

router = APIRouter()
router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/{user_id}")
async def get_user(user_id: int):
    if user_id == 1:
        return {"id": 1, "name": "Hardik"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
