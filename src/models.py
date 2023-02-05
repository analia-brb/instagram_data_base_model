import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class Following(Base):
    __tablename__ = 'following'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    following_id = Column(Integer, ForeignKey('following.id'))
    follower_id = Column(Integer, ForeignKey('follower.id'))
    post_id = Column(Integer, ForeignKey('post_id.id'))

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    following_id = Column(Integer, ForeignKey('following.id'))
    follower_id = Column(Integer, ForeignKey('follower.id'))
    user_id = Column(Integer, ForeignKey('user.id'))


    def to_dict(self):
        return {}

render_er(Base, 'diagram.png')

# # Draw from SQLAlchemy base
# try:
#     result = render_er(Base, 'diagram.png')
#     print("Success! Check the diagram.png file")
# except Exception as e:
#     print("There was a problem genering the diagram")
#     raise e
