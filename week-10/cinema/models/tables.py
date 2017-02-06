from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
# from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Float
# from cinema.settings.settings import CONNECTION_STRING, DB_TYPE
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rating = Column(Float)


class Projection(Base):
    __tablename__ = 'projection'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movie.id'))
    projection_type = Column(String(250), nullable=False)
    date = Column(String(250), nullable=False)
    time = Column(String(250), nullable=False)

    # movie = relationship('movie', foreign_keys='Projection.movie_id')


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


class Reservation(Base):
    __tablename__ = 'reservation'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    projection_id = Column(Integer, ForeignKey('projection.id'), nullable=False)
    row = Column(Integer, nullable=False)
    col = Column(Integer, nullable=False)

    # user = relationship('user', foreign_keys='Reservation.user_id')
    # projection = relationship('projection', foreign_keys=[projection_id])


def insert_movies(session):
    movies = [("Max Steel", 4.7),
              ("The light Between Oceans", 2.0),
              ("The man who knew", 5.6),
              ("Strorks", 4.3),
              ("Shooter", 2.1),
              ("The man in the high castel", 2.2),
              ("Cossacks", 5.0)]

    session.add_all([Movie(name=x, rating=y) for x, y in movies])
    session.commit()


def insert_projections(session):
    projec = [(1, '3D', '2016-04-02', '19:00'),
              (3, '2D', '2016-04-05', '19:30'),
              (2, '2D', '2016-04-10', '19:30'),
              (4, '3D', '2016-04-10', '20:00'),
              (3, '3D', '2016-04-12', '20:20'),
              (1, '4DX', '2016-04-13', '20:30'),
              (6, '3D', '2016-04-20', '21:00'),
              (6, '2D', '2016-04-20', '22:00')]
    session.add_all([Projection(movie_id=x, projection_type=y, date=z, time=q) for x, y, z, q in projec])
    session.commit()


if __name__ == '__main__':
    # engine = create_engine('{}:///{}'.format(DB_TYPE, CONNECTION_STRING))
    # Importing in python is weird..
    engine = create_engine('{}:///{}'.format('sqlite', 'cinema/models/cinema.db'))
    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # insert_projections(session)

