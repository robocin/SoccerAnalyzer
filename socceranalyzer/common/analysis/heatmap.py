import numpy as np
import pandas

from socceranalyzer.common.basic.match import Match
from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.chore.mediator import Mediator
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.enums.ssl import SSL
from socceranalyzer.common.enums.vss import VSS
from socceranalyzer.common.geometric.point import Point


class Heatmap(AbstractAnalysis):
    def __init__(self, dataframe: pandas.DataFrame, category: SSL | SIM2D | VSS) -> None:
        self.__dataframe = dataframe
        self.__category = category

        self.__ball_positions: dict[str, list] = {}
        self.__left_players: dict[str, list[list[float], list[float]]] = {
            'player_l2': [[],[]],
            'player_l3': [[],[]],
            'player_l4': [[],[]],
            'player_l5': [[],[]],
            'player_l6': [[],[]],
            'player_l7': [[],[]],
            'player_l8': [[],[]],
            'player_l9': [[],[]],
            'player_l10': [[],[]],
            'player_l11': [[],[]],
        }
        self.__right_players: dict[str, list[list[float], list[float]]] = {
            'player_r2': [[],[]],
            'player_r3': [[],[]],
            'player_r4': [[],[]],
            'player_r5': [[],[]],
            'player_r6': [[],[]],
            'player_r7': [[],[]],
            'player_r8': [[],[]],
            'player_r9': [[],[]],
            'player_r10': [[],[]],
            'player_r11': [[],[]],
        }

        self._analyze()

    @property
    def dataframe(self):
        return self.__dataframe

    @property
    def category(self):
        return self.__category

    @property
    def data(self, left_players_unum: list[int] = [], right_players_unum: list[int] = []):
        
        return self.__left_players.values(), self.__right_players.values(), self.__ball_positions

    def _analyze(self):
        ball_x = np.array(self.dataframe[str(self.category.BALL_X)])
        ball_y = np.array(self.dataframe[str(self.category.BALL_Y)])
        
        # Reflect y positions due to SIM2D server config
        ball_y = ball_y * (-1)

        self.__ball_positions['x'] = ball_x
        self.__ball_positions['y'] = ball_y

        left_players_column = Mediator.players_left_position(self.category, gkeeper=False)
        right_players_column = Mediator.players_right_position(self.category, gkeeper=False)

        # TODO: Refactor when player class is implemented 
        for ith in range(0, 10):
            # +2 because it starts at 0 going up to 9 and needs to reach 2 up to 11
            self.__left_players[f'player_l{ith+2}'][0] = self.dataframe[left_players_column.items[ith].x]
            self.__left_players[f'player_l{ith+2}'][1] = self.dataframe[left_players_column.items[ith].y] * (-1)

            self.__right_players[f'player_r{ith+2}'][0] = self.dataframe[right_players_column.items[ith].x]
            self.__right_players[f'player_r{ith+2}'][1] = self.dataframe[right_players_column.items[ith].y] * (-1)


    def describe(self):
        raise NotImplementedError

    def results(self, config: dict[str, list[int]], ball: bool):
        pass

    def serialize(self):
        raise NotImplementedError