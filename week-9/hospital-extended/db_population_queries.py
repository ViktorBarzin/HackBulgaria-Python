INSERT_INTO_USER = '''INSERT INTO USER (USERNAME, PASSWORD, AGE)
 VALUES(?, ?, ?)
 '''

INSERT_INTO_HOSPITAL_STAY = ''' INSERT INTO HOSPITAL_STAY (STARTDATE, ENDDATE, ROOM, INJURY, PATIENT_ID)
VALUES (?, ?, ?, ?, ?)
'''