import pandas
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.enums.ssl import SSL
from socceranalyzer.common.enums.vss import VSS

class FindGoals:
    """
        Used to verify at which moments goals happened.

        GoalReplay(dataframe: pandas.DataFrame, category: enum)

        Attributes
        ----------
            private:
                dataframe: pandas.DataFrame
                    match's log
                category: SSL | SIM2D | VSS
                    match's category
                cycles: int
                    number of cycles to be analyzed before the occurrence of each goal
                goal_moments: [int]
                    a list containing dataframe's indexes of moments where goals happened
                
        Methods
        -------
            private:
                analyze() -> None
                    Finds out at which cycles a goal happened and populates goal_moments.
                    
            public:
                results() -> [int]
    """

    def __init__(self, dataframe: pandas.DataFrame, category: SSL | SIM2D | VSS) -> None:
        self.__dataframe = dataframe
        self.__category = category
        self.__goal_moments = []

        self._analyze()

    def _analyze(self) -> None:
        """
            Finds out at which cycles a goal happened and populates goal_moments.
        """
        filtered_dataframe = self.__dataframe.loc[(self.__dataframe[str(self.__category.PLAYMODE)] == str(self.__category.GOAL_SCORED_L)) |
                                                (self.__dataframe[str(self.__category.PLAYMODE)] == str(self.__category.GOAL_SCORED_R))]
        
        for index, row in filtered_dataframe.iterrows():
            if (self.__dataframe.iloc[index - 1][str(self.__category.PLAYMODE)] != row[str(self.__category.PLAYMODE)]):
                # Goal happened
                self.__goal_moments.append(index)

    def results(self) -> list:
        """
            Returns:
                    [int]: dataframe's indexes of moments where goals happened
        """
        return self.__goal_moments
