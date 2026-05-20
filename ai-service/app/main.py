from fastapi import FastAPI
from app.routes import ai_routes

app = FastAPI()

app.include_router(ai_routes.router, prefix="/api/ai")

@app.get("/")
def read_root():
    return {"message": "NeuroStack AI Service Ready"}
