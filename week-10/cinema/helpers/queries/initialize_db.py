import db_creation_query as queries
import sqlite3
import cinema.settings.settings as settings
import cinema.queries.db_creation_query as query

class DatabaseCreator:
    def __init__(self, connection_string, db_creation_queries_file):
        self.db_name = connection_string
        self.db = sqlite3.connect(self.db_name)
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        # self.db_creation_queries = db_creation_queries_file
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

def main():
    # call all the db_creation methods and initialize db
    connection_string = settings.CONNECTION_STRING
    db_creator = DatabaseCreator(connection_string, query) 
    db_creator.create_database()

if __name__ == '__main__':
    main()
