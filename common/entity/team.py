from .player import Player

class Team:
    def __init__(self, name: str = None, side: str = None):
        """
        :param side: "l" for left or "r" for right side of the soccer field
        """

        # Initialization of variables #
        #   core vars
        self.__name = name
        # self.__color = None
        self.__side = side
        self.__players = []
        # self.__goals_scored = []
        # self.__free_kicks = []
        # self.__fouls_commited = []
        # self.__fouls_received = []
        # self.__penalties_shot = []
        # self.__penalties_received = []
        # self.__seen_on = []

        #   convenience vars
        # self.__number_of_goals_scored = 0
        # self.__number_of_free_kicks = 0
        # self.__number_of_fouls_commited = 0
        # self.__penalties_scored = []

        # organize data #
        #self.set_name(dataframe[f"team_name_{side}"][0].lower())

    """        players_list = []
        for i in range(0, 11):
            players_list.append(Player(team_name=self.get_name(), team_side=side, player_id=i+1, dataframe=dataframe))
        self.set_players(players_list)
    """

    # setters and getters #

    @property
    def name(self):
        return self.__name

    # def set_color(self, color):
    #     self.__color = color

    # def set_side(self, side):
    #     self.__side = side

    # def set_goals_scored(self, goals_scored):
    #     self.__goals_scored = goals_scored

    # def set_penalties_scored(self, penalties_scored):
    #     self.__penalties_scored = penalties_scored

    # def set_number_of_goals_scored(self, number_of_goals_scored):
    #     self.__number_of_goals_scored = number_of_goals_scored

    # def set_free_kicks(self, free_kicks):
    #     self.__free_kicks = free_kicks

    # def set_number_of_free_kicks(self, number_of_free_kicks):
    #     self.__number_of_free_kicks = number_of_free_kicks

    # def set_fouls_commited(self, faults_commited):
    #     self.__fouls_commited = faults_commited

    # def set_number_of_fouls_commited(self, number_of_fouls_commited):
    #     self.__number_of_fouls_commited = number_of_fouls_commited

    # def set_penalties_commited(self, penalties_commited):
    #     self.__penalties_commited = penalties_commited

    def set_players(self, players):
        self.__players = players

    # def append_goal(self, goal):
    #     self.__goals_scored.append(goal)

    # def set_seen_on(self, sen_on):
    #     self.__seen_on = seen_on

    # def set_substitutions(self, substitutions):
    #     self.__substitutions = substitutions

    # get

    def get_name(self):
        return self.__name

    # def get_color(self):
    #     return self.__color

    def get_side(self):
        return self.__side

    # def get_goals_scored(self):
    #     return self.__goals_scored

    # def get_penaltis_scored(self):
    #     return self.__penaltis_scored

    # def get_number_of_goals_scored(self):
    #     return self.__number_of_goals_scored

    # def get_free_kicks(self):
    #     return self.__free_kicks

    # def get_number_of_free_kicks(self):
    #     return self.__number_of_free_kicks

    # def get_fouls_commited(self):
    #     return self.__fouls_commited

    # def get_number_of_fouls_commited(self):
    #     return self.__number_of_fouls_commited

    # def get_penaltis_commited(self):
    #     return self.__penaltis_commited

    def get_players(self):
        return self.__players

    # def get_substitutions(self):
    #     return self.__substitutions

    def get_player(self, playerId):
        return self.__players[playerId-1]
