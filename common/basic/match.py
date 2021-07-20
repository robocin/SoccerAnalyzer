from ..entity.team import Team

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
        # self.__setTeamLeftName()
        # self.__setTeamRightName()

        self.__build()


    @property
    def dataframe(self):
        return self.__dataframe

    @property
    def team_left(self):
        return self.__teams[0]

    @property
    def team_right(self):
        return self.__teams[1]

    def __build(self):
        self.__teams.append(Team("RobôCIn", "left"))
        self.__teams.append(Team("Outro", "right"))
