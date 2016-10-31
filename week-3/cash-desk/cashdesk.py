from collections import defaultdict

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
        self._bills = bills

    def __len__(self):
        return len(self._bills)

    def total(self):
        return sum(self._bills)

    def get_bills(self):
        return self._bills

    @classmethod
    def is_list_of_bills(cls, list_of_bills):
        if not isinstance(list_of_bills, list):
            raise TypeError('Not a list')
        for x in list_of_bills:
            if not isinstance(x, Bill):
                raise TypeError('Not all elements are Bills')
        return True


class CashDesk:
    def __init__(self):
        self.__total = 0
        self.__inventory = defaultdict(int)

    def take_money(self, money):
        if isinstance(money, BillBatch):
            for bill in money.get_bills():
                self.__total += int(bill)
                self.__inventory[int(bill)] += 1
        elif isinstance(money, Bill):
            self.__total += int(money)
            self.__inventory[str(money)] += 1

    def inspect(self):
        result = 'We have the following count of bills, sorted in ascending order:'
        for key in sorted(self.__inventory.keys()):
            result += '\n{0}$ bills - {1}'.format(key, self.__inventory[key])
        return result

    def get_inventory(self):
        return self.__inventory


    def total(self):
        return 'We have a total of {0}$ in the desk'.format(int(Bill))