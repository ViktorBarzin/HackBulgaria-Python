from cinema.models import models
from cinema.settings.settings import CONNECTION_STRING
from cinema.settings.settings import LOG_FILE as LOG_FILE
from cinema.helpers.decorators import hash_password, log


class ViewModel:
    def __init__(self):
        self.db_model = models.DbContext(CONNECTION_STRING)

    @hash_password
    def login(self, username, password):
        return self.db_model.login(username, password)

    @log(LOG_FILE, 'Registered a new user!')
    @hash_password
    def register(self, username, password):
        # TODO: hash password and verify it
        return self.db_model.register(username, password)

    def show_all_movies(self):
        return self.db_model.show_all_movies()

    def show_projections_for_movie(self, movie_id, date=''):
        all_projections = self.db_model.get_all_projections_for(movie_id)
        if date == '':
            return all_projections
        result = []
        for projection in all_projections:
            # Add some sort or verification of date?
            if projection['DATE'] == date:
                result.append(projection)
        return result

    @log(LOG_FILE, 'Created new reservation!')
    def create_reservation(self, user_id, projection_id, row, col):
        # Check if there is no such reservation already
            # Perhaps save all_projections to class to avoid searching the db for
            # every reservation
        all_projections = [(x['ROW'], x['COL']) for x in self.db_model.get_all_reservations_for_projection(projection_id)]
        if (row, col) in all_projections:
            return False
        self.db_model.create_reservation(user_id, projection_id, row, col)
        return True

    def get_user_id(self, username):
        return self.db_model.get_user_id(username)

    def get_all_user_reservations(self, user_id):
        return self.db_model.get_all_user_reversations(user_id)

    @log(LOG_FILE, 'A reservation was deleted!')
    def cancel_registration(self, user_id, projection_key):
        return self.db_model.delete_reservation(user_id, projection_key)
