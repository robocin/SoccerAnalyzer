class StringListPositions:
    """
        This class is a named container of elements 
    """
    def __init__(self):
        self.items = []


class StringListItem:
    """
        This class is a named container element
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

class ThresholdCollection:
    """
        This class is a named container that can have it's values reset.

        Methods
        -------
            public:
                reset: None
                    Reset all values class attr to default
    """
    def __init__(self):
        self.corner_thr = 10
        self.kick_in_thr = 10
        self.foul_thr = 10

    def reset(self, ck=10, ki=10, fk=10):
        self.corner_thr = ck
        self.kick_in_thr = ki
        self.foul_thr = fk
