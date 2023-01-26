from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.evaluators.ball_holder import BallHolderEvaluator

class BallTakingInCornerArea(AbstractAnalysis):

    """
        Calculate the number of ball takings in corner area.
    """

    def __init__(self, dataframe, category):
        self.__dataframe = dataframe
        self.__category = category
        self.__current_holder = ''
        self.__corner_x_limit = [-36, -52]
        self.__corner_y_limit = 17
        self.__ball_taking = 0
        
    @property
    def category(self):
        return self.__category

    @property
    def dataframe(self):
        return self.__dataframe

    def _analyze(self):

        corner_dataframe = self.__dataframe[
            (self.__dataframe[str(self.category.PLAYMODE)] == 'play_on') & 
            (self.__dataframe[str(self.category.BALL_X)] <= self.__corner_x_limit[0]) & 
            (self.__dataframe[str(self.category.BALL_X)] >= self.__corner_x_limit[1]) & 
            ((self.__dataframe[str(self.category.BALL_Y)] >= self.__corner_y_limit) | 
            (self.__dataframe[str(self.category.BALL_Y)] <= -self.__corner_y_limit))
        ]

        ball_holder = BallHolderEvaluator(corner_dataframe, self.__category)

        for cycle, row in corner_dataframe.iterrows():
            holder_side = ball_holder.at(cycle)[2]

            if self.__current_holder != holder_side:
                
                if holder_side == 'left' and self.__current_holder == 'right':
                    self.__ball_taking += 1
                self.__current_holder = holder_side

    def results(self):
        return self.__ball_taking

    def describe(self):
        print(f'The ball was taken {self.__ball_taking} times in corner area')

    def serialize(self):
        raise NotImplementedError
