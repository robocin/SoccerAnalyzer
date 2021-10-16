from SoccerAnalyzer.socceranalyzer.common.abstract.abstract_factory import AbstractFactory
from SoccerAnalyzer.socceranalyzer.common.evaluators.ball_holder import BallHolderEvaluator

from SoccerAnalyzer.socceranalyzer.common.basic.match import Match
from SoccerAnalyzer.socceranalyzer.common.enums.sim2d import SIM2D
from SoccerAnalyzer.socceranalyzer.common.enums.ssl import SSL
from SoccerAnalyzer.socceranalyzer.common.enums.vss import VSS
from SoccerAnalyzer.socceranalyzer.common.analysis.ball_possession import BallPossession
from SoccerAnalyzer.socceranalyzer.common.analysis.foul_charge import FoulCharge
from SoccerAnalyzer.socceranalyzer.common.analysis.playmodes import Playmodes
from SoccerAnalyzer.socceranalyzer.common.analysis.penalty import Penalty
from SoccerAnalyzer.socceranalyzer.common.analysis.ball_history import BallHistory
from SoccerAnalyzer.socceranalyzer.common.analysis.corners_occurrencies import CornersOcurrencies
from SoccerAnalyzer.socceranalyzer.agent2D.analysis.tester_free_kick import TesterFK
from SoccerAnalyzer.socceranalyzer.common.analysis.time_after_corner import TimeAfterCorner



class MatchAnalyzer(AbstractFactory):
    def __init__(self, match: Match = None):
        self.__match = match
        self.__cat = match.category
        self.__analysis_dict = {}

        # evaluators
        self.__ball_holder_evaluator = None
        self.__shoot_evaluator = None

        try:
            if self.__cat is None:
                raise ValueError('MatchAnalyzer requires a Category as argument and none was given')
        except ValueError as err:
            print(err)
            raise
        else:
            self._generate_evaluators()
            self._run_analysis()

    @property
    def match(self):
        return self.__match

    @property
    def ball_possession(self):
        return self.__ball_possession

    @property
    def tester_free_kick(self):
        return self.__tester_free_kick

    @property
    def foul_charge(self):
        return self.__foul_charge

    @property
    def penalty(self):
        return self.__penalty

    @property
    def corners(self):
        return self.__corners_occurrencies

    @property
    def playmodes(self):
        return self.__playmodes

    def winner(self):
        return self.__match.winning_team

    def loser(self):
        return self.__match.losing_team

    def final_score(self):
        print(f'{self.__match.team_left_name} {self.__match.score_left} x {self.__match.score_right} {self.__match.team_right_name}')

    @property
    def category(self):
        return self.__cat

    @property
    def analysis_dict(self):
        raise NotImplementedError
        # return self.__analysis_dict

    @property
    def ball_holder(self):
        raise NotImplementedError
        # return BallHolder(self.match.dataframe, self.match.category)

    def available(self):
        BallPossession = ("BallPossession", True)
        FoulCharge = ("FoulCharge", True)
        Playmodes = ("Playmodes", True)
        Corners = ("Corners", True)
        Penalty = ("Penalty", True)
        BallHistory = ("BallHistory", True)
        TesterFK = ("Tester Free Kick", True)
        TimeAfterCorner = ("TimeAfterCorner", False)
        TimeAfterFreeKick = ("TimeAfterFreeKick", False)
        TimeAfterSideKick = ("TimeAfterSideKick", False)

        analysis = [BallPossession, FoulCharge, Penalty, BallHistory, Playmodes, Corners, TesterFK,TimeAfterCorner, TimeAfterFreeKick,
                    TimeAfterSideKick]

        for a in analysis:
            if a[1]:
                print(a[0])

    def _generate_evaluators(self):
        pass

    def _run_analysis(self):
        if self.__cat is SIM2D:
            setattr(self, "__ball_possession", None)
            self.__ball_possession = BallPossession(self.__match.dataframe, self.category)

            setattr(self, "__tester_free_kick", None)
            self.__tester_free_kick = TesterFK(self.__match.dataframe, self.category)

            setattr(self, "__foul_charge", None)
            self.__foul_charge = FoulCharge(self.__match.dataframe, self.category)

            setattr(self, "__penalty", None)
            self.__penalty = Penalty(self.__match.dataframe, self.category)

            setattr(self, "__playmodes", None)
            self.__playmodes = Playmodes(self.__match.dataframe, self.category)

            setattr(self, "__corners", None)
            self.__corners_occurrencies = CornersOcurrencies(self.__match.dataframe, self.category)

            setattr(self, "__ball_history", None)
            self.__ball_history = BallHistory(self.__match.dataframe, self.category)

            #setattr(self, "__time_after_corner", None)
            #self.__time_after_corner = TimeAfterCorner(self.__match.dataframe, self.category)

        elif self.__cat is SSL:
            raise NotImplementedError
            # add SSL analysis

        elif self.__cat is VSS:
            raise NotImplementedError
            # add SSL analysis

    def collect_results(self):
        raise NotImplementedError