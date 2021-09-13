from SoccerAnalyzer.socceranalyzer.common.abstract.abstract_factory import AbstractFactory

from SoccerAnalyzer.socceranalyzer.common.basic.match import Match
from SoccerAnalyzer.socceranalyzer.agent2D.analysis.ball_possession import BallPossession
from SoccerAnalyzer.socceranalyzer.agent2D.analysis.foul_charge import FoulCharge


class MatchAnalyzer(AbstractFactory):
    def __init__(self, match: Match = None):
        self.__match = match
        self.__analysis_dict = {}

        # Analysis
        self.__ball_possession = None
        self.__foul_charge = None

        self._run_analysis()

    @property
    def match(self):
        return self.__match

    @property
    def analysis_dict(self):
        return self.__analysis_dict

    def _run_analysis(self):
        # ball possession
        print("Instantiating ball possession")
        print("Running ball possession")
        self.__ball_possession = BallPossession(self.__match.dataframe)

        # foul charge
        print("Instantiating foul charge")
        print("Running foul charge")
        self.__foul_charge = FoulCharge(self.__match.dataframe)

    def collect_results(self):
        print("------------------------------------------------------")
        print("Collecting analysis...")
        print("Ball possession")
        print(self.__ball_possession.results())
        print("Foul charge")
        print(self.__foul_charge.results())
