from getpass import getpass


class UserInterface:
    def __init__(self, resource_file, hospital_instance, settings_file):
        self.r = resource_file
        self.settings = settings_file
        self.hospital_instance = hospital_instance
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

    # def __logged_in_interaction(self, username):
    #     print(self.hospital_instance.welcome(username))
    #     self.logging_out = False
    #     if self.r.DR_TITLE in username:
    #         return self.__logged_in_doctor_interaction(username)
    #     return self.__logged_in_patient_interaction(username)

    def __is_doctor(self, username):
        return self.r.DR_TITLE in username

    def __print_doctor_options(self):
        for number, option in self.settings.LOGGED_IN_DOCTOR_OPTIONS.items():
            print('{0}) {1}'.format(number, option))

    def __print_user_options(self):
        for number, option in self.settings.LOGGED_IN_PATIENT_OPTIONS.items():
            print('{0}) {1}'.format(number, option))

    def __logged_in_interaction(self, username):
        is_doctor = self.__is_doctor(username)

        if is_doctor:
            self.__print_doctor_options()
        else:
            self.__print_user_options()
        comm = input(self.r.CHOOSE_OPTION_MESSAGE)

        # todo: coupling too much to the options menu :/, find a fix
        # todo: repeating logic from initial interaction
        while comm != self.r.EXIT:
            try:
                if comm.lower() == 'help':
                    self.__print_doctor_options()
                    continue
                if is_doctor:
                    result = self.__act_upon_doctor_choice(int(comm), username)
                else:
                    result = self.__act_upon_patient_choice(int(comm), username)
                print(result[0])
                if len(result) > 1 and result[1] == self.settings.LOGOUT_KEY:
                    self.logging_out = True
                    break

            except ValueError:
                print(self.r.VALUE_ERROR_MESSAGE)
                print(self.r.ENTER_HELP_TO_SEE_HELP_MENU)
            except KeyError:
                print(self.r.VALUE_ERROR_MESSAGE)
            finally:
                if self.logging_out:
                    return
                comm = input(self.r.CHOOSE_OPTION_MESSAGE)

    # Returns a tuple in order to check if not logged out
    def __act_upon_doctor_choice(self, choice, doctor_username):
        # List your patients
        if choice == 1:
            # Format result for priting
            result = self.hospital_instance.list_patients(doctor_username)
            return self.r.YOUR_PATIENTS_ARE_MESSAGE + ', '.join(result),
        # Add hours for visitation
        elif choice == 2:
            visitation_start_hour = input(self.r.ENTER_VISITATION_START_HOUR)
            self.hospital_instance.add_visitation_hour(doctor_username, visitation_start_hour)
            return self.r.SUCCESSFULLY_ADDED_VISITATION,
        # Delete free hours of visitation
        elif choice == 3:
            self.hospital_instance.delete_free_visitation_hours()
            return self.r.SUCCESSFULLY_DELETED_FREE_VISITATION_HOURS_MESSAGE,
        # See room and duration of hospital stay for each of your patients
        elif choice == 4:
            results = self.hospital_instance.get_room_and_username_duration_start_and_end_for_all_patients()
            formatted_message = ''
            for result in results:
                # Format message for output
                formatted_message += 'User: {0}, Room: {1}, Start Date: {2}, End Date: {3}\n'\
                    .format(result['username'], result['room'], result['startdate'], result['enddate']
                            if result['enddate'] is not None
                            else self.r.ONGOING_MESSAGE)
            return formatted_message,
        # Change username and/or age
        elif choice == 5:
            formatted_message = ''
            uname_changed = False
            # Change username
            change_username = str(input(self.r.CHANGE_USERNAME_PROMPT))
            if change_username.lower() == self.r.YES_OPTION:
                # todo: this will be problematic when setting usernames unique
                new_username = str(input(self.r.NEW_USERNAME_PROMPT))
                self.hospital_instance.change_username(doctor_username, new_username)
                formatted_message += self.r.SUCCESSFULLY_CHANGED_USERNAME + new_username + '\n'
                uname_changed = True
            # Change age
            change_age = str(input(self.r.CHANGE_AGE_PROMPT))
            if change_age.lower() == self.r.YES_OPTION:
                try:
                    new_age = input(self.r.NEW_AGE_PROMPT)
                    new_age = int(new_age)
                    # Check if username is changed in previous prompt and change age accordingly
                    if not uname_changed:
                        self.hospital_instance.change_age(doctor_username, new_age)
                    else:
                        self.hospital_instance.change_age(new_username, new_age)
                    formatted_message += self.r.SUCCESSFULLY_CHANGED_AGE + str(new_age) + '\n'
                except ValueError:
                    print(self.r.VALUE_ERROR_MESSAGE)
            return formatted_message,
        # Raise into the hierarchy:
        elif choice == 6:
            new_title = input(self.r.NEW_ACADEMIC_TITLE_PROMPT)
            self.hospital_instance.change_academic_title(doctor_username, new_title)
            return self.r.SUCCESSFULLY_CHANGED_ACADEMIC_TITLE + new_title,
        # Log out
        elif choice == 7:
            self.hospital_instance.logout(doctor_username)
            return self.r.SUCCESSFUL1LY_LOGGED_OUT, self.settings.LOGOUT_KEY

    def __act_upon_patient_choice(self,choice, patient_username):
        print('WORKS!')

    def __logged_in_patient_interaction(self, username):
        for number, option in self.settings.LOGGED_IN_PATIENT_OPTIONS.items():
            print('{0}) {1}'.format(number, option))

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
                    password = input(self.r.ENTER_PASSWORD_MESSAGE)
                    if self.hospital_instance.login(username, password):
                        # Start logged in user interaction
                        self.__logged_in_interaction(username)

                    else:
                        print(self.r.LOGIN_FAILED_MESSAGE)
                # Register option
                elif comm == self.settings.MAIN_MENU_OPTIONS[2]:
                    # todo: usernames MUST be unique
                    username = input(self.r.ENTER_USERNAME_MESSAGE)
                    password = input(self.r.ENTER_PASSWORD_MESSAGE)
                    conf_password = input(self.r.CONFIRM_PASSWORD_MESSAGE)
                    age = input(self.r.ENTER_AGE_MESSAGE)
                    if password != conf_password:
                        print(self.r.PASSWORD_MISMATCH_MESSAGE)
                        continue
                    self.hospital_instance.register(username, password, age)
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
