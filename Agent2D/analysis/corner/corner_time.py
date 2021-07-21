from AnalyzerCommon.common.abstract.abstract_analysis import AbstractAnalysis
from AnalyzerCommon.common.utility.finders import find_unique_event_ocurrences


class Corner(AbstractAnalysis):
    def __init__(self, dataframe):
        self.__df = dataframe
        self.__left_team_occurrences = []
        self.__right_team_occurrences = []
        self.__left_team_avg = []
        self.__right_team_avg = []

    def _analyze(self):
        self.__left_team_occurrences = find_unique_event_ocurrences("corner_kick_l")
        self.__right_team_occurrences = find_unique_event_ocurrences("corner_kick_r")

    def results(self):
        raise NotImplementedError