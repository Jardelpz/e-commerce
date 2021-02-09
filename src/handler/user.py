from fastapi import APIRouter

from src.schemas.user import UserInput, UserEdit, UserLogin, UserRecover
from src.utils.database import insert_user, create_user_cart, get_user_by_cpf, list_all_users, update_user_by_id, delete_user_by_id, login, generate_token, recover_password
from src.utils.jwt import create_access_token

user_router = APIRouter()


@user_router.get('/user/list')
async def list_users():
    return {"users": list_all_users()}


@user_router.post('/user/register')
async def send_user(user: UserInput):
    if insert_user(user):
        create_user_cart(get_user_by_cpf(user.cpf))


@user_router.post('/user/login')
async def make_login(user: UserLogin):
    user = login(user)
    if user:
        return create_access_token(user)


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
