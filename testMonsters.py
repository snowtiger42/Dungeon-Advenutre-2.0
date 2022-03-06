from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///:memory:', echo=True)
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from sqlalchemy import Column, Integer, String, ForeignKey

class Monster(Base):
    __tablename__ = 'monsters'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    room_id = Column(Integer, ForeignKey('rooms.id'))

class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    monsters = relationship("Monster")

Base.metadata.create_all(engine)

