from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis

class TimeInPenaltyArea(AbstractAnalysis):

    """
        Calculate the numbers of cycles that the ball is inside penalty area.
    """

    def __init__(self, dataframe, category):
        self.__category = category
        self.__dataframe = dataframe
        self.__cycles_inside = 0
        self.__penalty_x_limits = [-36, -52]
        self.__penalty_y_limit = 20

    @property
    def category(self):
        return self.__category

    @property
    def dataframe(self):
        return self.__dataframe

    def _analyze(self):

        inside_penalty_area_dataframe = self.__dataframe[
            (self.__dataframe[str(self.category.BALL_X)] <= self.__penalty_x_limits[0]) & 
            (self.__dataframe[str(self.category.BALL_X)] >= self.__penalty_x_limits[1]) & 
            (abs(self.__dataframe[str(self.category.BALL_Y)]) <= self.__penalty_y_limit) &
            (self.__dataframe[str(self.category.PLAYMODE)] == 'play_on')
        ]
        
        self.__cycles_inside = inside_penalty_area_dataframe.shape[0]

    def results(self):
        return self.__cycles_inside

    def describe(self):
        print(f'{self.__cycles_inside} cycles inside penalty area')

    def serialize(self):
        raise NotImplementedError
