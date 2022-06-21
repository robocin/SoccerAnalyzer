import math
from socceranalyzer.common.geometric.point import Point


def distance(point, position) -> float:
    """
    Returns the distance between a point and the position of the object.

            Parameters:
                    point (Point): A Point object
                    position (Point): Another Point object

            Returns:
                    dist (float): value of the distance
    """
    dist = math.sqrt(pow(position.x - point.x, 2) + pow(position.y - point.y, 2))

    return dist

def distance_sqrd(p1: Point, p2: Point) -> float:
    """
    Returns the distance squared between two points.

            Parameters:
                    p1 (Point): First point
                    p2 (Point): Second point

            Returns:
                    dist^2 (float): integer value of the distance squared
    """

    return (p1.x - p2.x)**2 + (p1.y - p2.y)**2

def line_intersection(line1: tuple[tuple[float, float]], line2: tuple[tuple[float, float]]) -> tuple[float, float]:
    """
    Returns a tuple where lines intersect.

            Parameters:
                    line1 (tuple[tuple[float, float]]): First line
                    line2 (tuple[tuple[float, float]]): Second line

            Returns:
                    (x, y) (tuple[float, float]): Point where lines intersect

            Raises:
                    Exception('lines do not intersect!')
    """
    def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])
    div = det(xdiff, ydiff)
    if div == 0:
            raise Exception('lines do not intersect!')
    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def dot(v1: list[float], v2: list[float]) -> float:
    """
    Returns the dot product between v1 and v2.

        Parameters:
                    v1 (list[float]): Vector 1
                    v2 (list[float]): Vector 2

            Returns:
                    result (float): The dot product between vector 1 and vector 2
    """
    result = 0.0
    for m, n in zip(v1,v2):
        result += m*n
    return result
