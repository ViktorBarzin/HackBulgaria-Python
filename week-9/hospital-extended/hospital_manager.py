import sqlite3
import common_sql_queries  # introducing a dependency; consider moving in constructor?
import db_population_queries
from passlib.hash import pbkdf2_sha256


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

    @staticmethod
    def __hash_password(password):
        return pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=128)

    @staticmethod
    def __verify_password(password, h):
        return pbkdf2_sha256.verify(password, h)

    def __register_user(self, username, password, age):
        self.__execute_query(db_population_queries.INSERT_INTO_USER, (username, self.__hash_password(password), age))

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

    def __register_patient(self, username, password, age):
        self.__register_user(username, password, age)
        # Ask to assign doctor
        all_doctors = self.cursor.execute(common_sql_queries.SELECT_DOCTOR_JOIN_USER).fetchall()
        id_doct_dict = {}
        print(self.r.CHOOSE_DOCTOR)
        # indexing is changed to format output
        for i in range(len(all_doctors)):
            id_doct_dict[i] = all_doctors[i]
            print('{0}) {1}'.format(i + 1, all_doctors[i]['username']))
        try:
            choice = int(input())
        except ValueError:
            print(self.r.VALUE_ERROR_MESSAGE)

        new_user_id = (self.cursor.execute(common_sql_queries.GET_USER_ID_BY_USERNAME, (username,))).fetchone()['id']
        self.__execute_query(db_population_queries.INSERT_INTO_PATIENT,
                             (new_user_id, id_doct_dict[choice - 1]['id'] if choice - 1 in id_doct_dict else None))

        # Login newly registered patient:
        if self.login(username, password):
            print(self.welcome(username))

    def __welcome_patient(self, username):
        return self.r.WELCOME_PATIENT_MESSAGE.format(username)

    def __welcome_doctor(self, username):
        return self.r.WELCOME_DOCTOR_MESSAGE.replace('{0}', username).replace(
            '{1}', self.__execute_query(common_sql_queries.SELECT_DOCTOR_TITLE, (username,))
                     .fetchone()['academic_title'])

    def __get_user_id_by_username(self, username):
        return self.__execute_query(common_sql_queries.GET_USER_ID_BY_USERNAME, (username,)).fetchone()['id']

    def login(self, username, password):
        result = self.__execute_query(common_sql_queries.VALIDATE_USER, (username,))
        user = result.fetchone()
        if user is not None and self.__verify_password(password, user['password']):
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

    # Logged in section methods (perhaps move in another class?)
    def list_patients(self, username):
        doctor = self.__execute_query(common_sql_queries.GET_DOCTOR_ID_BY_USERNAME, (username,)).fetchone()

        # Gets patient username for all patients whose doctor id matches the given one
        return [x['USERNAME'] for x in
                self.__execute_query(common_sql_queries.LIST_PATIENTS_OF_DOCTOR, (doctor['id'],)).fetchall()]

    def logout(self, username):
        user_id = self.__get_user_id_by_username(username)
        return self.__execute_query(common_sql_queries.LOGOUT_USER_BY_ID, (user_id,))

    def add_visitation_hour(self, doctor_username, starthour):
        doctor_id = self.__get_user_id_by_username(doctor_username)
        return self.__execute_query(db_population_queries.INSERT_INTO_VISITATION, (doctor_id, starthour))

    def delete_free_visitation_hours(self):
        return self.__execute_query(common_sql_queries.DELETE_FREE_VISITATION_HOURS, ())

    def get_room_and_username_duration_start_and_end_for_all_patients(self):
        result = self.__execute_query(common_sql_queries.GET_ROOM_AND_USERNAME_DURATION_START_AND_END_FOR_ALL_PATIENTS, ())\
            .fetchall()
        return result

    def change_username(self, old_username, new_username):
        self.__execute_query(common_sql_queries.CHANGE_USERNAME_BY_USERNAME, (new_username, old_username))

    def change_age(self, username, age):
        self.__execute_query(common_sql_queries.CHANGE_AGE_BY_USERNAME, (int(age), username))

    def change_academic_title(self, username, title):
        doctor_id = self.__get_user_id_by_username(username)
        print(doctor_id, title)
        self.__execute_query(common_sql_queries.CHANGE_ACADEMIC_TITLE_BY_ID, (title, doctor_id))
