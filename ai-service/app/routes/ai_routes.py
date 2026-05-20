from fastapi import APIRouter

router = APIRouter()

@router.post("/generate")
def generate_response():
    return {"response": "AI Generated Content"}
