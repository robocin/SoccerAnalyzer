class StringListPositions:
    def __init__(self):
        self.items = []


class StringListItem:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class ThresholdCollection:
    def __init__(self):
        self.corner_thr = 10
        self.kick_in_thr = 10
        self.foul_thr = 10

    def reset(self, ck=10, ki=10, fk=10):
        self.corner_thr = ck
        self.kick_in_thr = ki
        self.foul_thr = fk
