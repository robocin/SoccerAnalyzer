from socceranalyzer.common.events.abstract_event import AbstractEvent
from socceranalyzer.common.basic.match import Match
from socceranalyzer.common.basic.team import Team
from socceranalyzer.agent2D.agent import Agent2D
from socceranalyzer.common.geometric.point import Point

class CornerKickEvent(AbstractEvent): 
    def __init__(self, 
                match: Match,
                cicles: tuple[int, int], 
                players_left: list[Agent2D],
                players_right: list[Agent2D],
                team_actor: Team):
        """
            A class to represent a Corner kick Event in the match

            corner_kick_event(match: Match,  cicles: tuple[int, int], players_left: list[Agent2D], players_right: list[Agent2D], team_actor: Team)

            Attributes
            ----------
                public through @properties: 
                    cicles: tuple[int, int]
                        The start and end cicles of the event
                    players_left: list[Agent2D]
                        The left players who participate in the event
                    players_right: list[Agent2D]
                        The right players who participate in the event
                    team_actor: Team
                        The team who commited the action
                    
        """
        self.__match = match
        self.__cicles = cicles
        self.__players_left = players_left
        self.__players_right = players_right
        self.__team_actor = team_actor

    def corner(self):
        """
        Returns the corner that the corner kick occurred. 
        """
        # TODO
        pass



    @property
    def cicles(self):
        return self.__cicles
    
    @property
    def players_left(self):
        return self.__players_left
    
    @property
    def players_right(self):
        return self.__players_right
    
    @property
    def team_actor(self):
        return self.__team_actor