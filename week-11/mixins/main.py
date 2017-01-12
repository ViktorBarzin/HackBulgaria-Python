import serializers


class A(serializers.Jsonable, serializers.Xmlable):
    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def print_me(self):
        print(self.__dict__)


a = A(age=10, name='ime')
b = A(age=20, friend=a)
d = A(age=20, friend=b)
a_to_json_str = (a.to_xml())
print(a_to_json_str)
e = A.from_xml(a_to_json_str)
e.print_me()
# print(c.print_me())

