from pydantic import BaseModel


class ItemCartInput(BaseModel):
    product_id: int
    amount: int
