from socceranalyzer.common.geometric.point import Point

class Rectangle:
        def __init__(self, top_left:Point, bottom_right:Point):
            self.__top_left = top_left
            self.__bottom_right = bottom_right
            self.__width = self.__bottom_right.x - self.__top_left.x
            self.__height = self.__top_left.y - self.__bottom_right.y

        @property
        def top_left(self):
            return self.top_left

        @top_left.setter
        def top_left(self, point):
            self.__top_left = point

        @property
        def bottom_right(self):
            return self.bottom_right

        @bottom_right.setter
        def bottom_right(self, point):
            self.__bottom_right = point
        
        @property
        def width(self):
            return self.__width

        @property
        def height(self):
            return self.__height

        def is_inside(self, point: Point):
            if  self.__top_left.x <= point.x  <= self.__bottom_right.x and self.__bottom_right.y <= point.y  <= self.__top_left.y:
                return True
            else:
                return False



