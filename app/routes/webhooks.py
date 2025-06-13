from fastapi import APIRouter, Request, HTTPException
from supabase import create_client, Client
import os
from dotenv import load_dotenv
from svix.webhooks import Webhook
import json

load_dotenv()

router = APIRouter()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
CLERK_WEBHOOK_SECRET = os.getenv("CLERK_WEBHOOK_SECRET")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@router.post("/webhooks/clerk")
async def clerk_webhook(request: Request):
    raw_body = await request.body()
    headers = {
        "svix-id": request.headers.get("svix-id"),
        "svix-timestamp": request.headers.get("svix-timestamp"),
        "svix-signature": request.headers.get("svix-signature"),
    }

    if not all(headers.values()):
        raise HTTPException(status_code=400, detail="Missing Svix headers")

    webhook = Webhook(CLERK_WEBHOOK_SECRET)
    try:
        webhook.verify(raw_body, headers)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid signature")

    parsed_body = json.loads(raw_body.decode("utf-8"))
    event_type = parsed_body.get("type")
    data = parsed_body.get("data", {})

    if event_type not in ["user.created", "user.updated"]:
        return {"message": f"Ignored event: {event_type}"}

    try:
        # Accept fields from the webhook payload
        user_record = {
            "clerk_user_id": data.get("id"),
            "email": data.get("email_addresses", [{}])[0].get("email_address"),
            "first_name": data.get("first_name", ""),
            "last_name": data.get("last_name", "")
        }

        # Upsert user based on clerk_user_id
        result = supabase.table("users").upsert(
            user_record,
            on_conflict="clerk_user_id"
        ).execute()

        return {"message": "User synced successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Supabase error: {str(e)}")