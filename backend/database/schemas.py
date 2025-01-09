from datetime import datetime
from pydantic import BaseModel, UUID4


class FileBase(BaseModel):
    file_path: str


class UserBase(BaseModel):
    username: str
    fullname: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: UUID4
    is_active: bool

    class Config:
        from_attributes = True


class UserRoleBase(BaseModel):
    name: str


class UserRole(UserRoleBase):
    id: UUID4
