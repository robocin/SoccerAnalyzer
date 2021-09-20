from SoccerAnalyzer.socceranalyzer.common.abstract.abstract_factory import AbstractFactory

from SoccerAnalyzer.socceranalyzer.common.basic.match import Match
from SoccerAnalyzer.socceranalyzer.common.enums.sim2d import SIM2D
from SoccerAnalyzer.socceranalyzer.common.enums.ssl import SSL
from SoccerAnalyzer.socceranalyzer.common.enums.vss import VSS
from SoccerAnalyzer.socceranalyzer.common.analysis.ball_possession import BallPossession
from SoccerAnalyzer.socceranalyzer.common.analysis.foul_charge import FoulCharge
from SoccerAnalyzer.socceranalyzer.common.analysis.playmodes import Playmodes


class MatchAnalyzer(AbstractFactory):
    def __init__(self, match: Match = None):
        self.__match = match
        self.__cat = match.category
        self.__analysis_dict = {}

        try:
            if self.__cat is None:
                raise ValueError('MatchAnalyzer requires a Category as argument and none was given')
        except ValueError as err:
            print(err)
            raise
        else:
            self._run_analysis()

    @property
    def match(self):
        return self.__match

    @property
    def category(self):
        return self.__cat

    @property
    def analysis_dict(self):
        return self.__analysis_dict

    def _run_analysis(self):
        if self.__cat is SIM2D:
            setattr(self, "__ball_possession", None)
            self.__ball_possession = BallPossession(self.__match.dataframe, self.category)

            setattr(self, "__foul_charge", None)
            self.__foul_charge = FoulCharge(self.__match.dataframe, self.category)

            setattr(self, "__playmodes", None)
            self.__playmodes = Playmodes(self.__match.dataframe, self.category)

        elif self.__cat is SSL:
            raise NotImplementedError
            # add SSL analysis

        elif self.__cat is VSS:
            raise NotImplementedError
            # add SSL analysis

    def collect_results(self):
        print("------------------------------------------------------")
        print("Collecting analysis...")
        print("Ball possession")
        print(self.__ball_possession.results())
        print("Foul charge")
        print(self.__foul_charge.results())
        print("Playmodes")
        print(self.__playmodes.results())
