from ikea.base import BaseMeta


class Field(metaclass=BaseMeta):
    __tablename__ = None


class PKColumn(Field):
    __tablename__ = 'PKColumn'


class IntegerColumn(Field):
    __tablename__ = 'IntegerColumn'


class TextColumn(Field):
    __tablename__ = 'TextColumn'

