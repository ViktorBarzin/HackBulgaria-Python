import cinema.helpers.queries.insertion_queries as insert
# import cinema.helpers.queries.update_queries as update
import cinema.helpers.queries.delete_queries as delete
import cinema.helpers.queries.select_queries as select
import sqlite3


class DbContext:
    def __init__(self, connection_string):
        self.db = sqlite3.connect(connection_string)
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()

    def login(self, username, password):
        result = self.cursor.execute(select.VALIDATE_USER, (username, ))
        user = result.fetchone()
        # Add an Is_Active field to stop logging multiple times
        if user is not None and user['PASSWORD'] == password:
            return True
        return False

    def register(self, username, password):
        self.cursor.execute(insert.REGISTER, (username, password))
        self.db.commit()

    def show_all_movies(self):
        return self.cursor.execute(select.SHOW_ALL_MOVIES).fetchall()

    def get_all_projections_for(self, movie_id):
        result = self.cursor.execute(select.SELECT_PROJECTIONS_FOR_MOVIE, (movie_id,))
        return result.fetchall()

    def create_reservation(self, user_id, projection_id, row, col):
        self.cursor.execute(insert.CREATE_RESERVATION, (user_id, projection_id, row, col))
        self.db.commit()

    def get_user_id(self, username):
        return self.cursor.execute(select.GET_USER_ID_FROM_USERNAME, (username,)).fetchone()['ID']

    def get_all_reservations_for_projection(self, projection_key):
        return self.cursor.execute(select.GET_ALL_RESERVATIONS_FOR_PROJECTION, (projection_key,)).fetchall()

    def get_all_user_reversations(self, user_id):
        # Returns : Rows<reservation.id, movie.name, projection.date,
        # projection.time>
        return self.cursor.execute(select.GET_ALL_PROJECTIONS_RESERVATIONS_MOVIES_FOR_USER, (user_id,)).fetchall()

    def delete_reservation(self, user_id, projection_key):
        result = self.cursor.execute(delete.DELETE_RESERVATION, (projection_key, user_id))
        self.db.commit()
        return result