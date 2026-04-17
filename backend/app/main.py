from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import summarize, health

app = FastAPI()

# ✅ ADD THIS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(summarize.router)