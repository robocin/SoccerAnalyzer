from socceranalyzer.common.operations.measures import distance
from socceranalyzer.common.geometric.point import Point
from socceranalyzer.common.chore.mediator import Mediator
from socceranalyzer.common.collections.collections import StringListItem
from socceranalyzer.common.collections.collections import StringListPositions
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.evaluators.ball_holder import BallHolderEvaluator

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
                closest_player_side(cycle : int,
                                player_left_position : common.basic.point.Point,
                                player_right_position : common.basic.point.Point,
                                ball_position_this_cycle : common.basic.point.Point) -> str
                    returns the closest player of the ball in the cycle passed as argument
                calculate() -> None
                    populates the left_team_possession and right_team_possession
            public:
                getcurrent_game_log() -> pandas.Dataframe
                    returns the dataframe of the current game being analyzed
                get() -> [a,b]
                    returns the left_team_possession(a) and right_team_possession(b) in percentual
                newGame(game : DataFrame)
                    updates the object with new game and calculates the new ball possession
    """

    def __init__(self, data_frame, category):
        self.__left_team_possession = 0
        self.__right_team_possession = 0
        self.__category = category
        self.__current_game_log = data_frame
        self.__total = 0

        self.__calculate()

    def __str__(self):
        values = self.results()
        return f'Team left: {values[0]}\nTeam right: {values[1]}'

    @property
    def category(self):
        return self.__category

    def __filter_playmode(self, playmode: str):
        return self.__current_game_log[self.__current_game_log[str(self.category.PLAYMODE)] == playmode]


    def __calculate(self):

        filtered_game = self.__filter_playmode('play_on')

        player_left_position = Point()
        player_right_position = Point()
        ball_position_this_cycle = Point()

        for current_cycle, row in filtered_game.iterrows():

            closest_side = BallHolderEvaluator(filtered_game).at(current_cycle)[2]

            if closest_side == 'left':
                self.__left_team_possession += 1
            else:
                self.__right_team_possession += 1

        self.__total = self.__right_team_possession + self.__left_team_possession

    def __closest_player_side(self,
                            cycle: int,
                            player_left_position: Point,
                            player_right_position: Point,
                            ball_position_this_cycle: Point):

        current_cycle = cycle

        ball_x = self.__current_game_log.loc[current_cycle, str(self.category.BALL_X)]
        ball_y = self.__current_game_log.loc[current_cycle, str(self.category.BALL_Y)]

        ball_position_this_cycle.x = ball_x
        ball_position_this_cycle.y = ball_y

        closest_right = 1000
        closest_left = 1000

        players_left = Mediator.players_left_position(self.category, False)
        players_right = Mediator.players_right_position(self.category, False)

        # 10 players only because goalkeeper is not checked in this analysis
        for i in range(0, 10):
            player_left_position.x = self.__current_game_log.loc[current_cycle, players_left.items[i].x]
            player_left_position.y = self.__current_game_log.loc[current_cycle, players_left.items[i].y]

            player_left_distance = distance(player_left_position, ball_position_this_cycle)

            if player_left_distance <= closest_left:
                closest_left = player_left_distance

            player_right_position.x = self.__current_game_log.loc[current_cycle, players_right.items[i].x]
            player_right_position.y = self.__current_game_log.loc[current_cycle, players_right.items[i].y]

            player_right_distance = distance(player_right_position, ball_position_this_cycle)

            if player_right_distance <= closest_right:
                closest_right = player_right_distance

        if closest_left < closest_right:
            return "left"
        else:
            return "right"

    def results(self):
        return (self.__left_team_possession / self.__total, self.__right_team_possession / self.__total)

    def describe(self):
        name_l = self.__current_game_log.loc[1, str(self.category.TEAM_LEFT)]
        name_r = self.__current_game_log.loc[1, str(self.category.TEAM_RIGHT)]
        print(f'{name_l}: {self.__left_team_possession/self.__total}\n' 
                f'{name_r}: {self.__right_team_possession/self.__total}')

    def serialize(self):
        raise NotImplementedError