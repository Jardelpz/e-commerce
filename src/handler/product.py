from fastapi import APIRouter

from src.schemas.product import ProductInput
from src.utils.database import insert_product, list_all_products_by_user

product = APIRouter()


@product.get('/product/list/user/{user_id}')
def list_product_by_user(user_id):
    products = list_all_products_by_user(user_id)
    return {"Products": products}


@product.post('/product/register')
def register_product(product: ProductInput):
    insert_product(product)

