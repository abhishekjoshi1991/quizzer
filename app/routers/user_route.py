from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.dependency import get_db
from app.services.user_service import UserProfile
from app.schemas.schema import UserCreate, UserResponse

router = APIRouter(tags=['User'])
user_profile = UserProfile()

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate, db:Session = Depends(get_db)):
    try:
        return user_profile.create_user(db, user)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error creating user: {str(e)}"
        )