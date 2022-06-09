import pandas as pd

from socceranalyzer.common.geometric.point import Point
from socceranalyzer.common.geometric.rectangle import Rectangle
from socceranalyzer.common.basic.field import Field
from socceranalyzer.common.basic.team import Team 
from socceranalyzer.common.basic.ball import Ball
from socceranalyzer.agent2D.agent import Agent2D

from socceranalyzer.common.enums.vss import VSS
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.enums.ssl import SSL

class Builder:
    def __init__(self, dataframe: pd.DataFrame=None, category: SIM2D | SSL | VSS=None):
        self.__df = dataframe
        self.__category = category

    def playerBuilder(self, team: Team) -> list[Agent2D]:
        """
        Returns a list of Agent2D intances representing the players/Robots in the match.

            Parametes:
                team (Team): Team of the players
            Returns:
                players_array (list[Agent2D]): list of Agent2D instances with informations about their team
        
        """
        if self.__category == SIM2D:
            players_array = []
            for i in range(1, 12):
                players_array.append(Agent2D(team.name, team.identifier, i))
            return players_array
        elif self.__category == VSS:
            raise NotImplementedError

        elif self.__category == SSL:
            raise NotImplementedError

    def teamBuilder(self, identifier: str) -> Team:
        """
        Builds an instance of a Team class representing the team playing the match
            Parameters:
                identifier (str): A string to differenciate between the teams in the match. SIM2D uses 'left' and 'right' while VSS and SSL use colors
            Returns:
                team (Team): Team instance with its identifier
        """
        if self.__category == SIM2D:
            if identifier == 'left':
                team_name = self.__df.loc[1, str(self.__category.TEAM_LEFT)]
                team = Team(team_name, "left")
            else:   
                team_name = self.__df.loc[1, str(self.__category.TEAM_RIGHT)]
                team = Team(team_name, "right")
        
            return team
        elif self.__category == VSS:
            raise NotImplementedError

        elif self.__category == SSL:
            raise NotImplementedError

    def ballBuilder(self) -> Ball:
        """
        Retuns an instance of a Ball class representing the ball in the field, starting at the center of the field
            Returns:
                ball (Ball): Ball instance starting at position (0,0)
        """
        ball = Ball(0.0, 0.0)

        return ball
    
    def fieldBuilder(self) -> Field:
        """
        Returns an instance of the Field class representing the field that the game occured. Passes the field measures depending on the game category.
            Returns:
                field (Field): Field instance with the field measures
        """
        if self.__category == SIM2D:
            field = Field(68, 105, 
                        Point(0,0), 
                        Rectangle(Point(-52, -20), 16, 72), 
                        Rectangle(Point(36,-20), 16, 72), 
                        Rectangle(Point(-52,-9), 5 ,18), 
                        Rectangle(Point(47,-9), 5, 18),
                        Rectangle(Point(-53, -7), 1, 14),
                        Rectangle(Point(53, -7), 1, 14))
            return field

        elif self.__category == VSS:
            raise NotImplementedError
        elif self.__category == SSL:
            raise NotImplementedError

        

        # -7 até +7 -> trave (x=52)