from SoccerAnalyzer.socceranalyzer.common.abstract.abstract_analysis import AbstractAnalysis
from SoccerAnalyzer.socceranalyzer.common.enums.sim2d import SIM2D
from SoccerAnalyzer.socceranalyzer.common.chore.mediator import Mediator

class Stamina(AbstractAnalysis):
    def __init__(self, dataframe, category):
        self.__dataframe = dataframe
        self.__category = category
        self.__l_players_stamina = []
        self.__l_players_stamina_mean = 0
        self.__r_players_stamina = []
        self.__r_players_stamina_mean = 0

    @property
    def category(self):
        return self.__category

    @property
    def dataframe(self):
        return self.__dataframe

    def _analyze(self):

        if self.__l_players_stamina is not []:
            self.__l_players_stamina = []

        for stamina_attr in Mediator.players_left_stamina_attr(SIM2D):
            self.__l_players_stamina.append(self.dataframe[stamina_attr].tolist())

        for stamina_attr in Mediator.players_right_stamina_attr(self.dataframe):
            self.__r_players_stamina.append(self.dataframe[stamina_attr].tolist())

    @property
    def stamina_left(self):
        return self.__l_players_stamina

    @property
    def stamina_right(self):
        return self.__r_players_stamina

    def results(self):
        return (self.stamina_left, self.stamina_right)

    def describe(self):
        raise NotImplementedError

    def serialize(self):
        raise NotImplementedError