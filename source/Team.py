"""
EM MainWIndow.py:

class MainWindow(QMainWindow):     
    def __init__(self, name):
            #screen initialization
        (...)
            #other initializations
        (...)
            # call define_log() and instaciates a dataCollector() 
        (...)
            #definition of custom functions
        (...)
            #showing
        robocin_number_of_goals = data.get_Team("l").get_NumberOfGoals()
        robocin_player1_number_of_goals = data.get_Team(robocin).get_Player(1).get_NumberOfGoals()


"""

#################################################################################################################################################
import numpy as np
import pandas as pd

from Player import Player
from Position import Position
from Event import Event

LOG = pd.read_csv('./files/t1.rcg.csv')

NUMBER_OF_PLAYERS_PER_TEAM = 11 

class Team:
    def __init__(self, data_frame, side):
        
        # initializes variables that will hold the values taken from de log (.csv file)
        self.__name = ""
        self.__data_frame = data_frame
        self.__side = side
        self.__players = [] 
        self.__goalsMade = []
        self.__numberOfGoalsMade = 0
        self.__freeKicks = []
        self.__numberOfFreeKicks = 0
        self.__faultsCommited = []
        self.__numberOfFaultsCommited = 0
        self.__penaltisMade = []
        self.__seenOn = []
        #self.__substitutions 

        #calls for computation of data
        self.team_init()

    # set methods
    def setName(self, name):
        self.__name = name

    def setSide(self, side):
        self.__side = side

    def setGoalsMade(self, goalsMade):
        self.__goalsMade = goalsMade

    def setNumberOfGoalsMade(self, numberOfGoals):
        self.__numberOfGoals = numberOfGoals

    def setFreKicks(self, freeKicks):
        self.__freeKicks = freeKicks

    def set_number_of_free_kicks(self, numberOfFreeKicks):
        self.__numberOfFreeKicks = numberOfFreeKicks

    def set_faults_commited(self, faultsCommited):
        self.__faultsCommited = faultsCommited
    
    def set_number_of_faults_commited(self, numberOfFaults):
        self.__numberOfFaultsCommited = numberOfFaults
    
    def setPenaltisMade(self, penaltisPro):
        self.__penaltisPro = penaltisPro

    def appendPlayer(self, player):
        self.__players.append(player)

    def appendGoal(self, goal):
        self.__goalsMade.append(goal)
        
    def setSeenOn(self, seenOn):
        self.__seenOn = seenOn
    
    def setSubstitutions(self, substitutions):
        self.__substitutions = substitutions

    
    #get methods

    def getName(self):
        return self.__name

    def getSide(self):
        return self.__side

    def getGoalsMade(self):
        return self.__goalsMade

    def getNumberOfGoalsMade(self):
        return self.__numberOfGoalsMade
    
    def getFaultsCommited(self):
        return self.__faultsCommited

    def getNumberOfFaultsCommited(self):
        return self.__numberOfFaultsCommited

    def getPenaltisMade(self):
        return self.__penaltisMade
    
    def getPlayers(self):
        return self.__players

    def getSubstitutions(self):
        return self.__substitutions

    def getPlayer(self, playerId):
        return self.__players[playerId-1] 


    # Initialization of Players and names

    def team_init(self):
        pass

'''    #the compute() function 
    def compute(self): 
Here is where all the reading and computing of data stored in the given .csv file happens 

        # sets the team name based on the log data 
        if(self.__side == "l"):
            self.setName(self.__log.iloc[0,2])
        elif(self.__side =="r"):
            self.setName(self.__log.iloc[0,3]) 
        
        # instanciates the players of the team passing the team name to all, and giving each one a integer id from 1 to NUMBER_OF_PLAYERS_PER_TEAM
        for i in range(1,NUMBER_OF_PLAYERS_PER_TEAM):
            self.appendPlayer(Player(self.getLog(), self.getName(), self.getSide(), i))
            #self.appendPlayer(playerClass.Player( "", "", "", 1))
'''
