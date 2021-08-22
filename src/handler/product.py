from fastapi import APIRouter
from starlette.responses import JSONResponse

from src.schemas.product import ProductInput
from src.database.category import get_category_by_id
from src.database.product import insert_product, get_products_by_category

product_router = APIRouter()


@product_router.post('/product/register')
def register_product(product: ProductInput):
    category = get_category_by_id(product.category_id)
    if category:
        return insert_product(product, category)
    return {}


@product_router.get('/product/list/{category}')
def get_by_category(category: int):
    products = get_products_by_category(category)
    return JSONResponse(status_code=200, content={'products': products})


