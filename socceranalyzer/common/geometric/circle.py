from socceranalyzer.common.geometric.point import Point
from socceranalyzer.common.operations.measures import distance


class Circle:
    """
    The circle class

    Circle(radius: float, center: socceranalyzer.common.geometric.point.Point)

    Attributes
    ----------
            private:
                radius : float
                    the circle radius
                center: socceranalyzer.common.geometric.point.Point
                    the circle center point

    Methods
    -------
            public:
                is_inside(point : socceranalyzer.common.geometric.point.Point) -> bool
                    checks if point is inside the circle
                distance_to_center(point : socceranalyzer.common.geometric.point.Point) -> float
                    computes distance from 'point' to center of the circle
    """
    def __init__(self, radius: float, center: Point):
        self.__radius = radius
        self.__center = center

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, r: float):
        self.__radius = r

    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, point: Point):
        self.__center = point

    def is_inside(self, point: Point):
        """
        Returns a boolean indicating if point is inside the circle.

                Parameters:
                        point (Point): Point of interest

                Returns:
                        is_inside (bool): Indicates if point is inside the circle.
        """

        dist = distance(self.__center, point)

        if dist <= self.__radius:
            return True
        else:
            return False

    def distance_to_center(self, point: Point) -> float:
        """
        Returns a float indicating the distance between the point coordinates and the circle.

                Parameters:
                        point (Point): Point of interest

                Returns:
                        dist (float): Distance value.
        """
        return distance(self.__center, point)

