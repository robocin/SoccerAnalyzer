from abc import ABCMeta, abstractmethod
from socceranalyzer.common.geometric.point import Point

class AbstractPlayer(metaclass=ABCMeta):
    @abstractmethod
    def positionAt(self, cycle : int) -> Point:
        pass

