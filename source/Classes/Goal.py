import Event

class Goal(Event):
    def __init__(self, position=None, owner=None):
        super().__init__(self, position, owner)