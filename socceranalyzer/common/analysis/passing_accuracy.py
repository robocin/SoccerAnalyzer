from socceranalyzer.common.evaluators.passing import Passing
from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis

class PassingAccuracy(AbstractAnalysis):
    """
        Used to calculate the passing accuracy of the game.
        PassingAccuracy(pandas.DataFrame)
        Attributes
        ----------
            private: 
                left_team_passing_accuracy : float
                    The accuracy percentage of the left team
                right_team_passing_accuracy : float
                    The accuracy percentage of the right team   
                left_team_total_passes : float
                    The total number of passes of the left team 
                right_team_passing_accuracy : float
                    The total number of passes of the right team 

        Methods
        -------
            private: 
                analyze() -> None:
                    Calculates all wrong and correct passes occurrences
            public: 
                results() -> (float, float)
                    returns the teams passing accuracy and total passes 
                describe() -> none  
                    Shows the teams respective passing accuracy and total passes
    """


    def __init__(self, data_frame, category, passing_evaluator: Passing):
        self.__passing_accuracy = {}
        self.__category = category
        self.__current_game_log = data_frame
        self.__passing_evaluator = passing_evaluator

        self._analyze()

    def __str__(self):
        values = self.results()
        return f'Team left: {values[0]}\nTeam right: {values[1]}'

    @property
    def category(self):
        return self.__category

    def _analyze(self):
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
    
    def results(self):
        return (self.__passing_accuracy['left_team']['accuracy'], self.__passing_accuracy['right_team']['accuracy'], 
                self.__passing_accuracy['left_team']['total_passes'], self.__passing_accuracy['right_team']['total_passes'])

    def describe(self):
        name_l = self.__current_game_log.loc[1, str(self.category.TEAM_LEFT)]
        name_r = self.__current_game_log.loc[1, str(self.category.TEAM_RIGHT)]
        print(f'{name_l}: acurácia = {self.__passing_accuracy["left_team"]["accuracy"]:.4f}    passes totais = {self.__passing_accuracy["left_team"]["total_passes"]}\n' 
                f'{name_r}: acurácia = {self.__passing_accuracy["right_team"]["accuracy"]:.4f}    passes totais = {self.__passing_accuracy["right_team"]["total_passes"]}')

    def serialize(self):
        return self.__passing_accuracy
