from pydantic import BaseModel


class UserInput(BaseModel):
    name: str
    email: str
    token: str = None
    age: int
    job: str
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserRecover(BaseModel):
    username: str
    new_password: str
    token: str


class UserEdit(BaseModel):
    job: str
