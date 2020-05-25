import numpy as np
import pandas as pd

LOG = pd.read_csv('./files/t1.rcg.csv')

class Team:

    def __init__(self, name = "No name", goalsPro = 0, goalsAgainst = 0, faultsPro = 0, 
    faultsAgainst = 0, penaltisPro = 0, penaltisAgainst = 0, seenOn = 1, substitutions = 0,
    side = "No side"):

        self.__name = name
        self.__goalsPro = goalsPro
        self.__goalsAgainst = goalsAgainst
        self.__faultsPro = faultsPro
        self.__faultsAgainst = faultsAgainst
        self.__penaltisPro = penaltisPro
        self.__penaltisAgainst = penaltisAgainst
        self.__seenOn = seenOn
        self.__substitutions = substitutions
        self.__side = side

    #set methods
    def setName(self, name):
        self.__name = name
        
    def setSide(self, side):
        self.__side = side

    def setGoalsPro(self, goalsPro):
        self.__goalsPro = goalsPro

    def setGoalsAgainst(self):
        pass
    def setFaultsPro(self):
        pass
    def setFaultsAgainst(self):
        pass
    def setPenaltisPro(self):
        pass
    def setPenaltisAgainst(self):
        pass
    def setSeenOn(self):
        pass
    def setSubstitutions(self):
        pass

    #get methods
    def getName(self):
        return self.__name

    def getGoalsPro(self):
        return self.__goalsPro

    def getGoalsAgainst(self):
        return self.__goalsAgainst

    def getFaultsPro(self):
        return self.__faultsPro
    
    def getFaultsAgainst(self):
        return self.__faultsAgainst

    def getPenaltisPro(self):
        return self.__penaltisPro
    
    def getPenaltisAgainst(self):
        return self.__penaltisAgainst

    def getSubstitutions(self):
        return self.__substitutions

    def getSide(self):
        return self.__side


teste = Team()
teste.setGoalsPro()