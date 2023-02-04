from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.evaluators.ball_holder import BallHolderEvaluator
from socceranalyzer.utils.logger import Logger

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
            Uses socceranalyzer.common.evaluators.ball_holder to populate left_team_possession and right_team_possession
        """
        filtered_game = self.__filter_playmode('play_on')

        ball_holder_analysis = BallHolderEvaluator(filtered_game, self.category)

        for current_cycle, row in filtered_game.iterrows():
            closest_side = ball_holder_analysis.at(current_cycle)[2]

            if closest_side == 'left':
                self.__left_team_possession += 1
            else:
                self.__right_team_possession += 1

        self.__total = self.__right_team_possession + self.__left_team_possession

    def results(self):
        return (self.__left_team_possession / self.__total, self.__right_team_possession / self.__total)

    def describe(self):
        name_l = self.__current_game_log.loc[1, str(self.category.TEAM_LEFT)]
        name_r = self.__current_game_log.loc[1, str(self.category.TEAM_RIGHT)]
        print(f'{name_l}: {self.__left_team_possession/self.__total}\n' 
                f'{name_r}: {self.__right_team_possession/self.__total}')

    def serialize(self):
        raise NotImplementedError