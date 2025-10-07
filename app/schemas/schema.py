from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    first_name : str
    last_name : str
    email : EmailStr

class UserCreate(UserBase):
    password : str

class UserResponse(UserBase):
    id : int

class UserResponseWrapper(BaseModel):
    user: UserResponse

class UserLogin(BaseModel):
    email : EmailStr
    password : str

class UserTypeSchema(BaseModel):
    id: int