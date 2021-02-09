from fastapi import APIRouter, Depends, HTTPException, status

from src.utils.database import get_user_by_cpf, get_cart_by_user_id, insert_item_cart, get_product_by_product_id
from src.utils.jwt import oauth2_scheme, decode_jwt
from src.schemas.item_cart import ItemCartInput

item_cart_router = APIRouter()


@item_cart_router.post('/item-cart/add')
def add_item(item: ItemCartInput, token: str = Depends(oauth2_scheme)):
    try:
        user = get_user_by_cpf(decode_jwt(token).get('cpf'))
        product = get_product_by_product_id(item.product_id, item.amount)

        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="token expired")

        if not product:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="amount not available")

        cart = get_cart_by_user_id(user.id, item.amount * product.price)
        insert_item_cart(item, cart, product)
        return "Registered with success"
    except HTTPException as e:
        return e.detail
