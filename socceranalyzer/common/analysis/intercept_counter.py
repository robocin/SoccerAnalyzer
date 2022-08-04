import pandas as pd
from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.evaluators.passing import Passing
from socceranalyzer.common.basic.match import Match

class InterceptCounter(AbstractAnalysis):
    def __init__(self, match : Match, passing_evaluator: Passing):
        super().__init__(match)
        self.__passing_evaluator = passing_evaluator

        self.__interceptions = {}

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
        self.__passing_evaluator.run_passing_evaluation()
        self.__interceptions = {
            'left_team': self.__passing_evaluator.left_team_passing_stats['interceptions'],
            'right_team': self.__passing_evaluator.right_team_passing_stats['interceptions']
        }

    def results(self):
        return (self.__interceptions['left_team'], self.__interceptions['right_team'])

    def describe(self):
        name_l = self._match.team_left.name
        name_r = self._match.team_right.name
        left_team = 'left_team'
        right_team = 'right_team'

        print(f'{name_l}: {self.__interceptions[left_team]}\n' 
                f'{name_r}: {self.__interceptions[right_team]}')

    def serialize(self):
        return self.__interceptions
