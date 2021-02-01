from sqlalchemy import and_
from datetime import datetime, timedelta
from starlette.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_422_UNPROCESSABLE_ENTITY
from starlette.responses import UJSONResponse

from src.utils.transaction import session_scope
from src.schemas.user import UserInput, UserLogin, UserRecover
from src.models.user import User
from src.models.product import Product
from src.utils.crypt import encrypt, decrypt
from src.utils import random_token
from src.utils.send_email import send_email


def insert_user(user: UserInput):
    with session_scope() as db:
        user_to_insert = User(name=user.name, age=user.age, email=user.email, job=user.job, username=user.username,
                              password=encrypt(user.password))
        db.add(user_to_insert)
        return f"{user.name} inserted with success", HTTP_200_OK
    pass


def login(user: UserLogin):
    with session_scope() as db:
        encode_password = encrypt(user.password)
        user = db.query(User).filter(
            and_(
                User.username == user.username,
                User.password == encode_password
            )
        ).first()

        user = user.as_dict()
        return f"{user.get('name')} is logged in!"
    return "Bad login, try again"


def list_all_users():
    users_list = []
    with session_scope() as db:
        for user in db.query(User).all():
            users_list.append(user.as_dict())
        return users_list
    pass


def delete_user_by_id(id: int):
    with session_scope() as db:
        user = db.query(User).filter(User.id == id).first()
        db.delete(user)
        return "delete with success"
    pass


def update_user_by_id(id: int, job: str):
    with session_scope() as db:
        user = db.query(User).filter(User.id == id).first()
        user.job = job
        db.add(user)
        return "updated"
    pass


def generate_token(email):
    new_token = random_token()
    with session_scope() as db:
        user = db.query(User).filter(User.email == email).first()
        user.token = new_token
        user.tte = datetime.now() + timedelta(minutes=5)
        db.add(user)
        send_email(new_token, email)
        return new_token

    return "User Not Found", 204


def recover_password(user_recover: UserRecover):
    with session_scope() as db:
        user = db.query(User).filter(
            and_(
                User.username == user_recover.username,
                User.token == user_recover.token,
                User.tte > datetime.now()
            )
        ).first()
        user.token = None
        user.tte = None
        user.password = encrypt(user_recover.new_password)
        db.add(user)
        return "Password updated with success"
    pass


def get_user_by_id(id: int):
    with session_scope() as db:
        user = db.query(User).filter(User.id == id).first()
        return User(id=user.id, name=user.name, age=user.age, job=user.job)
    pass


# -----------------------------   products    -------------------------------------- #

def insert_product(product):
    with session_scope() as db:
        user = get_user_by_id(product.user_id)
        p = Product(user_id=user.id, name=product.name, amount=product.amount, price=product.price)
        db.add(p)
        return f"{p.name} inserted with success"
    pass


def list_all_products_by_user(id: int):
    products_list = []
    with session_scope() as db:
        for product in db.query(Product).filter(Product.user_id == id).all():
            products_list.append(product.as_dict())
        return products_list
    pass
