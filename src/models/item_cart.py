from sqlalchemy import Column, Integer, Float, ForeignKey
from src.models.base import Base
from src.models.product import Product
from src.models.cart import Cart


class ItemCart(Base):
    __tablename__ = "item_cart"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey(Product.id))
    cart_id = Column(Integer, ForeignKey(Cart.id))
    amount = Column(Integer)
    value = Column(Float)
    total = Column(Float)

    def as_dict(self):
        return {item.name: getattr(self, item.name) for item in self.__table__.columns}
