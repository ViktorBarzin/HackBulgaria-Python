import sqlite3
from prettytable import PrettyTable


class ManageHospital:
    def __init__(self, connection):
        self.db_name = connection
        self.db = sqlite3.connect(self.db_name)
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self.entities = {'patients': 'patients',
                         'doctors': 'doctors',
                         'hospital': 'hospital_stay'}

    def list_all(self, entities):
        query = '''SELECT * FROM ''' + entities
        result = self.cursor.execute(query)
        pretty_table = PrettyTable([f[0] for f in result.description])
        for row in result:
            pretty_table.add_row(row)


        print(pretty_table)
    def add_doctor(self):
        firstname = input('Enter doctor firstname:')
        lastname = input('Enter doctor lastname:')
        self.__add_doctor(firstname,lastname)

    def __add_doctor(self, firstname, lastname):
        query = '''INSERT INTO DOCTORS (FIRSTNAME, LASTNAME)
        VALUSES (?, ?)
        '''
        self.cursor.execute(query, (firstname, lastname))
        self.db.commit()

    def add_patient(self):
        firstname = input('Enter patient firstname:')
        lastname = input('Enter doctor lastname:')
        age = input('Enter age:')
        gender = input('Enter gender:')
        doctor_id = input('Enter doctor id')
        self.__add_patient(firstname, lastname, age, gender, doctor_id)

    def __add_patient(self, firstname, lastname, age, gender, doctor_id):
        query = '''INSERT INTO PATIENTS (FIRSTNAME, LASTNAME, AGE, GENDER, DOCTOR)
        VALUES (?, ?, ?, ?, ?)'''
        self.cursor.execute(query, (firstname, lastname, age, gender, doctor_id))
        self.db.commit()

    def add_hospital_stay(self):
        room = input('Enter room number:')
        startdate = input('Enter start date:')
        enddate = input('Enter end date:')
        injury = input('Enter injury:')
        patient = input('Enter patiend id:')
        self.__add_hospital_stay(room, startdate, enddate, injury, patient)

    def __add_hospital_stay(self, room, startdate, enddate, injury, patient):
        query = '''INSERT INTO HOSPITAL_STAY (ROOM, STARTDATE, ENDDATE, INJURY, PATIENT)
        VALUES (?, ?, ?, ?, ?)'''
        self.cursor.execute(query, (room, startdate, enddate, injury, patient))
        self.db.commit()

    def update_patient(self):
        p_id = input('Enter patient id:')
        fname = input('Enter new first name:')
        lname = input('Enter new last name:')
        age = input('Enter new age:')
        gender = input('Enter new gender:')
        doctor = input('Enter new doctor id:')
        self.__update_patient(p_id, fname, lname, age, gender, doctor)

    # todo: add an option to change on desired fields, not all
    def __update_patient(self, id, firstname, lastname, age, gender, doctor):
        query = '''UPDATE PATIENTS
        SET FIRSTNAME = ?, LASTNAME = ?, AGE = ?, GENDER = ?, DOCTOR = ?
        WHERE ID = ?
        '''
        self.cursor.execute(query, (firstname, lastname, age, gender, doctor, id))
        self.db.commit()

    def update_doctor(self):
        d_id = input('Enter doctor id:')
        fname = input('Enter new first name:')
        lname = input('Enter new last name:')
        self.__update_doctor(d_id, fname, lname)

    def __update_doctor(self, id, firstname, lastname):
        query = '''UPDATE DOCTORS
        SET FIRSTNAME = ?, LASTNAME = ?
        WHERE ID = ?
        '''
        self.cursor.execute(query, (firstname, lastname, id))
        self.db.commit()

    def update_hospital_stay(self):
        h_id = input('Enter hospital stay id:')
        room = input('Enter new roow:')
        startdate = input('Enter new start date:')
        enddate = input('Enter new end date:')
        injury = input('Enter new injury:')
        patient = input('Enter new patient:')
        self.__update_hospital_stay(h_id, room, startdate, enddate, injury, patient)

    def __update_hospital_stay(self, id, room, startdate, enddate, injury, patient):
        query = '''UPDATE HOSPITAL_STAY
        SET ROOM = ?, STARTDATE = ?, ENDDATE = ?, INJURY = ?, PATIENT = ?
        WHERE ID = ?'''
        self.cursor.execute(query, (room, startdate, enddate, injury, patient, id))
        self.db.commit()

    def delete_entity(self):
        self.__delete_entity(self.entities[input('Enter entity to delete:')])

    def __delete_entity(self, entity, entity_id):
        # entity is called from within the program so no need to escape it
        query = 'DELETE FROM {0} WHERE ID = ?'.format(entity)
        self.cursor.execute(query, entity_id)
        self.db.commit()

    def all_patients_by_doctor(self, doctor_id):
        query = '''SELECT *, GROUP_CONCAT(P.FIRSTNAME || ' ' || P.LASTNAME, ',')
        FROM DOCTORS AS D
        LEFT JOIN PATIENTS AS P
        ON P.DOCTORID = D.ID
        GROUP BY D.FIRSTNAME AND D.LASTNAME
        WHERE D.ID = ?'''
        self.cursor.execute(query, doctor_id)
        self.db.commit()

    def all_sick_patients_by_injury(self):
        query = '''SELECT P.INJURY, GROUP_CONCAT('P.FIRSTNAME' || ' ' || P.LASTNAME, ',')
        PATIENTS AS P
        GROUP BY P.INJURY'''
        self.cursor.execute(query)
        self.db.commit()

    # todo: test, cuz probably not working
    def doctors_by_injury_they_treat(self):
        query = '''SELECT D.FIRSTNAME || D.LASTNAME, GROUP_CONCAT(P.INJURY, ',')
        FROM DOCTORS AS D
        LEFT JOIN PATIENTS AS P
        ON P.DOCTORID = D.ID
        GROUP BY P.INJURY'''
        self.cursor.execute(query)
        self.db.commit()

    def all_patients_between(self, startdate, enddate):
        query = '''SELECT *
        FROM PATIENTS AS P
        JOIN HOSPITAL_STAY AS HS
        ON HS.PATIENT = P.ID
        WHERE '''
        # TODO: finish later




