from sqlalchemy.orm.session import sessionmaker

from .user import users
from .post import posts


Session = sessionmaker()
session = Session()