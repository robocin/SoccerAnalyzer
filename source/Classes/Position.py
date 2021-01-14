class Position:
    def __init__(self, x = 0, y = 0, timestamp = 0):
        self.__x = x
        self.__y = y
        self.__timestamp = timestamp

    def set_x(self, x):
        self.__x = x
    def set_y(self, y):
        self.__y = y
    def set_time(self, timestamp):
        self.__timestamp = timestamp
    def set_position(self, x, y):
        self.__x = x
        self.__y = y
    def set_moment(self, x, y, timestamp):
        self.set_position(x,y)
        self.set_time(timestamp)

    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def getTimestamp(self):
        return self.__timestamp
    def getPosition(self):
        pos = [self.__x, self.__y]
        return pos
    def getMoment(self):
        e = [self.__x, self.__y, self.__timestamp]
        return e