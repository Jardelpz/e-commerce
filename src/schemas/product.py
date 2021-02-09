from pydantic import BaseModel


class ProductInput(BaseModel):
    name: str
    price: float
    amount: int
    category_id: int
