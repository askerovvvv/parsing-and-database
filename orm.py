# ORM(Object Relational Mapping - обьектно-реляционное отображение) - технология программирования, которая позволяет связывать БД с концепциями обьектно-ориентированных языков программирования

from parsing import main
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://hello:1@localhost:5432/for_orm")
# engine.connect()

Base = declarative_base()
class Deputy(Base):
    __tablename__= "deputy"
    id = Column(Integer, primary_key = True)
    fullname = Column(String,)
    fraction = Column(String)

    def __init__(self, fullname, fraction):
        self.fullname = fullname
        self.fraction = fraction

Deputy.metadata.create_all(engine)

Session = sessionmaker(engine)
session = Session()

data = main()
# print(data)
for i in data:
    session.add(Deputy(i[0],i[1]))
    session.commit()
