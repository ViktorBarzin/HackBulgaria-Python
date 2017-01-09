CREATE_CLIENT_TABLE = '''
CREATE TABLE IF NOT EXISTS CLIENTS(
    ID integer primary key autoincrement,
    USERNAME text,
    PASSWORD text,
    BALANCE real default 0,
    MESSAGE text
    )
'''
