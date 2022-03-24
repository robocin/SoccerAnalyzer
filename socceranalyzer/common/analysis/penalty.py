from socceranalyzer.common.abstract.abstract_analysis import AbstractAnalysis


class Penalty(AbstractAnalysis):
    def __init__(self, dataframe, category):
        self.__dataframe = dataframe
        self.__category = category
        self.__penalty_left = []
        self.__penalty_right = []

        self._analyze()

    @property
    def category(self):
        return self.__category

    @property
    def dataframe(self):
        return self.__dataframe

    def _analyze(self):
        # penalty in favor of left side
        t_dataframe = self.dataframe[self.dataframe[str(self.category.PLAYMODE)] == self.category.PENALTY_TO_LEFT]
        self.__penalty_left = t_dataframe[str(self.category.GAME_TIME)].tolist()

        # penalty in favor of right side
        t_dataframe = self.dataframe[self.dataframe[str(self.category.PLAYMODE)] == str(self.category.PENALTY_TO_RIGHT)]
        self.__penalty_right = t_dataframe[str(self.category.GAME_TIME)].tolist()

    def results(self):
        return (self.__penalty_left, self.__penalty_right)

    def describe(self):
        print(f'This game had {len(self.__penalty_left) + len(self.__penalty_right)} penalties.\n')

    def serialize(self):
        raise NotImplementedError
