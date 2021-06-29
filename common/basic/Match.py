from AnalyzerCommon.common.entity.Team import Team


class Match:
    def __init__(self, dataFrame):

        # Initialization of variables #
        #   core vars
        self.__dataframe = dataFrame
        self.__teams = []  # teams[0] is team_l and teams[1] is team_r
        # self.__players = []  # all players, starting with the ones from the team_l
        # self.__ball = None  # a ball class
        # self.__events = []  # [goals, fouls]
        # self.__goals = []       # all goals scored
        # self.__fouls = []       # all fouls scored
        #   convenience vars
        # self.__teamLeftName = None
        # self.__teamRightName = None
        # self.__winningTeam = None
        # self.__losingTeam = None
        # self.__faultQuantity = 0
        # self.__cornerQuantity = 0
        # self.__penaltyQuantity = 0
        # self.__goalQuantity = 0

        # organize data #
        self.__setDataframe(self.__dataframe)
        self.__setTeams([Team("l", self.__dataframe), Team("r", dataFrame)])

        # self.__setTeamLeftName()
        # self.__setTeamRightName()

    # setters and getters #

    # set
    def __setDataframe(self, dataFrame):
        self.__dataframe = dataFrame

    # def __setTeamLeftName(self):
    #     self.__teamLeftName = str(self.__dataframe.iloc[0, 2])

    # def __setTeamRightName(self):
    #     self.__teamRightName = str(self.__dataframe.iloc[0, 3])

    # def __setGoals(self, x):
    #     self.__goals = x

    # def setFouls(self, x):
    #     self.__fouls = x

    # def __setEvents(self, x):
    #     self.__events = x
    #
    # def __setBall(self, x):
    #     self.__ball = x

    def __setTeams(self, x):
        self.__teams = x

    # get
    def getDataframe(self):
        return self.__dataframe

    # def getTeamLeftName(self) -> str:
    #     return self.__teamLeftName

    # def getTeamRightName(self) -> str:
    #     return self.__teamRightName

    # def getEvents(self):
    #     return self.__events

    # def getBall(self):
    #     return self.__ball

    def get_teams(self):
        return self.__teams

    def get_team(self, arg):
        if type(arg) == str:
            if arg == "l":
                return self.__teams[0]
            elif arg == "r":
                return self.__teams[1]
        elif type(arg) == int:
            return self.__teams[arg]

    # def get_players(self):
    #     return self.__players
