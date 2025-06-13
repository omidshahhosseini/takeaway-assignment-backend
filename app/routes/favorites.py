from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from config import supabase

router = APIRouter()

class FavoriteRestaurants(BaseModel):
    restaurant_ids: List[str]
    clerk_user_id: str

@router.post("/favorites", operation_id="saveFavoriteRestaurants")
async def save_favorite_restaurants(favorites: FavoriteRestaurants):
    try:
        result = supabase.table("users").update({
            "favorites_restaurants": favorites.restaurant_ids
        }).eq("clerk_user_id", favorites.clerk_user_id).execute()
        
        if not result.data:
            raise HTTPException(status_code=404, detail="User not found")
            
        return {"message": "Favorite restaurants updated successfully"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/favorites/{clerk_user_id}", operation_id="getFavoriteRestaurants")
async def get_favorite_restaurants(clerk_user_id: str):
    try:
        result = supabase.table("users").select("favorites_restaurants").eq("clerk_user_id", clerk_user_id).execute()
        
        if not result.data:
            raise HTTPException(status_code=404, detail="User not found")
            
        favorite_restaurants = result.data[0].get("favorites_restaurants", [])
        return {"favorite_restaurants_ids": favorite_restaurants}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 