import re
from exceptions import *


class Panda:
    def __init__(self, name, email, gender):
        self.__name = name
        if self.__check_email(email):
            self.__email = email
        else:
            raise InvalidEmailError
        self.__gender = gender

    def __str__(self):
        return 'I am {name} and my email is {email}'.format(name=self.__name, email=self.__email)

    def __eq__(self, other):
        return self.__name == other.name()\
                and self.__email == other.email()\
                and self.__gender == other.gender()

    def __hash__(self):
        return 41 * hash(self.__name) + hash(self.__email) * hash(self.__gender) + 69

    @staticmethod
    def __check_email(email):
        return re.match('[a-zA-Z]+@[a-zA-Z]+\.', email)

    def name(self):
        return self.__name

    def email(self):
        return self.__email

    def gender(self):
        return self.__gender

    def is_male(self):
        return 'male' in self.__gender

    def is_female(self):
        return not self.is_male()


class PandaSocialNetwork:
    def __init__(self):
        self.network = {}

    def add_panda(self, panda):
        if panda in self.network:
            raise PandaAlreadyThereError
        self.network[panda] = []

    def has_panda(self, panda):
        return panda in self.network

    def make_friends(self, panda1, panda2):
        if panda1 not in self.network:
            self.add_panda(panda1)
        if panda2 not in self.network:
            self.add_panda(panda2)

        self.network[panda1].append(panda2)
        self.network[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        return panda2 in self.network[panda1]\
         and panda1 in self.network[panda2]

    def friends_of(self, panda):
        if panda not in self.network:
            return False
        return self.network[panda]

    def connection_level(self, panda1, panda2):
        visited = [panda1]
        queue = [panda1]
        counter = 0

        while queue:
            current = queue.pop()
            counter += 1
            print([x.name() for x in self.network[current]])
            print(current.name(), panda2.name())
            if current == panda2:
                return counter
            for friend in self.network[current]:
                if friend not in visited:
                    visited.append(friend)
                    queue.extend(self.network[friend])
        return -1

