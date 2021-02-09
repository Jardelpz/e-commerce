from sqlalchemy import Column, Integer, String, ForeignKey, Float
from src.models.base import Base
from src.models.user import User


class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    total = Column(Float)

    def as_dict(self):
        return {item.name: getattr(self, item.name) for item in self.__table__.columns}

    def __repr__(self):
        return f'This cart costs R$ {self.total}'
