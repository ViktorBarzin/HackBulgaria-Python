from getpass import getpass
class MainMenu:
    def __init__(self, resource_file, settings_file):
        self.r = resource_file
        self.settings = settings_file
        # logging_out is used to logout user
        self.logging_out = False
        # same goes for closing app after user logged out
        self.closing_app = False
        print(self.__start_ui())

    # Acts like a second constructor for printing to console
    def __start_ui(self):
        return self.r.LOAD_UP

    # Prints main menu options
    def __print_main_menu(self):
        for k, v in self.r.MAIN_MENU_OPTIONS_DICT.items():
            # Print main menu options     
            print(str(k) + self.r.MAIN_MENU_OPTIONS_SEPARATOR + ' ' + v)

     # main user interaction is done here
    def start_interaction(self):
        self.__print_main_menu()
        comm = str(input(self.r.CHOOSE_OPTION_MESSAGE)).lower()
        while comm != self.r.EXIT:
            try:
                if comm == 'help':
                    self.__print_main_menu()
                    continue
                comm = self.settings.MAIN_MENU_OPTIONS[int(comm)]

                # todo: make 1 check only
                # Login option
                if comm == self.settings.MAIN_MENU_OPTIONS[1]:
                    username = input(self.r.ENTER_USERNAME_MESSAGE)
                    password = getpass(self.r.ENTER_PASSWORD_MESSAGE)
                    if self.cinema_instance.login(username, password):
                        # Start logged in user interaction
                        self.__logged_in_interaction(username)

                    else:
                        print(self.r.LOGIN_FAILED_MESSAGE)
                # Register option
                elif comm == self.settings.MAIN_MENU_OPTIONS[2]:
                    # todo: usernames MUST be unique
                    username = input(self.r.ENTER_USERNAME_MESSAGE)
                    password = getpass(self.r.ENTER_PASSWORD_MESSAGE)

                    # Validate password against password constraints
                    if not self.__is_valid_password(password):
                        print(self.r.REGISTRATION_FAILED_MESSAGE)
                        continue
                    conf_password = getpass(self.r.CONFIRM_PASSWORD_MESSAGE)

                    if password != conf_password:
                        print(self.r.PASSWORD_MISMATCH_MESSAGE)
                        continue
                    age = input(self.r.ENTER_AGE_MESSAGE)
                    self.cinema_instance.register(username, password, age)
                    # todo: add some sort of verification that registration was successful?
                    return self.__logged_in_interaction(username)
                # Help menu option
                elif comm == self.settings.MAIN_MENU_OPTIONS[3]:
                    print(self.__print_main_menu())
                # Exit option
                elif comm == self.settings.MAIN_MENU_OPTIONS[4]:
                    self.closing_app = True
                    break

            except ValueError:
                print(self.r.VALUE_ERROR_MESSAGE)
                print(self.r.ENTER_HELP_TO_SEE_HELP_MENU)
            except KeyError:
                print(self.r.VALUE_ERROR_MESSAGE)
            finally:
                if self.closing_app:
                    return
                comm = input(self.r.CHOOSE_OPTION_MESSAGE)
       
