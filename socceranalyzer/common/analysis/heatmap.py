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

class Heatmap(AbstractAnalysis):
    def __init__(self, dataframe: pandas.DataFrame, category: SSL | SIM2D | VSS, debug, plot_Players = True) -> None:
        self.__dataframe = dataframe
        self.__category = category

        self.left_players_x = []
        self.left_players_y = []

        self.right_players_x = []
        self.right_players_y = []

        self.ball_x = []
        self.ball_y = []

        self.__plot_Players = plot_Players

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
        
        if self.__plot_Players:
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

        if self.__plot_Players:
            sns.kdeplot(x=self.left_players_x, y=self.left_players_y, fill=True, thresh=0.05, n_levels = 7, alpha=0.5, cmap='Greens')
            sns.kdeplot(x=self.right_players_x, y=self.right_players_y, fill=True, thresh=0.05, n_levels = 7, alpha=0.5, cmap='Reds')
        
        else:
            sns.kdeplot(x=self.ball_x, y=self.ball_y, fill=True, thresh=0.05, n_levels = 7, alpha=0.5, cmap='Greens')
        
        # Add background pitch and title
        if (self.__category == SSL):
            module_path = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(module_path, '../../images/ssl-pitch.png')
            soccer_pitch = plt.imread(image_path)
            ax.imshow(soccer_pitch, extent=[-5200, 5200, -3700, 3700])
            ax.set_xlim(-5200, 5200)
            ax.set_ylim(-3700, 3700)
            ax.set_xticks([])
            ax.set_yticks([])

        plt.title('Team position heatmap')

        # Show the plot
        plt.show()

    def describe(self):
        raise NotImplementedError

    def results(self, config: dict[str, list[int]], ball: bool):
        pass

    def serialize(self):
        raise NotImplementedError
    

df = pandas.read_csv('/home/emilly/github/SoccerAnalyzer/socceranalyzer/objPositions.csv')

df.query('whatObject == "ball" ', inplace = True)

df.drop (['Unnamed: 0', 'id'], axis = 1)

df.rename(columns={'position_x': 'ball_position_x', 'position_y': 'ball_position_y'}, inplace = True)

heatmap = Heatmap(df, SSL, debug = False, plot_Players = False)