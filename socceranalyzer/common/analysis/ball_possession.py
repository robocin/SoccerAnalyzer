from socceranalyzer.common.basic.match import Match
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.evaluators.ball_holder import BallHolderEvaluator
from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis

class BallPossession(AbstractAnalysis):
    """
        Used to calculate the simple ball possession of the game.
        BallPossession(match)
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
            
            public through @properties:
                dataframe: pandas.DataFrame
                    match's log
                category: SSL | SIM2D | VSS
                    match's category 


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

    def __init__(self, match : Match):
        super().__init__(match)
        self.__left_team_possession = 0
        self.__right_team_possession = 0
        self.__total = 0

        self._analyze()

    def __str__(self):
        values = self.results()
        return f'Team left: {values[0]}\nTeam right: {values[1]}'

    @property
    def dataframe(self):
        return self._dataframe

    @property
    def category(self):
        return self._category

    def __filter_playmode(self, playmode: str):
        return self._dataframe[self._dataframe[str(self.category.PLAYMODE)] == playmode]


    def _analyze(self):
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
        name_l = self._dataframe.loc[1, str(self._category.TEAM_LEFT)]
        name_r = self._dataframe.loc[1, str(self._category.TEAM_RIGHT)]
        print(f'{name_l}: {self.__left_team_possession/self.__total}\n' 
                f'{name_r}: {self.__right_team_possession/self.__total}')

    def serialize(self):
        raise NotImplementedError