from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .base import BaseModel, metadata


# class User(BaseModel):
#     __tablename__ = 'users'
#
#     id = Column(Integer, primary_key=True)
#     login = Column(String(64), index=True, unique=True)
#     name = Column(String(300), index=True)
#     email = Column(String(300))
#     password = Column(String(64))
#     #posts = relationship('Post', backref='author', lazy='dynamic')
#



users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('login', String(64), nullable=False),
    Column('name', String(300), nullable=False),
    Column('email', String(300), nullable=False),
    Column('password', String(64)),
)