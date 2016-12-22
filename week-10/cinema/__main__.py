import cinema.views.main_menu as main_menu
import cinema.settings.resources as resource_file 
import cinema.settings.settings as settings

from cinema.helpers.queries.initialize_db import DatabaseCreator
import cinema.helpers.queries.db_creation_query as query
#def main():
    
 #   user_interface = main_menu.MainMenu(resource_file, settings)
  #  user_interface.start_interaction()
#if __name__ == '__main__':
 #   main()


def main():
    # call all the db_creation methods and initialize db
    connection_string = settings.CONNECTION_STRING
    db_creator = DatabaseCreator(connection_string, query) 
    db_creator.create_database()

if __name__ == '__main__':
    main()
