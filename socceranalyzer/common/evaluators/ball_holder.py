import pandas

from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.enums.ssl import SSL
from socceranalyzer.common.enums.vss import VSS
from socceranalyzer.common.geometric.point import Point

from socceranalyzer.common.geometric.circle import Circle
from socceranalyzer.common.core.mediator import Mediator
from socceranalyzer.common.operations.measures import distance

class BallHolderEvaluator:
    """
        Calculates which players are within a given ball area range.
        
        BallHolderEvaluator(dataframe: pandas.DataFrame, category: enum)

        Attributes
        ----------
            public through @properties:
                df: dataframe
                    the pandas object that contains the game data
                category: enum
                    match's category (2D, SSL or VSS)
                possible_players_l: [int]
                    a list of players objects from the left team inside the ball area radius
                possible_player_r: [int]
                    a list of players objects from the right team inside the ball area radius

        Methods
        -------
            private:
                at(cycle: int) -> [int], [int], str
                    returns two lists containing left side players and right side players inside the
                    ball area range, respectively, along with a string "left" or "right", representing which team 
                    has the ball possession
    """
    def __init__(self, dataframe: pandas.DataFrame, category: SIM2D | SSL | VSS):
        self.__df = dataframe
        self.__category = category
        self.__possible_players_l = []
        self.__possible_players_r = []
        self.__closer_to_ball_side = ""
        
    @property
    def dataframe(self):
        return self.__df

    @dataframe.setter
    def dataframe(self, new_df):
        self.__df = new_df
    
    @property
    def category(self):
        return self.__category
    
    @property
    def left_players(self):
        return self.__possible_players_l
    
    @property
    def right_players(self):
        return self.__possible_players_r

    @property
    def closer_to_ball(self):
        return self.__closer_to_ball_side

    def at(self, cycle: int):
        """
            Iterates through each player's position, calculates their distance to the ball
            and appends them to the possible players list if they are within range, also keeping track of which player is closest

            :return: [int], [int], str
                returns two lists containing left side players and right side players inside the ball area range, 
                respectively, along with a string "left" or "right", representing which team has the ball possession
        """

        ball_x = self.dataframe.loc[cycle, str(self.category.BALL_X)]
        ball_y = self.__df.loc[cycle, str(self.category.BALL_Y)]
        ball_position = Point(ball_x, ball_y)
        
        closest_distance = 1000
        possession_side = ""

        ball_radius = 0.85 # here to define ball area radius

        players_left = Mediator.players_left_position(self.category, True)
        players_right = Mediator.players_right_position(self.category, True)

        for i in range(0, 11):  # ith player is player_unum(i + 1)
            player_left_x = self.__df.loc[cycle, players_left.items[i].x]
            player_left_y = self.__df.loc[cycle, players_left.items[i].y]
        
            player_right_x = self.__df.loc[cycle, players_right.items[i].x]
            player_right_y = self.__df.loc[cycle, players_right.items[i].y]
        
            player_l_location = Point(player_left_x, player_left_y)
            player_r_location = Point(player_right_x, player_right_y)

            player_l_distance = distance(player_l_location, ball_position)
            player_r_distance = distance(player_r_location, ball_position)
        
            if player_l_distance <= ball_radius:
                self.__possible_players_l.append(i+1)
            else:
                self.__possible_players_l.append(None)
        
            if player_r_distance <= ball_radius:
                self.__possible_players_r.append(i+1)
            else:
                self.__possible_players_r.append(None)

            if player_l_distance < closest_distance:
                closest_distance = player_l_distance

                possession_side = "left"

            if player_r_distance < closest_distance:
                closest_distance = player_r_distance

                possession_side = "right"
        
        self.__closer_to_ball_side = possession_side

        return self.left_players, self.right_players, self.closer_to_ball
