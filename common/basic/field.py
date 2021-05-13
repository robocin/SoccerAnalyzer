from common.geometry.elements import Point
from common.geometry.elements import Rectangle

class Field:
    ''' 
    A class to create a point somewhere in the field.

    ...

    Attributes
    ----------
    width: float
        total width of the field
    length: float
        total length of the field
    center: float
        center of the field
    small_penalty_area: Rectangle object
        defines the small penalty area in the field
    penalty_area: Rectangle object
        defines the penalty area in the field

    '''
    def __init__(self, width, length, center, small_penalty_area, penalty_area):
        '''
        Constructs all the necessary attributes for the field object.

        Parameters
        ----------
        width: float
            total width of the field
        length: float
            total length of the field
        center: float
            center of the field
        small_penalty_area: Rectangle object
            defines the small penalty area in the field
        penalty_area: Rectangle object
            defines the penalty area in the field

        '''
        self.__width = width
        self.__length = length
        self.__center = center
        self.__small_penalty_area = small_penalty_area
        self.__penalty_area = penalty_area

class Field2D(Field):
    raise NotImplementedError
    """
        self.width = 105
        self.height = 68
        self.pa_front = 36
        self.pa_upper = 20
        self.pa_lower = -20
        self.spa_front = 47
        self.spa_upper = 9
        self.spa_lower = -9 
        self.max_x = 52.5
        self.min_x = -52.5
        self.max_y =  34
        self.min_y = -34

    """