import numpy as np 
import pandas as pd

import eventClass
import positionClass
import oponentClass
import robocinClass
import teamClass
import playerClass

class DataCollector:
    def __init__(self, teamsArray = None, gameFaults = 0, gamePenaltis = 0, category = "unknown"):
        self.__teams = teamsArray
        self.__gameFaults = gameFaults
        self.__gamePenaltis = gamePenaltis
        self.__category = category

    #get methods
    def getTeams(self):
        return self.__teams

    def getGameFaults(self):
        return self.__gameFaults

    def getGamePenaltis(self):
        return self.__gamePenaltis
    
    def getCategory(self):
        return self.__category
    
    """
        more methods here
    """

    #set methods (improve implementations)
    def setTeams(self, teams):
        self.__teams = teams
    
    def setGameFaults(self, value):
        self.__gameFaults = value
    
    def setGamePenaltis(self, value):
        self.__gamePenaltis
    
    def setCategory(self, cat):
        self.__category = cat