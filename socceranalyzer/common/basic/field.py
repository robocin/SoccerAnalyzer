from socceranalyzer.common.geometric.point import Point
from socceranalyzer.common.geometric.rectangle import Rectangle

class Field:
    """"
        A class to represent a soccer field.

        field(width: float, length: float, center: Point,penalty_area_left: Rectangle, penalty_area_right: Rectangle, small_penalty_area_left: Rectangle,  small_penalty_area_right: Rectangle,  goalpost_left: Rectangle, goalpost_right: Rectangle)

        Attributes
        ----------
            public through @properties:
                width: float
                    total width of the field
                length: float
                    total length of the field
                center: Point
                    center of the field
                penalty_area_left: Rectangle
                    defines the left penalty area in the field
                penalty_area_right: Rectangle
                    defines the right penalty area in the field
                small_penalty_area_left: Rectangle
                    defines the left small penalty area in the field
                small_penalty_area_right: Rectangle
                    defines the right small penalty area in the field
                goalpost_left: Rectangle 
                    defines the left goalpost in the field 
                goalpost_right: Rectangle 
                    defines the right goalpost in the field 
                
    """
    def __init__(self, width: float = None, length: float = None, center: Point = None,
                penalty_area_left: Rectangle = None,
                penalty_area_right: Rectangle = None,
                small_penalty_area_left: Rectangle = None, 
                small_penalty_area_right: Rectangle = None,
                goalpost_left: Rectangle = None,
                goalpost_right: Rectangle = None
                ):
                
        self.__width = width
        self.__length = length
        self.__center = center
        self.__penalty_area_left = penalty_area_left
        self.__penalty_area_right = penalty_area_right
        self.__small_penalty_area_left = small_penalty_area_left
        self.__small_penalty_area_right = small_penalty_area_right
        self.__goalpost_left = goalpost_left
        self.__goalpost_right = goalpost_right
    
    @property
    def width(self):
        return self.__width
    
    @property
    def length(self):
        return self.__length
    
    @property
    def center(self):
        return self.__center
    
    @property
    def penalty_area_left(self):
        return self.__penalty_area_left
    
    @property
    def penalty_area_right(self):
        return self.__penalty_area_right

    @property
    def small_penalty_area_left(self):
        return self.__small_penalty_area_left
    
    @property
    def small_penalty_area_right(self):
        return self.__small_penalty_area_right
    
    @property
    def goalpost_left(self):
        return self.__goalpost_left
    
    @property
    def goalpost_right(self):
        return self.__goalpost_right



class Field2D(Field):
    def __init__(self):
        raise NotImplementedError
