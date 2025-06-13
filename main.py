#  uvicorn main:app
#  uvicorn main:app --reload
#  source venv/bin/activate
#  python3 -m venv venv
#  pip install -r requirements.txt

from fastapi import FastAPI
import os
from dotenv import load_dotenv
from app.routes import webhooks, favorites
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

# Define allowed origins
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
    "https://takeaway-assignment-backend.vercel.app/",
]

app = FastAPI(
    title="Takeaway Backend",
    description="Backend API for Takeaway application",
    version="1.0.0"
)

# Add CORS middleware with specific configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=[
        "Content-Type",
        "Authorization",
        "Accept",
        "Origin",
        "X-Requested-With",
        "svix-id",
        "svix-timestamp",
        "svix-signature"
    ],
    max_age=3600,  # Cache preflight requests for 1 hour
)

app.include_router(webhooks.router)
app.include_router(favorites.router, prefix="/api/v1", tags=["favorites"])
