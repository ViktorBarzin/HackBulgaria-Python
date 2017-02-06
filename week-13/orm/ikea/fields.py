from base import ColumnMeta


class Column(metaclass=ColumnMeta):
    pass


class PKColumn(Column):
    pass


class IntegerColumn(Column):
    pass


class TextColumn(Column):
    pass

