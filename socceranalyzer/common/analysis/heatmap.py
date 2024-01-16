import pandas
import matplotlib.pyplot as plt
import seaborn as sns
import os

from socceranalyzer.common.basic.match import Match
from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.chore.mediator import Mediator
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.enums.ssl import SSL
from socceranalyzer.common.enums.vss import VSS
from socceranalyzer.common.geometric.point import Point
from socceranalyzer.utils.logger import Logger
from socceranalyzer.common.basic.field import Field

class Heatmap(AbstractAnalysis):
    def __init__(self, dataframe: pandas.DataFrame, category: SSL | SIM2D | VSS, debug, plot_players = True) -> None:
        self.__dataframe = dataframe
        self.__category = category

        self.left_players_x = []
        self.left_players_y = []

        self.right_players_x = []
        self.right_players_y = []

        self.ball_x = []
        self.ball_y = []

        self.__plot_players = plot_players

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
        
        if self.__plot_players:
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
        
        else:
            ball_column = Mediator.ball_position()

            self.ball_x = self.ball_x + self.__dataframe[ball_column.items[0].x].values.tolist()
            self.ball_y = self.ball_y + self.__dataframe[ball_column.items[0].y].values.tolist()

        self.plot()
        
    def plot(self):
        fig, ax = plt.subplots(figsize=(13.5, 8))
        image = "../../images/ssl-pitch.png"
        field = Field(width = 3000, length = 4500) 
        self._background(field, image, ax)

        if self.__plot_players:
            sns.kdeplot(x=self.left_players_x, y=self.left_players_y, fill=True, thresh=0.05, n_levels = 7, alpha=0.5, cmap='Greens')
            sns.kdeplot(x=self.right_players_x, y=self.right_players_y, fill=True, thresh=0.05, n_levels = 7, alpha=0.5, cmap='Reds')
        
        else:
            sns.kdeplot(x=self.ball_x, y=self.ball_y, fill=True, thresh=0.05, n_levels = 7, alpha=0.5, cmap='Greens')
        
        plt.title('Team position heatmap')

        plt.show()

    def _background(self, field, image_path, ax):
        module_path = os.path.dirname(os.path.abspath(__file__))
        absolute_image_path = os.path.join(module_path, image_path)
        soccer_pitch = plt.imread(absolute_image_path)
        ax.imshow(soccer_pitch, extent=[-field.length, field.length, -field.width, field.width])
        ax.set_xlim(-field.length, field.length)
        ax.set_ylim(-field.width, field.width)
        ax.set_xticks([-4500, -3000, -1500, 0, 1500, 3000, 4500])
        ax.set_yticks([-3000, -2000, -1000, 0, 1000, 2000, 3000])

    def describe(self):
        raise NotImplementedError

    def results(self, config: dict[str, list[int]], ball: bool):
        pass

    def serialize(self):
        raise NotImplementedError
    
