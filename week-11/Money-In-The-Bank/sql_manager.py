import random
import smtplib
import uuid
from decorators import hash_password, check_password_requirements, check_username_requirements, check_if_banned, check_ban_list_file, check_email_requirements
from helpers import change_failed_password_attempts, clear_login_ban_records
from settings import CONNECTION_STRING, DB_TYPE, BAN_LIST_FILE as ban_file, WRONG_PASSWORD_ATTEPMTS, EMAIL_ACCOUNT_USER, EMAIL_ACCOUNT_PASSWORD, EMAIL_SUBJ, EMAIL_BODY, MAX_TAN_CODES

from models import Client, TanCode
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class Db_Manager:
    def __init__(self):
        self.engine = create_engine('{}:///{}'.format(DB_TYPE, CONNECTION_STRING))
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

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

    def change_message(self, new_message, client):
        if not client:
            raise ValueError('No user with the provided id!')
        client.message = new_message
        client.message = new_message
        self.session.commit()

    def change_pass(self, password, username):
        client = self.session.query(Client).filter(Client.username == username).first()
        if not client:
            raise ValueError('No such user')
        return self.__change_pass(password, client)

    def __change_pass(self, password, user):
        self.validate_password(password=password, username=user.username)
        password = self.set_password(password=password)

        user.password = password
        self.session.commit()
        return True

    def _register(self, username, password, email):
        client = Client(username=username, password=password, email=email)
        self.session.add(client)
        self.session.commit()

    def reset_password(self, username):
        token = self.__set_reset_token_for(username)
        client = self.session.query(Client).filter(Client.username == username).first()
        if not client:
            raise ValueError('There is no user with this username')
        self.__send_token_to_email(token, client.email)

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
        client = self.session.query(Client).filter(Client.username == username).first()
        if not client:
            raise ValueError('There is no user with this username')
        client.password_reset_token = token
        self.session.commit()
        return token

    @check_ban_list_file
    @hash_password
    @check_if_banned(ban_file)
    def login(self, username, password):
        user = self.session.query(Client).filter(Client.username == username).filter(Client.password == password).first()
        if user:
            clear_login_ban_records(ban_file, username, WRONG_PASSWORD_ATTEPMTS)
            return user
        else:
            # If such user exists, put a black point, else just ignore
            if username in [x.username for x in self.get_all_users()]:
                change_failed_password_attempts(ban_file, username, 1)
            return False

    def get_all_users(self):
        return self.session.query(Client).all()

    def check_token(self, username, token):
        client = self.session.query(Client).filter(Client.username == username).first()
        if not client:
            raise ValueError('There is no user with this username')
        return client.password_reset_token == str(token)

    def show_balance(self, username):
        client = self.session.query(Client).filter(Client.username == username).first()
        if not client:
            raise ValueError('No such user')
        return client.balance

    def __request_tan(self, user):
        tan = input('Enter your tan code:')
        tans = user.tan_codes
        if tan not in [x.tan_code for x in tans]:
            raise ValueError('Invalid tan code')
        return tan

    def update_balance(self, username, amount):
        # Expected to catch the value error in an upper level
        amount = float(amount)

        user = self.session.query(Client).filter(Client.username == username).first()
        if not user:
            raise ValueError('No such user')
        new_balance = float(user.balance + amount)
        if new_balance < 0:
            raise ValueError('Cannot have negative balance!')
        tan = self.__request_tan(user)
        user.balance = new_balance
        self.session.query(TanCode).filter(TanCode.tan_code == tan).delete()
        self.session.commit()
        return True

    def get_tan(self, username):
        user = self.session.query(Client).filter(Client.username == username).first()
        if not user:
            raise ValueError('No such user')
        # If the user has no tan_codes return
        if len(list(user.tan_codes)) != 0:
            raise ValueError('You have {} more codes!'.format(len(user.tan_codes)))

        # User has no tan_codes so create and email to him new codes
        tans = [TanCode(tan_code=str(uuid.uuid4()), user_id=user.id) for x in range(MAX_TAN_CODES)]
        for x in tans:
            user.tan_codes.append(x)
        self.session.commit()

        # Email message
        message = 'These are your unique TAN codes. Keep them safe!\n\n{}'.format('\n\n'.join(x.tan_code for x in tans))
        self.send_email(EMAIL_ACCOUNT_USER, EMAIL_ACCOUNT_PASSWORD, user.email, 'TAN codes', message)
