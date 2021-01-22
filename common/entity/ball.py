import warnings

class Ball:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    
    def x(self):
        return self.__x

    def y(self):
        return self.__y