from pandas import DataFrame
from socceranalyzer.common.abstract.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.geometric.point import Point
from socceranalyzer.common.operations.measures import *
from math import sqrt, acos
from numpy import exp

R_GOAL_POS = [52.5, 0]
R_GOAL_TOP_BAR = [52.5, 7.01]
R_GOAL_BOTTOM_BAR = [52.5, -7.01]
L_GOAL_POS = [-52.5, 0]
L_GOAL_TOP_BAR = [-52.5, 7.01]
L_GOAL_BOTTOM_BAR = [-52.5, -7.01]
XG_MODEL_VARIABLES = ['angle','distance', 'players_in_between']
XG_MODEL_PARAMS = [2.678591, 1.788279, -0.164496, -0.671407]

class Shooting(AbstractAnalysis):
    def __init__(self, dataframe: DataFrame, category):
        self.__category = category
        self.__df = dataframe
        self.__shooting_stats = []
        self.__play_on_cycles = []
        self.__last_shooter = 'not'
        self._analyze()
    
    @property
    def category(self):
        return self.__category

    @property
    def dataframe(self):
        return self.__df

    def __filter_playmode(self, playmode: str):
        return self.__df[self.__df[str(self.__category.PLAYMODE)] == playmode]

    def __get_kicker(self, cycle):
        for i in range(1, 12):
            for side in ['l', 'r']:
                player = 'player_{}{}'.format(side, i)
                player_counting_kicks = self.__df.loc[cycle, f'{player}_counting_kick']
                player_counting_tackles = self.__df.loc[cycle, f'{player}_counting_tackle']
                
                previous_cycle = cycle - 1
                if(previous_cycle > 0):
                    player_counting_kicks_before = self.__df.loc[previous_cycle, f'{player}_counting_kick']
                    player_counting_tackles_before = self.__df.loc[previous_cycle, f'{player}_counting_tackle']

                    if player_counting_kicks > player_counting_kicks_before or player_counting_tackles > player_counting_tackles_before:
                        return player
        return ''

    def __get_players_inside_area(self, cycle: int, a: list[float], b: list[float], c: list[float]) -> int:
        players_inside = 0
        for i in range(1, 12):
            for side in ['l', 'r']:
                player = 'player_{}{}'.format(side, i)                
                agent_pos = [self.__df.loc[cycle, f'{player}_x'], self.__df.loc[cycle, f'{player}_y']]
                if is_point_inside_triangle(a, b, c, agent_pos):
                    players_inside += 1
        return players_inside

    def __calculate_xG(self, sh: dict[str, float]) -> float:
        bsum=XG_MODEL_PARAMS[0]
        for i,v in enumerate(XG_MODEL_VARIABLES):
            bsum=bsum+XG_MODEL_PARAMS[i+1]*sh[v]
        xG = 1 - 1/(1+exp(bsum))
        return xG

    def __update_shot_data(self, cycle: int, player: str, x: float, y: float, players_inside: int, on_target: bool):
        dist = distance(Point(x,y), Point(R_GOAL_POS[0], R_GOAL_POS[1]))
        p1 = distance_sqrd([x,y], R_GOAL_TOP_BAR)
        p2 = distance_sqrd([x,y], R_GOAL_BOTTOM_BAR)
        p3 = distance_sqrd(R_GOAL_TOP_BAR, R_GOAL_BOTTOM_BAR)
        p12 = sqrt(p1)
        p13 = sqrt(p2)
        angle = acos((p1+p2-p3)/(2*p12*p13))
        show_time = int(self.__df.loc[cycle, str(self.__category.GAME_TIME)])
        data = {
            'show_time': show_time,
            'player': player,
            'team': player.split('_')[-1][0],
            'x': x,
            'y': y,
            'distance': dist,
            'angle': angle,
            'on_target': on_target,
            'players_in_between': players_inside,
            'xG': self.__calculate_xG({'distance': dist, 'angle': angle, 'players_in_between': players_inside}),
            'goal': 0
        }
        self.__shooting_stats.append(data)

    def __check_shoot(self, cycle):
        if not self.__df.loc[cycle, str(self.__category.GAME_TIME)] in self.__play_on_cycles:
            return

        if((self.__df.loc[cycle, 'ball_vx']**2 + self.__df.loc[cycle, 'ball_vy']**2)** 0.5  > 2.0):
            kicker = self.__get_kicker(cycle)
            
            # Right team registered shot
            if(kicker != '' and 'r' in kicker.split('_')[-1] and self.__df.loc[cycle, f'{kicker}_x'] < 0 and self.__df.loc[cycle, 'ball_vx'] != 0):
                # print(cycle)
                ball_pos_before = (self.__df.loc[cycle-1, 'ball_x'], self.__df.loc[cycle-1, 'ball_y'])
                ball_pos = (self.__df.loc[cycle, 'ball_x'], self.__df.loc[cycle, 'ball_y'])
                # print(ball_pos_before, ball_pos)
                
                (x_right, y_right) = line_intersection((ball_pos_before,ball_pos), ((-53.0,1),(-53.0,0)))
                    
                if 7.5 < abs(y_right) < 17.5:
                    self.__last_shooter = kicker
                    pos_x = self.__df.loc[cycle, f'{kicker}_x']
                    pos_y = self.__df.loc[cycle, f'{kicker}_y']
                    x = abs(pos_x)
                    y = (-1)*pos_y
                    players_inside = self.__get_players_inside_area(cycle,[pos_x,pos_y],L_GOAL_TOP_BAR,L_GOAL_BOTTOM_BAR)
                    self.__update_shot_data(cycle,self.__last_shooter,x,y,players_inside,False)  
                elif abs(y_right) <= 7.5:
                    self.__last_shooter = kicker
                    pos_x = self.__df.loc[cycle, f'{kicker}_x']
                    pos_y = self.__df.loc[cycle, f'{kicker}_y']
                    x = abs(pos_x)
                    y = (-1)*pos_y
                    players_inside = self.__get_players_inside_area(cycle,[pos_x,pos_y],L_GOAL_TOP_BAR,L_GOAL_BOTTOM_BAR)
                    self.__update_shot_data(cycle,self.__last_shooter,x,y,players_inside,True)
            # Left team registered shot
            elif(kicker != '' and 'l' in kicker.split('_')[-1] and self.__df.loc[cycle, f'{kicker}_x'] > 0 and self.__df.loc[cycle, 'ball_vx'] != 0):
                # print(cycle)
                ball_pos_before = (self.__df.loc[cycle-1, 'ball_x'], self.__df.loc[cycle-1, 'ball_y'])
                ball_pos = (self.__df.loc[cycle, 'ball_x'], self.__df.loc[cycle, 'ball_y'])
                # print(ball_pos_before, ball_pos)

                (x_left, y_left) = line_intersection((ball_pos_before,ball_pos), ((53.0,1),(53.0,0)))

                if 7.5 < abs(y_left) < 17.5:
                    self.__last_shooter = kicker
                    x = self.__df.loc[cycle, f'{kicker}_x']
                    y = self.__df.loc[cycle, f'{kicker}_y']
                    players_inside = self.__get_players_inside_area(cycle,[x,y],R_GOAL_TOP_BAR,R_GOAL_BOTTOM_BAR)
                    self.__update_shot_data(cycle,self.__last_shooter,x,y,players_inside,False)
                elif abs(y_left) <= 7.5:
                    self.__last_shooter = kicker
                    x = self.__df.loc[cycle, f'{kicker}_x']
                    y = self.__df.loc[cycle, f'{kicker}_y']
                    players_inside = self.__get_players_inside_area(cycle,[x,y],R_GOAL_TOP_BAR,R_GOAL_BOTTOM_BAR)
                    self.__update_shot_data(cycle,self.__last_shooter,x,y,players_inside,True)

    def __check_goal(self, cycle):
        split_play_mode = self.__df.loc[cycle, str(self.category.PLAYMODE)].rsplit('_')
        mode = split_play_mode[0]
        side = split_play_mode[1]
        if side == 'kick': return
        if(mode == 'goal'):
            side = split_play_mode[1]
            if(side == 'r'):
                if(self.__last_shooter != 'not' and 'r' in self.__last_shooter.split('_')[-1]):
                    self.__shooting_stats[-1]['goal'] = 1
            elif(side == 'l'):
                if(self.__last_shooter != 'not' and 'l' in self.__last_shooter.split('_')[-1]):
                    self.__shooting_stats[-1]['goal'] = 1

    def _analyze(self):
        self.__play_on_cycles = list(self.__filter_playmode('play_on')[str(self.category.GAME_TIME)])
        for i, _ in self.__df.iterrows():
            self.__check_shoot(i)
            self.__check_goal(i)
        self.__shooting_stats_df = DataFrame(self.__shooting_stats)

    def describe(self):
        pass

    def results(self):
        return self.__shooting_stats

    def serialize(self):
        return NotImplementedError
    