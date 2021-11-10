from SoccerAnalyzer.socceranalyzer.common.geometric.point import Point
from SoccerAnalyzer.socceranalyzer.common.geometric.circle import Circle
from SoccerAnalyzer.socceranalyzer.common.chore.mediator import Mediator
from SoccerAnalyzer.socceranalyzer.common.utility.slicers import PlaymodeSlicer

class BallHolderEvaluator:
    def __init__(self, dataframe, category):
        self.__df = dataframe
        self.__category = category
        self.__possible_players_l = []
        self.__possible_players_r = []
        
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

    def at(self, cycle):

        ball_x = self.dataframe.loc[cycle, str(self.category.BALL_X)]
        ball_y = self.__df.loc[cycle, str(self.category.BALL_Y)]
        ball_position = Point(ball_x, ball_y)
        
        ball_radius = Circle(0.85, ball_position) # here to define ball area radius

        players_left = Mediator.players_left_position(self.category, True)
        players_right = Mediator.players_right_position(self.category, True)

        for i in range(0, 11):  # ith player is player_unum(i + 1)
            player_left_x = self.__df.loc[cycle, players_left.items[i].x]
            player_left_y = self.__df.loc[cycle, players_left.items[i].y]
        
            player_right_x = self.__df.loc[cycle, players_right.items[i].x]
            player_right_y = self.__df.loc[cycle, players_right.items[i].y]
        
            player_l_location = Point(player_left_x, player_left_y)
            player_r_location = Point(player_right_x, player_right_y)
        
            if ball_radius.is_inside(player_l_location):
                self.__possible_players_l.append(i+1)
            else:
                self.__possible_players_l.append(None)
        
            if ball_radius.is_inside(player_r_location):
                self.__possible_players_r.append(i+1)
            else:
                self.__possible_players_r.append(None)
        
        return self.left_players, self.right_players
