from abc import ABCMeta, abstractmethod
from socceranalyzer.agent2D.agent import Agent2D
from socceranalyzer.RobotSSL.robot_ssl import RobotSSL
from socceranalyzer.RobotVSS.robot_vss import RobotVSS
from socceranalyzer.common.basic.team import Team
class AbstractEvent(metaclass=ABCMeta):

    @property
    @abstractmethod
    def cicles(self) -> tuple[int, int]:
        pass

    @property
    @abstractmethod
    def players_left(self) -> list[Agent2D | RobotVSS | RobotSSL]:
        pass

    @property
    @abstractmethod
    def players_right(self) -> list[Agent2D | RobotVSS | RobotSSL]:
        pass

    @property
    @abstractmethod
    def team_actor(self) -> Team:
        pass

