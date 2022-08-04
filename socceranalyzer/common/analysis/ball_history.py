from socceranalyzer.common.basic.match import Match

from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.geometric.point import Point


class BallHistory(AbstractAnalysis):
    """
        Contains the position of the ball in all playmode=play_on moments of the game
    """
    def __init__(self, match : Match):
        super().__init__(match)
        self.__ball_positions = ()
        self._analyze()

    @property
    def dataframe(self):
        return self._dataframe

    @property
    def category(self):
        return self._category

    def _analyze(self):
        x = self.dataframe[str(self.category.BALL_X)]
        y = self.dataframe[str(self.category.BALL_Y)]
        self.__ball_positions = (x, y)

    def describe(self):
        print("No description available")

    def results(self):
        return self.__ball_positions

    def serialize(self):
        raise NotImplementedError