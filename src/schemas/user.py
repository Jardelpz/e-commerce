from pydantic import BaseModel


class UserInput(BaseModel):
    name: str
    email: str
    token: str = None
    age: int
    job: str
    cpf: str
    username: str
    password: str
    zip_code: str
    complement: str
    adress_number: str
    neighborhood: str
    phone: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserRecover(BaseModel):
    username: str
    new_password: str
    token: str


class UserEdit(BaseModel):
    job: str
