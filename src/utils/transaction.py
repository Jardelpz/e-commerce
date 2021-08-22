from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from starlette.responses import JSONResponse

from src.settings import DATABASE_URI
from src.models import *

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    s = Session()
    try:
        yield s
        s.commit()

    except Exception as e:
        s.rollback()
        print(e)

    finally:
        s.close()


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print(DATABASE_URI)


# recreate_database()
#