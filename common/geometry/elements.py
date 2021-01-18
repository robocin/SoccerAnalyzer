from common.operations.measures import distance

PI_VALUE = 3.1415

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, width, height, center):
        
        assert isinstance(center, Point) == True, "Center must be a point" 

        self.__width = width
        self.__height = height
        self.__center = center

    def is_inside(self, position):
        raise NotImplementedError

class Circle:
    def __init__(self, ray, center):

        assert isinstance(center, Point) == True, "Center must be a point" 
        
        self.__ray = ray
        self.__area = PI_VALUE * self.__ray * self.__ray
        self.__center = center
    
    def is_inside(self, point):
        dist = distance(point, self.__center)

        if dist > self.__ray:
            return False
        else:
            return True

class Line:
    def __init__(self, initial_point, final_point) :
        self.__initial_point = initial_point
        self.__final_point = final_point