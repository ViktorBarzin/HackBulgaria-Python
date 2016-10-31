class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{0} / {1}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __sub__(self, other):


