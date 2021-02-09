from fastapi import APIRouter

from src.schemas.product import ProductInput
from src.utils.database import insert_product

product_router = APIRouter()


@product_router.post('/product/register')
def register_product(product: ProductInput):
    return insert_product(product)

