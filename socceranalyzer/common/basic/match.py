import pandas

from socceranalyzer.common.entity.team import Team
from socceranalyzer.common.enums.vss import VSS
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.enums.ssl import SSL

from socceranalyzer.common.basic.field import Field
from socceranalyzer.common.entity.ball import Ball
from socceranalyzer.common.entity.team import Team
from socceranalyzer.common.entity.agent import Agent


from socceranalyzer.common.chore.builder import Builder


class Match:
    """
        A class that represents a soccer match and its core components such as
        players, fouls, corners, etc

        Match(dataframe: pandas.DataFrame, category: enum)

        Attributes
        ----------
            public through @properties:
                df: dataframe
                    the pandas object that contains the game data
                teams: tuple
                    a immutable object with the name of both teams
                score_left: int
                    a integer value with the final score of the left team
                score_right: int
                    a integer value with the final score of the right team
                winning_team: string
                    a string with the name of the team that won the game
                losing_team: string
                    a string with the name of the team that lost the game
                players_left: list[Agent]
                    a list of players objects from the left team
                player_right: list[Agent]
                    a list of players objects from the right team
                ball: Ball
                    the game's ball object
                fouls: [int]
                    a list with integers referencing the cycle of foul occurrences
                goals: [int]
                    a list with integers referencing the cycle of goals occurrences
                corners: [int]
                    a list with integers referencing the cycle of corners occurrences



    """
    def __init__(self, dataframe: pandas.DataFrame, category: SIM2D | SSL | VSS):
        self.__category = category

        self.__df = dataframe
        self.__score_left: int = None
        self.__score_right: int = None
        self.__winning_team: str = ""
        self.__losing_team: str = ""

        self.__fouls = []
        self.__goals = []
        self.__corners = []

        try:
            if self.category is None:
                raise ValueError('A Match requires a Category as argument and none was given')
            elif self.category is VSS: 
                raise RuntimeError(f'This version of SoccerAnalyzer does not support {self.category} matches.\n'
                f'Please visit https://github.com/robocin/SoccerAnalyzer for more information.')
        except RuntimeError:
            raise
        else:
            builder = Builder(self.__df, self.__category)

            self.__field: Field = builder.fieldBuilder() 
            self.__ball: Ball = builder.ballBuilder()
            self.__team_left: Team = builder.teamBuilder('left')
            self.__team_right: Team = builder.teamBuilder('right')

            self.__players_left: list[Agent] = builder.playerBuilder(self.__team_left)
            self.__players_right: list[Agent] = builder.playerBuilder(self.__team_right)

            self.__teams = (self.__team_left, self.__team_right)

        


    @property
    def dataframe(self):
        return self.__df

    @property
    def category(self):
        return self.__category
    
    @property
    def field(self):
        return self.__field

    @property
    def teams(self):
        return self.__teams

    @teams.setter
    def teams(self, t):
        self.__teams = t

    @property
    def team_left(self):
        return self.__team_left

    @property
    def team_left_name(self):
        return self.__teams[0].name

    @property
    def team_right(self):
        return self.__team_right

    @property
    def team_right_name(self):
        return self.__teams[1].name

    @property
    def score_left(self):
        return self.__score_left

    @property
    def score_right(self):
        return self.__score_right

    @property
    def winning_team(self):
        return self.__winning_team

    @property
    def losing_team(self):
        return self.__losing_team

    @property
    def players_left(self):
        return self.__players_left

    @property
    def players_right(self):
        return self.__players_right

    @property
    def ball(self):
        return self.__ball

    @property
    def fouls(self):
        return self.__fouls

    @property
    def goals(self):
        return self.__goals

    @property
    def corners(self):
        return self.__corners

    def __build(self):
        """
            Runs when a Match objected is created to populate its attributes with the given dataframe.

            :return: None
        """
        try:
            if self.category is None:
                raise ValueError('A Match requires a Category as argument and none was given')
            elif self.category is VSS: 
                raise RuntimeError(f'This version of SoccerAnalyzer does not support {self.category} matches.\n'
                                   f'Please visit https://github.com/robocin/SoccerAnalyzer for more information.')
        except RuntimeError:
            raise
        else:
            team_l_name = self.__df.loc[1, str(self.category.TEAM_LEFT)]
            team_r_name = self.__df.loc[1, str(self.category.TEAM_RIGHT)]

            self.__teams = (Team(team_l_name, "left"), Team(team_r_name, "right"))
            self.__team_left_name = team_l_name
            self.__team_right_name = team_r_name
 
            last_line = self.__df.shape[0] - 1
            score_l = self.__df.loc[last_line, str(self.category.TEAM_LEFT_SCORE)]
            score_r = self.__df.loc[last_line, str(self.category.TEAM_RIGHT_SCORE)]

            self.__score_left = score_l
            self.__score_right = score_r

            if score_l > score_r:
                self.__winning_team = team_l_name
                self.__losing_team = team_r_name
            elif score_l < score_r:
                self.__winning_team = team_r_name
                self.__losing_team = team_l_name
            else:
                self.__winning_team = "draw"
                self.__losing_team = "draw"
