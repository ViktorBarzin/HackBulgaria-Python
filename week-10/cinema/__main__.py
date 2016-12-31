import cinema.views.main_menu as main_menu
import cinema.settings.resources as resource_file 
import cinema.settings.settings as settings


def main():
    user_interface = main_menu.MainMenu(resource_file, settings)
    user_interface.start_interaction()
if __name__ == '__main__':
    main()

