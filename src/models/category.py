from sqlalchemy import Column, Integer, String

from src.models.base import Base


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def as_dict(self):
        return {item.name: getattr(self, item.name) for item in self.__table__.columns}

    def __repr__(self):
        return f'{self.description}'
