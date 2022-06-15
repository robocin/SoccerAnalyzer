from unicodedata import category
import pandas
import matplotlib.pyplot as plt
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.enums.ssl import SSL
from socceranalyzer.common.enums.vss import VSS
from socceranalyzer.common.geometric.point import Point
from socceranalyzer.common.chore.mediator import Mediator

class GoalReplay:
    """
        Used to verify ball and players positions through N cycles before the occurrence of a goal.

        GoalReplay(dataframe: pandas.DataFrame, category: enum, cycles: int)

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
    """

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
            current_playmode = self.__dataframe.iloc[i][str(self.__category.PLAYMODE)]
            previous_playmode = self.__dataframe.iloc[i - 1][str(self.__category.PLAYMODE)]

            if ((current_playmode == str(self.__category.GOAL_SCORED_L) or current_playmode == "goal_r") 
                and previous_playmode != current_playmode):
                # Goal happened
                self.calculate(i)

    def calculate(self, starting_point: int) -> None:
        ball_pos = []
        left_pos = []
        right_pos = []

        players_left = Mediator.players_left_position(self.__category)
        players_right = Mediator.players_right_position(self.__category)

        for i in range(starting_point, starting_point - self.__cycles, -1):
            if (i < 0):
                break

            ball_x = self.__dataframe.iloc[i][str(self.__category.BALL_X)]
            ball_y = self.__dataframe.iloc[i][str(self.__category.BALL_Y)]

            ball_pos.append(Point(ball_x, ball_y))

            for j in range(11):
                player_left_x = self.__dataframe.iloc[i][players_left.items[j].x]
                player_left_y = self.__dataframe.iloc[i][players_left.items[j].y]

                player_right_x = self.__dataframe.iloc[i][players_right.items[j].x]
                player_right_y = self.__dataframe.iloc[i][players_right.items[j].y]

                left_pos.append(Point(player_left_x, player_left_y))

                right_pos.append(Point(player_right_x, player_right_y))
        
        self.__ball_positions.append(ball_pos)
        self.__left_team_positions.append(left_pos)
        self.__right_team_positions.append(right_pos)

    def results(self) -> tuple:
        return (self.__ball_positions, self.__left_team_positions, self.__right_team_positions)

    def plot_ball(self, goal_number: int) -> None:
        x_axis = []
        y_axis = []

        for position in self.__ball_positions[goal_number]:
            x_axis.append(position.x)
            y_axis.append(position.y)

        fig, ax = plt.subplots()

        bg = plt.imread("sim2d_field.png")

        ax.imshow(bg, extent=[-57.5, 57.5, -39, 39])

        ax.plot(x_axis, y_axis)

        plt.show()

