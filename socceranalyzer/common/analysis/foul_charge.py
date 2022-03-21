from socceranalyzer.common.abstract.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.geometric.point import Point


class FoulCharge(AbstractAnalysis):
    def __init__(self, dataframe=None, category=None):
        self.__dataframe = dataframe
        self.__category = category
        self.__team_left_charges = []
        self.__team_right_charges = []

        self._analyze()

    @property
    def left_charges(self):
        return self.__team_left_charges

    @property
    def category(self):
        return self.__category

    @property
    def dataframe(self):
        return self.__dataframe

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

        return (quantities[0] / total, quantities[1] / total)

    def _analyze(self):
        for i in range(len(self.__dataframe)):
            if (self.__dataframe.loc[i, str(self.category.PLAYMODE)] == str(self.category.FAULT_COMMITED_L)
                    and self.__dataframe.loc[i - 1, str(self.category.PLAYMODE)] != str(
                        self.category.FAULT_COMMITED_L)):

                self.left_charges = Point(int(self.__dataframe.loc[i, str(self.category.BALL_X)]),
                                          int(self.__dataframe.loc[i, str(self.category.BALL_Y)]))

            elif (self.__dataframe.loc[i, str(self.category.PLAYMODE)] == str(self.category.FAULT_COMMITED_R)
                  and self.__dataframe.loc[i - 1, str(self.category.PLAYMODE)] != str(self.category.FAULT_COMMITED_R)):

                self.right_charges = Point(int(self.__dataframe.loc[i, str(self.category.BALL_X)]),
                                           int(self.__dataframe.loc[i, str(self.category.BALL_X)]))

    def results(self, side=None, tuple=False):
        all_positions = []
        if tuple:
            return (self.__team_left_charges, self.__team_right_charges)
        else:
            if side is not None:
                if side.lower()[0] == "l":
                    for p in self.__team_right_charges:
                        all_positions.append((p.x, p.y))
                elif side.lower()[0] == "r":
                    for p in self.__team_right_charges:
                        all_positions.append((p.x, p.y))
            else:
                for p in self.__team_right_charges:
                    all_positions.append((p.x, p.y))
                for p in self.__team_right_charges:
                    all_positions.append((p.x, p.y))

        return all_positions

    def describe(self):
        name_l = self.dataframe.loc[1, str(self.category.TEAM_LEFT)]
        name_r = self.dataframe.loc[1, str(self.category.TEAM_RIGHT)]
        print(f'{name_l} commited {len(self.__team_left_charges)} faults against {name_r}.\n'
              f'That is {self.proportion()[0]*100}% of the total.'
              f'To see the x and y positions use results(side)\n'
              f'------------------------------------------------------------------------------------')
        print(f'{name_r} commited {len(self.__team_right_charges)} faults against {name_l}.\n'
              f'That is {self.proportion()[1]*100}% of the total\n'
              f'To see the x and y positions use results(side)\n')

        print(f'The game had a total of {len(self.__team_left_charges) + len(self.__team_right_charges)}')

    def serialize(self):
        raise NotImplementedError