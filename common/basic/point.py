class Point:
    '''
    A class to create a point somewhere in the field.
    ...
    Attributes
    ----------
    x: float
        x coordinates of the point in the field
    y: float
        y coordinates of the point in the field
    '''

    def __init__(self, x=0, y=0):
        '''
        Constructs all the necessary attributes for the point object.
        Parameters
        ----------
        x: float
            x coordinates of the point in the field
        y: float
            y coordinates of the point in the field
        '''
        self.x = x
        self.y = y

    def __str__(self):
        return "x: {} - y: {}".format(self.x, self.y)