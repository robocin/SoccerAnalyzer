from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.basic.match import Match
from socceranalyzer.common.collections.collections import ThresholdCollection
from socceranalyzer.common.evaluators.ball_holder import BallHolderEvaluator


class TimeAfterEvents(AbstractAnalysis):
    def __init__(self, match : Match, corners, fouls=None, kick_ins=None):
        super().__init__(match)

        self.__threshold = ThresholdCollection()

        self.__corners_cycles = corners
        self.__time_after_corner = 0
        self.__corner_event_duration = 200

        self.__fouls_cycles = fouls
        self.__time_after_fouls = 0
        self.__fouls_event_duration = 200

        self.__kick_ins = kick_ins
        self.__time_after_kick_ins = 0
        self.__kick_ins_event_duration = 200

        self.__goals_scored_l = 0
        self.__goals_scored_r = 0

        self._analyze()

    @property
    def category(self):
        return self._category

    @property
    def dataframe(self):
        return self._dataframe

    @property
    def thr(self):
        return self.__threshold

    @property
    def corner_thr(self):
        return self.__threshold.corner_thr

    @corner_thr.setter
    def corner_thr(self, value: int):
        self.__threshold.corner_thr = value

    @property
    def kick_in_thr(self):
        return self.__threshold.kick_in_thr

    @kick_in_thr.setter
    def kick_in_thr(self, value: int):
        self.__threshold.kick_in_thr = value

    @property
    def foul_thr(self):
        return self.__threshold.foul_thr

    @foul_thr.setter
    def foul_thr(self, value: int):
        self.__threshold.foul_thr = value

    def _is_play_on(self, cycle):
        pm = self.dataframe.loc[cycle, str(self.category.PLAYMODE)]
        return True if pm == str(self.category.RUNNING_GAME) else False

    def _is_goal_scored(self, cycle):

        pm = self.dataframe.loc[cycle, str(self.category.PLAYMODE)]

        if pm == str(self.category.GOAL_SCORED_L):
            self.__goals_scored_l += 1
        elif pm == str(self.category.GOAL_SCORED_R):
            self.__goals_scored_r += 1

    def corner(self):
        event_duration = 200

        # corner to left team
        for c in self.__corners_cycles[0]:
            for i in range(c, c + event_duration):
                if self._is_play_on(i):
                    if BallHolderEvaluator(self.dataframe, self.category).at(i)[2] == "left":
                        self.__time_after_corner += 1
                    else:
                        self.corner_thr -= 1
                        if self.corner_thr >= 0:
                            self.__time_after_corner += 1
                else:
                    self._is_goal_scored(i)

        # corner to right team
        for c in self.__corners_cycles[1]:
            for i in range(c, c + event_duration):
                if self._is_play_on(i):
                    if BallHolderEvaluator(self.dataframe, self.category).at(i)[2] == "right":
                        self.__time_after_corner += 1
                    else:
                        self.corner_thr -= 1
                        if self.corner_thr >= 0:
                            self.__time_after_corner += 1
                else:
                    self._is_goal_scored(i)

    def _analyze(self):
        pass

    def results(self):
        pass

    def describe(self):
        pass

    def serialize(self):
        pass