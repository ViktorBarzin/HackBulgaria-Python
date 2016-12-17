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