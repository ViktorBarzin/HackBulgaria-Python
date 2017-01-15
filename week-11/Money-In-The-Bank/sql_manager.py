import creation_queries as create_db
import insert_queries as insert
import random
import select_queries as select
import smtplib
import sqlite3
import update_queries as update
import uuid
from client import Client
from decorators import hash_password, check_password_requirements, check_username_requirements, check_if_banned, check_ban_list_file, check_email_requirements
from helpers import change_failed_password_attempts, clear_login_ban_records
from settings import CONNECTION_STRING, BAN_LIST_FILE as ban_file, WRONG_PASSWORD_ATTEPMTS, EMAIL_ACCOUNT_USER, EMAIL_ACCOUNT_PASSWORD, EMAIL_SUBJ, EMAIL_BODY, MAX_TAN_CODES


class Db_Manager:
    def __init__(self):
        self.conn = sqlite3.connect(CONNECTION_STRING)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def register(self, username, password, email):
        self.validate_username(username=username)
        self.validate_password(username=username, password=password)
        self.validate_email(email=email)

        password = self.set_password(password=password)
        username = self.set_username(username)
        self._register(username, password, email)
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

    @check_email_requirements
    def validate_email(self, email):
        pass

    def set_username(self, username):  # Add a decorator to modify username if needed
        return username

    def create_clients_table(self):
        # self.cursor.execute(create_db.CREATE_CLIENT_TABLE)
        self.cursor.execute(create_db.CREATE_TAN_CODE_USER_TABLE)

    def change_message(self, new_message, logged_user):
        self.cursor.execute(update.CHANGE_MESSAGE, (new_message, logged_user.get_id()))
        self.conn.commit()
        logged_user.set_message(new_message)

    def _change_pass(self, password, logged_user):
        self.cursor.execute(update.CHANGE_PASS, (password, logged_user.get_id()))
        self.conn.commit()

    def change_pass(self, password, username):
        try:
            user = [x for x in self.get_all_users() if x['username'] == username][0]
        except IndexError:
            raise ValueError('No such user')
        user_to_client = Client(user['id'], user['username'], user['balance'], user['message'])
        return self.__change_pass(password, user_to_client)

    def __change_pass(self, password, user):
        self.validate_password(password=password, username=user.get_username())
        password = self.set_password(password=password)
        self._change_pass(password, user)

        return True

    def _register(self, username, password, email):
        self.cursor.execute(insert.CREATE_USER, (username, password, email))
        self.conn.commit()

    def reset_password(self, username):
        token = self.__set_reset_token_for(username)
        try:
            user = [x for x in self.get_all_users() if x['USERNAME'] == username][0]
        except IndexError as e:
            print(e)
        #     raise ValueError('No such user')
        self.__send_token_to_email(token, user['EMAIL'])

    def __send_token_to_email(self, token, email):
        self.send_email(EMAIL_ACCOUNT_USER, EMAIL_ACCOUNT_PASSWORD,
                email, EMAIL_SUBJ,
                '{}{}'.format(EMAIL_BODY, token))

    def send_email(self, user, pwd, recipient, subject, body):
        gmail_user = user
        gmail_pwd = pwd
        FROM = user
        TO = recipient if type(recipient) is list else [recipient]
        SUBJECT = subject
        TEXT = body

        # Prepare actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message)
            server.close()
            # print('successfully sent the mail')
        except:
            raise ValueError("Failed to send mail")

    def __set_reset_token_for(self, username):
        token = random.randint(1, abs(hash(username)) + 2) % 10000000
        self.cursor.execute(update.CREATE_PASSWORD_RESET_TOKEN, (str(token), username))
        self.conn.commit()
        return token

# Why the fuck are the decorators executed from top-to-bottom?
    @check_ban_list_file
    @hash_password
    @check_if_banned(ban_file)
    def login(self, username, password):
        self.cursor.execute(select.LOGIN, (username, password))
        user = self.cursor.fetchone()
        if(user):
            clear_login_ban_records(ban_file, username, WRONG_PASSWORD_ATTEPMTS)
            return Client(user['ID'], user['USERNAME'], user['BALANCE'], user['MESSAGE'])
        else:
            # If such user exists, put a black point, else just ignore
            if username in [x['username'] for x in self.get_all_users()]:
                change_failed_password_attempts(ban_file, username, 1)
            return False

    def get_all_users(self):
        return self.cursor.execute(select.SELECT_ALL_USERS).fetchall()

    def check_token(self, username, token):
        try:
            user = [x for x in self.cursor.execute(select.SELECT_ALL_USERS).fetchall() if x['username'] == username][0]
        except IndexError:
            raise ValueError('There is no user with this username')
        return user['password_reset_token'] == str(token)

    def show_balance(self, username):
        try:
            users = self.cursor.execute(select.SELECT_ALL_USERS).fetchall()
            user = users[0]
        except IndexError:
            raise ValueError('No such user')
        return user['balance']

    def update_balance(self, username, amount):
        try:
            users = self.cursor.execute(select.SELECT_ALL_USERS).fetchall()
            user = [x for x in users if x['USERNAME'] == username][0]
        except IndexError:
            raise ValueError('No such user')
        new_balance = float(user['balance'] + amount)
        if new_balance < 0:
            raise ValueError('Cannot have negative balance!')
        self.cursor.execute(update.CHANGE_BALANCE_FOR_USER, (new_balance, username))
        self.conn.commit()
        return True

    def get_tan(self, username):
        try:
            users = self.cursor.execute(select.SELECT_ALL_USERS).fetchall()
            user = [x for x in users if x['USERNAME'] == username][0]
        except IndexError:
            raise ValueError('No such user')
        tan_codes = self.cursor.execute(select.SELECT_ALL_TAN_CODES).fetchall()
        user_tan_codes = [x for x in tan_codes if x['USER_ID'] == user['ID']]
        # If the user has no tan_codes return
        if len(user_tan_codes) != 0:
            raise ValueError('You have {} more codes!'.format(MAX_TAN_CODES - len(user_tan_codes)))

        # User has no tan_codes so create and email to him new codes
        tans = [str(uuid.uuid4()) for x in range(MAX_TAN_CODES)]
        # Doing a for because executemany did not work out ;\
        for tan in tans:
            self.cursor.execute(insert.INSERT_TAN, (user['ID'], tan))
        self.conn.commit()
        # Email message
        message = 'These are your unique TAN codes. Keep them safe!\n{}'.format('\n\n'.join(tans))
        self.send_email(EMAIL_ACCOUNT_USER, EMAIL_ACCOUNT_PASSWORD, user['email'], 'TAN codes', message)
