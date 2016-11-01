class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.not_fraction_error_message = 'Argument not from type {0}'.format(__name__)

    def __str__(self):
        return "{0} / {1}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if not Fraction.is_fraction(other):
            raise TypeError(self.not_fraction_error_message)
        result = Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                          self.denominator * other.denominator)
        return result.simplify_fraction()

    def __mul__(self, other):
        if not Fraction.is_fraction(other):
            raise TypeError(self.not_fraction_error_message)
        result = Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        return result.simplify_fraction()

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __sub__(self, other):
        if not Fraction.is_fraction(other):
            raise TypeError(self.not_fraction_error_message)
        result = Fraction(self.numerator * other.denominator - other.numerator * self.denominator,
                          self.denominator * other.denominator)
        if result.numerator > 0:
            return result.simplify_fraction()
        elif result.numerator < 0:
            result = result.simplify_fraction()
            result.numerator = -result.numerator
            return result
        # Return 0 because numerator is 0
        return 0

    def __truediv__(self, other):
        if not Fraction.is_fraction(other):
            raise TypeError(self.not_fraction_error_message)
        return self.__mul__(Fraction(other.denominator, other.numerator))

    @staticmethod
    def is_fraction(f):
        return isinstance(f, Fraction)

    def simplify_fraction(self):
        # Make both numerator and denominator positive
        # in order not to brake logic
        self.numerator = abs(self.numerator)
        self.denominator = abs(self.denominator)

        def get_divisors(n):
            return [x for x in range(1, n + 1) if n % x == 0]

        def get_common_divisors(a, b):
            nominator_divisors = get_divisors(a)
            denominator_divisors = get_divisors(b)
            return set(nominator_divisors) & set(denominator_divisors)

        biggest_divisor = max(get_common_divisors(self.numerator, self.denominator))
        return Fraction(self.numerator // biggest_divisor, self.denominator // biggest_divisor)
