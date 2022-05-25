from socceranalyzer.common.basic.match import Match
from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.enums.ssl import SSL
from socceranalyzer.common.enums.vss import VSS


class Heatmap(AbstractAnalysis):
    def __init__(self, match: Match, category: SSL | SIM2D | VSS) -> None:
        self.__match = match
        self.__category = category

    @property
    def match(self):
        return self.__match

    @property
    def category(self):
        return self.__category

    def _analyze(self):
        

    def describe(self):
        raise NotImplementedError

    def results(self):
        raise NotImplementedError

    def serialize(self):
        raise NotImplementedError