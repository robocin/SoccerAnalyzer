from socceranalyzer.common.geometric.point import Point
from socceranalyzer.common.operations.measures import dot


class Triangle:
    """
    The triangle class

    Triangle(a: socceranalyzer.common.geometric.point.Point, b: socceranalyzer.common.geometric.point.Point, c: socceranalyzer.common.geometric.point.Point)

    Attributes
    ----------
            private:
                vertices : list[socceranalyzer.common.geometric.point.Point]
                    the triangle vertices

    Methods
    -------
            public:
                is_inside(point : socceranalyzer.common.geometric.point.Point) -> bool
                    checks if point is inside the triangle
    """

    def __init__(self, a: Point, b: Point, c: Point):
        self.__vertices = [a, b, c]
    
    def is_inside(self, point: Point) -> bool:
        """
        Returns a boolean indicating if point is inside triangle.

                Parameters:
                        point (list[float]): Point of interest

                Returns:
                        is_inside (bool): Indicates if point is inside triangle defined by vertices
        """
        v0 = [self.__vertices[2].x - self.__vertices[0].x, self.__vertices[2].y - self.__vertices[0].y]
        v1 = [self.__vertices[1].x - self.__vertices[0].x, self.__vertices[1].y - self.__vertices[0].y]
        v2 = [point.x - self.__vertices[0].x, point.y - self.__vertices[0].y]

        # Compute dot products
        dot00 = dot(v0, v0)
        dot01 = dot(v0, v1)
        dot02 = dot(v0, v2)
        dot11 = dot(v1, v1)
        dot12 = dot(v1, v2)

        # Compute barycentric coordinates
        invDenom = 1.0 / (dot00 * dot11 - dot01 * dot01)
        u = (dot11 * dot02 - dot01 * dot12) * invDenom
        v = (dot00 * dot12 - dot01 * dot02) * invDenom

        # Check if point is in triangle
        return (u >= 0.) and (v >= 0.) and(u + v < 1.)