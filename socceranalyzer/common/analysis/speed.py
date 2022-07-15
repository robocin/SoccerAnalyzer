from turtle import speed
from matplotlib import pyplot as plt
from pandas import DataFrame
import numpy as np
from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.utility.slicers import PlaymodeSlicer

class Speed(AbstractAnalysis):
    def __init__(self, dataframe: DataFrame, category) -> None:
        self.__dataframe = dataframe
        self.__category = category
        self.__l_players_speed: list = []
        self.__r_players_speed: list = []
        self.__cans: list = []

        self._analyze()

    @property
    def category(self):
        return self.__category

    @property
    def dataframe(self):
        return self.__dataframe

    @property
    def speed_left(self):
        return self.__l_players_speed

    @property
    def speed_right(self):
        return self.__r_players_speed

    def results(self):
        plt.plot(self.__cans)
        plt.show()

    def describe(self):
        raise NotImplementedError

    def serialize(self):
        return NotImplementedError

    def _analyze(self):
        clean_df = PlaymodeSlicer.slice(self.__dataframe,str(SIM2D.RUNNING_GAME))
        clean_df.head()
        vx = np.array(clean_df['player_l7_vx'].tolist())
        vy = np.array(clean_df['player_l7_vy'].tolist())

        velocity_vector = [[x,y] for x, y in zip(vx,vy)]

        self._calculate_speed(velocity_vector)

    def _calculate_speed(self, velocity_over_time):
        velocity_over_time = np.array(velocity_over_time)
        velocity_scalar = [np.linalg.norm(coordinate) for coordinate in velocity_over_time]

        self.__cans = velocity_scalar
