from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.evaluators.ball_holder import BallHolderEvaluator
from socceranalyzer.utils.logger import Logger

class KickIn(AbstractAnalysis):

    """
        Class for analysis regarding kick in ball losses
    """

    def __init__(self, dataframe, category, debug):
        self.__dataframe = dataframe
        self.__category = category
        self.__ball_losses = 0

        try:
            self._analyze()
        except Exception as err:
            Logger.error(f"Kick in failed: {err.args[0]}")
            if debug:
                raise
        else:
            Logger.success("Kick in has results")

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

            if(row['playmode'] == 'play_on' and last_playmode == 'kick_in_l'):
                kick_in_cycle = cycle
                
                while kick_in_cycle < cycle + 30 and kick_in_cycle < last_cycle and row['playmode'] == 'play_on':
                    holder_side = ball_holder.at(kick_in_cycle)[2]
                    
                    if holder_side == 'right':
                        self.__ball_losses += 1
                        break
                    kick_in_cycle += 1
                
            last_playmode = row['playmode']

    def describe(self):
        print(f'Number of ball losses in kick in is { self.__ball_losses }')

    def results(self):
        return self.__ball_losses

    def serialize(self):
        raise NotImplementedError

