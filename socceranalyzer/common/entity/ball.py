from socceranalyzer.common.entity.abstract_entity import AbstractEntity

class Ball(AbstractEntity):
    ''' 
    A class to define the position of the ball in the field.

    ...

    Attributes
    ----------
    x: float
        x coordinates of the ball in the field
    y: float
        y coordinates of the ball in the field

    Methods
    -------
    x:
        Returns the attribute x.
    y: 
        Returns the attribute y.
            
    '''
    def __init__(self,x,y):
        '''
        Constructs all the necessary attributes for the ball object.

        Parameters
        ----------
        x: float
            x coordinates of the ball in the field
        y: float
            y coordinates of the ball in the field

        '''
        self.__x = x
        self.__y = y
    
    def x(self):
        '''
        Returns the attribute x (x coordinates of the ball).
        '''
        return self.__x

    def y(self):
        '''
        Returns the attribute y (y coordinates of the ball).
        '''
        return self.__y