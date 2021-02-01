from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from src.models.base import Base


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    price = Column(Float)
    amount = Column(Integer)

    def as_dict(self):
        return {item.name: getattr(self, item.name) for item in self.__table__.columns}

    def __repr__(self):
        return f'{self.name} has {self.amount} units and costs {self.price}'
