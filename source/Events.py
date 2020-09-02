class Events():
    def __init__(self):
        self.__all_goals = []
        self.__all_fouls = []
        self.__all_penalties = []

    # setters and getters
    def set_all_goals(self, goals):
        self.__all_goals = goals
    def set_all_fouls(self, fouls):
        self.__all_fouls = fouls
    def set_all_penalties(self, penalties):
        self.__all_penalties = penalties

    def get_all_goals(self):
        return self.__all_goals
    def get_all_fouls(self):
        return self.__all_fouls
    def get_all_penalties(self):
        return self.__all_penalties