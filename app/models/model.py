from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    user_type_id = Column(Integer, ForeignKey("user_type.id"), default=2)

class UserType(Base):
    __tablename__ = "user_type"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(255))

class QuizTopic(Base):
    __tablename__ = "quiz_topic"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    is_active = Column(Boolean, default=True)
    