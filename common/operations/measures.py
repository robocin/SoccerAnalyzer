import math

def distance(point, position):
    dist = math.sqrt(pow(position.x - point.x, 2) + pow(position.y - point.y,2))

    return dist