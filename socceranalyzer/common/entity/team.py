from .agent import Agent

class Team:
    """
    A class that represents a team that playing the match and informations about it

    team(name: str, identifier: str)

    Attributes
    ----------
        public through @properties:
            name: str
                The team name 
            identifier: str
                A string representing an identifier that distinguish between the teams playing. SIM2D uses 'left' and 'right' while VSS and SSL use colors
            
    """


    def __init__(self, name: str = None, identifier: str = None):

        self.__name = name
        self.__color = None # não sei se ainda é necessário
        self.__identifier = identifier
        self.__players = []


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier):
        self.__identifier = identifier

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, player_array):
        self.__players = player_array

    def ith_player(self, i):
        return self.__players[i]