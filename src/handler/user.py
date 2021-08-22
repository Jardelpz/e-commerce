from fastapi import APIRouter

from src.schemas.user import UserInput, UserEdit, UserLogin, UserRecover
from src.database.user import insert_user, create_user_cart, get_user_by_cpf, list_all_users, update_user_by_id, delete_user_by_id, login, generate_token, recover_password
from src.utils.jwt import create_access_token
from src.utils.email import is_valid_email
from starlette.responses import JSONResponse
from src.utils.email import send_email

user_router = APIRouter()


@user_router.get('/user/list')
async def list_users():
    return JSONResponse(status_code=200, content={'Users': list_all_users()})


@user_router.post('/user/register')
async def send_user(user: UserInput):
    insert_user(user)
    create_user_cart(get_user_by_cpf(user.cpf))


@user_router.post('/user/login')
async def make_login(user: UserLogin):
    user = login(user)
    if user:
        return JSONResponse(status_code=200, content={'Authenticate': create_access_token(user)})

    return JSONResponse(status_code=404, content={'message': 'User not found'})


@user_router.delete('/user/{user_id}/delete')
async def delete_user(user_id):
    return delete_user_by_id(user_id)


@user_router.patch('/user/{user_id}/edit')
async def edit_user(user_id: int, user: UserEdit):
    return update_user_by_id(user_id, user.job)


@user_router.get('/user/recover/{email}')
async def token(email):
    if not is_valid_email(email):
        return JSONResponse(status_code=400, content={'message': 'Incorrect email format'})

    new_token = generate_token(email)
    try:
        send_email(new_token, email)
        return JSONResponse(status_code=200, content={'message': 'Email sent!'})
    except Exception as e:
        return JSONResponse(status_code=400, content={'message': 'Error sending email'})


@user_router.post('/user/recover')
async def token(user: UserRecover):
    if not recover_password(user):
        return JSONResponse(status_code=404, content={'message': 'information not found'})

    return JSONResponse(status_code=200, content={'message': 'OK'})