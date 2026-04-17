from fastapi import FastAPI
from app.core.config import settings
from app.routes import summarize, health

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

app.include_router(health.router)
app.include_router(summarize.router)

@app.get("/")
async def root():
    return {"message": "API is running 🚀"}