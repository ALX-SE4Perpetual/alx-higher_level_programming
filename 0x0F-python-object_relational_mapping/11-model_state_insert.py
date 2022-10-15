#!/usr/bin/python3
"""
Add the State object “Louisiana” to the database hbtn_0e_6_usa
"""


if __name__ = "__main__":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sys import argv

    if (len(argv) != 4):
        print('Use: username, password database_name')
        exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    new_instance = session.query(State).filter_by(name='Louisiana').first()
    print(new_instance.id)
    session.commit()
    session.close()
