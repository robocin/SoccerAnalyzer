from enum import Enum
from socceranalyzer.common.geometric.point import Point

class SIM2D(Enum):
    """
        This class is a parent of enum.Enum.
        Python 3.4 or above is needed to use this class.
        It's purpose is to map all parameters of SIM2D with the
        same keys used in other categories. The keys are used inside
        the analysis for them to be category agnostic.
        
        All parameters are strings
    """
    GAME_TIME = "show_time"
    PLAYMODE = "playmode"
    RUNNING_GAME = "play_on"
    FAULT_COMMITED_L = "foul_charge_l"
    FAULT_COMMITED_R = "foul_charge_r"
    BALL_X = "ball_x"
    BALL_Y = "ball_y"
    TEAM_LEFT = "team_name_l"
    TEAM_RIGHT = "team_name_r"
    TEAM_LEFT_SCORE = "team_score_l"
    TEAM_RIGHT_SCORE = "team_score_r"
    TEAM_LEFT_CORNER = "corner_kick_l"
    TEAM_RIGHT_CORNER = "corner_kick_r"
    PENALTY_TO_LEFT = "penalty_ready_l"
    PENALTY_TO_RIGHT = "penalty_ready_r"
    FK_LEFT = "free_kick_l"
    FK_RIGHT = "free_kick_r"
    GOAL_SCORED_L = "goal_l"
    GOAL_SCORED_R = "goal_r"

    def __str__(self):
        return self.value

class Landmarks:
    R_GOAL_POS = Point(52.5, 0)
    R_GOAL_TOP_BAR = Point(52.5, 7.01)
    R_GOAL_BOTTOM_BAR = Point(52.5, -7.01)
    L_GOAL_POS = Point(-52.5, 0)
    L_GOAL_TOP_BAR = Point(-52.5, 7.01)
    L_GOAL_BOTTOM_BAR = Point(-52.5, -7.01)
    R_PEN_C = Point(35.75, 0.)
    R_PEN_TOP = Point(35.75, 20.16)
    R_PEN_BOTTOM = Point(35.75, -20.16)
    L_PEN_C = Point(-35.75, 0.)
    L_PEN_TOP = Point(-35.75, 20.16)
    L_PEN_BOTTOM = Point(-35.75, -20.16)
    CENTER = Point(0., 0.)
    CENTER_BOTTOM = Point(0., -34.)
    CENTER_TOP = Point(0., 34.)
    BOTTOM_0 = Point(0., -39.)
    BOTTOM_L_10 = Point(-10., -39.)
    BOTTOM_L_20 = Point(-20., -39.)    
    BOTTOM_L_30 = Point(-30., -39.)
    BOTTOM_L_40 = Point(-40., -39.)
    BOTTOM_L_50 = Point(-50., -39.)    
    BOTTOM_R_10 = Point(10., -39.)
    BOTTOM_R_20 = Point(20., -39.)    
    BOTTOM_R_30 = Point(30., -39.)
    BOTTOM_R_40 = Point(40., -39.)
    BOTTOM_R_50 = Point(50., -39.)
    TOP_0 = Point(0., 39.)
    TOP_L_10 = Point(-10., 39.)
    TOP_L_20 = Point(-20., 39.)    
    TOP_L_30 = Point(-30., 39.)
    TOP_L_40 = Point(-40., 39.)
    TOP_L_50 = Point(-50., 39.)    
    TOP_R_10 = Point(10., 39.)
    TOP_R_20 = Point(20., 39.)    
    TOP_R_30 = Point(30., 39.)
    TOP_R_40 = Point(40., 39.)
    TOP_R_50 = Point(50., 39.)
    LEFT_0 = Point(-57.5, 0)
    LEFT_BOTTOM = Point(-52.5, -34.)
    LEFT_B_10 = Point(-57.5, -10.)
    LEFT_B_20 = Point(-57.5, -20.)
    LEFT_B_30 = Point(-57.5, -30.)
    LEFT_TOP = Point(-52.5, 34.)
    LEFT_T_10 = Point(-57.5, 10.)
    LEFT_T_20 = Point(-57.5, 20.)
    LEFT_T_30 = Point(-57.5, 30.)
    RIGHT_0 = Point(57.5, 0)
    RIGHT_BOTTOM = Point(52.5, -34.)
    RIGHT_B_10 = Point(57.5, -10.)
    RIGHT_B_20 = Point(57.5, -20.)
    RIGHT_B_30 = Point(57.5, -30.)
    RIGHT_TOP = Point(52.5, 34.)
    RIGHT_T_10 = Point(57.5, 10.)
    RIGHT_T_20 = Point(57.5, 20.)
    RIGHT_T_30 = Point(57.5, 30.)
