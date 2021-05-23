import pandas as pd
import sys
sys.path.append("..")
from common.operations import mean



class SlMeanTeamStaminaAllCategories:
    def __init__(self, dataFrame : pd.DataFrame):
        self.dataframe = dataframe
    
    def __init__(self, stamina_log_of_each_player):
        self.stamina_log_of_each_player = stamina_log_of_each_player

    def query(self):
        pass

    def get_mean(self):
        """ Returns a list with the mean stamina of a team from all given matches """
        # stamina_log_of_each_player must be a list containing a list for each player of a team. Each list must be the whole player stamina column
        return mean.mean_list_given_multiple_lists(self.stamina_log_of_each_player)
        