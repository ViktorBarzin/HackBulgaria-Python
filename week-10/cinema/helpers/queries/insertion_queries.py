REGISTER = '''
INSERT INTO USER (USERNAME, PASSWORD)
VALUES (?, ?);
'''

CREATE_RESERVATION = '''
INSERT INTO RESERVATION (USER_ID, PROJECTION_KEY, ROW, COL)
VALUES (?, ?, ? ,?);
'''