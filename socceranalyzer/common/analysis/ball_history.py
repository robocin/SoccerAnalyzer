from enum import Enum

from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.geometric.point import Point
from socceranalyzer.logger import Logger


class BallHistory(AbstractAnalysis):
    """
        Contains the position of the ball in all playmode=play_on moments of the game
    """
    def __init__(self, dataframe, category: Enum):
        self.__dataframe = dataframe
        self.__category = category
        self.__ball_positions = ()
        try:
            self._analyze()
            raise RuntimeError("this is a runtime error")
            Logger.success("BallHistory has results.")
        except RuntimeError as error:
            Logger.error(f"BallHistory failed: {error}")
    @property
    def dataframe(self):
        return self.__dataframe

    @property
    def category(self):
        return self.__category

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