import math


def distance(point, position):
    """
    Returns the distance between a point and the position of the object.

            Parameters:
                    point (Point): A Point object
                    position (Point): Another Point object

            Returns:
                    dist (int): integer value of the distance
    """
    dist = math.sqrt(pow(position.x - point.x, 2) + pow(position.y - point.y, 2))

    return dist

def distance_sqrd(p1: list[float], p2: list[float]) -> float:
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def line_intersection(line1: tuple[tuple[float, float]], line2: tuple[tuple[float, float]]) -> tuple[float, float]:
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
        result = 0.0
        for m, n in zip(v1,v2):
            result += m*n
        return result

def is_point_inside_triangle(a: list[float], b: list[float], c: list[float], point: list[float]) -> bool:
        v0 = [c[0] - a[0], c[1] - a[1]]
        v1 = [b[0] - a[0], b[1] - a[1]]
        v2 = [point[0] - a[0], point[1] - a[1]]

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
