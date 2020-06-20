import numpy as numpy
import pandas as pd

from Position import Position
from Event import Event

class Player:
    def __init__(self, log, team_name, team_side, player_id): 
        self.__team_name = team_name #name of the team this player belongs to
        self.__team_side = team_side 
        self.__player_id = player_id #id of this player (internal to the team)
        self.__log = log

        self.__pos = None
        self.__f_pro = []
        self.__faults_commited = []
        self.__number_of_faults_commited = 0
        self.__f_shot = []
        self.__goals = []
        self.__number_of_goals_made = 0
        self.__tries = []
        self.__good_try = []
        self.__tackles = []
        

    #set methods
   
    def set_pos(self, pos):
        self.__pos = pos

    def set_faults_commited(self, faults_pro):
        self.__f_pro = faults_pro
    
    def set_number_of_faults_commited(self, numberOfFaults):
        self.__number_of_faults_commited = numberOfFaults   
    
    def set_goals(self, goals):
        self.__goals = goals

    def set_number_of_goals_made(self, goals_made):
        self.__number_of_goals_made = goals_made

    def set_tries(self, tries):
        self.__tries = tries

    def set_good_try(self, goodTry):
        self.__good_try = goodTry
   
    def set_tackles(self, tackles):
        self.__tackles

    #get methods
    def get_team_name(self):
        return self.__team_name

    def get_team_side(self):
        return self.__team_side

    def get_pos(self):
        return self.__pos

    def get_faults_pro(self):
        return self.__f_pro

    def get_faults_commited(self):
        return self.__faults_commited

    def get_number_of_faults_commited(self):
        return self.__number_of_faults_commited

    def get_goals_made(self):
        
        if len(self.__goals) > 0:
            return self.__goals
        else:
            return None        

    def get_number_of_goals_made(self):
        return self.__number_of_goals_made

    def get_tries(self):
        return self.__tries

    def get_good_tries(self):
        return self.__good_try
    
    def get_tackles(self):
        return self.__tackles
