import numpy as numpy
import pandas as pd

import positionClass

class Player:
    def __init__(self, team = "No team", number = 0, pos = "No position", f_pro = 0, f_commited = 0,
    f_shot = 0, goals = 0, tries = 0, good_try = 0, tackles = 0):

        self.__team = team
        self.__number = number
        self.__pos = pos
        self.__f_pro = f_pro
        self.__f_commited = f_commited
        self.__f_shot = f_shot
        self.__goals = goals
        self.__tries = tries
        self.__good_try = good_try
        self.__tackles = tackles


    #set methods
    def setTeam(self, team):
        self.__team = team

    def setNumber(self, n):
        self.__number = n
    
    def setPos(self, pos):
        self.__pos = pos

    def setFaultsPro(self, faultsPro):
        self.__f_pro = faultsPro
    
    def setFaultsCommited(self, faultsCommited):
        self.__f_commited = faultsCommited
    
    def setFaultsShot(self, faulstShot):
        self.__f_shot = faulstShot
    
    def setGoals(self, goals):
        self.__goals = goals

    def setTries(self, tries):
        self.__tries = tries

    def setGoodTry(self, goodTry):
        self.__good_try = goodTry
    
    def setTackles(self, tackles):
        self.__tackles

    #get methods
    def getTeam(self):
        return self.__team

    def getNumber(self):
        return self.__number

    def getPos(self):
        return self.__pos

    def getFaultsPro(self):
        return self.__f_pro

    def getFaultsCommited(self):
        return self.__f_commited
    
    def getFaultsShot(self):
        return self.__f_shot

    def getGoals(self):
        return self.__goals

    def getTries(self):
        return self.__tries

    def getGoodTries(self):
        return self.__good_try
    
    def getTackles(self):
        return self.__tackles