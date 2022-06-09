from typing import Literal
from pandas import DataFrame
from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.geometric.point import Point
from socceranalyzer.common.geometric.triangle import Triangle
from socceranalyzer.common.operations.measures import *
from socceranalyzer.common.utility.slicers import PlaymodeSlicer
from socceranalyzer.common.enums.sim2d import Landmarks
from math import sqrt, acos
from numpy import exp

XG_MODEL_VARIABLES = ['angle','distance', 'players_in_between']
XG_MODEL_PARAMS = [2.678591, 1.788279, -0.164496, -0.671407]

class Shooting(AbstractAnalysis):
    """
        Used to calculate simple and advanced shooting stats for specified game.

        Shooting(dataframe: pandas.DataFrame, category)
        
        Attributes
        ----------
            private:
                shooting_stats : dict
                    shooting stats in Python dict format for the game
                shooting_stats_df : pands.DataFrame
                    shooting stats in DataFrame format for the game
                play_on_cycles : list[int]
                    list with game's play on cycles
                last_shooter : str
                    name of last player to register a shot
                    
        Methods
        -------
            private:
                get_kicker(cycle : int) -> str
                    returns the first player to register a counting_kick or counting_tackle change at cycle
                get_players_inside_area(cycle: int, a: list[float], b: list[float], c: list[float]) -> int
                    returns players inside triangular area defined by vertices
                calculate_xG(sh: dict[str, float]) -> float
                    calculates goal probability based on MODEL_VARIABLES
                update_shot_data(cycle: int, player: str, x: float, y: float, players_inside: int, on_target: int) -> None
                    populates the shooting_stats dict
                check_shot(cycle: int) -> None
                    checks for a shot at cycle
                check_goal(cycle: int) -> None
                    checks for a goal at cycle
            public:
                _analyze() -> None
                    performs match analysis
                get_total_team_shots(team: str) -> int
                    returns the total team shots
                get_team_on_target_shots(team: str) -> int
                    returns the total team on target shots
                get_total_team_xG(team: str) -> float
                    returns team total xG for the match
                describe() -> None
                    shows table like structure of the match shooting summary
                results() -> dict
                    returns match detailed shooting stats as a Python dict
                results_as_dataframe() -> pandas.DataFrame:
                    returns a copy of the match detailed shooting stats DataFrame
    """
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

    def __get_kicker(self, cycle: int) -> str:
        """
        Returns the first player to register a counting_kick or counting_tackle change at cycle.

            Parameters:
                    cycle (int): Current index being evaluated
            
            Returns:
                    player (str): Player name or ''.
        """
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

    def __get_players_inside_area(self, cycle: int, a: Point, b: Point, c: Point) -> int:
        """
        Returns the amount of players inside triangular area.

            Parameters:
                    cycle (int): Current index being evaluated
                    a, b, c (Point): The vertices of the triangle
            
            Returns:
                    players_inside (int): Players inside the triangle at specified cycle.
        """
        players_inside = 0

        for i in range(1, 12):
            for side in ['l', 'r']:
                player = 'player_{}{}'.format(side, i)                
                agent_pos = Point(self.__df.loc[cycle, f'{player}_x'], self.__df.loc[cycle, f'{player}_y'])
                if Triangle(a, b, c).is_inside(agent_pos):
                    players_inside += 1
        return players_inside

    def __calculate_xG(self, sh: dict[str, float]) -> float:
        """
        Returns the calculated xG for a shot.

            Parameters:
                    sh (dict[str, float]): A dictionary with MODEL_VARIABLES as keys

            Returns:
                    xG (float): Calculated goal probability for the shot
        """
        bsum=XG_MODEL_PARAMS[0]
        for i,v in enumerate(XG_MODEL_VARIABLES):
            bsum=bsum+XG_MODEL_PARAMS[i+1]*sh[v]
        xG = 1 - 1/(1+exp(bsum))
        return xG

    def __update_shot_data(self, cycle: int, player: str, x: float, y: float, players_inside: int, on_target: int):
        """
        Calculates angle, distance, show_time from a registered shot and updates the shooting stats list.

            Parameters:
                    cycle (int): Indicates the index being evaluated                    
                    player (str): Player name
                    x (float): Normalized x position
                    y (float): Normalized y position
                    players_inside (int): Indicates the amount of players between the shooter and the goal
                    on_target (int): Indicates if the registered shot was on target
        """
        dist = distance(Point(x,y), Landmarks.R_GOAL_POS)
        p1 = distance_sqrd(Point(x,y), Landmarks.R_GOAL_TOP_BAR)
        p2 = distance_sqrd(Point(x,y), Landmarks.R_GOAL_BOTTOM_BAR)
        p3 = distance_sqrd(Landmarks.R_GOAL_TOP_BAR, Landmarks.R_GOAL_BOTTOM_BAR)
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

    def __check_shot(self, cycle: int):
        """
        Checks if a shot ocurred at the specified index.

            Parameters:
                    cycle (int): Indicates the index to look for on match DataFrame
        """
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
                    players_inside = self.__get_players_inside_area(cycle,Point(pos_x,pos_y),Landmarks.L_GOAL_TOP_BAR,Landmarks.L_GOAL_BOTTOM_BAR)
                    self.__update_shot_data(cycle,self.__last_shooter,x,y,players_inside,0)  
                elif abs(y_right) <= 7.5:
                    self.__last_shooter = kicker
                    pos_x = self.__df.loc[cycle, f'{kicker}_x']
                    pos_y = self.__df.loc[cycle, f'{kicker}_y']
                    x = abs(pos_x)
                    y = (-1)*pos_y
                    players_inside = self.__get_players_inside_area(cycle,Point(pos_x,pos_y),Landmarks.L_GOAL_TOP_BAR,Landmarks.L_GOAL_BOTTOM_BAR)
                    self.__update_shot_data(cycle,self.__last_shooter,x,y,players_inside,1)
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
                    players_inside = self.__get_players_inside_area(cycle,Point(x,y),Landmarks.R_GOAL_TOP_BAR,Landmarks.R_GOAL_BOTTOM_BAR)
                    self.__update_shot_data(cycle,self.__last_shooter,x,y,players_inside,0)
                elif abs(y_left) <= 7.5:
                    self.__last_shooter = kicker
                    x = self.__df.loc[cycle, f'{kicker}_x']
                    y = self.__df.loc[cycle, f'{kicker}_y']
                    players_inside = self.__get_players_inside_area(cycle,Point(x,y),Landmarks.R_GOAL_TOP_BAR,Landmarks.R_GOAL_BOTTOM_BAR)
                    self.__update_shot_data(cycle,self.__last_shooter,x,y,players_inside,1)

    def __check_goal(self, cycle: int):
        """
        Checks if playmode at index indicates a goal.

            Parameters:
                    cycle (int): Indicates the index to look for on match DataFrame
        """
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
        """
        Performs match shooting analysis.
        """
        self.__play_on_cycles = list(PlaymodeSlicer.slice(self.dataframe, 'play_on')[str(self.category.GAME_TIME)])
        for i, _ in self.__df.iterrows():
            self.__check_shot(i)
            self.__check_goal(i)
        self.__shooting_stats_df = DataFrame(self.__shooting_stats)

    def get_total_team_shots(self, team: Literal['l', 'r']) -> int:
        """
        Returns total team shots during the match.

            Parameters:
                    team ('l' | 'r'): String indicating the team

            Returns:
                    shots (int): The amount registered shots
        """
        if team != 'l' and team != 'r':
            raise Exception('Team must be l or r')
        return self.__shooting_stats_df[self.__shooting_stats_df.team == team].shape[0]

    def get_team_on_target_shots(self, team: Literal['l', 'r']) -> int:
        """
        Returns total team on target shots during the match.

            Parameters:
                    team ('l' | 'r'): String indicating the team

            Returns:
                    on_target_shots (int): The amount of on target shots
        """
        if team != 'l' and team != 'r':
            raise Exception('Team must be l or r')
        return self.__shooting_stats_df[(self.__shooting_stats_df.team == team) & self.__shooting_stats_df.on_target == True].shape[0]
    
    def get_total_team_xG(self, team: Literal['l', 'r']) -> float:
        """
        Returns total team xG during the match.

            Parameters:
                    team ('l' | 'r'): String indicating the team

            Returns:
                    xG (float): goal probability between 0 and 1
        """
        if team != 'l' and team != 'r':
            raise Exception('Team must be l or r')
        return self.__shooting_stats_df[self.__shooting_stats_df.team == team]['xG'].sum()

    def describe(self):
        """
        Shows a table with teams shooting stats.
        """
        name_l = self.__df.loc[1, str(self.category.TEAM_LEFT)]
        left_shots = self.get_total_team_shots('l')
        left_on_target_shots = self.get_team_on_target_shots('l')
        left_xG = self.get_total_team_xG('l')
        name_r = self.__df.loc[1, str(self.category.TEAM_RIGHT)]
        right_shots = self.get_total_team_shots('r')
        right_on_target_shots = self.get_team_on_target_shots('r')
        right_xG = self.get_total_team_xG('r')

        print(f'{name_l}   |   {name_r}\n'
              f'{left_shots}   shots   {right_shots}\n'
              f'{left_on_target_shots}   on target   {right_on_target_shots}\n'
              f'{left_xG}   xG   {right_xG}\n'
              f'{left_xG/left_shots}   xG/Shot   {right_xG/right_shots}')

    def results(self) -> dict:
        """
        Returns the shooting stats as a dict.

            Returns:
                    dict:
                        show_time(int): Game running time,
                        player (str): The player who registered the shot,
                        team ('r' | 'l'): The team in which the player is on,
                        x (float): Normalized x position,
                        y (float): Normalized y position,
                        distance (float): Distance from (x,y) to goal center,
                        angle (float in radians): Angle between the shot location and the goal posts,
                        on_target (int): Indicates if the shot was on target,
                        players_in_between (int): Indicates the amount of players between the shooter and the goal,
                        xG (float): Goal probability between 0 and 1,
                        goal (int): Indicates if the shot was a goal. 
        """
        return self.__shooting_stats

    def results_as_dataframe(self) -> DataFrame:
        """
        Returns the shooting stats as pandas.DataFrame.

            Returns:
                    DataFrame:
                        show_time(int): Game running time,
                        player (str): The player who registered the shot,
                        team ('r' | 'l'): The team in which the player is on,
                        x (float): Normalized x position,
                        y (float): Normalized y position,
                        distance (float): Distance from (x,y) to goal center,
                        angle (float in radians): Angle between the shot location and the goal posts,
                        on_target (int): Indicates if the shot was on target,
                        players_in_between (int): Indicates the amount of players between the shooter and the goal,
                        xG (float): Goal probability between 0 and 1,
                        goal (int): Indicates if the shot was a goal. 
        """
        return self.__shooting_stats_df.copy()

    def serialize(self) -> list[dict]:
        """
        Returns the shooting stats as json serializable object.
        """
        return self.__shooting_stats
