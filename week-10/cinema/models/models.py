from cinema.settings.settings import DB_TYPE, CONNECTION_STRING
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from cinema.models.tables import User, Movie, Projection, Reservation


class DbContext:
    def __init__(self, connection_string):
        self.engine = create_engine('{}:///{}'.format(DB_TYPE, CONNECTION_STRING))
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        # self.db = sqlite3.connect(connection_string)
        # self.db.row_factory = sqlite3.Row
        # self.cursor = self.db.cursor()

    def login(self, username, password):
        user = self.session.query(User).filter(User.username == username).first()
        # result = self.cursor.execute(select.VALIDATE_USER, (username, ))
        # user = result.fetchone()
        # Add an Is_Active field to stop logging multiple times
        if user is not None and user.password == password:
            return True
        return False

    def register(self, username, password):
        user = User(username=username, password=password)
        self.session.add(user)
        self.session.commit()
        # self.cursor.execute(insert.REGISTER, (username, password))
        # self.db.commit()

    def show_all_movies(self):
        return self.session.query(Movie).all()
        # return self.cursor.execute(select.SHOW_ALL_MOVIES).fetchall()

    def get_all_projections_for(self, movie_id):
        return self.session.query(Projection).filter(Projection.movie_id == movie_id).all()
        # result = self.cursor.execute(select.SELECT_PROJECTIONS_FOR_MOVIE, (movie_id,))
        # return result.fetchall()

    def create_reservation(self, user_id, projection_id, row, col):
        reservation = Reservation(user_id=user_id, projection_id=projection_id, row=row, col=col)
        self.session.add(reservation)
        self.session.commit()
        # self.cursor.execute(insert.CREATE_RESERVATION, (user_id, projection_id, row, col))
        # self.db.commit()

    def get_user_id(self, username):
        return self.session.query(User).filter(User.username == username).first().id
        # return self.cursor.execute(select.GET_USER_ID_FROM_USERNAME, (username,)).fetchone()['ID']

    def get_all_reservations_for_projection(self, projection_key):
        return self.session.query(Reservation).filter(Reservation.projection_id == projection_key).all()
        # return self.cursor.execute(select.GET_ALL_RESERVATIONS_FOR_PROJECTION, (projection_key,)).fetchall()

    def get_all_user_reversations(self, user_id):
        result = self.session.query(Reservation, Projection, Movie).filter(Reservation.user_id == user_id).filter(Reservation.projection_id == Projection.id).filter(Movie.id == Projection.movie_id).all()
        print(result)
        return result
        # Returns : Rows<reservation.id, movie.name, projection.date,
        # projection.time>
        # return self.cursor.execute(select.GET_ALL_PROJECTIONS_RESERVATIONS_MOVIES_FOR_USER, (user_id,)).fetchall()

    def delete_reservation(self, user_id, projection_key):
        reservation_to_del = self.session.query(Reservation).filter(Reservation.user_id == user_id and Reservation.projection_id == projection_key).first()
        if not reservation_to_del:
            raise ValueError('No such reservation!')
        self.session.delete(reservation_to_del)
        self.session.commit()
        return reservation_to_del
        # result = self.cursor.execute(delete.DELETE_RESERVATION, (projection_key, user_id))
        # self.db.commit()
        # return result
