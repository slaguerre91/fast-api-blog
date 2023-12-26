from pydantic import BaseModel, EmailStr
from datetime import datetime

class CreateUser(BaseModel):
    email: EmailStr
    password: str

class User(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True

class UserAuth(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: EmailStr
    token_type: str

class TokenData(BaseModel):
    id: str

class BasePost(BaseModel):
    title: str
    content: str
    published: bool

class CreatePost(BasePost):
    pass

class Post(BasePost):
    id: int
    created_at: datetime
    user_id: int
    author: User
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int

class Vote(BaseModel):
    post_id: int
    dir: int
    class Config:
        orm_mode = True

