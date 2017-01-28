from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from settings import CONNECTION_STRING, DB_TYPE


Base = declarative_base()


class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    balance = Column(Float, default=0)
    message = Column(String(250))
    email = Column(String(250))
    password_reset_token = Column(String(250))

    tan_codes = relationship('TanCode')

    def get_username(self):
        return self.username

    def get_id(self):
        return self.id

    def get_balance(self):
        return self.balance

    def get_message(self):
        return self.message


class TanCode(Base):
    __tablename__ = 'tan_code'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    tan_code = Column(String(250), nullable=False)


if __name__ == '__main__':
    engine = create_engine('{}:///{}'.format(DB_TYPE, CONNECTION_STRING))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    # session = Session()

