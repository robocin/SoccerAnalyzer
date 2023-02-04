import pandas as pd
from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.evaluators.passing import Passing
from socceranalyzer.common.basic.match import Match
from socceranalyzer.logger import Logger

class InterceptCounter(AbstractAnalysis):
    def __init__(self, match: Match, passing_evaluator: Passing, debug):
        self.__match: Match = match
        self.__category = match.category
        self.__current_game_log: pd.DataFrame = match.dataframe
        self.__passing_evaluator = passing_evaluator

        self.__interceptions = {}

        try:
            self._analyze()
        except Exception as err:
            Logger.error(f"InterceptCounter failed: {err.args[0]}")
            if debug:
                raise
        else:
            Logger.success("InterceptCounter has results.")

    def __str__(self):
        values = self.results()
        return f'Team left: {values[0]}\nTeam right: {values[1]}'

    @property
    def category(self): return self.__category

    @property
    def dataframe(self): return self.__current_game_log

    def _analyze(self):
        self.__passing_evaluator.run_passing_evaluation()
        self.__interceptions = {
            'left_team': self.__passing_evaluator.left_team_passing_stats['interceptions'],
            'right_team': self.__passing_evaluator.right_team_passing_stats['interceptions']
        }

    def results(self):
        return (self.__interceptions['left_team'], self.__interceptions['right_team'])

    def describe(self):
        name_l = self.__match.team_left.name
        name_r = self.__match.team_right.name
        left_team = 'left_team'
        right_team = 'right_team'

        print(f'{name_l}: {self.__interceptions[left_team]}\n' 
                f'{name_r}: {self.__interceptions[right_team]}')

    def serialize(self):
        return self.__interceptions
