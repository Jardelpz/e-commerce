from src.utils.transaction import session_scope
from src.models import *


def insert_category(category):
    with session_scope() as db:
        cat = Category(name=category.name, description=category.description)
        db.add(cat)


def get_category_by_id(id: int):
    with session_scope() as db:
        category = db.query(Category).filter(Category.id == id).first()
        return Category(id=category.id, name=category.name, description=category.description)
    pass
