from socceranalyzer.common.geometric.point import Point


class Ball:
    """ 
    A class to define the position of the ball in the field.

    ...

    Attributes
    ----------
        public through @properties
            x: float
                x coordinates of the ball in the field
            y: float
                y coordinates of the ball in the field
    """
    def __init__(self,x,y):
        """
        Constructs all the necessary attributes for the ball object.

        Parameters
        ----------
        x: float
            x coordinates of the ball in the field
        y: float
            y coordinates of the ball in the field

        """
        self.__x = x
        self.__y = y
    
    def positionAt(self, dataframe, category, cycle):
        ball_x = dataframe.loc[cycle, str(category.BALL_X)]
        ball_y = dataframe.loc[cycle, str(category.BALL_Y)]

        return Point(ball_x, ball_y)
    
    @property
    def x(self):
        """
        Returns the attribute x (x coordinates of the ball).
        """
        return self.__x

    @x.setter
    def x(self, x_position):
        self.__x = x_position

    @property
    def y(self):
        """
        Returns the attribute y (y coordinates of the ball).
        """
        return self.__y

    @y.setter
    def y(self, y_position):
        self.__y = y_position