from abc import ABCMeta, abstractmethod
from socceranalyzer.common.geometric.point import Point

class AbstractPlayer(metaclass=ABCMeta):
    @abstractmethod
    def positionAt(self, cycle : int) -> Point:
        pass

    @property
    @abstractmethod
    def team_identifier(self):
        pass

    @property
    @abstractmethod
    def number_id(self):
        pass

    @property
    @abstractmethod
    def team_name(self):
        pass



