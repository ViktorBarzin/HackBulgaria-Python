
DROP_MOVIE_TABLE = '''
DROP TABLE IF EXISTS MOVIE;
'''

DROP_PROJECTION_TABLE ='''
DROP TABLE IF EXISTS PROJECTION;
'''

DROP_USER_TABLE = '''
DROP TABLE IF EXISTS USER;
'''

DROP_TABLE_RESERVATION = '''
DROP TABLE IF EXISTS RESERVATION
'''


CREATE_MOVIE_TABLE = '''
CREATE TABLE IF NOT EXISTS MOVIE(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT N,
    RATING REAL
)
'''

CREATE_PROJECTION_TABLE = '''
CREATE TABLE IF NOT EXISTS PROJECTION(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    MOVIE_ID INTEGER,
    TYPE TEXT N,
    DATE TEXT N,
    TIME TEXT N,
    FOREIGN KEY (MOVIE_ID) REFERENCES MOVIE(ID)
)
'''

CREATE_USER_TABLE = '''
CREATE TABLE IF NOT EXISTS USER(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    USERNAME TEXT N,
    PASSWORD TEXT N
)
'''

CREATE_RESERVATION_TABLE = '''
CREATE TABLE IF NOT EXISTS RESERVATION(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    USER_ID INTEGER N,
    PROJECTION_KEY INTEGER N,
    ROW INTEGER N,
    COL INTEGER N
)
'''


