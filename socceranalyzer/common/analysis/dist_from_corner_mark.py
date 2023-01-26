import pandas as pd
from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.geometric.point import Point
from socceranalyzer.common.operations.measures import distance

class DistFromCornerMark(AbstractAnalysis):

    """
        Calculate average distance from corner mark of defense players 
    """

    def __init__(self, dataframe, category):
        self.__dataframe = dataframe
        self.__category = category
        self.__average_distance = 0.0
        self.__players_inside_area = 0.0

    @property
    def category(self):
        return self.__category

    @property
    def dataframe(self):
        return self.__dataframe
    
    def _analyze(self):
        last_playmode = self.__dataframe.iloc[0]['playmode']

        for cycle, row in self.__dataframe.iterrows():
            if row['playmode'] != last_playmode and last_playmode == 'corner_kick_l':
                ball_pos = Point(row['ball_x'], row['ball_y'])

                for i in range(1, 12):
                    player = 'player_l{}'.format(i)                
                    agent_pos = Point(row[f'{player}_x'], row[f'{player}_y'])
                    
                    if(distance(ball_pos, agent_pos) < 25):
                        self.__average_distance += distance(agent_pos, ball_pos)
                        self.__players_inside_area += 1

            last_playmode = row['playmode']

        if self.__players_inside_area != 0:        
            self.__average_distance /= self.__players_inside_area

    def describe(self):
        print(f'Average distance of players from corner mark is {self.__average_distance}')

    def results(self):
        return self.__average_distance

    def serialize(self):
        raise NotImplementedError

    