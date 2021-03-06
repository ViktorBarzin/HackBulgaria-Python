CREATE_CLIENT_TABLE = '''
CREATE TABLE IF NOT EXISTS CLIENTS(
    ID integer primary key autoincrement,
    USERNAME text,
    PASSWORD text,
    BALANCE real default 0,
    MESSAGE text,
    EMAIL text,
    PASSWORD_RESET_TOKEN text
    )
'''

CREATE_TAN_CODE_USER_TABLE = '''
CREATE TABLE IF NOT EXISTS TAN_CODES(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    USER_ID INTEGER,
    TAN_CODE TEXT,
    FOREIGN KEY(USER_ID) REFERENCES CLIENT(ID)
 )
'''
