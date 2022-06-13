from pandas import DataFrame
from socceranalyzer.common.chore.mediator import Mediator
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.enums.ssl import SSL
from socceranalyzer.common.enums.vss import VSS
from socceranalyzer.common.evaluators.kick import kick
from socceranalyzer.common.geometric.circle import Circle
from socceranalyzer.common.geometric.point import Point


class Passing:
    def __init__(self, data_frame: DataFrame, category: SIM2D | SSL | VSS):
        self.__left_team_passing_accuracy = 0
        self.__right_team_passing_accuracy = 0
        self.__left_team_total_passes = 0
        self.__right_team_total_passes = 0
        self.__left_team_completed_passes = 0
        self.__right_team_completed_passes = 0
        self.__left_team_interceptions = 0
        self.__right_team_interceptions = 0
        self.__category = category
        self.__current_game_log = data_frame
        self.__ran_all_analysis = False
        if category is not SIM2D:
            raise NotImplementedError

    @property
    def category(self): return self.__category
    
    @property
    def dataframe(self): return self.dataframe

    @property
    def left_team_passing_stats(self):
        return {
            'completed_passes': self.__left_team_completed_passes,
            'total_passes': self.__left_team_total_passes,
            'accuracy': self.__left_team_passing_accuracy,
            'interceptions': self.__left_team_interceptions
        }
    
    @property
    def right_team_passing_stats(self):
        return {
            'completed_passes': self.__right_team_completed_passes,
            'total_passes': self.__right_team_total_passes,
            'accuracy': self.__right_team_passing_accuracy,
            'interceptions': self.__right_team_interceptions
        }

    def __define_player_possession(self, cycle, player_left_position: Point, player_right_position: Point, player_who_possesses=False):
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
                if player_who_possesses:
                    return 'left', i+2
                return 'left'
            
            player_right_position.x = self.__current_game_log.loc[cycle, players_right.items[i].x]
            player_right_position.y = self.__current_game_log.loc[cycle, players_right.items[i].y]

            if ball_zone.is_inside(player_right_position):
                if player_who_possesses:
                    return 'right', i+2
                return 'right'
        if player_who_possesses:
            return None, -1
        return None

    def run_passing_evaluation(self):
        if (self.__ran_all_analysis): return

        game_log = self.__current_game_log

        correct_passes_l = 0
        wrong_passes_l = 0
        intercepted_passes_l = 0

        correct_passes_r = 0
        wrong_passes_r = 0
        intercepted_passes_r = 0

        pass_r = False
        pass_l = False

        player_right_position = Point()
        player_left_position = Point()

        for current_cycle, row in game_log.iterrows():
            #Right Passing
            if not pass_r:
                pass_r, player_who_kicked = kick(current_cycle, 'r', game_log, True) # Checks if a pass occurred
            else:
                pass_l = False
                
                if game_log[str(self.category.PLAYMODE)][current_cycle] == 'kick_in_l': # Ball out by right team
                    pass_r  = False
                    wrong_passes_r += 1
                    continue
                
                possession, player_who_possesses = self.__define_player_possession(current_cycle, player_left_position, player_right_position, True) 
                
                if possession == 'right': #ball to the same team
                    pass_r = False
                    if player_who_kicked != player_who_possesses: # only counts if the pass is to another player
                        correct_passes_r += 1
                    

                if possession == 'left': # enemy intercepted
                    pass_r = False
                    intercepted_passes_l += 1
                    try:
                        for l in range(5):
                            if game_log[str(self.category.PLAYMODE)][current_cycle+l] in ['kick_off_l', str(self.category.FAULT_COMMITED_L)]:
                                intercepted_passes_l -= 1
                                break
                    except: 
                        pass                    
            
            # Left Passing
            if not pass_l:
                pass_l, player_who_kicked = kick(current_cycle, 'l', game_log, True) # Checks if a pass occurred
            else:
                pass_r = False
                
                if game_log[str(self.category.PLAYMODE)][current_cycle] == 'kick_in_r': # Ball out by left team
                    pass_l  = False
                    wrong_passes_l += 1
                    continue

                possession, player_who_possesses = self.__define_player_possession(current_cycle, player_left_position, player_right_position, True)
                if possession == 'left': # ball to the same team
                    pass_l = False
                    if player_who_kicked != player_who_possesses: # only counts if the pass is to another player
                        correct_passes_l += 1
                    
                
                if possession == 'right': # enemy intercepted
                    pass_l = False
                    intercepted_passes_r += 1
                    try:
                        for l in range(5):
                            if game_log[str(self.category.PLAYMODE)][current_cycle+l] in ['kick_off_r',  str(self.category.FAULT_COMMITED_R)]:
                                intercepted_passes_r -= 1
                                break
                    except: 
                        pass
                
        self.__left_team_total_passes = correct_passes_l + wrong_passes_l + intercepted_passes_r
        self.__right_team_total_passes = correct_passes_r + wrong_passes_r + intercepted_passes_l
        
        self.__left_team_passing_accuracy = correct_passes_l/(self.__left_team_total_passes)
        self.__right_team_passing_accuracy = correct_passes_r/(self.__right_team_total_passes)

        self.__left_team_completed_passes = correct_passes_l
        self.__right_team_completed_passes = correct_passes_r

        self.__left_team_interceptions = intercepted_passes_l
        self.__right_team_interceptions = intercepted_passes_r
        self.__ran_all_analysis = True
    