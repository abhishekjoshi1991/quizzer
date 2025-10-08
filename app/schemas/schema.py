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

class QuizTopicCreateRequest(BaseModel):
    name: list[str]

class QuizTopicResponse(BaseModel):
    id: int
    name: str
    is_active: bool

class QuizTopicResponseWrapper(BaseModel):
    topics: list[QuizTopicResponse]
    message: str = "Quiz topics fetched successfully"

class QuizTopicUpdateRequest(BaseModel):
    id: int
    name: str
    is_active: bool
