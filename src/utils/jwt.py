from jose import jwt, JWSError, exceptions
from datetime import timedelta, datetime
from pydantic import BaseModel
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Optional

from src.settings import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(user: dict, tte: str = ACCESS_TOKEN_EXPIRE_MINUTES):
    expires = datetime.utcnow() + timedelta(minutes=int(tte))
    data = {"cpf": user.get('cpf'), "exp": expires}
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def decode_jwt(token: str):
    try:
        decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return decoded_jwt
    except exceptions.ExpiredSignatureError as exp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Could not validate token")

