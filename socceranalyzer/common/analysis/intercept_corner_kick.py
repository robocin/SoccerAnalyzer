from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.evaluators.ball_holder import BallHolderEvaluator

class InterceptCornerKick(AbstractAnalysis):

    """
        Calculate the number of intercepts in corner kick
    """

    def __init__(self, dataframe, category):
        self.__dataframe = dataframe
        self.__category = category
        self.__intercept_counts = 0.0

    @property
    def category(self):
        return self.__category

    @property
    def dataframe(self):
        return self.__dataframe
    
    def _analyze(self):

        last_playmode = self.__dataframe.iloc[0]['playmode']
        last_cycle = self.__dataframe.shape[0]
        ball_holder = BallHolderEvaluator(self.__dataframe, self.__category)

        for cycle, row in self.__dataframe.iterrows():
            
            if row['playmode'] != last_playmode and last_playmode == 'corner_kick_r':
                corner_cycle = cycle
                while corner_cycle < cycle + 6 and corner_cycle < last_cycle:
                    holder_side = ball_holder.at(corner_cycle)[2]
                    if holder_side == 'left':
                        self.__intercept_counts += 1
                        break
                    corner_cycle += 1
            last_playmode = row['playmode']

    def describe(self):
        print(f'Number of corner intercepts is {self.__intercept_counts}')

    def results(self):
        return self.__intercept_counts

    def serialize(self):
        raise NotImplementedError

    