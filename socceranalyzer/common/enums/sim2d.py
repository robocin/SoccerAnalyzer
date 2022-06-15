from enum import Enum

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

class Landmarks(Enum):
    R_GOAL_POS = [52.5, 0]
    R_GOAL_TOP_BAR = [52.5, 7.01]
    R_GOAL_BOTTOM_BAR = [52.5, -7.01]
    L_GOAL_POS = [-52.5, 0]
    L_GOAL_TOP_BAR = [-52.5, 7.01]
    L_GOAL_BOTTOM_BAR = [-52.5, -7.01]
    R_PEN_SPOT = [41.5, 0.]
    R_PEN_C = [35.75, 0.]
    R_PEN_TOP = [35.75, 20.16]
    R_PEN_BOTTOM = [35.75, -20.16]
    L_PEN_SPOT = [-41.5, 0.]
    L_PEN_C = [-35.75, 0.]
    L_PEN_TOP = [-35.75, 20.16]
    L_PEN_BOTTOM = [-35.75, -20.16]
    CENTER = [0., 0.]
    CENTER_BOTTOM = [0., -34.]
    CENTER_TOP = [0., 34.]
    BOTTOM_0 = [0., -39.]
    BOTTOM_L_10 = [-10., -39.]
    BOTTOM_L_20 = [-20., -39.]    
    BOTTOM_L_30 = [-30., -39.]
    BOTTOM_L_40 = [-40., -39.]
    BOTTOM_L_50 = [-50., -39.]    
    BOTTOM_R_10 = [10., -39.]
    BOTTOM_R_20 = [20., -39.]    
    BOTTOM_R_30 = [30., -39.]
    BOTTOM_R_40 = [40., -39.]
    BOTTOM_R_50 = [50., -39.]
    TOP_0 = [0., 39.]
    TOP_L_10 = [-10., 39.]
    TOP_L_20 = [-20., 39.]    
    TOP_L_30 = [-30., 39.]
    TOP_L_40 = [-40., 39.]
    TOP_L_50 = [-50., 39.]    
    TOP_R_10 = [10., 39.]
    TOP_R_20 = [20., 39.]    
    TOP_R_30 = [30., 39.]
    TOP_R_40 = [40., 39.]
    TOP_R_50 = [50., 39.]
    LEFT_0 = [-57.5, 0]
    LEFT_BOTTOM = [-52.5, -34.]
    LEFT_B_10 = [-57.5, -10.]
    LEFT_B_20 = [-57.5, -20.]
    LEFT_B_30 = [-57.5, -30.]
    LEFT_TOP = [-52.5, 34.]
    LEFT_T_10 = [-57.5, 10.]
    LEFT_T_20 = [-57.5, 20.]
    LEFT_T_30 = [-57.5, 30.]
    RIGHT_0 = [57.5, 0]
    RIGHT_BOTTOM = [52.5, -34.]
    RIGHT_B_10 = [57.5, -10.]
    RIGHT_B_20 = [57.5, -20.]
    RIGHT_B_30 = [57.5, -30.]
    RIGHT_TOP = [52.5, 34.]
    RIGHT_T_10 = [57.5, 10.]
    RIGHT_T_20 = [57.5, 20.]
    RIGHT_T_30 = [57.5, 30.]
    PITCH_SIZE = [105, 68]
