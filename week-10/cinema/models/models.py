import cinema.helpers.queries.insertion_queries as insert
import cinema.helpers.queries.update_queries as update
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
        print(password, user['PASSWORD'])
        if user is not None and user['PASSWORD'] == password:
            return True
        return False
    
    def register(self, username, password):
        self.cursor.execute(insert.REGISTER, (username, password))
        self.db.commit()
