from common.operations.measures import distance

PI_VALUE = 3.1415

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
    def __init__(self, x, y):
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

class Rectangle:
    ''' 
    A class to create a rectangle somewhere in the field.

    ...

    Attributes
    ----------
    width: float
        width of the rectangle
    height: float
        height of the rectangle
    center: Point object
        center of the rectangle

    '''
    def __init__(self, width, height, center):
        '''
        Constructs all the necessary attributes for the rectangle object.

        Parameters
        ----------
        width: float
            width of the rectangle
        height: float
            height of the rectangle
        center: Point object
            center of the rectangle
            
        '''

        assert isinstance(center, Point) == True, "Center must be a point" 

        self.__width = width
        self.__height = height
        self.__center = center

    def is_inside(self, position):
        raise NotImplementedError

class Circle:
    ''' 
    A class to create a circle somewhere in the field.

    ...

    Attributes
    ----------
    ray: float
        ray of the circle
    center: Point object
        center of the circle
    area: float
        area of the circle

    Methods
    -------
    is_inside(point): bool
        returns True if the point is inside the circle or False if it is not inside the circle
            

    '''
    def __init__(self, ray, center):
        '''
        Constructs all the necessary attributes for the circle object.

        Parameters
        ----------
        ray: float
            ray of the circle
        center: Point object
            center of the circle

        '''

        assert isinstance(center, Point) == True, "Center must be a point" 
        
        self.__ray = ray
        self.__area = PI_VALUE * self.__ray * self.__ray
        self.__center = center
    
    def is_inside(self, point):
        '''
        Returns True if the point is inside the circle or False if it is not inside the circle. 
        '''
        dist = distance(point, self.__center)

        if dist > self.__ray:
            return False
        else:
            return True

class Line:
    ''' 
    A class to create a line somewhere in the field.

    ...

    Attributes
    ----------
    intial_point: Point object
        initial point of the line
    final_point: Point object
        final point of the line
    
    '''
    def __init__(self, initial_point, final_point) :
        '''
        Constructs all the necessary attributes for the line object.

        Parameters
        ----------
        intial_point: Point object
            initial point of the line
        final_point: Point object
            final point of the line

        '''
        self.__initial_point = initial_point
        self.__final_point = final_point