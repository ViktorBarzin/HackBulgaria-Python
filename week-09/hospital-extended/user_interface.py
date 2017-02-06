import re
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

    def __change_username(self, current_username):
        formatted_message = ''
        uname_changed = False
        # Change username
        change_username = str(input(self.r.CHANGE_USERNAME_PROMPT))
        if change_username.lower() == self.r.YES_OPTION:
            # todo: this will be problematic when setting usernames unique
            new_username = str(input(self.r.NEW_USERNAME_PROMPT))
            self.hospital_instance.change_username(current_username, new_username)
            formatted_message += self.r.SUCCESSFULLY_CHANGED_USERNAME + new_username + '\n'
            uname_changed = True
            global username
            username = new_username
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
        return formatted_message

    def __is_valid_password(self, password):
        invalid_attempts = 0
        is_valid = False
        while not is_valid and invalid_attempts < self.settings.MAX_FAILED_PASSWORD_ATTEMPTS:
            if re.match('.*[0-9].*', password) and\
               re.match('.*[A-Z].*', password) and\
               re.match('.*[a-z].*', password):
                return True
            invalid_attempts += 1
            password = input(self.r.NEW_PASSWORD_PROMPT + '({0} attempts remaining)'.
                             format(self.settings.MAX_FAILED_PASSWORD_ATTEMPTS - invalid_attempts + 1))
        return False

    # Prints main menu options
    def __print_main_menu(self):
        for k, v in self.r.MAIN_MENU_OPTIONS_DICT.items():
            # Print main menu options
            print(str(k) + self.r.MAIN_MENU_OPTIONS_SEPARATOR + ' ' + v)

    def __is_doctor(self, username):
        return self.r.DR_TITLE in username

    def __print_doctor_options(self):
        for number, option in self.settings.LOGGED_IN_DOCTOR_OPTIONS.items():
            print('{0}) {1}'.format(number, option))

    def __print_patient_options(self):
        for number, option in self.settings.LOGGED_IN_PATIENT_OPTIONS.items():
            print('{0}) {1}'.format(number, option))

    # Logged in user interaction
    def __logged_in_interaction(self, username):
        is_doctor = self.__is_doctor(username)
        print(self.hospital_instance.welcome(username))
        if is_doctor:
            self.__print_doctor_options()
        else:
            self.__print_patient_options()
        comm = input(self.r.CHOOSE_OPTION_MESSAGE)

        # todo: coupling too much to the options menu :/, find a fix
        # todo: repeating logic from initial interaction
        while comm != self.r.EXIT:
            try:
                if comm.lower() == 'help':
                    if is_doctor:
                        self.__print_doctor_options()
                    else:
                        self.__print_patient_options()
                    continue
                if is_doctor:
                    result = self.__act_upon_doctor_choice(int(comm), username)
                else:
                    result = self.__act_upon_patient_choice(int(comm), username)
                is_result_none = result is None
                print(result[0] if not is_result_none else '')
                if not is_result_none and len(result) > 1 and result[1] == self.settings.LOGOUT_KEY:
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
            return self.__change_username(doctor_username),
        # Raise into the hierarchy:
        elif choice == 6:
            new_title = input(self.r.NEW_ACADEMIC_TITLE_PROMPT)
            self.hospital_instance.change_academic_title(doctor_username, new_title)
            return self.r.SUCCESSFULLY_CHANGED_ACADEMIC_TITLE + new_title,
        # Log out
        elif choice == 7:
            self.hospital_instance.logout(doctor_username)
            return self.r.SUCCESSFULLY_LOGGED_OUT, self.settings.LOGOUT_KEY

    def __act_upon_patient_choice(self, choice, patient_username):
        # See free hours of your doctor
        if choice == 1:
            return 'Your doctor\'s free hours are:\n ' + \
                   ', '.join(self.hospital_instance.free_hours_of_patient_doctor(patient_username)),
        # Reserve hour for visitation
        elif choice == 2:
            free_hours = self.hospital_instance.free_hours_of_patient_doctor(patient_username)

            # Print choices
            for i in range(len(free_hours)):
                print('{0}) {1}\n'.format(i + 1, free_hours[i]))
            try:
                chosen_hour = free_hours[int(input(self.r.CHOOSE_FREE_HOUR)) - 1]
            except ValueError:
                return self.r.VALUE_ERROR_MESSAGE,
            except IndexError:
                return self.r.INDEX_ERROR_MESSAGE,

        # todo: visitation table's PK is id only, which may lead to inconsistent results
            doctor_id = self.hospital_instance.get_doctor_of(patient_username)['DOCTOR_ID']
            print(doctor_id, patient_username)
            self.hospital_instance.update_visitation(doctor_id,
                                                     self.hospital_instance.get_id_by_username(patient_username),
                                                     chosen_hour)
            return self.r.SUCCESSFULLY_CHOSE_VISITATION,

        # Stay at the hospital
        elif choice == 3:
            # In future make user chose from a set of options
            startdate = input(self.r.CHOOSE_HOSPITAL_STAY_START_DATE)
            enddate = input(self.r.CHOOSE_HOSPITAL_STAY_END_DATE)
            # Room number may consist of letters
            room = input(self.r.CHOOSE_ROOM)
            injury = input(self.r.CHOOSE_INJURY)
            patient_id = self.hospital_instance.get_id_by_username(patient_username)
            self.hospital_instance.insert_in_hospital_stay(startdate, room, injury, patient_id, enddate)
            return self.r.SUCCESSFULLY_ADDED_TO_HOSPITAL_STAY_LIST,
        # See your doctor's academic title
        elif choice == 4:
            doctor = self.hospital_instance.get_doctor_of(patient_username)
            return 'Your doctor {0} is {1}'.format(doctor['DOCTOR_USERNAME'], doctor['DOCTOR_ACADEMIC_TITLE']),
        # List your hospital stays
        elif choice == 5:
            stays = self.hospital_instance.get_all_hospital_stays_of(patient_username)
            # Formatting output
            return '\n'.join(['{start} - {end}, {room}, {injury}'.
                             format(start=x['startdate'], room=x['room'], injury=x['injury'],
                                    end=x['enddate'] if x['enddate'] is not '' else self.r.ONGOING_MESSAGE)
                              for x in stays]),

        # Change your doctor
        elif choice == 6:
            all_doctors = self.hospital_instance.get_all_doctors()
            # Perhaps not list the current patients doctor?
            print(self.r.CHOOSE_DOCTOR)
            # Formatting output
            for i in range(len(all_doctors)):
                print('{0}) {1}; Academic Title: {2}, Age: {3}'.format(i + 1, all_doctors[i]['USERNAME'],
                                                                       all_doctors[i]['ACADEMIC_TITLE'],
                                                                       all_doctors[i]['AGE']))
            try:
                doctor_choice = all_doctors[int(input()) - 1]
            except ValueError:
                return self.r.VALUE_ERROR_MESSAGE,
            except IndexError:
                return self.r.INDEX_ERROR_MESSAGE,
            self.hospital_instance.change_doctor_of(patient_username, doctor_choice['ID'])
            return self.r.SUCCESSFULLY_CHANGED_DOCTOR,
        # Change username and/or age
        elif choice == 7:
            return self.__change_username(patient_username),
        # Logout
        elif choice == 8:
            self.hospital_instance.logout(patient_username)
            return self.r.SUCCESSFULLY_LOGGED_OUT, self.settings.LOGOUT_KEY

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
                    if self.hospital_instance.login(username, password):
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

