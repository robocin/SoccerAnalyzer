import math


def distance(point, position):
<<<<<<< Updated upstream
    '''
    Returns the distance between a point and the position of the object.

            Parameters:
                    point (Point): A Point object
                    position (Point): Another Point object

            Returns:
                    dist (int): integer value of the distance
    '''
    dist = math.sqrt(pow(position.x - point.x, 2) + pow(position.y - point.y,2))
=======
    dist = math.sqrt(pow(position.x - point.x, 2) + pow(position.y - point.y, 2))
>>>>>>> Stashed changes

    return dist
