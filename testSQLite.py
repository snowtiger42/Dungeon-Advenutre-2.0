from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo=True)
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

    @classmethod
    def find_by_name(cls, session, name):
        return session.query(cls).filter_by(name=name).all()

    def __repr__(self):
        return f'User {self.name}'


Base.metadata.create_all(engine)
user = User(name='John Snow', password='johnspassword')
session.add(user)

print(user.id)  # None
session.commit()
print(user.id)
query = session.query(User).filter_by(name='John')
query.count()
session.query(User).filter(User.name=='John').first()
session.query(User).filter(User.name.like('%John%')).first()

# from sqlalchemy import Column, Integer, String
#
# class Product(Base):
#     __tablename__ = 'products'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String)

# class User(Base):
#   ...



print(User.find_by_name(session, 'John Snow'))
