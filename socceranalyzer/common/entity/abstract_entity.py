from abc import ABCMeta, abstractmethod
from socceranalyzer.common.geometric.point import Point

class AbstractEntity(metaclass=ABCMeta):
    @abstractmethod
    def positionAt(self, cycle : int) -> Point:
        pass

