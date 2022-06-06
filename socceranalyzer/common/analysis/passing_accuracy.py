from socceranalyzer.common.operations.measures import distance
from socceranalyzer.common.geometric.point import Point
from socceranalyzer.common.geometric.circle import Circle
from socceranalyzer.common.chore.mediator import Mediator
from socceranalyzer.common.collections.collections import StringListItem
from socceranalyzer.common.collections.collections import StringListPositions
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.evaluators.kick import kick
from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.entity.team import Team


class PassingAccuracy(AbstractAnalysis):
    """
        Used to calculate the passing accuracy of the game.
        PassingAccuracy(pandas.DataFrame)
        Attributes
        ----------
            private: 
                left_team_passing_accuracy : float
                    The accuracy percentage of the left team
                right_team_passing_accuracy : float
                    The accuracy percentage of the right team   
                left_team_total_passes : float
                    The total number of passes of the left team 
                right_team_passing_accuracy : float
                    The total number of passes of the right team 

        Methods
        -------
            private: 
                calculate() -> None:
                    Calculates all wrong and correct passes occurrences
                define_player_possession(cycle: int, player_left_position: Point, player_right_position: Point, player_who_possesses: Bool) -> str, int
                    Defines the team that is in the radius of the ball in a particular cycle, if player_who_possesses = True, also returns the index of the player who is in that area
            public: 
                results() -> (float, float)
                    returns the teams passing accuracy and total passes 
                describe() -> none  
                    Shows the teams respective passing accuracy and total passes
    """


    def __init__(self, data_frame, category):
        self.__left_team_passing_accuracy = 0
        self.__right_team_passing_accuracy = 0
        self.__left_team_total_passes = 0
        self.__right_team_total_passes = 0
        self.__category = category
        self.__current_game_log = data_frame

        self._analyze()

    def __str__(self):
        values = self.results()
        return f'Team left: {values[0]}\nTeam right: {values[1]}'

    @property
    def category(self):
        return self.__category


    def _analyze(self):
        game_log = self.__current_game_log

        correct_passes_l = 0
        wrong_passes_l = 0

        correct_passes_r = 0
        wrong_passes_r = 0

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
                    wrong_passes_r += 1
                    
            
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
                    wrong_passes_l += 1
                    
        self.__left_team_passing_accuracy = correct_passes_l/(correct_passes_l + wrong_passes_l)
        self.__right_team_passing_accuracy = correct_passes_r/(correct_passes_r + wrong_passes_r)

        self.__left_team_total_passes = correct_passes_l + wrong_passes_l
        self.__right_team_total_passes = correct_passes_r + wrong_passes_r



            

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




    def results(self):
        return (self.__left_team_passing_accuracy, self.__right_team_passing_accuracy, 
                self.__left_team_total_passes, self.__right_team_total_passes)

    def describe(self):
        name_l = self.__current_game_log.loc[1, str(self.category.TEAM_LEFT)]
        name_r = self.__current_game_log.loc[1, str(self.category.TEAM_RIGHT)]
        print(f'{name_l}: acurácia = {self.__left_team_passing_accuracy:.4f}    passes totais = {self.__left_team_total_passes}\n' 
                f'{name_r}: acurácia = {self.__right_team_passing_accuracy:.4f}    passes totais = {self.__right_team_total_passes}')

    def serialize(self):
        raise NotImplementedError
