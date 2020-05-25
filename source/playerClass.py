import numpy as numpy
import pandas as pd

class Player:
    def __init__(self, number = 0, pos = "No position", f_pro = 0, f_commited = 0,
    f_shot = 0, goals = 0, tries = 0, good_try = 0, tackles = 0):

        self.__number = number
        self.__pos = pos
        self.__f_pro = f_pro
        self.__f_commited = f_commited
        self.__f_shot = f_shot
        self.__goals = goals
        self.__tries = tries
        self.__good_try = good_try
        self.__tackles = tackles

    def setNumber(self, n):
        self.__number = n