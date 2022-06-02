import pandas
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.enums.ssl import SSL
from socceranalyzer.common.enums.vss import VSS
from socceranalyzer.common.geometric.point import Point

class GoalReplay:

    def __init__(self, dataframe: pandas.DataFrame, category: SSL | SIM2D | VSS, cycles: int) -> None:
        self.__dataframe = dataframe
        self.__filtered_dataframe = dataframe[(dataframe.playmode == "goal_l") or (dataframe.playmode == "goal_r")]
        self.__category = category
        self.__cycles = cycles
        self.__goals_moments = []

        self.__find_goals()
    
    @property
    def goals_moments(self):
        return self.__goals_moments

    def __find_goals(self) -> None:
        for i in range(len(self.__filtered_dataframe)):
            show_time = self.__filtered_dataframe.at[i, "show_time"]

            if (self.__dataframe.at[show_time - 1, "playmode"] == "play_on"):
                self.__goals_moments.append(show_time)

    def results(self, goal_number: int) -> tuple:
        goal_moment = self.goals_moments[goal_number]

        ball_pos = []

        for i in range(self.__cycles):
            if ((goal_moment - 1) < 0):
                break

            ball_x = self.__dataframe.at[goal_moment - i, "ball_x"]
            ball_y = self.__dataframe.at[goal_moment - i, "ball_y"]

            ball_position = Point(ball_x, ball_y)

            ball_pos.append(ball_position)

        return ball_pos