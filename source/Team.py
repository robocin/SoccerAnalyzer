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

import Player
import Position
import Event

LOG = pd.read_csv('./files/t1.rcg.csv')

NUMBER_OF_PLAYERS_PER_TEAM = 11 

class Team:
    def __init__(self, log, side):
        
        # initializes variables that will hold the values taken from de log (.csv file)
        self.__name = ""
        self.__side = side
        self.__log = log 
        self.__side = side
        self.__players = [] 
        self.__goals_made = []
        self.__number_of_goals_made = 0
        self.__faults_commited = []
        self.__number_of_faults_commited = 0
        self.__penaltisMade = []
        #self.__seenOn 
        #self.__substitutions 

        #calls for computation of data
        self.compute()

    # set methods
    def setName(self, name):
        self.__name = name

    def setSide(self, side):
        self.__side = side

    def setGoalsMade(self, goals):
        self.__goals_made = goals

    def setNumberOfGoalsMade(self, numberOfGoals):
        self.__number_of_goals_made = numberOfGoals

    def setFaultsCommited(self, faultsPro):
        self.__faultsPro = faultsPro
    
    def setNumberOfFaultsCommited(self, numberOfFaults):
        self.__number_of_faults_commited = numberOfFaults
    
    def setPenaltisMade(self, penaltisPro):
        self.__penaltisPro = penaltisPro

    def appendPlayer(self, player):
        self.__players.append(player)

    def appendGoal(self, goal):
        self.__goals_made.append(goal)
        
    def setSeenOn(self, seenOn):
        self.__seenOn = seenOn
    
    def setSubstitutions(self, substitutions):
        self.__substitutions = substitutions

    #get methods
    def getLog(self):
        return self.__log

    def getName(self):
        return self.__name

    def getSide(self):
        return self.__side

    def getGoalsMade(self):
        return self.__goals_made

    def getNumberOfGoalsMade(self):
        return self.__number_of_goals_made
    
    def getFaultsCommited(self):
        return self.__faults_commited

    def getNumberOfFaultsCommited(self):
        return self.__number_of_faults_commited

    def getPenaltisMade(self):
        return self.__penaltisMade

    def getSubstitutions(self):
        return self.__substitutions

    def getPlayer(self, playerId):
        return self.__players[playerId-1] 

    #the compute() function 
    def compute(self): 
        ''' Here is where all the reading and computing of data stored in the given .csv file happens '''

        # sets the team name based on the log data 
        if(self.__side == "l"):
            self.setName(self.__log.iloc[0,2])
        elif(self.__side =="r"):
            self.setName(self.__log.iloc[0,3]) 
        
        # instanciates the players of the team passing the team name to all, and giving each one a integer id from 1 to NUMBER_OF_PLAYERS_PER_TEAM
        for i in range(1,NUMBER_OF_PLAYERS_PER_TEAM):
            self.appendPlayer(Player.entity(self.getLog(), self.getName(), self.getSide(), i))
            #self.appendPlayer(playerClass.Player( "", "", "", 1))

        #TODO: tirar comentários (debugar?) 
        '''  
        # sets the goals made, by appending the goals made by each of the team players
        for player_id in range(1,NUMBER_OF_PLAYERS_PER_TEAM): #for each player,
            player_goals = self.__player[i].getGoals #gets all the goals made by this player
            if(player_goals != None): #if this player has made at least one goal,
                for i in range(0,len(player_goals)): #for each goal made by this player, 
                    self.appendGoal(player_goals[i])#append this goal to the team goals list
        # sets the number of goals made
        self.setNumberOfGoalsMade(len(self.getGoalsMade()))
        '''

        # sets the faults commited, by appending the faults of each of the team players
        ''' 
        aux = [] 
        for i in range(1,NUMBER_OF_PLAYERS_PER_TEAM-1):
            aux.append(self.__players[i].getFaultsCommited())
        self.setFaultsCommited(aux)
        print("FAULTS COMMITED:")
        print(self.getFaultsCommited())
        ''' 

         
        #self.setNumberOfFaultsCommited(len(self.getFaultsCommited())) 
        aux2 = [] 
        for i in range(0, NUMBER_OF_PLAYERS_PER_TEAM-1):
            for fault in range(0, len(self.__players[i].getFaultsCommited())):
                aux2.append(self.__players[i].getFaultsCommited()[fault])
        print(len(aux2))
        self.setNumberOfFaultsCommited(len(aux2))
        