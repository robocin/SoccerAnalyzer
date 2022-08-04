from socceranalyzer.common.basic.match import Match
from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis


class Penalty(AbstractAnalysis):
    """
        Used to calculate how many penalties each team had in their favor and the moments they happened

        Attributes
        ----------
            private:
                penalty_left : list[int]
                    list containing every moment when left team had a penalty in their favor
                penalty_right : list[int]
                    list containing every moment when right team had a penalty in their favor

            public through @properties:
                dataframe : pandas.Dataframe
                    match's log to be analyzed
                category : enum
                    match's category (2D, VSS or SSL)

        Methods
        -------
            private:
                _analyze() -> None
                    finds every penalty in the match and appends each one to the respective team's list

            public:
                results() -> (list[int], list[int])
                    returns the moments when left and right team had penalties in their favor, respectively
                describe() -> None
                    provides how many penalties happened in the match
    """
    def __init__(self, match : Match):
        super().__init__(match)
        self.__penalty_left = []
        self.__penalty_right = []

        self._analyze()

    @property
    def category(self):
        return self._category

    @property
    def dataframe(self):
        return self._dataframe

    def _analyze(self):
        """
            Finds every penalty in the match and appends each one to the respective team's list.
        """
        # penalty in favor of left side
        t_dataframe = self.dataframe[self.dataframe[str(self.category.PLAYMODE)] == self.category.PENALTY_TO_LEFT]
        self.__penalty_left = t_dataframe[str(self.category.GAME_TIME)].tolist()

        # penalty in favor of right side
        t_dataframe = self.dataframe[self.dataframe[str(self.category.PLAYMODE)] == str(self.category.PENALTY_TO_RIGHT)]
        self.__penalty_right = t_dataframe[str(self.category.GAME_TIME)].tolist()

    def results(self):
        """
            Returns the moments when left and right team had penalties in their favor, respectively.
        """
        return (self.__penalty_left, self.__penalty_right)

    def describe(self):
        """
            Provides how many penalties happened in the match.
        """
        print(f'This game had {len(self.__penalty_left) + len(self.__penalty_right)} penalties.\n')

    def serialize(self):
        raise NotImplementedError
