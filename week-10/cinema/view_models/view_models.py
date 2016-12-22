from cinema.models import models
from cinema.settings.settings import CONNECTION_STRING

class ViewModel:
    def __init__(self):
        self.db_model = models.DbContext(CONNECTION_STRING)

    def login(self, username, password):
        return self.db_model.login(username,  password)
