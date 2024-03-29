#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """links to the MySQL table cities

    Attributes:
        id(str): The city's id.
        name (sqlalchemy.Integer):The city's name.
        state_id (sqlalchemy.String): The city's state id.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
