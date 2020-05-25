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

    #set methods (interface)
    def setName(self, name):
        self.__name = name
    
    def setSide(self):

        team_left = LOG.iloc[0].team_name_l
        
        if team_left == self.getName():
            self.__side = "left"
        else:
            self.__side = "right"

    def setGoalsPro(self):

        end_row = LOG.loc[LOG["playmode"] == "time_over"].team_score_r.to_list()

        if self.getSide == "left":
            score = end_row.team_score_l.to_list()
            return score[0]
        else:
            score = end_row.team_score_r.to_list()
            return score[0]

        
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