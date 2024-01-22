import pandas
import math
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.enums.ssl import SSL
from socceranalyzer.common.enums.vss import VSS
from socceranalyzer.common.analysis.find_goals import FindGoals
from socceranalyzer.common.geometric.point import Point
from socceranalyzer.common.core.mediator import Mediator
from socceranalyzer.common.operations.measures import distance
from socceranalyzer.utils.logger import Logger

class GoalkeeperAnalysis:
    """
        Used to provide insights on the goalkeeper's performance, such as distance to ball in occurrences of goals
        and catches count.

        GoalReplay(dataframe: pandas.DataFrame, category: SIM2D | SSL | VSS)

        Attributes
        ----------
            private:
                dataframe: pandas.DataFrame
                    match's log
                category: SSL | SIM2D | VSS
                    match's category
                goalie_positions: [Point]
                    goalkeeper's position at the moment of each goal
                ball_positions: [Point]
                    ball's position at the moment of each goal
                distances: [float]
                    goalkeeper-ball distance at the moment of each goal
                max_distance: float
                    greatest value of distances
                average_distance: float
                    average of distances' values
                catches: int
                    goalkeeper's catches count over the entire game
                
        Methods
        -------
            private:
                analyze() -> None
                    For each enemy goal, consults the dataframe and populates goalie_positions, ball_positions and distances.
                    
            public:
                results() -> ([float], [Point], [Point])
                    (distances, ball_positions, goalie_positions)
                describe() -> None
                    Prints information obtained from results().

                
    """
    def __init__(self, dataframe: pandas.DataFrame, category: SIM2D | SSL | VSS, debug) -> None:
        self.__dataframe = dataframe
        self.__category = category
        self.__goalie_positions = []
        self.__ball_positions = []
        self.__distances = []
        self.__max_distance = 0
        self.__average_distance = 0
        self.__catches = None
        self.__error_magnitude = []
        self.__debug = debug

        try:
            self._analyze()
        except Exception as err:
            Logger.error(f"GoalkeeperAnalysis failed: {err.args[0]}")
            if debug:
                raise
        else:
            Logger.success("GoalkeeperAnalysis has results.")
    
    def __analyze_default(self):
        """
            For each enemy goal, consults the dataframe and populates goalie_positions, ball_positions and distances.
        """
        enemy_team = ""

        left_team_name = self.__dataframe.iloc[0][str(self.__category.TEAM_LEFT)]

        if (left_team_name == "RoboCIn"):
            enemy_team = "right"

            self.__catches = self.__dataframe.iloc[len(self.__dataframe) - 1][str(self.__category.LEFT_GOALKEEPER_CATCHES)]

        else:
            enemy_team = "left"

            self.__catches = self.__dataframe.iloc[len(self.__dataframe) - 1][str(self.__category.RIGHT_GOALKEEPER_CATCHES)]

        enemy_goals = FindGoals(self.__dataframe, SIM2D, self.__debug).results(enemy_team)

        for goal_moment in enemy_goals:
            ball_x = self.__dataframe.iloc[goal_moment][str(self.__category.BALL_X)]
            ball_y = self.__dataframe.iloc[goal_moment][str(self.__category.BALL_Y)]

            ball_pos = Point(ball_x, ball_y)

            self.__ball_positions.append(ball_pos)

            goalie_x = None
            goalie_y = None

            if (enemy_team == "left"):
                goalie_x = Mediator.players_right_position(self.__category, True).items[0].x
                goalie_y = Mediator.players_right_position(self.__category, True).items[0].y

                goalie_x = self.__dataframe.iloc[goal_moment][goalie_x]
                goalie_y = self.__dataframe.iloc[goal_moment][goalie_y]

            else:
                goalie_x = Mediator.players_left_position(self.__category, True).items[0].x
                goalie_y = Mediator.players_left_position(self.__category, True).items[0].y

                goalie_x = self.__dataframe.iloc[goal_moment][goalie_x]
                goalie_y = self.__dataframe.iloc[goal_moment][goalie_y]

            goalie_pos = Point(goalie_x, goalie_y)

            self.__goalie_positions.append(goalie_pos)

            dist = distance(ball_pos, goalie_pos)

            self.__distances.append(dist)

            self.__average_distance += dist
            
            if (dist > self.__max_distance):
                self.__max_distance = dist
        
        adversary_goal_quantity = max(1, len(enemy_goals))
        self.__average_distance = self.__average_distance / adversary_goal_quantity        

    def __calculate_absolute_error(self, play_on_dataframe, goalie_ball_position_dataframe):
        play_on_dataframe.reset_index(inplace=True)
        x_error_list = play_on_dataframe["ball_x"] - goalie_ball_position_dataframe["ball_x"]
        y_error_list = play_on_dataframe["ball_y"] - goalie_ball_position_dataframe["ball_y"]
        
        error_magnitude = []
        for x_error, y_error in zip(x_error_list, y_error_list):
            magnitude = math.sqrt(math.pow(x_error,2) + math.pow(y_error,2))
            error_magnitude.append(magnitude)
        
        return error_magnitude

    def __analyze_ball_position_error(self):
        goalie_ball_position_dataframe = pandas.read_csv("gk_ball_position.csv", header=None)
        goalie_ball_position_dataframe.columns =['unum', 'show_time', 'ball_x', 'ball_y']

        play_on_dataframe = self.__dataframe[self.__dataframe["playmode"] == "play_on"]
        play_on_dataframe = play_on_dataframe[["show_time","ball_x","ball_y"]]
        
        self.__error_magnitude = self.__calculate_absolute_error(play_on_dataframe, goalie_ball_position_dataframe)

    def _analyze(self) -> None:
        # self.__analyze_default()
        self.__analyze_ball_position_error()

        
    def results(self) -> tuple:
        """
            Returns:
                    tuple: (distances, ball_positions, goalie_positions)
        """
        #return (self.__distances, self.__ball_positions, self.__goalie_positions)
        return self.__error_magnitude

    def describe(self) -> None:
        """
            Prints information obtained from results().
        """
        print(f"Average distance: {self.__average_distance:.2f}")
        print(f"Maximum distance: {self.__max_distance:.2f}")
        print(f"Catches: {self.__catches}")

        