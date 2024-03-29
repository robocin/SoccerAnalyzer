from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.geometric.point import Point
from socceranalyzer.utils.logger import Logger


class FoulCharge(AbstractAnalysis):
    """
        Used to calculate faults committed by both teams and the positions where they happened.

        Attributes
        ----------
            private:
                dataframe : pandas.Dataframe
                    match's log to be analyzed
                category : enum
                    match's category (2D, VSS or SSL)
                team_left_charges : list[Point]
                    list containing tuples relative to the positions (x and y) where faults committed by the left team
                    happened
                team_right_charges : list[Point]
                    list containing tuples relative to the positions (x and y) where faults committed by the right team
                    happened

        Methods
        -------
            private:
                quantity() -> (int, int)
                    returns a tuple containing how many faults left and right team committed, respectively
                proportion() -> (float, float)
                    returns a tuple containing the proportion of faults committed by left and right team, respectively 
                _analyze() -> None
                    for every cycle in the log, investigates wether a fault happened and updates one of the lists if 
                    it is really the case.

            public:
                results(side: str, tuple: bool) -> (list[Point], list[Point]) or list[Point]
                    returns the positions of fouls charges
                describe() -> None
                    provides how many faults each team committed and their proportions relative to the total.
    """
    def __init__(self, dataframe, category, debug):
        self.__dataframe = dataframe
        self.__category = category
        self.__team_left_charges = []
        self.__team_right_charges = []

        try:
            self._analyze()
        except Exception as err:
            Logger.error(f"FoulCharge failed: {err.args[0]}")
            if debug:
                raise
        else:
            Logger.success("FoulCharge has results.")

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
        """
            Returns
            -------
            tuple
                a tuple containing how many faults left and right team committed, respectively
        """
        return (len(self.__team_left_charges), len(self.__team_right_charges))

    def proportion(self):
        """
            Returns
            -------
            tuple
                a tuple containing the proportion of faults committed by left and right team, respectively
        """
        quantities = self.quantity()
        total = quantities[0] + quantities[1]

        return (quantities[0] / total, quantities[1] / total)

    def _analyze(self):
        for i in range(len(self.__dataframe)):
            """
                For every cycle in the log, investigates wether a fault happened and updates one of the lists if 
                it is really the case.
            """
            if (self.__dataframe.loc[i, str(self.category.PLAYMODE)] == str(self.category.FAULT_COMMITED_L)
                    and self.__dataframe.loc[i - 1, str(self.category.PLAYMODE)] != str(
                        self.category.FAULT_COMMITED_L)):

                self.left_charges = Point(int(self.__dataframe.loc[i, str(self.category.BALL_X)]),
                                          int(self.__dataframe.loc[i, str(self.category.BALL_Y)]))

            elif (self.__dataframe.loc[i, str(self.category.PLAYMODE)] == str(self.category.FAULT_COMMITED_R)
                  and self.__dataframe.loc[i - 1, str(self.category.PLAYMODE)] != str(self.category.FAULT_COMMITED_R)):

                self.right_charges = Point(int(self.__dataframe.loc[i, str(self.category.BALL_X)]),
                                           int(self.__dataframe.loc[i, str(self.category.BALL_Y)])) 
        

    def results(self, side=None, tuple=False):
        """
            Returns the positions of fouls charges.

            If no side is given, returns information for both sides.

            If tuple is set to true, returns a tuple containing left and right teams charges, respectively.

            Parameters
            ----------
            side: str, optional
                Specific team to be analyzed (default is None).

            tuple: bool, optional
                Wether the result should be a tuple containing both teams' information (default is False).

            Returns
            -------
            tuple
                a tuple containing both teams charges, if tuple parameter is set to True.

            list
                a list containing charges from the team given in side parameter, or from both if none was given.
        """
        all_positions = []
        if tuple:
            return (self.__team_left_charges, self.__team_right_charges)
        else:
            if side is not None:
                if side.lower()[0] == "l":
                    for p in self.__team_left_charges:
                        all_positions.append((p.x, p.y))
                elif side.lower()[0] == "r":
                    for p in self.__team_right_charges:
                        all_positions.append((p.x, p.y))
            else:
                for p in self.__team_left_charges:
                    all_positions.append((p.x, p.y))
                for p in self.__team_right_charges:
                    all_positions.append((p.x, p.y))

        return all_positions

    def describe(self):
        """
            Provides how many faults each team committed and their proportions relative to the total.
        """
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