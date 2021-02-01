from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship

from src.models.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    product = relationship('Product')
    name = Column(String)
    email = Column(String)
    username = Column(String)
    password = Column(String)
    token = Column(String)
    tte = Column(DateTime)
    age = Column(Integer)
    job = Column(String)

    def as_dict(self):
        return {item.name: getattr(self, item.name) for item in self.__table__.columns}

    def __repr__(self):
        return f"id = {self.id}, name = {self.name}, age = {self.age}, job = {self.job}"
