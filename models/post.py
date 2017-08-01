from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel, metadata

#
# class Post(BaseModel):
#     __tablename__ = 'posts'
#
#     id = Column(Integer, primary_key = True)
#     body = Column(String(140))
#     timestamp = Column(DateTime)
#     user_id = Column(Integer, ForeignKey('user.id'))
#
#     def __repr__(self):
#         return '<Post %r>' % (self.body)


posts = Table('posts', metadata,
    Column('id', Integer, primary_key=True),
    Column('body', String(140), nullable=False),
    Column('timestamp', DateTime()),
    Column('user_id', Integer()),
)
