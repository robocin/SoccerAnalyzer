import pandas
import matplotlib.pyplot as plt
import seaborn as sns

from socceranalyzer.common.basic.match import Match
from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.chore.mediator import Mediator
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.enums.ssl import SSL
from socceranalyzer.common.enums.vss import VSS
from socceranalyzer.common.geometric.point import Point
from socceranalyzer.utils.logger import Logger


class Heatmap(AbstractAnalysis):
    def __init__(self, dataframe: pandas.DataFrame, category: SSL | SIM2D | VSS, debug) -> None:
        self.__dataframe = dataframe
        self.__category = category

        self.left_players_x = []
        self.left_players_y = []

        self.right_players_x = []
        self.right_players_y = []

        try:
            self._analyze()
        except Exception as err:
            Logger.error(f"Heatmap failed: {err.args[0]}")
            if debug:
                raise
        else:
            Logger.success("Heatmap has results.")
    @property
    def dataframe(self):
        return self.__dataframe

    @property
    def category(self):
        return self.__category

    def _analyze(self):
        # Filtering to playmode where the game is running
        self.__dataframe = self.__dataframe[self.__dataframe[str(self.__category.PLAYMODE)] == str(self.__category.RUNNING_GAME)]

        left_players_column = Mediator.players_left_position(self.category, gkeeper=False)
        right_players_column = Mediator.players_right_position(self.category, gkeeper=False)
        
        for i in range(len(left_players_column.items)):
            self.left_players_x = self.left_players_x + self.__dataframe[left_players_column.items[i].x].values.tolist()
            self.left_players_y = self.left_players_y + self.__dataframe[left_players_column.items[i].y].values.tolist()

        for i in range(len(right_players_column.items)):
            self.right_players_x = self.right_players_x + self.__dataframe[right_players_column.items[i].x].values.tolist()
            self.right_players_y = self.right_players_y + self.__dataframe[right_players_column.items[i].y].values.tolist()
        
    def plot(self):
        sns.kdeplot(x=self.left_players_x, y=self.left_players_y, fill=True, thresh=False, n_levels = 15, alpha=0.5, cmap='Greens')
        sns.kdeplot(x=self.right_players_x, y=self.right_players_y, fill=True, thresh=False, n_levels = 15, alpha=0.5, cmap='Reds')

        # Add labels and a title
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Team position heatmap')

        # Show the plot
        plt.show()

    def describe(self):
        raise NotImplementedError

    def results(self, config: dict[str, list[int]], ball: bool):
        pass

    def serialize(self):
        raise NotImplementedError