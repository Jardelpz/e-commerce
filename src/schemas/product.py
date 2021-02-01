from pydantic import BaseModel


class ProductInput(BaseModel):
    user_id: int
    name: str
    price: float
    amount: int