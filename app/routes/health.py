from fastapi import APIRouter

router = APIRouter()

@router.get("/health", operation_id="checkHealth")
def health():
    return {"status": "ok"} 