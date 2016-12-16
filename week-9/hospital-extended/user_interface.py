from getpass import getpass


class UserInterface:
    def __init__(self, resource_file, hospital_instance):
        self.r = resource_file
        self.hospital_instance = hospital_instance
        self.__start_ui()

    # Acts like a second constructor for printing to console
    def __start_ui(self):
        print(self.r.LOAD_UP)

    # Prints main menu options
    def __print_main_menu(self):
        for k, v in self.r.MAIN_MENU_OPTIONS_DICT.items():
            # Print main menu options
            print(str(k) + self.r.MAIN_MENU_OPTIONS_SEPARATOR + ' ' + v)

    # main user interaction is done here
    def start_interaction(self):
        self.__print_main_menu()
        comm = str(input(self.r.CHOOSE_OPTION_STRING))
        while comm.lower() != self.r.EXIT:
            try:
                if comm.lower() == 'help':
                    self.__print_main_menu()
                    comm = input(self.r.CHOOSE_OPTION_STRING)
                    continue
                comm = int(comm)
                # print(self.r.MAIN_MENU_OPTIONS_DICT[comm])

                # todo: make 1 check only
                if comm == 1:
                    username = input(self.r.ENTER_USERNAME_MESSAGE)
                    password = input(self.r.ENTER_PASSWORD_MESSAGE)
                    if self.hospital_instance.login(username, password):
                        print(self.hospital_instance.welcome(username))
                elif comm == 2:
                    # todo: uniqueness of usernames?
                    username = input(self.r.ENTER_USERNAME_MESSAGE)
                    password = input(self.r.ENTER_PASSWORD_MESSAGE)
                    conf_password = input(self.r.CONFIRM_PASSWORD_MESSAGE)
                    if password != conf_password:
                        print(self.r.PASSWORD_MISMATCH_MESSAGE)
                        continue
                    self.hospital_instance.register(username, password)
            except ValueError:
                print(self.r.VALUE_ERROR_MESSAGE)
                print(self.r.ENTER_HELP_TO_SEE_HELP_MENU)
            except KeyError:
                print(self.r.VALUE_ERROR_MESSAGE)

            comm = input(self.r.CHOOSE_OPTION_STRING)




