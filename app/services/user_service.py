from app.models.model import User, UserType
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.utils.util import hash_password, verify_password

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

    def validate_user(self, db:Session, user):
        user_exists = self.get_user_by_email(db, user.email)
        if not user_exists:
            raise HTTPException(status_code=400, detail="User does not exists.")
        else:
            hashed_pw = verify_password(user.password, user_exists.password)
            if hashed_pw:
                db_user = User(
                    id=user_exists.id,
                    first_name=user_exists.first_name,
                    last_name=user_exists.last_name,
                    email=user.email
                )
                return db_user
            else:
                raise HTTPException(status_code=400, detail="Password do not match.")
    
    def get_user_type(self, db:Session, user_id: int):
        # Join UserType to User to fetch the type string for the provided user id
        user_type_row = (
            db.query(UserType)
            .join(User, User.user_type_id == UserType.id)
            .filter(User.id == user_id)
            .first()
        )

        if not user_type_row:
            raise HTTPException(status_code=400, detail="User does not exists.")

        return user_type_row.type

