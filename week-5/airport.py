import constants
from custom_date import Date
from flight import Flight
from terminal import Terminal

from constants import *



class Airport:
    def __init__(self, flights=constants.flights):
        self.flights = flights
        # print([str(x.start_time) for x in self.flights])

    def get_flights_for(self, date):
        return [x for x in self.flights if str(x.start_time) == str(date)]
        # return [x for x in self.flights if str(x.start_time) == date]

    def get_flights_before(self, date):
        return [x for x in self.flights if x.start_time < date]

    def get_flight_from(self, from_dest):
        return [x for x in self.flights if x.from_dest == from_dest]

    def get_flight_to(self, to_dest):
        return [x for x in self.flights if x.to_dest == to_dest]

    def get_flight_to(self, destination, date):
        return [x for x in self.flights if x.to_dest == destination and x.start_time == date]

    def get_flight_from(self, destination, date):
        return [x for x in self.flights if x.from_dest == destination and x.start_time == date]

    def get_terminal_flights(self, terminal):
        return [x for x in self.flights if x.terminal == terminal]

    def get_terminal_flights_on(self,terminal, date):
        return [x for x in self.get_terminal_flights(terminal) if x.start_time == date]


def main():
    pass

if __name__ == '__main__':
    main()