from Classes import Position
from Classes import Event

#TODO: remove unused variables and methods.
class Player:
    def __init__(self, team_side=None, player_id=None): 
        self.__team_name = None #name of the team this player belongs to
        self.__team_side = team_side 
        self.__player_id = player_id #id of this player (internal to the team)
        self.__stamina_log = []
        self.__pos = None
        self.__f_pro = []
        self.__faults_commited = []
        self.__number_of_faults_commited = 0
        self.__f_shot = []
        self.__goals = []
        self.__number_of_goals_scored = 0
        self.__tries = []
        self.__good_try = []
        self.__tackles = []
        

    #set methods
   
    def set_pos(self, pos):
        self.__pos = pos
    def set_faults_commited(self, faults_pro):
        self.__f_pro = faults_pro
    def set_number_of_faults_commited(self, number_of_faults_commited):
        self.__number_of_faults_commited = number_of_faults_commited   
    def set_goals(self, goals):
        self.__goals = goals
    def set_number_of_goals_scored(self, goals_scored):
        self.__number_of_goals_scored = goals_scored
    def set_tries(self, tries):
        self.__tries = tries
    def set_good_try(self, good_try):
        self.__good_try = good_try
    def set_tackles(self, tackles):
        self.__tackles
    def set_stamina_log(self, log):
        self.__stamina_log = log

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
    def get_goals_scored(self):
        if len(self.__goals) > 0:
            return self.__goals
        else:
            return None        
    def get_number_of_goals_scored(self):
        return self.__number_of_goals_scored
    def get_tries(self):
        return self.__tries
    def get_good_tries(self):
        return self.__good_try
    def get_tackles(self):
        return self.__tackles
    def get_stamina_log(self):
        return self.__stamina_log