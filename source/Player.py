import numpy as numpy
import pandas as pd

import positionClass
import computingFunctions as computing
import fault


class Player:
    def __init__(self, log, teamName, teamSide, player_id): 
        self.__team_name = teamName #name of the team this player belongs to
        self.__team_side = teamSide 
        self.__player_id = player_id #id of this player (internal to the team)
        self.__log = log

        self.__pos = None
        self.__f_pro = []
        self.__faults_commited = []
        self.__number_of_faults_commited = 0
        self.__f_shot = []
        self.__goals = []
        self.__tries = []
        #self.__good_try
        #self.__tackles 

        #calls for computing
        self.compute()

    #set methods
   
    def setPos(self, pos):
        self.__pos = pos

    def setFaultsCommited(self, faultsPro):
        self.__f_pro = faultsPro
    
    def setNumberOfFaultsCommited(self, numberOfFaults):
        self.__number_of_faults_commited = numberOfFaults   
    
    def setFaultsCommited(self, faulstShot):
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
    def getTeamName(self):
        return self.__team_name

    def getTeamSide(self):
        return self.__team_side

    def getPos(self):
        return self.__pos

    def getFaultsPro(self):
        return self.__f_pro

    def getFaultsCommited(self):
        return self.__f_shot

    def getNumberOfFaultsCommited(self):
        return self.__number_of_faults_commited

    def getGoalsMade(self):
        return (self.__goals_made if len(self.__goals_made)>0 else None)

    def getNumberOfGoalsMade(self):
        return self.__number_of_goals_made

    def getTries(self):
        return self.__tries

    def getGoodTries(self):
        return self.__good_try
    
    def getTacklesMade(self):
        return self.__tackles_made

    def compute(self):
        '''
        Here is where all the reading and computing of data stored in the given .csv file happens
        '''
              #TODO: delete this block when computingFaults(inside dataCollector) is implemented. (is just here for debuggin process)
        if(self.getTeamSide() == "l"):
            self.setFaultsCommited([fault.Fault()])
            #self.setNumberOfFaultsCommited(20)
        elif(self.getTeamSide() == "r"):
            lista = []
            for i in range(0,2):
                lista.append(fault.Fault())
            self.setFaultsCommited(lista)

            #self.setNumberOfFaultsCommited(5)

    def computeGoals(self):
        '''
        Because, for performance, all the goals are already computed in the dataCollector after
        this object is instaciated, whe only set the goals made by this player once the compute()
        funtion is called in the dataCollector
        ''' 
        pass 