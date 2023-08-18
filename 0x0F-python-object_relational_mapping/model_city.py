#!/usr/bin/python3
"""
Explaination a_City_model.
Inherits_from SQLAlchemy Base_and_links to_the_MySQL table_cities.
 """

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Representation_a city for_a_MySQL database.
    Attribute:
        id (str): The_city_id.
        name (sqlalchemy.Integer): The_city_name.
        state_id (sqlalchemy.String): The_city_state_id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
