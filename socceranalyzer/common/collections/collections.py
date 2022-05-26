from socceranalyzer.common.basic.match import Match
from socceranalyzer.common.entity.ball import Ball
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.enums.ssl import SSL
from socceranalyzer.common.enums.vss import VSS
from socceranalyzer.common.evaluators.player_detector import PlayerDetector


class StringListPositions:
    """
        This class is a named container of elements 
    """
    def __init__(self):
        self.items = []


class StringListItem:
    """
        This class is a named container element
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


class ThresholdCollection:
    """
        This class is a named container that can have it's values reset.

        Methods
        -------
            public:
                reset: None
                    Reset all values class attr to default
    """
    def __init__(self):
        self.corner_thr = 10
        self.kick_in_thr = 10
        self.foul_thr = 10

    def reset(self, ck=10, ki=10, fk=10):
        self.corner_thr = ck
        self.kick_in_thr = ki
        self.foul_thr = fk


class EntityCollection:
    def __init__(self, match: Match, category: SSL | SIM2D | VSS) -> None:
        self.__match = match
        self.__category: SSL | SIM2D | VSS = category
        
        if self.__category is SSL:
            detector = PlayerDetector(self.__match)
            left_players = detector.left_players()
            right_players = detector.right_players()

            return left_players, right_players
        else:
            raise NotImplementedError
    
    @property
    def category(self):
        return self.__category

class EvaluatorCollection:
    """
    A collection of evaluators created for a specific category game.
    """
    def __init__(self, match: Match) -> None:
        self.__evaluators: list = self._generateEvaluators(match)

    def _generateEvaluators(self, match: Match) -> list:
        if match.category is SIM2D:
            raise NotImplementedError

        elif match.category is SSL: 
            player_detector = PlayerDetector(match)
            return [player_detector]

        elif match.category is VSS:
            raise NotImplementedError