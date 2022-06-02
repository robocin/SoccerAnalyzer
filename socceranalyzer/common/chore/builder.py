from socceranalyzer.common.basic.match import Match
from socceranalyzer.common.geometric.point import Point
from socceranalyzer.common.geometric.rectangle import Rectangle
from socceranalyzer.common.basic.field import Field
from socceranalyzer.common.entity.team import Team 
from socceranalyzer.common.entity.agent import Agent 
from socceranalyzer.common.entity.ball import Ball 

from socceranalyzer.common.enums.vss import VSS
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.enums.ssl import SSL

class Builder:
    def __init__(self, match: Match = None):
        self.__match = match
        self.__cat = match.category

    def playerBuilder(self, team: Team):
        if self.__cat == SIM2D:
            players_array = []
            for i in range(1, 12):
                players_array.append(Agent(team.name, team.side, i))
        
            return players_array
        elif self.__cat == VSS:
            raise NotImplementedError

        elif self.__cat == SSL:
            raise NotImplementedError

    def teamBuilder(self, identifier: str):
        if self.__cat == SIM2D:
            if identifier == 'left':
                team_name = self.__match.team_left_name
                team = Team(team_name, "left")
            else:   
                team_name = self.__match.team_right_name
                team = Team(team_name, "right")
        
            return team
        elif self.__cat == VSS:
            raise NotImplementedError

        elif self.__cat == SSL:
            raise NotImplementedError

    def ballBuilder(self):
        ball = Ball(0.0, 0.0)

        return ball
    
    def fieldBuilder(self):
        if self.__cat == SIM2D:
            # falta saber o tamanho da pequena área e da área de penalti
            # TODO: colocar os valores da pequena área e da área de penalti
            field = Field(68, 105, Point(0,0), Rectangle(Point(38, 56), 61, 43), Rectangle(Point(0,0), 0, 0), Rectangle(Point(0,0), 0 ,0), Rectangle(Point(0,0), 0, 0))

        elif self.__cat == VSS:
            raise NotImplementedError
        elif self.__cat == SSL:
            raise NotImplementedError

        return field