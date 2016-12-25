import cinema.settings.resources as resources 


class LoggedInMenu():
    def __init__(self, username):
        self.username = username
        self.r = resources

    def __print_menu_options(self):
        for k,v in self.r.LOGGED_IN_MENU_OPTIONS_DICT.items():
            print('{0}) {1}'.format(k,v))

    def start_interaction(self, username):
        print('hi ' + username)
        print(self.r.CHOOSE_OPTION_MESSAGE)
        self.__print_menu_options()






