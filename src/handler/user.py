from fastapi import APIRouter
from starlette.responses import UJSONResponse

from src.schemas.user import UserInput, UserEdit, UserLogin, UserRecover
from src.utils.database import insert_user, list_all_users, update_user_by_id, delete_user_by_id, login, generate_token, recover_password
from src.models.user import User

user_router = APIRouter()


@user_router.get('/user/list')
async def list_users():
    users = list_all_users()
    return {"users": users}


@user_router.post('/user/register')
async def send_user(user: UserInput):
    resp = insert_user(user)
    return resp


@user_router.post('/user/login')
async def make_login(user: UserLogin):
    resp = login(user)
    return resp


@user_router.delete('/user/{user_id}/delete')
async def delete_user(user_id):
    return delete_user_by_id(user_id)


@user_router.patch('/user/{user_id}/edit')
async def edit_user(user_id: int, user: UserEdit):
    return update_user_by_id(user_id, user.job)


@user_router.get('/user/recover/{email}')
async def token(email):
    return generate_token(email)


@user_router.post('/user/recover')
async def token(user: UserRecover):
    return recover_password(user)
