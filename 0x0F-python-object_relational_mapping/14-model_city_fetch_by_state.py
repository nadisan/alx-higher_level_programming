#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa
Usage: ./7-model_state_fetch_all.py <mysql username> /
                                     <mysql password> /
                                     <database name>"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State)\
                               .filter(City.state_id == State.id)\
                               .order_by(City.id):
        print("{}: {} {}".format(state.name, city.id, city.name))
