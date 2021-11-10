from SoccerAnalyzer.socceranalyzer.common.abstract.abstract_analysis import AbstractAnalysis
from SoccerAnalyzer.socceranalyzer.common.utility.finders import find_last_unique_event_ocurrences

class CornersOcurrencies(AbstractAnalysis):
    def __init__(self, dataframe, category):
        self.__category = category
        self.__df = dataframe

        self.__left_occurrencies = []
        self.__right_occurrencies = []

        self._analyze()

    @property
    def dataframe(self):
        return self.__df

    @property
    def category(self):
        return self.__category

    def _analyze(self):
        self.__left_occurrencies = find_last_unique_event_ocurrences(self.dataframe, str(self.category.TEAM_LEFT_CORNER))
        self.__right_occurrencies = find_last_unique_event_ocurrences(self.dataframe, str(self.category.TEAM_RIGHT_CORNER))

    def results(self):
        return (self.__left_occurrencies, self.__right_occurrencies)

    def describe(self):
        name_l = self.dataframe.loc[1, str(self.category.TEAM_LEFT)]
        name_r = self.dataframe.loc[1, str(self.category.TEAM_RIGHT)]
        print(f'{name_l} had {len(self.__left_occurrencies)} corner to kick at: {self.__left_occurrencies}\n'
              f'{name_r} had {len(self.__right_occurrencies)} corner to kick at: {self.__right_occurrencies}')

    def serialize(self):
        raise NotImplementedError