class CashDesk:
    def __init__(self):
        self.total = 0


class Bill:
    def __init__(self, value):
        self._is_int_and_positive(value)
        self.value = value

    def __str__(self):
        return 'A {0}$ bill'.format(self.value)

    def __int__(self):
        return self.value

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    @staticmethod
    def _is_int_and_positive(value):
        if not isinstance(value, int):
            raise TypeError('Invalid value: {0}'.format(value))
        if value < 0:
            raise ValueError('Negative value:{0}'.format(value))


class BillBatch:
    def __init__(self, bills):
        self.is_list_of_bills(bills)
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

    def total(self):
        return sum(self.bills)

    def get_bills(self):
        return self.bills

    @classmethod
    def is_list_of_bills(cls, list_of_bills):
        if not isinstance(list_of_bills, list):
            raise TypeError('Not a list')
        for x in list_of_bills:
            if not isinstance(x, Bill):
                raise TypeError('Not all elements are Bills')
        return True

