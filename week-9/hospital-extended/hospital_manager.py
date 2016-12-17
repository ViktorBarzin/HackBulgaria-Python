import sqlite3
import common_sql_queries  # introducing a dependency; consider moving in constructor?
import db_population_queries


class HospitalManager:
    def __init__(self, connection_string, resource_file):
        self.db_name = connection_string
        self.db = sqlite3.connect(self.db_name)
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self.r = resource_file

    def __execute_query(self, query, params):
        result = self.cursor.execute(query, params)
        self.db.commit()
        return result

    def __register_user(self, username, password, age):
        self.__execute_query(db_population_queries.INSERT_INTO_USER, (username, password, age))

    def __register_doctor(self, username, password, age):
        # todo: move asking for user input in higher level?
        academic_title = input('Enter you academic title:')
        self.__register_user(username, password, age)

        # Get user id to set to doctor entity
        new_user_id = (self.cursor.execute(common_sql_queries.GET_USER_ID_BY_USERNAME, (username,))).fetchone()['id']
        self.__execute_query(db_population_queries.INSERT_INTO_DOCTOR, (academic_title, new_user_id))

        # login the newly registered doctor
        if self.login(username, password):
            print(self.welcome(username))

    def __register_patient(self, username, password):
        pass

    def __welcome_patient(self, username):
        return self.r.WELCOME_PATIENT_MESSAGE.format(username)

    def __welcome_doctor(self, username):
        return self.r.WELCOME_DOCTOR_MESSAGE.replace('{0}', username).replace(
            '{1}', self.__execute_query(common_sql_queries.SELECT_DOCTOR_TITLE, (username,))
                     .fetchone()['academic_title'])

    def __get_user_id_by_username(self, username):
        return self.__execute_query(common_sql_queries.GET_USER_ID_BY_USERNAME(), (username,))

    # todo: hash passwords to beef up security
    def login(self, username, password):
        result = self.__execute_query(common_sql_queries.VALIDATE_USER, (username,))
        user = result.fetchone()
        if user['password'] == password:
            self.__execute_query(common_sql_queries.LOGIN_USER, (username,))
            return True
        return False

    def welcome(self, username):
        if self.r.DR_TITLE in username:
            return self.__welcome_doctor(username)
        return self.__welcome_patient(username)

    def register(self, username, password, age):
        if self.r.DR_TITLE in username:
            return self.__register_doctor(username, password, age)
        return self.__register_patient(username, password, age)
