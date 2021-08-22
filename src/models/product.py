from sqlalchemy import Column, Integer, String, Float, ForeignKey
from datetime import datetime

from src.models.base import Base
from src.models.category import Category


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey(Category.id))
    name = Column(String)
    price = Column(Float)
    amount = Column(Integer)

    def as_dict(self):
        return {item.name: getattr(self, item.name) for item in self.__table__.columns if not isinstance(getattr(self, item.name), datetime)}

    def __repr__(self):
        return f'{self.name} has {self.amount} units and costs {self.price}'
