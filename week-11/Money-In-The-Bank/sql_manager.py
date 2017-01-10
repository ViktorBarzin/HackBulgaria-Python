import sqlite3
import creation_queries as create_db
import update_queries as update
import select_queries as select
import insert_queries as insert
from decorators import hash_password, check_password_requirments, check_username_requirements
from settings import CONNECTION_STRING
from client import Client


class Db_Manager:
    def _init__(self):
        self.conn = sqlite3.connect(CONNECTION_STRING)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def register(self, username, password):
        if not self.validate_username(username):
            return False
        if not self.validate_password(password):
            return False
        password = self.set_password(username=username, password=password)
        username = self.set_username(username)
        self._register(username, password)

    @hash_password
    def set_password(self, password):
        return password

    @check_password_requirments
    def validate_password(self, username, password):  # Username is required for 1 of the requirements
        pass
        # Strange to put a func's body in a decorator?

    @check_username_requirements
    def validate_username(self, username):
        pass

    def set_username(self, username):  # Add a decorator to modify username if needed
        return username

    def create_clients_table(self):
        self.cursor.execute(create_db.CREATE_CLIENT_TABLE)

    def change_message(self, new_message, logged_user):
        self.cursor.execute(update.CHANGE_MESSAGE, (new_message, logged_user.get_id()))
        self.conn.commit()
        logged_user.set_message(new_message)

    # TODO: hash pass and check if against requirements after improved decorator
    def change_pass(self, new_pass, logged_user):
        self.cursor.execute(update.CHANGE_PASS, (new_pass, logged_user.get_id()))
        self.conn.commit()

    def _register(self, username, password):
        self.cursor.execute(insert.CREATE_USER, (username, password))
        self.conn.commit()

    @hash_password
    def login(self, username, password):
        self.cursor.execute(select.LOGIN, (username, password))
        user = self.cursor.fetchone()

        if(user):
            return Client(user['ID'], user['USERNAME'], user['BALANCE'], user['MESSAGE'])
        else:
            return False
