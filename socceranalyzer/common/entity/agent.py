class Agent:
    def __init__(self, team_name=None, team_side=None, number_id=None):
        self.__team_name = team_name
        self.__team_side = team_side
        self.__number_id = number_id
        self.__positions = []
        self.__stamina = []

    def __str__(self):
        pos_status = "EMPTY" if self.__positions == [] else "FILLED"
        sta_status = "EMPTY" if self.__stamina == [] else "FILLED"

        return "team_name: {}\nteam_side: {}\nnumber_id: {}\npositions is {}\nstamina is {}".format(self.__team_name,
                                                                                                    self.__team_side,
                                                                                                    self.__number_id,
                                                                                                    pos_status,
                                                                                                    sta_status)

    @property
    def team_name(self):
        return self.__team_name

    @team_name.setter
    def team_name(self, team_name):
        self.__team_name = team_name

    @property
    def team_side(self):
        return self.__team_side

    @team_side.setter
    def team_side(self, side):
        self.__team_side = side

    @property
    def number_id(self):
        return self.__number_id

    @number_id.setter
    def number_id(self, number_id):
        self.__number_id = number_id

    @property
    def positions(self):
        return self.__positions

    @positions.setter
    def positions(self, pos_list):
        self.__positions = pos_list

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, stamina_list):
        self.__stamina = stamina_list