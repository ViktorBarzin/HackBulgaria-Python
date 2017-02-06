from flight import Flight


class Passenger:
    def __init__(self, first_name="Rositsa", last_name="Zlateva", flight=Flight(), age=22):
        self.first_name = first_name
        self.last_name = last_name
        self.flight = flight
        self.age = age

    def __eq__(self, other):
        return self.first_name == other.first_name\
    and self.last_name == other.last_name\
    and self.flight == other.flight\
    and self.age == other.age