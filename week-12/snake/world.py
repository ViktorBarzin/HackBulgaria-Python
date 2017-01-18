class GameObject(object):
    pass


class GameWorld(GameObject):
    def __init__(self, size):
        self.size = size


class Cell(GameObject):
    def __init__(self, content=None):
        if isinstance(content, GameObject):
            self.content = content

