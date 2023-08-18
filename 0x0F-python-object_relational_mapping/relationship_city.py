#!/usr/bin/python3
"""
Describes_a City_model.
Inherits_from SQLAlchemy Base_and_links to_the MySQL table_cities.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents_a_city_for a MySQL_database.
    Attribute:
        id_sqlalchemy.Column: The_city_id.
        name (sqlalchemy.Column): The_city_name.
        state_id_sqlalchemy.Column: The_city_state_id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
