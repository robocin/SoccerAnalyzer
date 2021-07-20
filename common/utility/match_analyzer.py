from .factory.abstract_factory import AbstractFactory

from AnalyzerCommon.common.basic.match import Match
from AnalyzerCommon.analysis.ball_possession import BallPossession
from AnalyzerCommon.analysis.foul_charge import FoulCharge
from AnalyzerCommon.analysis.nova_analise import NovaAnalise

class MatchAnalyzer(AbstractFactory):
    def __init__(self, match : Match):
        self.__match = match
        self.__analysis_dict = {}

        #self.__team_mean_stamina = None
        self.__ball_possession = None
        self.__foul_charge = None
        self.__nova_analise = None

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
        #self.__ball_possession = BallPossession(self.match.getDataframe())
        print("Running ball possession")

        # foul charge
        print("Instantiating foul charge")
        #self.__foul_charge = FoulCharge(self.match.getDataframe())
        print("Running foul charge")

        # foul charge quantity
        print("Running foul charge quantity")

        # foul charge proportion
        print("Running foul charge proportion")

        # Nova analise criada
        self.__nova_analise = NovaAnalise(self.match)

    def collect_analysis(self):
        print("------------------------------------------------------")
        print("Collecting analysis...")

        self.analysis_dict['team_l_name'] = self.match.team_left.name
        self.analysis_dict['team_r_name'] = self.match.team_right.name

    def gd(self):
        return self.analysis_dict
