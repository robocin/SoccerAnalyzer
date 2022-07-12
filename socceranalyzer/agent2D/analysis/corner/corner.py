from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.utility import Utility


class Corner(AbstractAnalysis):
    def __init__(self, dataframe):
        self.__df = dataframe

        self.__left_team_occurrences = []
        self.__left_team_time_after = []
        self.__left_team_avg = []

        self.__right_team_occurrences = []
        self.__right_team_time_after = []
        self.__right_team_avg = []

        self._analyze()

    def _analyze(self):
        self.__occurrences()

    def __occurrences(self):
        self.__left_team_occurrences = Utility.find_last_unique_event_ocurrences(self.__df, "corner_kick_l")
        self.__right_team_occurrences = Utility.find_last_unique_event_ocurrences(self.__df, "corner_kick_r")

    def t_occ_l(self):
        return self.__left_team_occurrences

    def t_occ_r(self):
        return self.__right_team_occurrences


    def __time_after(self):
        # left team
        for corner_start_cycle in self.__left_team_occurrences:
            pass


    def results(self):
        raise NotImplementedError