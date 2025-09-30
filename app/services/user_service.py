from app.models.model import User
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.utils.util import hash_password

class UserProfile:
    def get_user_by_email(self, db:Session, email: str):
        user_exists = db.query(User).filter(User.email == email).first()
        return user_exists

    def create_user(self, db:Session, user):
        user_exists = self.get_user_by_email(db, user.email)
        if user_exists:
            raise HTTPException(status_code=400, detail="Email already registered")

        hashed_pw = hash_password(user.password)
        db_user = User(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=hashed_pw
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
