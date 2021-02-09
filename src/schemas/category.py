from pydantic import BaseModel


class CategoryInput(BaseModel):
    name: str
    description: str
