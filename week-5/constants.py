from custom_date import Date
from terminal import Terminal
from flight import Flight


flights = [Flight(start_time=Date(29, 12, 2016, hour='12:20'), end_time=Date(29, 11, 2016, hour='15:30'),
                             passengers=100, max_passengers=120, from_dest="Sofia",
                             to_dest="Sofia", terminal=Terminal(2, 30), declined=False), Flight(start_time=Date(30, 11, 2016, hour='12:20'), end_time=Date(29, 11, 2016, hour='15:30'),
                             passengers=100, max_passengers=120, from_dest="Plovdiv",
                             to_dest="London", terminal=Terminal(2, 30), declined=False),
           Flight(start_time=Date(29, 11, 2016, hour='12:20'), end_time=Date(29, 11, 2016, hour='15:30'),
                             passengers=100, max_passengers=120, from_dest="Burgas",
                             to_dest="Varna", terminal=Terminal(2, 30), declined=False)]