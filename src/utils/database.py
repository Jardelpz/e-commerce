from sqlalchemy import and_
from datetime import datetime, timedelta
from starlette.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_422_UNPROCESSABLE_ENTITY
from starlette.responses import UJSONResponse

from src.utils.transaction import session_scope
from src.schemas.user import UserInput, UserLogin, UserRecover
from src.schemas.category import CategoryInput
from src.models.user import User
from src.models.category import Category
from src.models.product import Product
from src.models.item_cart import ItemCart
from src.models.cart import Cart
from src.utils.crypt import encrypt, decrypt
from src.utils import random_token
from src.utils.send_email import send_email

# -----------------------------   user    -------------------------------------- #


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
        return True
    return False


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
    return None


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
        return "Password updated with success"
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


def get_category_by_id(id: int):
    with session_scope() as db:
        category = db.query(Category).filter(Category.id == id).first()
        return Category(id=category.id, name=category.name, description=category.description)
    pass
# -----------------------------   category    -------------------------------------- #


def insert_category(category):
    with session_scope() as db:
        cat = Category(name=category.name, description=category.description)
        db.add(cat)
        return "Category created", HTTP_200_OK
    pass

# -----------------------------   product    -------------------------------------- #


def insert_product(product):
    with session_scope() as db:
        category = get_category_by_id(product.category_id)
        p = Product(category_id=category.id, name=product.name, amount=product.amount, price=product.price)
        db.add(p)
        return f"{p.name} inserted with success"
    pass


def get_product_by_product_id(id: int, item_amount):
    with session_scope() as db:
        product = db.query(Product).filter(
            and_(
                Product.id == id,
                Product.amount >= item_amount
                )
            ).first()
        if product:
            return Product(id=product.id, category_id=product.category_id, name=product.name, amount=product.amount, price=product.price)
        return None


def get_cart_by_user_id(id: int, total_item: float):
    with session_scope() as db:
        cart = db.query(Cart).filter(Cart.user_id == id).first()
        cart.total += total_item
        db.add(cart)
        return Cart(id=cart.id, user_id=cart.user_id, total=cart.total)


def insert_item_cart(item, cart, product):
    with session_scope() as db:
        item_cart = db.query(ItemCart).join(Cart).filter(
            and_(
                ItemCart.product_id == product.id,
                ItemCart.cart_id == cart.id
                )
            ).first()
        if item_cart:
            item_cart.total += product.price * item.amount
            item_cart.amount += item.amount
        else:
            item_cart_total = product.price * item.amount
            item_cart = ItemCart(product_id=product.id, cart_id=cart.id, value=product.price,
                                 amount=item.amount, total=item_cart_total)

        db.add(item_cart)
        return
    pass


# def sum_all_itens_cart(item, cart, product):
#     with session_scope() as db:
#         total = product.price * item.amount
#         item_cart = ItemCart(product_id=item.id, cart_id=cart.id, value=product.value,
#                              amount=item.amount, total=total)
#         # somar os totais dos itens e dar um update no cart
#         cart = Cart(id=cart.id, user_id=cart.user_id, total=)
#         # db.add(p)
#         return,
#     pass