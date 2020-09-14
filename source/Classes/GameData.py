

class GameData():
    def __init__(self):
        self.__dataframe = None
        self.__goals = [] # all goals scored
        self.__fouls = [] # all fouls scored
        self.__events = [] # [goals, fouls]
        self.__ball = None # a ball class
        self.__teams = [] # teams[0] is team_l and teams[1] is team_r
        self.__players = [] # all players, starting with the ones from the team_l

    def set_dataframe(self, x):
        self.__dataframe = x
    def set_goals(self, x):
        self.__goals = x
    def set_fouls(self, x):
        self.__fouls = x
    def set_events(self, x):
        self.__events = x
    def set_ball(self, x):
        self.__ball = x
    def set_teams(self, x):
        self.__teams = x
    def set_players(self, x):
        self.__players = x

    def get_dataframe(self):
        return self.__dataframe
    def get_goals(self):
        return self.__goals
    def get_fouls(self):
        return self.__fouls
    def get_events(self):
        return self.__events
    def get_ball(self):
        return self.__ball
    def get_teams(self):
        return self.__teams
    def get_team(self, i):
        return self.__teams[i]
    def get_players(self):
        return self.__players