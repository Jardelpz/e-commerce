from sqlalchemy import and_

from src.utils.transaction import session_scope
from src.models import *


def insert_product(product, category):
    with session_scope() as db:
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


def get_products_by_category(category: int):
    products = []
    with session_scope() as db:
        for product in db.query(Product).filter(Product.category_id == category).all():
            products.append(product.as_dict())

    return products if products else []
