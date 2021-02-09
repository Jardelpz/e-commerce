from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime
from datetime import datetime

DeclarativeBase = declarative_base()


def get_now():
    return datetime.now()


class Base(DeclarativeBase):
    __abstract__ = True
    created_at = Column(DateTime, default=get_now())
    updated_at = Column(DateTime, onupdate=get_now())
