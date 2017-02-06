class DeclarativeMeta(type):
    def __new__(cls, name, bases, objdict):
        pass


class Serializer(metaclass=DeclarativeMeta):
    def __init__(self, obj):
        pass

class CommentSerializer(Serializer):
    # email = EmailField()
    # content = CharField()
    # created_at = DateTimeField()
    def __init__(self, arg*):
        CURSOR


class EmailField(object):
    def __init__(self):
        return
