import pandas
from socceranalyzer.common.basic.match import Match
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.enums.ssl import SSL
from socceranalyzer.common.enums.vss import VSS
from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis


class FindGoals(AbstractAnalysis):
    """
        Used to verify at which moments goals happened.
        GoalReplay(match)
        Attributes
        ----------
            private:
                cycles: int
                    number of cycles to be analyzed before the occurrence of each goal
                goal_moments: [int]
                    a list containing dataframe's indexes of moments where goals happened
                left_team_goals: [int]
                    a list containing dataframe's indexes of moments where left team goals happened
                right_team_goals: [int]
                    a list containing dataframe's indexes of moments where right team goals happened
            
            public through @properties:
                dataframe: pandas.DataFrame
                    match's log
                category: SSL | SIM2D | VSS
                    match's category
        Methods
        -------
            private:
                analyze() -> None
                    Finds out at which cycles a goal happened and populates goal_moments.
                    
            public:
                results() -> [int]
    """

    def __init__(self, match : Match) -> None:
        super().__init__(match)
        self.__goal_moments = []
        self.__left_team_goals = []
        self.__right_team_goals = []

        self._analyze()
    
    @property
    def dataframe(self):
        return self._dataframe

    @property
    def category(self):
        return self._category

    def _analyze(self) -> None:
        """
            Finds out at which cycles a goal happened and populates goal_moments.
        """
        filtered_dataframe = self.dataframe.loc[(self.dataframe[str(self.category.PLAYMODE)] == str(self.category.GOAL_SCORED_L)) |
                                                (self.dataframe[str(self.category.PLAYMODE)] == str(self.category.GOAL_SCORED_R))]
        
        for index, row in filtered_dataframe.iterrows():
            if (self.dataframe.iloc[index - 1][str(self.category.PLAYMODE)] != row[str(self.category.PLAYMODE)]):
                # Goal happened
                self.__goal_moments.append(index)

                if (row[str(self.category.PLAYMODE)] == str(self.category.GOAL_SCORED_L)):
                    self.__left_team_goals.append(index)

                else:
                    self.__right_team_goals.append(index)

    def results(self, team: str = None) -> list:
        """
            Parameters:
                    goal_number (optional) ("left" | "right"): Team's goals to be returned. By default it returns results from both.
            
            Returns:
                    [int]: dataframe's indexes of moments where goals happened
        """
        if (team == None):
            return self.__goal_moments
        
        elif (team == "left"):
            return self.__left_team_goals
        
        elif (team == "right"):
            return self.__right_team_goals
    
    def describe(self):
        print("No description available")
    
    def serialize(self):
        raise NotImplementedError