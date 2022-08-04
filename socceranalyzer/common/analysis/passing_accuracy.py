from socceranalyzer.common.basic.match import Match

from socceranalyzer.common.evaluators.passing import Passing
from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.basic.team import Team


class PassingAccuracy(AbstractAnalysis):
    """
        Used to calculate the passing accuracy of the game.

        PassingAccuracy(data_frame: pandas.DataFrame, category: SIM2D | VSS | SSL, passing_evaluator: socceranalyzer.common.evaluators.Passing)

        Attributes
        ----------
            private: 
                passing_accuracy: dict[str, dict[str, Any]]
                    Contains passing stats of the teams
            
            public through @properties:
                dataframe: pandas.DataFrame
                    match's log
                category: SSL | SIM2D | VSS
                    match's category

        Methods
        -------
            private: 
                analyze() -> None:
                    Calculates all wrong and correct passes occurrences
            public: 
                results() -> (float, float)
                    Returns the teams passing accuracy and total passes 
                describe() -> none  
                    Shows the teams respective passing accuracy and total passes
                serialize() -> dict[str, dict[str, Any]]
                    Returns an object containing computed stats
    """
    def __init__(self, match : Match, passing_evaluator: Passing):
        super().__init__(match)
        self.__passing_accuracy = {}
        self.__passing_evaluator = passing_evaluator

        self._analyze()

    def __str__(self):
        values = self.results()
        return f'Team left: {values[0]}\nTeam right: {values[1]}'

    @property
    def category(self):
        return self._category
    
    @property
    def dataframe(self):
        return self._dataframe

    def _analyze(self):
        """
        Performs match passing accuracy analysis.
        """
        self.__passing_evaluator.run_passing_evaluation()
        self.__passing_accuracy = {
            'left_team': {
                'completed_passes': self.__passing_evaluator.left_team_passing_stats['completed_passes'],
                'total_passes': self.__passing_evaluator.left_team_passing_stats['total_passes'],
                'accuracy': self.__passing_evaluator.left_team_passing_stats['accuracy']
            },
            'right_team': {
                'completed_passes': self.__passing_evaluator.right_team_passing_stats['completed_passes'],
                'total_passes': self.__passing_evaluator.right_team_passing_stats['total_passes'],
                'accuracy': self.__passing_evaluator.right_team_passing_stats['accuracy']
            }
        }
    
    def results(self) -> tuple[float, float, int, int]:
        """
        Returns match passing accuracy stats.
            
            Returns:
                tuple (float, float, int, int): left team passing accuracy, right team passing accuracy left team total passes, right team total passes.
        """
        return (self.__passing_accuracy['left_team']['accuracy'], self.__passing_accuracy['right_team']['accuracy'], 
                self.__passing_accuracy['left_team']['total_passes'], self.__passing_accuracy['right_team']['total_passes'])

    def describe(self):        
        """
        Shows a teams' passing stats.
        """
        name_l = self.dataframe.loc[1, str(self.category.TEAM_LEFT)]
        name_r = self.dataframe.loc[1, str(self.category.TEAM_RIGHT)]
        print(f'{name_l}: acurácia = {self.__passing_accuracy["left_team"]["accuracy"]:.4f}    passes totais = {self.__passing_accuracy["left_team"]["total_passes"]}\n' 
                f'{name_r}: acurácia = {self.__passing_accuracy["right_team"]["accuracy"]:.4f}    passes totais = {self.__passing_accuracy["right_team"]["total_passes"]}')

    def serialize(self):
        """
        Returns computed passing accuracy stats for both teams.

                Returns:
                        passing_accuracy (dict[str, dict[str, Any]]): Overall teams' passing stats.
        """
        return self.__passing_accuracy
