from airport import *
from flight import Flight
from passenger import Passenger
from reservation import Reservation
from airport import Airport
from terminal import Terminal
from custom_date import Date
from constants import *


import unittest


class TestFlight(unittest.TestCase):
    def setUp(self):
        self.flight = None
        self.airport = Airport()

    def test_flight_constructor(self):
        self.flight = Flight(start_time=Date(29, 11, 2016, hour='12:20'), end_time=Date(29, 11, 2016, hour='15:30'),
                             passengers=100, max_passengers=120, from_dest="Sofia",
                             to_dest="London", terminal=Terminal(2, 30), declined=False)

    def test_terminal_constructor(self):
        self.terminal = Terminal(number=1, max_flights=20)

    def test_passenger_constructor(self):
        self.passenger = Passenger(first_name="Rositsa", last_name="Zlateva", flight=Flight(), age=22)

    def test_reservation_constructor(self):
        self.reservation = Reservation(flight=Flight(), passenger=Passenger(), accepted=True)

    def test_get_flights_for(self):
        self.flight = constants.flights[2]
        self.assertEqual(self.airport.get_flights_for(Date(29, 11, 2016, hour='12:20'))[0], self.flight)

    def test_get_flight_before(self):
        self.assertEqual(self.airport.get_flights_before(Date(29, 11, 2016, hour='15:29')),
                         [constants.flights[2]])

    def test_get_flight_from(self):
        self.assertEqual(constants.flights[0], self.airport.get_flight_from('Sofia')[0])

    def test_get_flight_to(self):
        self.assertEqual(constants.flights[0], self.airport.get_flight_to('Sofia')[0])

    #todo add get_flight_to and below


if __name__ == '__main__':
    unittest.main()
