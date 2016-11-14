from custom_date import Date
from terminal import Terminal


class Flight:
    def __init__(self, start_time=Date(29, 11, 2016, hour='12:20'), end_time=Date(29, 11, 2016, hour='15:30'),
                             passengers=100, max_passengers=120, from_dest="Sofia",
                             to_dest="London", terminal=Terminal(2, 30), declined=False):
        self.start_time = start_time
        self.end_time = end_time
        self.passengers = passengers
        self.max_passengers = max_passengers
        self.from_dest = from_dest
        self.to_dest = to_dest
        self.terminal = terminal
        self.declined = declined

    def __eq__(self, other):
        return self.start_time == other.start_time\
    and self.end_time == other.end_time\
    and self.passengers == other.passengers\
    and self.max_passengers == other.max_passengers\
    and self.from_dest == other.from_dest\
    and self.to_dest == other.to_dest\
    and self.terminal == other.terminal\
    and self.declined == other.declined

    def get_flight_duration(self):
        return 