import pandas
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.enums.ssl import SSL
from socceranalyzer.common.enums.vss import VSS
from socceranalyzer.common.geometric.point import Point
from socceranalyzer.common.chore.mediator import Mediator

class GoalReplay:

    def __init__(self, dataframe: pandas.DataFrame, category: SSL | SIM2D | VSS, cycles: int) -> None:
        self.__dataframe = dataframe
        self.__category = category
        self.__cycles = cycles
        self.__ball_positions = []
        self.__left_team_positions = []
        self.__right_team_positions = []

        self.__find_goals()
    
    @property
    def goals_moments(self):
        return self.__goals_moments

    def __find_goals(self) -> None:
        for i in range(len(self.__dataframe)):
            current_playmode = self.__dataframe.loc[i, "playmode"]
            previous_playmode = self.__dataframe.loc[i - 1, "playmode"]

            if ((current_playmode == "goal_l" or current_playmode == "goal_r") 
                and previous_playmode != current_playmode):
                # Goal happened
                self.calculate(i)

    def calculate(self, starting_point: int) -> None:
        ball_pos = []
        left_pos = []
        right_pos = []

        players_left = Mediator.players_left_position(self.category, False)
        players_right = Mediator.players_right_position(self.category, False)

        for i in range(starting_point, starting_point - self.__cycles, -1):
            if (i < 0):
                break

            ball_x = self.__dataframe.loc[i, "ball_x"]
            ball_y = self.__dataframe.loc[i, "ball_y"]

            ball_pos.append(Point(ball_x, ball_y))

            for j in range(11):
                player_left_x = self.__dataframe.loc[i, players_left.items[i].x]
                player_left_y = self.__dataframe.loc[i, players_left.items[i].y]

                player_right_x = self.__dataframe.loc[i, players_right.items[i].x]
                player_right_y = self.__dataframe.loc[i, players_right.items[i].y]

                left_pos.append(Point(player_left_x, player_left_y))

                right_pos.append(Point(player_right_x, player_right_y))
        
        self.__ball_positions.append(ball_pos)
        self.__left_team_positions.append(left_pos)
        self.__right_team_positions.append(right_pos)

    def results(self) -> tuple:
        return (self.__ball_positions, self.__left_team_positions, self.__right_team_positions)