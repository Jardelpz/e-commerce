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
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return {"Authenticate": encoded_jwt}


def decode_jwt(token: str):
    exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Could not validate token")
    try:
        decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        # print(decoded_jwt)
        return decoded_jwt
    except exceptions.ExpiredSignatureError as exp:
        raise exception

