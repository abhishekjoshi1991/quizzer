from app.schemas.schema import UserCreate, UserResponse
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependency import get_db

router = APIRouter(tags=['User'])

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate, db:Session = Depends(get_db)):
    pass