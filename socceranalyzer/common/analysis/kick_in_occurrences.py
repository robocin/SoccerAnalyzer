from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.dataframe.finders import find_last_unique_event_ocurrences
from socceranalyzer.utils.logger import Logger


class KickInOcurrences(AbstractAnalysis):
    def __init__(self, dataframe, category, debug):
        self.__category = category
        self.__df = dataframe
        self.__occurrences = []

        try:
            self._analyze()
        except Exception as err:
            Logger.error(f"KickInOccurrences failed {err.args[0]}")
            if debug:
                raise
        else:
            Logger.success("KickInOccurrences has results")

    @property
    def dataframe(self):
        return self.__df

    @property
    def category(self):
        return self.__category

    def _analyze(self):
        self.__occurrences = find_last_unique_event_ocurrences(self.dataframe, str(self.category.TEAM_LEFT_KICK_IN))

    def results(self):
        return len(self.__occurrences)

    def describe(self):
        print(f'{len(self.__occurrences)} kicks in occurred')

    def serialize(self):
        raise NotImplementedError
