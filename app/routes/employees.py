from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_employees():
    return {"message": "List of employees"}
