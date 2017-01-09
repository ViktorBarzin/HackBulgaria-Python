import sqlite3
import creation_queries as create_db
import update_queries as update
import select_queries as select
import insert_queries as insert
from settings import CONNECTION_STRING
from client import Client

conn = sqlite3.connect(CONNECTION_STRING)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


def create_clients_table():
    cursor.execute(create_db.CREATE_CLIENT_TABLE)


def change_message(new_message, logged_user):
    cursor.execute(update.CHANGE_MESSAGE, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    cursor.execute(update.CHANGE_PASS, (new_pass, logged_user.get_id()))
    conn.commit()


def register(username, password):
    cursor.execute(insert.CREATE_USER, (username, password))
    conn.commit()


def login(username, password):
    cursor.execute(select.LOGIN, (username, password))
    user = cursor.fetchone()

    if(user):
        return Client(user['ID'], user['USERNAME'], user['BALANCE'], user['MESSAGE'])
    else:
        return False
