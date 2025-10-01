from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.dependency import get_db
from app.services.user_service import UserProfile
from app.schemas.schema import UserCreate, UserResponse, UserResponseWrapper

router = APIRouter(tags=['User'])
user_profile = UserProfile()

@router.post("/register", response_model=UserResponseWrapper)
async def register(user: UserCreate, db:Session = Depends(get_db)):
    try:
        created_user = user_profile.create_user(db, user)
        response = UserResponseWrapper(
                user=UserResponse(
                id=created_user.id,
                email=created_user.email,
                first_name=f"{created_user.first_name}",
                last_name=f"{created_user.last_name}"
            )
        )
        return response
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error creating user: {str(e)}"
        )