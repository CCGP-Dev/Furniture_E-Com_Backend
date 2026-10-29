
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def auth_status():
    return {"message": "Authentication router is working"}
