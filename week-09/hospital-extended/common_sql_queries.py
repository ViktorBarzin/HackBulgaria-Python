SELECT_USERS = '''SELECT *
FROM USER
'''

SELECT_DOCTORS = ''' SELECT *
FROM DOCTOR
'''

SELECT_PATIENTS = ''' SELECT *
FROM PATIENT
'''

# TODO: check if promotion queries work fine
PROMOTE_TO_DOCTOR = '''INSERT INTO DOCTOR
VALUES (?, ?)
'''

PROMOTE_TO_PATIENT = ''' INSERT INTO PATIENT
VALUES (?, ?)
'''

VALIDATE_USER = ''' SELECT USER.PASSWORD
FROM USER WHERE USERNAME = ?
'''

# TODO: login by username when it is not PK ?
# 2 different queries so that it is clear what is user.is_active attribute
LOGIN_USER = ''' UPDATE USER
SET IS_ACTIVE = 1
WHERE USERNAME = ?
'''

LOGOUT_USER = ''' UPDATE USER
SET IS_ACTIVE = 0
WHERE USERNAME = ?
'''

LOGOUT_USER_BY_ID = '''
UPDATE USER
SET IS_ACTIVE = 0
WHERE ID = ?
'''

SELECT_DOCTOR_TITLE = '''SELECT D.ACADEMIC_TITLE
FROM DOCTOR AS D
JOIN USER
ON USER.ID = D.ID
WHERE USER.USERNAME = ?
'''

GET_USER_ID_BY_USERNAME = ''' SELECT ID
FROM USER
WHERE USERNAME = ?
'''

GET_DOCTOR_ID_BY_USERNAME = '''SELECT DOCTOR.ID as 'ID'
FROM USER
JOIN DOCTOR
ON USER.ID = DOCTOR.ID
WHERE USER.USERNAME = ?'''

SELECT_DOCTOR_JOIN_USER = ''' SELECT *
FROM DOCTOR
JOIN USER
ON DOCTOR.ID = USER.ID
'''

LIST_PATIENTS_OF_DOCTOR = ''' SELECT U.USERNAME AS 'USERNAME'
FROM USER AS U
JOIN PATIENT AS P
ON U.ID = P.ID
JOIN DOCTOR AS D
ON P.DOCTOR_ID = D.ID
WHERE D.ID = ?
'''

DELETE_FREE_VISITATION_HOURS = ''' DELETE FROM VISITATION
WHERE PATIENT_ID IS NULL
'''

GET_ROOM_AND_USERNAME_DURATION_START_AND_END_FOR_ALL_PATIENTS = '''SELECT HS.ROOM AS ROOM, USER.USERNAME AS USERNAME,
HS.STARTDATE AS STARTDATE, HS.ENDDATE AS ENDDATE
FROM HOSPITAL_STAY AS HS JOIN PATIENT ON PATIENT.ID = HS.PATIENT_ID
JOIN USER ON PATIENT.ID = USER.ID;
'''

CHANGE_USERNAME_BY_USERNAME = '''UPDATE USER
SET USERNAME = ?
WHERE USERNAME = ?'''

CHANGE_AGE_BY_USERNAME = ''' UPDATE USER
SET AGE = ?
WHERE USERNAME = ?
'''

CHANGE_ACADEMIC_TITLE_BY_ID = ''' UPDATE DOCTOR
SET ACADEMIC_TITLE = ?
WHERE ID = ?
'''

# TODO: check if username should be the doctor's or the user's
GET_DOCTOR_FREE_HOURS = '''
SELECT V.START_HOUR AS STARTHOUR
FROM USER AS U
JOIN PATIENT AS P
ON U.ID = P.ID
JOIN VISITATION AS V
ON P.DOCTOR_ID = V.DOCTOR_ID
WHERE V.PATIENT_ID IS NULL
AND U.USERNAME = ?
'''

UPDATE_VISITATION_TABLE = '''
UPDATE VISITATION
SET PATIENT_ID = ?
WHERE DOCTOR_ID = ?
AND START_HOUR = ?
'''

GET_DOCTOR_OF_PATIENT = '''
SELECT D.ID AS DOCTOR_ID,U2.USERNAME AS DOCTOR_USERNAME, D.ACADEMIC_TITLE AS DOCTOR_ACADEMIC_TITLE, U2.AGE AS DOCTOR_AGE
FROM USER AS U1
JOIN PATIENT AS P
ON U1.ID = P.ID
JOIN DOCTOR AS D
ON D.ID = P.DOCTOR_ID
JOIN USER AS U2
ON U2.ID = D.ID
WHERE U1.USERNAME = ?
'''

GET_ALL_HOSPITAL_STAYS_OF_ = '''
SELECT *
FROM HOSPITAL_STAY
WHERE PATIENT_ID = ?
'''

UPDATE_DOCTOR_OF = '''
UPDATE PATIENT
SET DOCTOR_ID = ?
WHERE ID = ?
'''