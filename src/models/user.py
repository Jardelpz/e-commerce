from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship

from src.models.base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String)
    email = Column(String)
    cpf = Column(String(11))
    username = Column(String)
    password = Column(String)
    token = Column(String)
    tte = Column(DateTime)
    age = Column(Integer)
    job = Column(String)
    zip_code = Column(String)
    complement = Column(String)
    neighborhood = Column(String)
    adress_number = Column(String)
    phone = Column(String)


    def as_dict(self):
        return {item.name: getattr(self, item.name) for item in self.__table__.columns}

    def __repr__(self):
        return f"id = {self.id}, name = {self.name}, age = {self.age}, job = {self.job}"

