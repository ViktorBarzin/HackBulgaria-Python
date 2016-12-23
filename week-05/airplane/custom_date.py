
class Date:
    def __init__(self, day, month, year, hour='00:00'):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour

    def __str__(self):
        return str(tuple([self.day, self.month, self.year, self.hour]))

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.day == other.day\
            and self.month == other.month\
            and self.year == other.year\
            and self.hour == other.hour

    def __lt__(self, other):
        self_hour = int(self.hour.split(':')[0])
        self_minute = int(self.hour.split(':')[1])

        other_hour = int(other.hour.split(':')[0])
        other_minute = int(other.hour.split(':')[1])

        return self.year <= other.year\
                and self.month <= other.month\
                and self.day <= other.day\
                and self_hour <= other_hour\
                and self_minute < other_minute

    def __gt__(self, other):
        return not self.__lt__(other)



