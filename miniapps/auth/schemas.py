from typing import Optional
from pydantic import BaseModel, EmailStr

class LoginIn(BaseModel):
    email = EmailStr()

class LoginOut(BaseModel):
    success: bool

class VerifyIn(BaseModel):
    token: str

class VerifyOut(BaseModel):
    success: bool
    access_token: Optional[str]
    refresh_token: Optional[str]

class RefreshIn(BaseModel):
    token: str

class RefreshOut(BaseModel):
    success: bool
    access_token: Optional[str]
    refresh_token: Optional[str]
