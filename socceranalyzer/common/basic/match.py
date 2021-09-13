import pandas

from SoccerAnalyzer.socceranalyzer.common.entity.team import Team


class Match:
    def __init__(self, dataframe: pandas.DataFrame, category):
        self.__category = category

        self.__df = dataframe
        self.__teams = ()
        self.__team_left_name = ""
        self.__team_right_name = ""
        self.__score_left = None
        self.__score_right = None
        self.__winning_team = ""
        self.__losing_team = ""
        self.__players_left = []
        self.__players_right = []
        self.__ball = None

        self.__fouls = []
        self.__goals = []
        self.__corners = []

        self.__build()


    @property
    def dataframe(self):
        return self.__df

    @property
    def category(self):
        return self.__category

    @property
    def teams(self):
        return self.__teams

    @teams.setter
    def teams(self, tuple):
        self.__teams = tuple

    @property
    def team_left(self):
        return self.__teams[0]

    @property
    def team_left_name(self):
        return self.__teams[0].name

    @property
    def team_right(self):
        return self.__teams[1]

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
