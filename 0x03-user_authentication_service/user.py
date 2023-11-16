#!/usr/bin/env python3
"""
Define a User class for authentication
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class User(Base):
    """
    User authentication class
    """
    __tablename__ = 'users'

    id = Column(Integer, autoincrement="auto", primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))
