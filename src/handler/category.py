from fastapi import APIRouter

from starlette.responses import JSONResponse
from src.schemas.category import CategoryInput
from src.database.category import insert_category

category_router = APIRouter()


@category_router.post('/category')
def post_category(category: CategoryInput):
    insert_category(category)
    return JSONResponse(status_code=200, content={'message': 'OK'})
