
import pandas as pd
from AnalyzerCommon.common.operations.mean import mean_list_given_multiple_lists


class MlMeanTeamStaminaAllCategories:
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    # TODO: tem como tirar esse warning do init? (pycharm)
    def __init__(self, team_mean_stamina_of_each_match):
        """stamina_log_of_each_player -> list of lists, in which each sublist is the mean team stamina of one game at
        each slice of time (index of the list) of a team in one match"""
        self.team_mean_stamina_of_each_match = team_mean_stamina_of_each_match

    def query(self):
        pass

    def get_mean(self):
        """ Returns a list with the mean stamina of a team from all of the matches given"""
        # TODO: tem como tirar esse warning abaixo? (pycharm) (acho que tem a ver com o overloading da classe)
        return mean_list_given_multiple_lists(self.team_mean_stamina_of_each_match)
        