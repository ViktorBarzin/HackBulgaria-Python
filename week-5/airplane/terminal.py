class Terminal:
    def __init__(self, number, max_flights):
        self.number = number
        self.max_flights = max_flights

    def __eq__(self, other):
        return self.number == other.number\
    and self.max_flights == other.max_flights

