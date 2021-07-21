from .factory.abstract_factory import AbstractFactory

from AnalyzerCommon.common.basic.match import Match
from AnalyzerCommon.Agent2D.analysis.ball_possession import BallPossession
from AnalyzerCommon.Agent2D.analysis.foul_charge import FoulCharge

class MatchAnalyzer(AbstractFactory):
    def __init__(self, match : Match):
        self.__match = match
        self.__analysis_dict = {}

        #self.__team_mean_stamina = None
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
        #team mean stamina
        print("------------------------------------------------------")
        print("Instantiating mean stamina")
        print("Running mean stamina")

        # ball possession
        print("Instantiating ball possession")
        print("Running ball possession")
        self.__ball_possession = BallPossession(self.__match.dataframe)

        # foul charge
        print("Instantiating foul charge")
        print("Running foul charge")
        self.__foul_charge = FoulCharge(self.__match.dataframe)


    def collect_analysis(self):
        print("------------------------------------------------------")
        print("Collecting analysis...")
        print("Ball possession")
        print(self.__ball_possession.results())
        print("Foul charge")
        print(self.__foul_charge.results())
