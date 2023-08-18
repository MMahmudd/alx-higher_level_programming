#!/usr/bin/python3
"""Script_that prints_the first_State object_from the_database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Creating the_connection_string
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, database_name))

    # Binding the_engine to_the Base_class
    Base.metadata.create_all(engine)

    # Creating a_session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying-for the_first State_object
    first_state = session.query(State).order_by(State.id).first()

    # Displaying_the_result
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Closing_the_session
    session.close()
