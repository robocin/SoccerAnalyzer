import pandas
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
                
        Methods
        -------
            private:
                analyze(goal_number: int, cycles: int (optional), players: bool (optional)) -> tuple
                    Iterates backwards through cycles from the moment a goal happened and populates ball_positions, left_team_positions and
                    right_team_positions using information from the dataframe.
                    
            public:
                results(goal_number: int, cycles: int (optional), players: bool (optional)) -> tuple
    """

    def __init__(self, dataframe: pandas.DataFrame, category: SSL | SIM2D | VSS) -> None:
        self.__dataframe = dataframe
        self.__category = category
        
    def _analyze(self, goal_number: int, cycles: int = 40, players: bool = True) -> tuple:
        """
            Iterates backwards through cycles from the moment a goal happened and populates ball_positions, left_team_positions and
            right_team_positions using information from the dataframe.

            Parameters:
                    goal_number (int): Goal to be analyzed, counting from 0 in the order they happened.
                    cycles (int): Number of cycles to be analyzed before the occurrence of the goal (default is 40).
                    players (bool): If it's set to False, players' positions won't be calculated (default is True).

            Returns:
                    ([Point], [[Point]], [[Point]]): (ball_positions, left_team_positions, right_team_positions), if players is True.
                    [Point]: ball_positions, if players is False
        """
        goal_moments = FindGoals(self.__dataframe, self.__category).results()

        starting_point = goal_moments[goal_number]

        ball_positions = []
        left_team_positions = []
        right_team_positions = []

        players_left = Mediator.players_left_position(self.__category)
        players_right = Mediator.players_right_position(self.__category)

        for i in range(starting_point, starting_point - cycles, -1):
            if (i < 0):
                break

            ball_x = self.__dataframe.iloc[i][str(self.__category.BALL_X)]
            ball_y = self.__dataframe.iloc[i][str(self.__category.BALL_Y)]

            ball_positions.append(Point(ball_x, ball_y))

            if (players == True):
                left_pos_this_cycle = []
                right_pos_this_cycle = []

                for j in range(11):
                    player_left_x = self.__dataframe.iloc[i][players_left.items[j].x]
                    player_left_y = self.__dataframe.iloc[i][players_left.items[j].y]

                    player_right_x = self.__dataframe.iloc[i][players_right.items[j].x]
                    player_right_y = self.__dataframe.iloc[i][players_right.items[j].y]

                    left_pos_this_cycle.append(Point(player_left_x, player_left_y))

                    right_pos_this_cycle.append(Point(player_right_x, player_right_y))

                left_team_positions.append(left_pos_this_cycle)
                right_team_positions.append(right_pos_this_cycle)

        if (players == True):
            return (ball_positions, left_team_positions, right_team_positions)

        else:
            return ball_positions

    def results(self, goal_number: int, cycles: int = 40, players: bool = True) -> tuple:
        """
            Parameters:
                    goal_number (int): Goal to be analyzed, counting from 0 in the order they happened.
                    cycles (int): Number of cycles to be analyzed before the occurrence of the goal (default is 40).
                    players (bool): If it's set to False, players' positions won't be calculated (default is True).

            Returns:
                    ([Point], [[Point]], [[Point]]): (ball_positions, left_team_positions, right_team_positions), if players is True.
                    [Point]: ball_positions, if players is False
        """
        return self._analyze(goal_number, cycles, players)

    