from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

from src.settings import DATABASE_URI
from src.models.base import Base
from src.models.user import User
from src.models.product import Product

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    s = Session()
    try:
        yield s
        s.commit()

    except:
        s.rollback()

    finally:
        s.close()


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print(DATABASE_URI)

# recreate_database()