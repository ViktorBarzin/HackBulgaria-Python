class PandaAlreadyThereError(Exception):
    def __init__(self, message=None):
        super.__init__(message)


class PandasAlreadyFriendsError(Exception):
    def __init__(self, message=None):
        super.__init__(message)


class InvalidEmailError(Exception):
    def __init__(self, message):
        super.__init__(message)


