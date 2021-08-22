from fastapi import APIRouter, Depends, HTTPException, status
from starlette.responses import JSONResponse

from src.database.cart import set_total_cart_value, get_cart_by_user_id
from src.database.item_cart import insert_item_cart, list_items_cart
from src.database.product import get_product_by_product_id
from src.database.user import get_user_by_cpf
from src.utils.jwt import oauth2_scheme, decode_jwt
from src.schemas.item_cart import ItemCartInput

item_cart_router = APIRouter()


@item_cart_router.post('/item-cart/add')
def add_item(item: ItemCartInput, token: str = Depends(oauth2_scheme)):
    user = get_user_by_cpf(decode_jwt(token).get('cpf'))

    if not user:
        return JSONResponse(status_code=400, content={'Message': 'Token Expired'})

    product = get_product_by_product_id(item.product_id, item.amount)

    if not product:
        return JSONResponse(status_code=400, content={'Message': 'Amount not available'})

    cart = set_total_cart_value(user.id, item.amount * product.price)
    insert_item_cart(item, cart, product)
    return JSONResponse(status_code=200, content={'Message': 'Ok'})


@item_cart_router.get('/item-cart/list')
def list_item_cart(token: str = Depends(oauth2_scheme)):
    user = get_user_by_cpf(decode_jwt(token).get('cpf'))

    cart = get_cart_by_user_id(user.id)
    payload = {
        'items': list_items_cart(cart.id),
        'total_value': cart.total
    }
    return JSONResponse(status_code=200, content=payload)
