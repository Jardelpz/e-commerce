from sqlalchemy import and_

from src.utils.transaction import session_scope
from src.models import *


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


def list_items_cart(cart):
    list_items = []
    with session_scope() as db:
        for item in db.query(ItemCart).join(Cart).filter(ItemCart.cart_id == cart).all():
            list_items.append(item.as_dict())

    return list_items
