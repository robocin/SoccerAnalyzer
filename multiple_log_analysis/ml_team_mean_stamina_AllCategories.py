
import pandas as pd
import sys
sys.path.append("..")
from common.operations import mean

class MlMeanTeamStaminaAllCategories:
    def __init__(self, dataFrame : pd.DataFrame):
        self.dataframe = dataframe
    
    def __init__(self, team_mean_stamina_of_each_match):
        self.team_mean_stamina_of_each_match = team_mean_stamina_of_each_match

    def query(self):
        pass

    def get_mean(self):
        """ Returns a list with the mean stamina of a team from all given matches """
        # stamina_log_of_each_player must be a list containing a list for each player of a team. Each list must be the whole player stamina column
        return mean.mean_list_given_multiple_lists(self.team_mean_stamina_of_each_match)
        