from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.enums.ssl import SSL
from socceranalyzer.utils.logger import Logger
from socceranalyzer.common.chore.mediator import Mediator
from socceranalyzer.common.geometric.point import Point
from socceranalyzer.common.operations.measures import distance_sqrd

class BallPossession:
    """
        Used to calculate the simple ball possession of the game.
        BallPossession(pandas.DataFrame)
        Attributes
        ----------
            private:
                left_team_possession : int
                    amount of cycles the left team was closest to the ball
                right_team_possession : int
                    amount of cycles the right team was closest to the ball
                current_game : common.basic.game.Game
                    a Game object of the current game
                BALL_X_COLUMN : int
                    ball x position in the dataframe
                BALL_Y_COLUMN : int
                    ball y position in the dataframe
        Methods
        -------
            private:
                filterPlaymode(playmode : str) -> None
                    filters the current_game dataframe and returns a filtered copy
                calculate() -> None
                    uses socceranalyzer.common.evaluators.ball_holder to populate left_team_possession and right_team_possession
            public:
                getcurrent_game_log() -> pandas.Dataframe
                    returns the dataframe of the current game being analyzed
                get() -> [a,b]
                    returns the left_team_possession(a) and right_team_possession(b) in percentual
                newGame(game : DataFrame)
                    updates the object with new game and calculates the new ball possession
    """

    def __init__(self, data_frame, category, debug):
        self.__left_team_possession = 0
        self.__right_team_possession = 0
        self.__category = category
        self.__current_game_log = data_frame
        self.__total = 0

        # Left players stand for RoboCIn team in SSL category
        self.__players_left = Mediator.players_left_position(self.category)
        self.__players_right = Mediator.players_right_position(self.category)
        self.__ball_range = 10 ** 2

        try:
            self.__calculate()
        except Exception as err:
            Logger.error(err.args[0])
            if debug:
                raise
        else: 
            Logger.success("BallPossession has results.")

    def __str__(self):
        values = self.results()
        return f'Team left: {values[0]}\nTeam right: {values[1]}'

    @property
    def category(self):
        return self.__category

    def __filter_playmode(self, playmode: str):
        return self.__current_game_log[self.__current_game_log[str(self.category.PLAYMODE)] == playmode]


    def __calculate(self):
        """
            Populates left_team_possession and right_team_possession using the ball_holder method
        """
        filtered_game = self.__filter_playmode(str(self.category.RUNNING_GAME))

        filtered_game['ball_possession'] = filtered_game.apply(self.__ball_holder, axis=1)

        self.__left_team_possession = filtered_game['ball_possession'].value_counts()['L']
        self.__right_team_possession = filtered_game['ball_possession'].value_counts()['R']

        self.__total = self.__right_team_possession + self.__left_team_possession

    def __ball_holder(self, df_row):
        """
            Receives a dataframe's row as argument and calculates the closest player to the ball to compute
            who has its possession. If two enemy players are within ball range, none receive its holder
            status
        """
        left_distance = float('inf')
        right_distance = float('inf')

        ball_x = df_row[str(self.category.BALL_X)]
        ball_y = df_row[str(self.category.BALL_Y)]
        ball_position = Point(ball_x, ball_y)

        for i in range(len(self.__players_left.items)):
            player_x = df_row[self.__players_left.items[i].x]
            player_y = df_row[self.__players_left.items[i].y]

            player_position = Point(player_x, player_y)

            player_distance = distance_sqrd(player_position, ball_position)

            if (player_distance < left_distance):
                left_distance = player_distance

        for i in range(len(self.__players_right.items)):
            player_x = df_row[self.__players_right.items[i].x]
            player_y = df_row[self.__players_right.items[i].y]

            player_position = Point(player_x, player_y)

            player_distance = distance_sqrd(player_position, ball_position)

            if (player_distance < right_distance):
                right_distance = player_distance
        
        if (abs(left_distance - right_distance) <= self.__ball_range):
            return 'D' # ball in dispute
        elif (left_distance < right_distance):
            return 'L'
        elif (right_distance < left_distance):
            return 'R'
        
    def results(self):
        return (self.__left_team_possession / self.__total, self.__right_team_possession / self.__total)

    def describe(self):
        if (self.category == SIM2D):
            name_l = self.__current_game_log.loc[1, str(self.category.TEAM_LEFT)]
            name_r = self.__current_game_log.loc[1, str(self.category.TEAM_RIGHT)]
            print(f'{name_l}: {self.__left_team_possession/self.__total}\n' 
                    f'{name_r}: {self.__right_team_possession/self.__total}')
        elif (self.category == SSL):
            print(f'RoboCIN: {(self.__left_team_possession/self.__total * 100):.2f}%\n' 
                    f'Enemy: {(self.__right_team_possession/self.__total * 100):.2f}%')

    def serialize(self):
        raise NotImplementedError