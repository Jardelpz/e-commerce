from sqlalchemy import and_
from datetime import datetime, timedelta

from src.utils.transaction import session_scope
from src.models import *
from src.utils.crypt import encrypt
from src.utils import random_token
from src.utils.email import send_email


def insert_user(user):
    with session_scope() as db:
        user_to_insert = User()
        user_to_insert.name = user.name
        user_to_insert.age = user.age
        user_to_insert.email = user.email
        user_to_insert.job = user.job
        user_to_insert.cpf = user.cpf
        user_to_insert.username = user.username
        user_to_insert.password = encrypt(user.password)
        user_to_insert.zip_code = user.zip_code
        user_to_insert.complement = user.complement
        user_to_insert.neighborhood = user.neighborhood
        user_to_insert.adress_number = user.adress_number
        user_to_insert.phone = user.phone
        db.add(user_to_insert)
        return user


def login(user):
    with session_scope() as db:
        encode_password = encrypt(user.password)
        user = db.query(User).filter(
            and_(
                User.username == user.username,
                User.password == encode_password
            )
        ).first()

        user = user.as_dict()
        return user


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
        return "deleted with success"
    pass


def update_user_by_id(id: int, job: str):
    with session_scope() as db:
        user = db.query(User).filter(User.id == id).first()
        user.job = job
        db.add(user)
        return "updated"
    pass


def create_user_cart(user):
    with session_scope() as db:
        cart = Cart(user_id=user.id, total=0)
        db.add(cart)
        return
    pass


def generate_token(email):
    new_token = random_token()
    with session_scope() as db:
        user = db.query(User).filter(User.email == email).first()
        user.token = new_token
        user.tte = datetime.now() + timedelta(minutes=5)
        db.add(user)

        return new_token

    raise Exception('Error sending email')


def recover_password(user_recover):
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
        return True
    pass

def get_user_by_id(id: int):
    with session_scope() as db:
        user = db.query(User).filter(User.id == id).first()
        return User(id=user.id, name=user.name, age=user.age, job=user.job)
    pass


def get_user_by_cpf(cpf: str):
    with session_scope() as db:
        user = db.query(User).filter(User.cpf == cpf).first()
        return User(id=user.id, name=user.name, age=user.age, job=user.job)
    pass


