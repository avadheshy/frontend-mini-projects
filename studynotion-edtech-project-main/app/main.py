from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.core.config import settings
from app.db.mongodb import get_database

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup() -> None:
    db = get_database()
    await db.otps.create_index("createdAt", expireAfterSeconds=60 * 5)


@app.get("/")
async def root() -> dict[str, str]:
    return {"success": True, "message": "Your server is up and running ..."}


app.include_router(api_router, prefix=settings.api_v1_str)
