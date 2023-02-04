from turtle import speed
from matplotlib import pyplot as plt
from pandas import DataFrame
import numpy as np
from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.dataframe.slicers import PlaymodeSlicer
from socceranalyzer.utils.logger import Logger

class Speed(AbstractAnalysis):
    def __init__(self, dataframe: DataFrame, category, player: int, side: str, debug) -> None:
        self.__dataframe = dataframe
        self.__category = category
        self.__l_players_speed: list = []
        self.__r_players_speed: list = []
        self.__player_speed: list = []

        try:
            self._analyze(player, side)
        except Exception as err:
            Logger.error(f"Speed failed: {err.args[0]}")
            if debug:
                raise
        else:
            Logger.success("Speed has results.")

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
        return self.__player_speed

    def describe(self):
        raise NotImplementedError

    def serialize(self):
        return NotImplementedError

    def _analyze(self, player_number: int, side: str):

        player_number, side = self.__handle_values(player_number, side)
        
        vx = np.array(self.__dataframe[f'player_{side}{player_number}_vx'].tolist())
        vy = np.array(self.__dataframe[f'player_{side}{player_number}_vy'].tolist())

        velocity_vector = [[x,y] for x, y in zip(vx,vy)]

        self.__player_speed = self._calculate_speed(velocity_vector)

    def _calculate_speed(self, velocity_over_time):
        velocity_over_time = np.array(velocity_over_time)
        velocity_scalar = [np.linalg.norm(coordinate) for coordinate in velocity_over_time]

        return velocity_scalar

    def __handle_values(self, player_number, side):
        if side[0] != 'l': 
            if side[0] != 'r':
                raise ValueError(f'Value: {side} is not accepted to socceranalyzer.speed.side')
        
        side = side[0]

        if not(0 <= player_number <= 11):
            raise ValueError(f'Value: {player_number} is not accepted to socceranalyzer.speed.player_number')
            
        return player_number, side
