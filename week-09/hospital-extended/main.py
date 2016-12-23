import create_db
import settings
import user_interface
import resources
import hospital_manager


def main():
    # Setup db
    # connection_string = settings.DB_CONNECTION_STRING
    # creation_queries = settings.DB_CREATION_QUERIES_FILE
    # database = create_db.DatabaseCreator(connection_string, creation_queries)
    # database.create_database()

    hospital = hospital_manager.HospitalManager(settings.DB_CONNECTION_STRING, resources)
    # Start user interface
    ui = user_interface.UserInterface(resources, hospital, settings)
    ui.start_interaction()
    
if __name__ == '__main__':
    main()
