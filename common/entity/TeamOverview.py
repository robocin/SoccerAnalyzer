import json


class TeamOverview:
    def __init__(self, dataframe, team_name):
        self.__dataframe = dataframe
        self.__name = team_name
        self.__mean_stamina_for_each_game = None

        # organize data
        stamina_from_dataframe = list(dataframe["mean_stamina"])
        if type(stamina_from_dataframe[0]) == float or type(stamina_from_dataframe[0]) == int:
            stamina_from_dataframe = [stamina_from_dataframe]
        elif type(stamina_from_dataframe[0]) == str:
            stamina_from_dataframe[0] = json.loads(stamina_from_dataframe[0])
        self.__set_mean_stamina_for_each_match(stamina_from_dataframe)

    # setters and getters #

    # set
    def __set_mean_stamina_for_each_match(self, mean_stamina: list):
        self.__mean_stamina_for_each_game = mean_stamina

    # get
    def get_team_name(self):
        return self.__name

    def get_mean_stamina_for_each_match(self):
        return self.__mean_stamina_for_each_game
