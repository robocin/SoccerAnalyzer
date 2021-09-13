from .agent import Agent

class Team:
    def __init__(self, name: str = None, side: str = None):

        self.__name = name
        self.__color = None
        self.__side = side
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
    def side(self):
        return self.__side

    @side.setter
    def side(self, side):
        self.__side = side

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, player_array):
        self.__players = player_array

    def ith_player(self, i):
        return self.__players[i]