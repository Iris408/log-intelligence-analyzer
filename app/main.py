from fastapi import FastAPI

from app.routes.log_routes import router as log_router

app = FastAPI(
    title="Log Intelligence Analyzer API",
    description="FastAPI dashboard/ API layer for log analysis results",
    version="1.0.0",
)

app.include_router(log_router)

@app.get("/")
def home():
    return {"message": "Welcome to the Log Intelligence Analyzer API!"}