import cinema.settings.resources as resources
import re
import cinema.view_models.view_models as view_models
import cinema.settings.settings as settings
from cinema.helpers.decorators import clear_screen


class LoggedInMenu():
    def __init__(self, username):
        self.username = username
        self.r = resources
        self.vm = view_models.ViewModel()
        self.settings = settings
        self.logout_commands = ['6', 'exit', 'quit']
        self.help_commands = ['help', 'h']

    @clear_screen
    def __print_menu_options(self):
        for k, v in self.r.LOGGED_IN_MENU_OPTIONS_DICT.items():
            print('{0}) {1}'.format(k, v))

    @clear_screen
    def __show_all_movies(self):
        movies = self.vm.show_all_movies()
        for movie in movies:
            print('[{}] - "{}" ({})'.format(movie.id, movie.name, movie.rating))

    def __continue_reservation(self):
        quit_registration = input('Do you want to cancel your reservation[Y/n]:')
        if quit_registration.lower() == 'y' or quit_registration.lower() == 'yes' or quit_registration == '':
            return False
        return True

    @clear_screen
    def __print_projections(self, result_projections, movie_name):
        if len(result_projections) == 0:
            print('There are no projections')
            return
        print('Projections for {}:'.format(movie_name))
        for projection in result_projections:
            print('[{}] - {} {} ({})'.format(projection.id, projection.date, projection.time, projection.projection_type))

    def __print_reservation(self, movie, projection, seats):
        print('This is your reservation:\nMovie:{} {}\nDate and time: {} {}\nSeats: {}'.format(movie.name, movie.rating,
                projection.date, projection.time, ', '.join([str(x) for x in seats])))

    @clear_screen
    def __print_user_reservations(self, user_id):
        reservations = self.vm.get_all_user_reservations(user_id)
        print('There are your reservations:')
        for r in reservations:
            print('{0}) {1} on {2} {3}'.format(r[0].id, r[2].name, r[1].date, r[1].time))

    @clear_screen
    def start_interaction(self, username):
        print('hi ' + username)
        self.__print_menu_options()
        comm = input(self.r.CHOOSE_OPTION_MESSAGE)
        user_id = self.vm.get_user_id(username)

        while comm not in self.logout_commands:
            try:
                comm = int(comm)
                if comm > len(self.r.LOGGED_IN_MENU_OPTIONS_DICT.keys()):
                    raise ValueError
            except ValueError:
                print('Invalid option selected.')
                self.__print_menu_options()

            # Check what option is chosen
            # Show movies option
            if comm == 1:
                self.__show_all_movies()
            elif comm == 2:
                # Get movie id
                try:
                    movie_id = int(input('Enter the movie id:'))

                    # Getting the movie name from id
                    try:
                        movie = [x for x in self.vm.show_all_movies() if x.id == movie_id][0]
                    except IndexError:
                        print('There is no movie with this id')
                        # The continue lets the user choose again movie id
                        continue
                    date = input('Enter projection date (format is: yyyy-mm-dd) [optional]:')
                except ValueError:
                    print('Invalid movie id')

                result_projections = self.vm.show_projections_for_movie(movie_id, date)
                self.__print_projections(result_projections, movie.name)

            # Make a reservation
            elif comm == 3:
                # Get number of tickets
                try:
                    number_of_tickets = int(input('Enter the number of tickets you wish to reserve:'))
                except ValueError:
                    print('Invalid number of tickets!')
                    if self.__continue_reservation():
                        # The continue lets the user choose again number of tickets
                        continue
                    else:
                        comm = input(self.r.CHOOSE_OPTION_MESSAGE)
                        continue

                self.__show_all_movies()
                all_movies = self.vm.show_all_movies()
                # Get movie id from user
                try:
                    movie_id = int(input('Please select the movie id:'))
                    if movie_id not in [x.id for x in all_movies]:
                        raise ValueError('There is no movie with this id')
                except ValueError as e:
                    print(e)
                    if self.__continue_reservation():
                        continue
                    else:
                        comm = input(self.r.CHOOSE_OPTION_MESSAGE)
                        continue

                movie = [x for x in all_movies if x.id == movie_id][0]
                projections = self.vm.show_projections_for_movie(movie_id)
                if len(projections) == 0:
                    choose_another_movie = input('There are no projections for this movie.\nDo you wish to make a reservation for another one?[Y/n]:')
                    if choose_another_movie.lower() == 'y' or choose_another_movie.lower() == 'yes' or choose_another_movie == '':
                        continue
                    else:
                        comm = input(self.r.CHOOSE_OPTION_MESSAGE)
                        continue
                self.__print_projections(projections, movie.name)
                # Get projection id
                try:
                    projection_id = int(input('Select projection date:'))
                    if projection_id not in [x.id for x in projections]:
                        raise ValueError('There is no projection with this id!')
                except ValueError as e:
                    print(e)
                    if self.__continue_reservation():
                        continue
                    else:
                        comm = input(self.r.CHOOSE_OPTION_MESSAGE)
                        continue
                print('In a future version you will see the seats you choose from')
                seats = []
                # Get row and col
                try:
                    for i in range(number_of_tickets):
                        row_col = [int(x) for x in re.split('[^0-9]', input('Cinema size is ({},{})\nChoose seat {}(row,col):'.format(self.settings.CINEMA_HALL_SIZE[0], self.settings.CINEMA_HALL_SIZE[1], i + 1))) if x != '']
                        row = row_col[0]
                        col = row_col[1]
                        if row > self.settings.CINEMA_HALL_SIZE[0] or col > self.settings.CINEMA_HALL_SIZE[1]:
                            raise ValueError('Invalid row or col!\nYou must start over!')
                        seats.append((row, col))
                except ValueError as e:
                    print(e)
                    if self.__continue_reservation():
                        continue
                    else:
                        comm = input(self.r.CHOOSE_OPTION_MESSAGE)
                        continue
                movie = [x for x in all_movies if x.id == movie_id][0]
                projection = [x for x in projections if x.id == projection_id][0]
                # print(movie['NAME'])
                self.__print_reservation(movie, projection, seats)

                should_finalize = True
                finalize_reservation = input('Confirm your reservation (type "finalize"):')
                if finalize_reservation.lower() != 'finalize' and finalize_reservation.lower() != 'y' and\
                        finalize_reservation.lower() != 'yes':
                        should_finalize = False
                        if self.__continue_reservation():
                            should_finalize = True
                        else:
                            comm = input(self.r.CHOOSE_OPTION_MESSAGE)
                            continue
                if should_finalize:
                    for ticket in seats:
                        # Option to cancel reservation here?
                        if not self.vm.create_reservation(user_id, projection.id, ticket[0], ticket[1]):
                            print('Seats "{0}" already taken! Not saving those.'.format(ticket))
                        else:
                            print('Saved {}'.format(ticket))

            # Cancel reservation
            elif comm == 4:
                # This works as cancel all reservations for a user but oh well
                self.__print_user_reservations(user_id)
                # Get reservation id
                try:
                    projection_id = int(input('Enter projection id:'))
                    # Add check if there is such a registration
                    self.vm.cancel_registration(user_id, projection_id)
                    print('Successfully deleted reservation!')
                except ValueError:
                    print('Invalid value!')
                    comm = input(self.r.CHOOSE_OPTION_MESSAGE)

            # Help
            elif comm == 5:
                self.__print_menu_options()
                comm = input(self.r.CHOOSE_OPTION_MESSAGE)
            # Exit
            elif comm == 6:
                return

            comm = input(self.r.CHOOSE_OPTION_MESSAGE)
            # Add the following line as decorator
            # os.system('clear')

