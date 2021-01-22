class Field:
    ''' 
    A class to create the field.

    '''
    def __init__(self):
        '''
        Constructs all the necessary attributes for the point object.

        Parameters
        ----------
        width: int
            width of the field
        height: int
            height of the field
        pa_front: int
        pa_upper: int
        pa_lower: int
        spa_front: int
        spa_upper: int
        spa_lower: int
        max_x: float
            maximum x coordinate of the field
        min_x: float
            minimum x coordinate of the field
        max_y: int
            maximum y coordinate of the field
        min_y: int
            minimum y coordinate of the field

        '''
        self.width = 105
        self.height = 68
        self.pa_front = 36
        self.pa_upper = 20
        self.pa_lower = -20
        self.spa_front = 47
        self.spa_upper = 9
        self.spa_lower = -9 
        self.max_x = 52.5
        self.min_x = -52.5
        self.max_y =  34
        self.min_y = -34

    def describe(self):
        raise NotImplementedError