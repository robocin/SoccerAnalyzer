from SoccerAnalyzer.socceranalyzer.common.operations.measures import distance

class Circle:
    def __init__(self, radius, center):
        self.__radius = radius
        self.__center = center

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, r):
        self.__radius = r

    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, point):
        self.__center = point

    def is_inside(self, point):

        dist = distance(self.__center, point)

        if dist <= self.__radius:
            return True
        else:
            return False

    def distance_to_center(self, point):
        return distance(self.__center, point)

