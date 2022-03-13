

class Rectangle:
        def __init__(self, start_point, width, height):
            self.__start_point = start_point
            self.__width = width
            self.__height = height

        @property
        def start_point(self):
            return self.__start_point

        @start_point.setter
        def start_point(self, point):
            self.__start_point = point
        
        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, width):
            self.__width = width

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, height):
            self.__height = height

        def is_inside(self, point):
            if  self.__start_point[0] <= point[0]  <= (self.__width + self.start_point[0]) and self.__start_point[1] <= point[1]  <= (self.__height + self.start_point[1]):
                return True
            else:
                return False

        

        
