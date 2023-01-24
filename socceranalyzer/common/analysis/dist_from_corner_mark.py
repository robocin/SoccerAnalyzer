import pandas as pd
from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.geometric.point import Point
from socceranalyzer.common.geometric.rectangle import Rectangle
from socceranalyzer.common.operations.measures import distance_sqrd

class DistFromCornerMark(AbstractAnalysis):

    """
        Calculate average distance from corner mark of defense players 
    """

    def __init__(self, dataframe, category):
        self.__dataframe = dataframe
        self.__category = category
        self.__average_distance = 0.0
        self.__players_inside_area = 0.0
        self.__upper_corner_area = Rectangle( Point(-52, -34), Point(-36, -16) )
        self.__down_corner_area = Rectangle( Point(-52, 34), Point(-36, 16) )

    @property
    def category(self):
        return self.__category

    @property
    def dataframe(self):
        return self.__dataframe
    
    def _analyze(self):
        corner_dataframe = pd.DataFrame()
        last_playmode = self.__dataframe.iloc[0]['playmode']
        last_row = self.__dataframe.iloc[0]

        for cycle, row in self.__dataframe.itterows():
            if row['playmode'] != last_playmode and last_playmode == 'corner_kick_l':
                corner_dataframe.append(last_row)
            last_playmode = row['playmode']
            last_row = row

        for cycle, row in corner_dataframe.itterows():
            ball_pos = Point(row['ball_x'], row['ball_y'])

            for i in range(1, 12):
                    player = 'player_l{}'.format(i)                
                    agent_pos = Point(corner_dataframe.loc[cycle, f'{player}_x'], corner_dataframe.loc[cycle, f'{player}_y'])

                    if( (row['ball_y'] < 0 and self.__upper_corner_area.is_inside(agent_pos)) or 
                        (row['ball_y'] > 0 and self.__down_corner_area.is_inside(agent_pos)) ):
                        self.__average_distance += distance_sqrd(agent_pos, ball_pos)
                        self.__players_inside_area += 1
                
        self.__average_distance /= self.__players_inside_area

    def describe(self):
        return self.__average_distance

    def results(self):
        print(f'Average distance of players from corner mark is {self.__average_distance}')

    def serialize(self):
        raise NotImplementedError

    