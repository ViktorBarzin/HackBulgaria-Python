from exceptions import *
from resources import *


class BankAccount:
    def __init__(self, name, balance, currency):
        self.__name = name
        self.__currency = currency
        if not self.__is_negative(balance):
            self.__balance = balance
        else:
            raise ValueError(NEGATIVE_NUMBER_ERROR_MESSAGE)
        self.__history = [ACCOUNT_CREATED_MESSAGE]

    def __str__(self):
        return 'Bank account for {name} with balance of {amount}{currency}'.format(
            name=self.__name, amount=self.__balance, currency=self.__currency)

    def __int__(self):
        self.__update_history(INT_CHECK_MESSAGE + self.__balance + ' ' + self.__currency)
        return self.__balance

    def transfer_to(self, account, amount):
        try:
            if type(account) != __class__:
                raise TypeError(NOT_BANK_ACCOUNT_TYPE_ERROR_MESSAGE)
            if self.__is_negative(amount):
                raise ValueError(NEGATIVE_NUMBER_ERROR_MESSAGE)
            if self.__is_negative(self.__balance - amount):
                raise ValueError(NEGATIVE_MONEY_ERROR_MESSAGE)
            if self.__currency != account.__currency:
                raise CurrencyError(DIFFERENT_CURRENCIES_ERROR_MESSAGE)
        except Exception:
            self.__update_history(TRANSFER + ' ' + FAILED)
            return False
        self.__balance -= amount
        account.__balance += amount
        self.__update_history(TRANSFER + ' ' + FROM + ' ' + account.__name +
                              ' ' + FOR + ' ' + str(amount) + ' ' + self.__currency)
        account.__update_history(TRANSFER + ' ' + TO + ' ' + self.__name +
                                 ' ' + FOR + ' ' + str(amount) + ' ' + self.__currency)
        return True

    def __update_history(self, item):
        self.__history.append(item)

    def history(self):
        return self.__history

    def deposit(self, value):
        if not self.__is_negative(value):
            self.__balance += value
            self.__update_history(DEPOSITED + ' ' + value + self.__currency)
        else:
            raise ValueError(NEGATIVE_NUMBER_ERROR_MESSAGE)

    def balance(self):
        self.__update_history(BALANCE_CHECK + str(self.__balance) + self.__currency)
        return self.__balance

    def withdraw(self, value):
        if not self.__is_negative(self.__balance - value) and not self.__is_negative(value):
            self.__balance -= value
            self.__update_history(value + self.__currency + WAS_WITHDRAWED)
            return True
        self.__update_history(WITHDRAW_MESSAGE + value + self.__currency + FAILED)
        return False

    @classmethod
    def __is_negative(cls, number):
        return number < 0
