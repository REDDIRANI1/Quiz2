from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def summary():
    return {"summary": "Performance or department summary here"}
