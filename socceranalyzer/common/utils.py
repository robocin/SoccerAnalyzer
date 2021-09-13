
class Utils:
    ''' 
    A class to give information about the other analyzer-common classes.

    ...
    Attributes
    -------
    info: str
        returns the instructions to acess the information about other classes of functions.
    
    Methods
    -------
    help(chosenclass): docstring
        returns the docstring of the chosen class of function.
            

    '''
    def __init__(self):
        self.info = 'CLASSE UTILS - Utilize Utils.help(Classe) para saber informações sobre uma classe ou função'
    
    @staticmethod
    def help(chosenclass):
        return chosenclass.__doc__



    