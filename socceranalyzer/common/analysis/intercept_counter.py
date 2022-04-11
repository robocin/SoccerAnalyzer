from socceranalyzer.common.operations.measures import distance
from socceranalyzer.common.geometric.point import Point
from socceranalyzer.common.geometric.circle import Circle
from socceranalyzer.common.chore.mediator import Mediator
from socceranalyzer.common.collections.collections import StringListItem
from socceranalyzer.common.collections.collections import StringListPositions
from socceranalyzer.common.enums.sim2d import SIM2D

class InterceptCounter:
    def __init__(self, data_frame, category):
        self.__left_team_interceptions = 0
        self.__right_team_interceptions = 0
        self.__category = category
        self.__current_game_log = data_frame

        self.__calculate()

    def __str__(self):
        values = self.results()
        return f'Team left: {values[0]}\nTeam right: {values[1]}'

    @property
    def category(self):
        return self.__category


    def __calculate(self):
        game_log = self.__current_game_log


        pass_r = False
        pass_l = False

        player_right_position = Point()
        player_left_position = Point()

        for current_cycle, row in game_log.iterrows():
            if not pass_r:
                pass_r = self.__ball_kick(current_cycle, 'r')
            else:
                pass_l = False
                
                if game_log['playmode'][current_cycle] == 'kick_in_l':
                    pass_r  = False
                    continue
                
                possession = self.__define_player_possession(current_cycle, player_left_position, player_right_position)
                if possession == 'right':
                    pass_r = False
                    
                if possession == 'left':
                    pass_r = False
                    self.__left_team_interceptions += 1
                        
                    try:
                        for l in range(5):
                            if game_log['playmode'][current_cycle+l] in ['kick_off_l', 'foul_charge_l']:
                                self.__left_team_interceptions -= 1
                                break
                    except: 
                        pass
            

            if not pass_l:
                pass_l = self.__ball_kick(current_cycle, 'l')
            else:
                pass_r = False
                
                if game_log['playmode'][current_cycle] == 'kick_in_r':
                    pass_l  = False
                    continue

                possession = self.__define_player_possession(current_cycle, player_left_position, player_right_position)
                if possession == 'left':
                    pass_l = False
                
                if possession == 'right':
                    pass_l = False
                    self.__right_team_interceptions += 1
                    
                    try:
                        for l in range(5):
                            if game_log['playmode'][current_cycle+l] in ['kick_off_r', 'foul_charge_r']:
                                self.__right_team_interceptions -= 1
                                break
                    except: 
                        pass
                

            

    def __ball_kick(self, cycle: int, team: str):
        for j in range(1,12):
            if cycle != 0 and (self.__current_game_log[f"player_{team}{j}_counting_kick"][cycle] > self.__current_game_log[f'player_{team}{j}_counting_kick'][cycle-1]):
                return True
        return False

    def __define_player_possession(self, cycle, player_left_position: Point, player_right_position: Point):
        player_influence_radius = 0.7

        players_left = Mediator.players_left_position(self.category, False)
        players_right = Mediator.players_right_position(self.category, False)
        
        ball_position = Point(self.__current_game_log.loc[cycle, str(self.category.BALL_X)], self.__current_game_log.loc[cycle, str(self.category.BALL_Y)])

        ball_zone = Circle(player_influence_radius, ball_position)

        # 10 players only because goalkeeper is not checked in this analysis
        for i in range(0, 10):
            player_left_position.x = self.__current_game_log.loc[cycle, players_left.items[i].x]
            player_left_position.y = self.__current_game_log.loc[cycle, players_left.items[i].y]

            if ball_zone.is_inside(player_left_position):
                return 'left'
            
            player_right_position.x = self.__current_game_log.loc[cycle, players_right.items[i].x]
            player_right_position.y = self.__current_game_log.loc[cycle, players_right.items[i].y]

            if ball_zone.is_inside(player_right_position):
                return 'right'
        return None




    def results(self):
        return (self.__left_team_interceptions, self.__right_team_interceptions)

    def describe(self):
        name_l = self.__current_game_log.loc[1, str(self.category.TEAM_LEFT)]
        name_r = self.__current_game_log.loc[1, str(self.category.TEAM_RIGHT)]
        print(f'{name_l}: {self.__left_team_interceptions}\n' 
                f'{name_r}: {self.__right_team_interceptions}')

    def serialize(self):
        raise NotImplementedError