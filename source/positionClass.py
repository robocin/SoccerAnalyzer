import numpy as np
import pandas as pd

class Position:
    def __init__(self, x, y, timestamp):
        self.__x = x
        self.__y = y
        self.__timestamp = timestamp

    def setX(self, x):
        self.__x = x
    
    def setY(self, y):
        self.__y = y
    
    def setTime(self, timestamp):
        self.__timestamp = timestamp
    
    def setPosition(self, x, y):
        self.__x = x
        self.__y = y

    def setEvent(self, x, y, timestamp):
        self.setPosition(x,y)
        self.setTime(timestamp)

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getTimestamp(self):
        return self.__timestamp

    def getPosition(self):
        pos = [self.__x, self.__y]
        return pos
    
    def getEvent(self):
        e = [self.__x, self.__y, self.__timestamp]
        return e