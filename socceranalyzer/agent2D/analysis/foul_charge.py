from SoccerAnalyzer.socceranalyzer.common.abstract.abstract_analysis import AbstractAnalysis
from SoccerAnalyzer.socceranalyzer.common.geometric.point import Point

class FoulCharge(AbstractAnalysis):
    def __init__(self, dataframe=None):
        self.__dataframe = dataframe
        self.__ball_x_row = 10
        self.__ball_y_row = 11
        self.__team_left_charges = []
        self.__team_right_charges = []
        self._analyze()

    @property
    def ball_x(self):
        return self.__ball_x_row

    @ball_x.setter
    def ball_x(self, val: int):
        self.__ball_x_row = val

    @property
    def ball_y(self):
        return self.__ball_y_row

    @ball_y.setter
    def ball_y(self, val: int):
        self.__ball_y_row = val

    @property
    def left_charges(self):
        return self.__team_left_charges

    @left_charges.setter
    def left_charges(self, val: Point):
        self.__team_left_charges.append(val)

    @property
    def right_charges(self):
        return self.__team_right_charges

    @right_charges.setter
    def right_charges(self, val: Point):
        self.__team_right_charges.append(val)

    def quantity(self):
        return (len(self.__team_left_charges), len(self.__team_right_charges))

    def proportion(self):
        quantities = self.quantity()
        total = quantities[0] + quantities[1]

        return (quantities[0]/total, quantities[1]/total)

    def _analyze(self):
        for i in range(len(self.__dataframe)):
            if (self.__dataframe.iloc[i, 1] == "foul_charge_l" and self.__dataframe.iloc[i - 1, 1] != "foul_charge_l"):

                self.left_charges = Point(int(self.__dataframe.iloc[i, self.ball_x]),
                                          int(self.__dataframe.iloc[i, self.ball_y]))

            elif (self.__dataframe.iloc[i, 1] == "foul_charge_r" and self.__dataframe.iloc[i - 1, 1] != "foul_charge_r"):

                self.right_charges = Point(int(self.__dataframe.iloc[i, self.ball_x]),
                                           int(self.__dataframe.iloc[i, self.ball_y]))


    def results(self):
        return (self.left_charges, self.right_charges)
