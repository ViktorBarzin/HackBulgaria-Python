import re
import json
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
        return re.match('[a-zA-Z0-9]+@[a-zA-Z0-9]+\.', email)

    def name(self):
        return self.__name

    def email(self):
        return self.__email

    def gender(self):
        return self.__gender

    def isMale(self):
        return 'male' in self.__gender

    def isFemale(self):
        return not self.isMale()

    def serialize(self):
        return self.__dict__


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
            if current == panda2:
                return counter
            counter += 1
            for friend in self.network[current]:
                if friend not in visited:
                    visited.append(friend)
                    queue.append(friend)
        return -1

    def are_connected(self, panda1, panda2):
        return self.connection_level(panda1, panda2) != -1

    def how_many_gender_in_network(self, level, panda, gender):
        visited = [panda]
        queue = [panda]
        counter = 0
        gender_counter = 0
        while queue:
            current = queue.pop()
            if current.gender() == gender and current != panda:
                gender_counter += 1
            counter += 1

            for friend in self.network[current]:
                if friend not in visited and counter <= level:
                    visited.append(friend)
                    queue.append(friend)
        return gender_counter

    def save(self, file_path):
        with open(file_path, 'w') as w:
            json.dump(dict(members=[x.serialize() for x in self.network]), w, indent=4)
        print(dict(members=[x.serialize() for x in self.network]))
