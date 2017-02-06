import sqlite3


class DatabaseCreator:
    def __init__(self, connection_string, db_creation_queries_file):
        self.db_name = connection_string
        self.db = sqlite3.connect(self.db_name)
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self.db_creation_queries = db_creation_queries_file

    # This method is used to execute and commit queries
    def __execute_commit(self, query):
        self.cursor.execute(query)
        self.db.commit()

    def __format_sql_file(self):
        with open(self.db_creation_queries, 'r') as sql:
            queries = [x.strip() for x in sql.read().split('\'\'\'')]
        return queries[1::2]

    def create_database(self):
        for x in self.__format_sql_file():
            self.__execute_commit(x)
