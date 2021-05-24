import pandas as pd
from AnalyzerCommon.common.operations.mean import  mean_list_given_multiple_lists


class SlMeanTeamStaminaAllCategories:
    def __init__(self, data_frame: pd.DataFrame):
        self.dataframe = data_frame

    # TODO: tem como tirar esse warning do init? (pycharm)
    def __init__(self, stamina_log_of_each_player):
        """stamina_log_of_each_player -> list of lists, in which each sublist is the log of stamina o a player from one
        mach"""
        self.stamina_log_of_each_player = stamina_log_of_each_player

    def query(self):
        pass

    def get_mean(self):
        """ Returns a list with the mean stamina of a team from the single match given as parameter"""
        return mean_list_given_multiple_lists(self.stamina_log_of_each_player)
