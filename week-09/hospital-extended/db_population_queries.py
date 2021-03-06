INSERT_INTO_USER = '''INSERT INTO USER (USERNAME, PASSWORD, AGE)
 VALUES(?, ?, ?)
 '''

INSERT_INTO_HOSPITAL_STAY = ''' INSERT INTO HOSPITAL_STAY (STARTDATE, ENDDATE, ROOM, INJURY, PATIENT_ID)
VALUES (?, ?, ?, ?, ?)
'''

INSERT_INTO_DOCTOR = '''     INSERT INTO DOCTOR (ACADEMIC_TITLE, ID)
VALUES (?, ?)
'''

INSERT_INTO_PATIENT = ''' INSERT INTO PATIENT (ID, DOCTOR_ID)
VALUES (?, ?)
'''

INSERT_INTO_VISITATION = '''INSERT INTO VISITATION (DOCTOR_ID, START_HOUR)
VALUES (?, ?)'''
