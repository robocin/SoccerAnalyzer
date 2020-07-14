"""
EM MainWIndow.py:

class MainWindow(QMainWindow):     
    def __init__(self, name):
            #screen initialization
        (...)
            #other initializations
        (...)
            # call define_log() and instaciates a DataCollector() 
        (...)
            #definition of custom functions
        (...)
            #showing
        robocin_number_of_goals = data.get_Team("l").get_NumberOfGoals()
        robocin_player1_number_of_goals = data.get_Team(robocin).get_Player(1).get_NumberOfGoals()


"""

#################################################################################################################################################

from Player import Player
from Position import Position
from Event import Event

NUMBER_OF_PLAYERS_PER_TEAM = 11 

class Team:
    def __init__(self):
        
        # initializes variables that will hold the values taken from de log (.csv file)
        self.__name = ""
        self.__side = None
        self.__players = [] 
        self.__goals_scored = []
        self.__number_of_goals_scored = 0
        self.__free_kicks = []
        self.__number_of_free_kicks = 0
        self.__faults_commited = []
        self.__number_of_faults_commited = 0
        self.__penaltis_commited = []
        self.__seen_on = []

    # set methods
    def set_name(self, name):
        self.__name = name

    def set_side(self, side):
        self.__side = side

    def set_goals_scored(self, goals_scored):
        self.__goalsscored = goals_scored

    def set_number_of_goals_scored(self, number_of_goals_scored):
        self.__number_of_goals_scored = number_of_goals_scored

    def set_free_kicks(self, free_kicks):
        self.__free_kicks = free_kicks

    def set_number_of_free_kicks(self, number_of_free_kicks):
        self.__number_of_free_kicks = number_of_free_kicks

    def set_faults_commited(self, faults_commited):
        self.__faults_commited = faults_commited
    
    def set_number_of_faults_commited(self, number_of_faults_commited):
        self.__number_of_faults_commited = number_of_faults_commited
    
    def set_penaltis_commited(self, penaltis_commited):
        self.__penaltis_commited = penaltis_commited

    def append_player(self, player):
        self.__players.append(player)

    def append_goal(self, goal):
        self.__goalsscored.append(goal)
        
    def set_seen_on(self, seen_on):
        self.__seen_on = seen_on
    
    def set_substitutions(self, substitutions):
        self.__substitutions = substitutions

    
    #get methods

    def get_name(self):
        return self.__name

    def get_side(self):
        return self.__side

    def get_goals_scored(self):
        return self.__goalsscored

    def get_number_of_goals_scored(self):
        return self.__number_of_goals_scored
    
    def get_faults_commited(self):
        return self.__faults_commited

    def get_number_of_faults_commited(self):
        return self.__number_of_faults_commited

    def get_penaltis_commited(self):
        return self.__penaltis_commited
    
    def get_players(self):
        return self.__players

    def get_substitutions(self):
        return self.__substitutions

    def get_player(self, playerId):
        return self.__players[playerId-1] 
