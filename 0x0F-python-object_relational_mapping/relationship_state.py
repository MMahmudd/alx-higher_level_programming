#!/usr/bin/python3
"""
Explaines_a_Stat_ model.
Inherits_from SQLAlchemy Base_and_links to_the MySQL table_states.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """Represents_a_state_for a MySQL database.
    Attribute:
        __tablename__ (str): The_name_of_the MySQL table_to_store_States.
        id_sqlalchemy.Integer: The_state_id.
        name_sqlalchemy.String: The_state_name.
        cities_sqlalchemy.orm.relationship: The_State-City_relationship.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
