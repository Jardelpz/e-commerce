from fastapi import APIRouter

from src.schemas.category import CategoryInput
from src.utils.database import insert_category

category_router = APIRouter()


@category_router.post('/category')
def post_category(category: CategoryInput):
    return insert_category(category)
