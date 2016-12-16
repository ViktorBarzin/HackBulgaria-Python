import sqlite3
import common_sql_queries  # introducing a dependency; consider moving in constructor?


class HospitalManager:
    def __init__(self, connection_string, resource_file):
        self.db_name = connection_string
        self.db = sqlite3.connect(self.db_name)
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self.r = resource_file

    def __register_doctor(self, username, password):
        pass

    def __register_patient(self, username, password):
        pass

    def __welcome_patient(self, username):
        return self.r.WELCOME_PATIENT_MESSAGE.format(username)

    def __welcome_doctor(self, username):
        return self.r.WELCOME_DOCTOR_MESSAGE.replace('{0}', username).replace(
            '{1}', self.cursor.execute(common_sql_queries.SELECT_DOCTOR_TITLE, (username,))
                .fetchone()['academic_title'])

    # todo: hash passwords to beef up security
    def login(self, username, password):
        result = self.cursor.execute(common_sql_queries.VALIDATE_USER, (username,))
        user = result.fetchone()
        if user['password'] == password:
            self.cursor.execute(common_sql_queries.LOGIN_USER, (username,))
            self.db.commit()
            return True
        return False

    def welcome(self, username):
        if self.r.DR_TITLE in username:
            return self.__welcome_doctor(username)
        return self.__welcome_patient(username)


    def register(self, username, password):
        pass