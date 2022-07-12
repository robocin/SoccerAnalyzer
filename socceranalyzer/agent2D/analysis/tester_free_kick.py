from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.utility import Utility


class TesterFK(AbstractAnalysis):
    def __init__(self, dataframe, category):
        self.__dataframe = dataframe
        self.__category = category

        # left team stats
        self.__free_kicks_l = 0
        self.__goals_taken_l = 0
        self.__goals_scored_l = 0

        # right team stats
        self.__free_kicks_r = 0
        self.__goals_taken_r = 0
        self.__goals_scored_r = 0

        self._analyze()

    def _analyze(self):
        free_kicks_to_left = Utility.find_last_unique_event_ocurrences(self.dataframe, str(self.category.FK_LEFT))
        free_kicks_to_right = Utility.find_last_unique_event_ocurrences(self.dataframe, str(self.category.FK_RIGHT))

        self.__free_kicks_l = len(free_kicks_to_left)
        self.__free_kicks_r = len(free_kicks_to_right)

        last_df_line = self.dataframe.shape[0] - 1

        self.__goals_taken_l = self.dataframe.loc[last_df_line, str(self.category.TEAM_RIGHT_SCORE)]
        self.__goals_scored_l = self.dataframe.loc[last_df_line, str(self.category.TEAM_LEFT_SCORE)]

        self.__goals_taken_r = self.__goals_scored_l
        self.__goals_scored_r = self.__goals_taken_l

    @property
    def dataframe(self):
        return self.__dataframe

    @property
    def category(self):
        return self.__category

    def results(self):
        return ((self.__goals_taken_l, self.__goals_scored_l, self.__free_kicks_l,
                 self.__goals_scored_l/self.__free_kicks_l, self.__goals_taken_l/self.__free_kicks_r),
                (self.__goals_taken_r, self.__goals_scored_r, self.__free_kicks_r,
                 self.__goals_scored_r/self.__free_kicks_r, self.__goals_taken_r/self.__free_kicks_l))

    def describe(self):
        team_l_name = self.dataframe.loc[0, str(self.category.TEAM_LEFT)]
        team_r_name = self.dataframe.loc[0, str(self.category.TEAM_RIGHT)]

        print(f'{team_l_name}:\n'
              f'    goals taken: {self.__goals_taken_l}\n'
              f'    goals scored: {self.__goals_scored_l}\n'
              f'    free_kicks: {self.__free_kicks_l}\n'
              f'    scored/fk_in_favor ratio {self.__goals_scored_l/self.__free_kicks_l}\n'
              f'    taken/fk_against ratio: {self.__goals_taken_l/self.__free_kicks_r}')

        print(f'{team_r_name}:\n'
              f'    goals taken: {self.__goals_taken_r}\n'
              f'    goals scored: {self.__goals_scored_r}\n'
              f'    free_kicks: {self.__free_kicks_r}\n'
              f'    scored/fk_in_favor ratio {self.__goals_scored_r/self.__free_kicks_r}\n'
              f'    taken/fk_against ratio: {self.__goals_taken_r/self.__free_kicks_l}')

    def serialize(self):
        raise NotImplementedError
