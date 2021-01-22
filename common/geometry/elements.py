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
    def __init__(self, width=0, height=0, center_x=0, center_y=0):
        self.width = width
        self.height = height
        self.center = [center_x, center_y]

    def center(self):
        center = [self.width/2, self.height/2]

        return center

    def is_inside(self, position):
        pass

class Circle:
    def __init__(self, ray, center):
        self.__ray = ray
        self.__area = PI_VALUE * self.__ray * self.__ray
        self.__center = center

    def describe(self):
        print('Ray: {}\nArea: {}'.format(self.ray,self.area))

    def is_inside(self, point):
        position = Point(self.center[0], self.center[1])
        dist = distance(point, position)

        if dist > self.ray:
            return False
        else:
            return True

class Line:
    def __init__(self, initial_point=None, final_point=None) :
        self.__initial_point = initial_point
        self.__final_point = final_point