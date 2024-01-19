import pandas as pd

from socceranalyzer.common.geometric.point import Point
from socceranalyzer.common.geometric.rectangle import Rectangle
from socceranalyzer.common.basic.field import Field
from socceranalyzer.common.basic.team import Team 
from socceranalyzer.common.basic.ball import Ball
from socceranalyzer.agent2D.agent import Agent2D

from socceranalyzer.common.enums.vss import VSS
from socceranalyzer.common.enums.sim2d import SIM2D, Landmarks
from socceranalyzer.common.enums.ssl import SSL, LandmarksSSL

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
            pass
            #to-do (nunes)- débito técnico

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
            pass

            #to-do (nunes)- débito técnico
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
            l_top_left_pen_area = Point(Landmarks.LEFT_TOP.x, Landmarks.L_PEN_TOP.y)
            r_bottom_right_pen_area = Point(Landmarks.RIGHT_BOTTOM.x, Landmarks.R_PEN_BOTTOM.y)
            field = Field(68, 105, 
                        Landmarks.CENTER, 
                        Rectangle(l_top_left_pen_area, Landmarks.L_PEN_BOTTOM), 
                        Rectangle(Landmarks.R_PEN_TOP, r_bottom_right_pen_area),
                        Rectangle(Point(-52,-9), Point(-47 , 9)), 
                        Rectangle(Point(47,-9), Point(52, 9)),
                        Rectangle(Landmarks.L_GOAL_TOP_BAR, Landmarks.L_GOAL_BOTTOM_BAR),
                        Rectangle(Landmarks.R_GOAL_TOP_BAR, Landmarks.R_GOAL_BOTTOM_BAR))
            return field

        elif self.__category == VSS:
            raise NotImplementedError
        
        elif self.__category == SSL:
            field = Field(3000, 4500, LandmarksSSL.CENTER)
            return field