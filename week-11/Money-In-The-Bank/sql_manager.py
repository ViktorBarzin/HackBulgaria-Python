import sqlite3
import creation_queries as create_db
import update_queries as update
import select_queries as select
import insert_queries as insert
import json
import datetime
from decorators import hash_password, check_password_requirements, check_username_requirements, check_if_banned, check_ban_list_file
from settings import CONNECTION_STRING, BAN_LIST_FILE as ban_file, WRONG_PASSWORD_ATTEPMTS
from client import Client


class Db_Manager:
    def __init__(self):
        self.conn = sqlite3.connect(CONNECTION_STRING)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def register(self, username, password):
        self.validate_username(username=username)
        self.validate_password(username=username, password=password)

        password = self.set_password(password=password)
        username = self.set_username(username)
        self._register(username, password)
        return True

    @hash_password
    def set_password(self, password):
        return password

    @check_password_requirements
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

    def _change_pass(self, password, logged_user):
        self.cursor.execute(update.CHANGE_PASS, (password, logged_user.get_id()))
        self.conn.commit()

    def change_pass(self, password, user):
        self.validate_password(password=password, username=user.get_username())
        password = self.set_password(password=password)
        self._change_pass(password, user)

        return True

    def _register(self, username, password):
        print(self, username, password)
        self.cursor.execute(insert.CREATE_USER, (username, password))
        self.conn.commit()

# Why the fuck are the decorators executed from top-to-bottom?
    @check_ban_list_file
    @hash_password
    @check_if_banned(ban_file)
    def login(self, username, password):
        self.cursor.execute(select.LOGIN, (username, password))
        user = self.cursor.fetchone()
        if(user):
            self.clear_login_ban_records(username)
            return Client(user['ID'], user['USERNAME'], user['BALANCE'], user['MESSAGE'])
        else:
            # If such user exists, put a black point, else just ignore
            if username in [x['username'] for x in self.get_all_users()]:
                self._change_failed_password_attempts(username, 1)
            return False

    def get_all_users(self):
        return self.cursor.execute(select.SELECT_ALL_USERS).fetchall()

    def __ban_json_to_dict(self):
        with open(ban_file, 'r') as r:
            return json.load(r)

    # Reusing this in the decorators which is not ok but I ain't gonna copy
    # paste this over there as well..
    def clear_login_ban_records(self, username):
        self._change_failed_password_attempts(username, -WRONG_PASSWORD_ATTEPMTS)

    # Updates failed attempts to login for a user
    # update is the actual value to be change with
    @check_ban_list_file
    def _change_failed_password_attempts(self, username, update):
        data = self.__ban_json_to_dict()
        try:
            user = [x for x in data if x['username'] == username][0]
            user['wrong-attempts'] += update
            user['ban-start-date'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            if user['wrong-attempts'] < 0:
                user['wrong-attempts'] = 0
        except IndexError:
            self.__add_user_to_ban_list(username)
            return

        # Save changes to .json file
        with open(ban_file, 'w') as w:
            w.write(json.dumps(data))

    def __add_user_to_ban_list(self, username):
        # Asserts ban-list file is not empty
        data = self.__ban_json_to_dict()
        with open(ban_file, 'w') as w:
            data.append({})
            data[-1]['username'] = username
            data[-1]['ban-start-date'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            data[-1]['wrong-attempts'] = 1

            w.write(json.dumps(data))
