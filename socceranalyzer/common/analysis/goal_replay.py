from unicodedata import category
import pandas
import matplotlib.pyplot as plt
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.enums.ssl import SSL
from socceranalyzer.common.enums.vss import VSS
from socceranalyzer.common.geometric.point import Point
from socceranalyzer.common.chore.mediator import Mediator
from socceranalyzer.common.analysis.find_goals import FindGoals

class GoalReplay:
    """
        Used to verify ball and players positions through N cycles before the occurrence of a goal.

        GoalReplay(dataframe: pandas.DataFrame, category: enum, cycles: int)

        Attributes
        ----------
            private:
                dataframe: pandas.DataFrame
                    match's log
                category: SSL | SIM2D | VSS
                    match's category
                cycles: int
                    number of cycles to be analyzed before the occurrence of each goal
                ball_positions: [[Point]]
                    a list containing a number of elements equivalent to the numbers of goals, with
                    each element being itself a list containing the ball's positions for every cycle
                    analyzed
                left_team_positions: [[[Point]]]
                    a list containing a number of elements equivalent to the numbers of goals, with
                    each element being itself a list containing, for every cycle analyzed, another list
                    corresponding to the left team players positions
                right_team_positions: [[[Point]]]
                    a list containing a number of elements equivalent to the numbers of goals, with
                    each element being itself a list containing, for every cycle analyzed, another list
                    corresponding to the right team players positions

        Methods
        -------
            private:
                calculate(starting_point: int) -> None
                    Iterates backwards through cycles from the moment a goal happened and populates ball_positions, left_team_positions and
                    right_team_positions using information from the dataframe.
                    
            public:
                results() -> (ball_positions, left_team_positions, right_team_positions)
                plot_ball(goal_number: int) -> None
                    Plots ball positions obtained from calculate() onto a SIM2D field.
    """

    def __init__(self, dataframe: pandas.DataFrame, category: SSL | SIM2D | VSS, cycles: int = 100) -> None:
        self.__dataframe = dataframe
        self.__category = category
        self.__cycles = cycles
        self.__ball_positions = []
        self.__left_team_positions = []
        self.__right_team_positions = []

        self.__calculate()
    
    def __calculate(self) -> None:
        """
            Iterates backwards through cycles from the moment a goal happened and populates ball_positions, left_team_positions and
            right_team_positions using information from the dataframe.

            Parameters:
                    starting_point (int): Cycle in which a goal happened.
        """
        goal_moments = FindGoals(self.__dataframe, self.__category).results()

        for starting_point in goal_moments:
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

                left_pos_this_cycle = []
                right_pos_this_cycle = []

                for j in range(11):
                    player_left_x = self.__dataframe.iloc[i][players_left.items[j].x]
                    player_left_y = self.__dataframe.iloc[i][players_left.items[j].y]

                    player_right_x = self.__dataframe.iloc[i][players_right.items[j].x]
                    player_right_y = self.__dataframe.iloc[i][players_right.items[j].y]

                    left_pos_this_cycle.append(Point(player_left_x, player_left_y))

                    right_pos_this_cycle.append(Point(player_right_x, player_right_y))

                left_pos.append(left_pos_this_cycle)
                right_pos.append(right_pos_this_cycle)
            
            self.__ball_positions.append(ball_pos)
            self.__left_team_positions.append(left_pos)
            self.__right_team_positions.append(right_pos)

    def results(self) -> tuple:
        """
            Returns:
                    tuple: (ball_positions, left_team_positions, right_team_positions)
        """
        return (self.__ball_positions, self.__left_team_positions, self.__right_team_positions)

    def plot_ball(self, goal_number: int) -> None:
        """
            Plots ball positions obtained from calculate() onto a SIM2D field.

            Parameters:
                    goal_number (int): Goal to be plotted number, counting from 0 in the order they happened.
        """
        x_axis = []
        y_axis = []

        for position in self.__ball_positions[goal_number]:
            x_axis.append(position.x)
            y_axis.append(position.y)

        fig, ax = plt.subplots()

        bg = plt.imread("socceranalyzer/images/sim2d_field.png")

        ax.imshow(bg, extent=[-57.5, 57.5, -39, 39])

        ax.plot(x_axis, y_axis)

        plt.show()