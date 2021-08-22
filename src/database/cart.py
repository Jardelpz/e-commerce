from src.utils.transaction import session_scope
from src.models import *


def set_total_cart_value(id: int, total_item: float):
    with session_scope() as db:
        cart = db.query(Cart).filter(Cart.user_id == id).first()
        cart.total += total_item
        db.add(cart)
        return Cart(id=cart.id, user_id=cart.user_id, total=cart.total)


def get_cart_by_user_id(id: int):
    with session_scope() as db:
        cart = db.query(Cart).filter(Cart.user_id == id).first()
        return Cart(id=cart.id, user_id=cart.user_id, total=cart.total)
    pass
