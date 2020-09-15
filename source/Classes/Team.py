from Classes import Player
from Classes import Position
from Classes import Event

NUMBER_OF_PLAYERS_PER_TEAM = 11 

#TODO: remove unused variables and methods.
class Team:
    def __init__(self, side=None):
        
        # initializes variables that will hold the values taken from de log (.csv file)
        self.__name = ""
        self.__color = None
        self.__side = side
        self.__players = [] 
        self.__goals_scored = []
        self.__number_of_goals_scored = 0
        self.__free_kicks = []
        self.__number_of_free_kicks = 0
        self.__fouls_commited = []
        self.__number_of_fouls_commited = 0
        self.__penaltis_commited = []
        self.__penaltis_scored = 0
        self.__seen_on = []

    # set methods
    def set_name(self, name):
        self.__name = name

    def set_color(self, color):
        self.__color = color

    def set_side(self, side):
        self.__side = side

    def set_goals_scored(self, goals_scored):
        self.__goalsscored = goals_scored

    def set_penaltis_scored(self, penaltis_scored):
        self.__penaltis_scored = penaltis_scored

    def set_number_of_goals_scored(self, number_of_goals_scored):
        self.__number_of_goals_scored = number_of_goals_scored

    def set_free_kicks(self, free_kicks):
        self.__free_kicks = free_kicks

    def set_number_of_free_kicks(self, number_of_free_kicks):
        self.__number_of_free_kicks = number_of_free_kicks

    def set_fouls_commited(self, faults_commited):
        self.__faults_commited = faults_commited
    
    def set_number_of_fouls_commited(self, number_of_fouls_commited):
        self.__number_of_fouls_commited = number_of_fouls_commited
    
    def set_penaltis_commited(self, penaltis_commited):
        self.__penaltis_commited = penaltis_commited

    def set_players(self, players):
        self.__players.append(players)

    def append_goal(self, goal):
        self.__goalsscored.append(goal)
        
    def set_seen_on(self, seen_on):
        self.__seen_on = seen_on
    
    def set_substitutions(self, substitutions):
        self.__substitutions = substitutions

    
    #get methods

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def get_side(self):
        return self.__side

    def get_goals_scored(self):
        return self.__goals_scored

    def get_penaltis_scored(self):
        return self.__penaltis_scored

    def get_number_of_goals_scored(self):
        return self.__number_of_goals_scored

    def get_free_kicks(self):
        return self.__free_kicks

    def get_number_of_free_kicks(self):
        return self.__number_of_free_kicks
    
    def get_fouls_commited(self):
        return self.__fouls_commited

    def get_number_of_fouls_commited(self):
        return self.__number_of_fouls_commited

    def get_penaltis_commited(self):
        return self.__penaltis_commited
    
    def get_players(self):
        return self.__players[0] #TODO: GAMBIARRA(ABC) EXPLICADA EM DATACOLLECTOR, DENTRO DE UM TODO EM INITIALIZE DEFINITION

    def get_substitutions(self):
        return self.__substitutions

    def get_player(self, playerId):
        return self.__players[0][playerId-1] #TODO: GAMBIARRA(ABC) EXPLICADA EM DATACOLLECTOR, DENTRO DE UM TODO EM INITIALIZE DEFINITION