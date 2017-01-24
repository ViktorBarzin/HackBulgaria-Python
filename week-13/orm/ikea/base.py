from collections import OrderedDict
from ikea.fields import Field


class BaseMeta(type):
    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(cls, name, bases, clsdict)

        if not hasattr(cls, '_registry'):
            setattr(cls, '_registry', set())

        if clsobj.__tablename__:
            cls._registry.add(clsobj)

        fields = {}

        for k, v in clsdict.items():
            if isinstance(v, Field):
                fields[k] = v

        for k, _ in clsdict.items():
            clsobj.pop(k)

        clsdict['fields'] = OrderedDict(fields)
        return clsobj
