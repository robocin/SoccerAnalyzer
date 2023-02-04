from socceranalyzer.common.evaluators.passing import Passing
from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.basic.team import Team
from socceranalyzer.logger import Logger


class PassingAccuracy(AbstractAnalysis):
    """
        Used to calculate the passing accuracy of the game.

        PassingAccuracy(data_frame: pandas.DataFrame, category: SIM2D | VSS | SSL, passing_evaluator: socceranalyzer.common.evaluators.Passing)

        Attributes
        ----------
            private: 
                passing_accuracy: dict[str, dict[str, Any]]
                    Contains passing stats of the teams

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
    def __init__(self, data_frame, category, passing_evaluator: Passing, debug):
        self.__passing_accuracy = {}
        self.__category = category
        self.__current_game_log = data_frame
        self.__passing_evaluator = passing_evaluator

        try:
            self._analyze()
        except Exception as err:
            Logger.error(f"PassingAccuracy failed: {err.args[0]}")
            if debug:
                raise
        else:
            Logger.success("PassingAccuracy has results.")

    def __str__(self):
        values = self.results()
        return f'Team left: {values[0]}\nTeam right: {values[1]}'

    @property
    def category(self):
        return self.__category

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
        name_l = self.__current_game_log.loc[1, str(self.category.TEAM_LEFT)]
        name_r = self.__current_game_log.loc[1, str(self.category.TEAM_RIGHT)]
        print(f'{name_l}: acurácia = {self.__passing_accuracy["left_team"]["accuracy"]:.4f}    passes totais = {self.__passing_accuracy["left_team"]["total_passes"]}\n' 
                f'{name_r}: acurácia = {self.__passing_accuracy["right_team"]["accuracy"]:.4f}    passes totais = {self.__passing_accuracy["right_team"]["total_passes"]}')

    def serialize(self):
        """
        Returns computed passing accuracy stats for both teams.

                Returns:
                        passing_accuracy (dict[str, dict[str, Any]]): Overall teams' passing stats.
        """
        return self.__passing_accuracy
