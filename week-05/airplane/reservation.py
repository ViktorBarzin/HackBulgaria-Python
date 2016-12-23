from flight import Flight
from passenger import Passenger


class Reservation:
    def __init__(self, flight=Flight(), passenger=Passenger(), accepted=True):
        self.flight = flight
        self.passenger = passenger
        self.accepted = accepted