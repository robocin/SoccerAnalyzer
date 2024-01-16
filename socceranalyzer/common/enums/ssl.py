from enum import Enum
from socceranalyzer.common.geometric.point import Point


class SSL(Enum):
    """
    This class is a parent of enum.Enum.
    Python 3.4 or above is needed to use this class.
    It's purpose is to map all parameters of SSL with the
    same keys used in other categories. The keys are used inside
    the analysis for them to be category agnostic.
    
    All parameters are strings
    """

    GAME_TIME = "showtime"
    PLAYMODE = "game_state_name"
    RUNNING_GAME = "GameRunning"
    # FAULT_COMMITED_L = "foul_charge_l"
    # FAULT_COMMITED_R = "foul_charge_r"
    BALL_X = "ball_position_x"
    BALL_Y = "ball_position_y"
    BALL_VX = "ball_vx",
    BALL_VY = "ball_vy",
    TEAM_LEFT = "team_l_name"
    TEAM_RIGHT = "team_r_name"
    TEAM_LEFT_SCORE = "team_l_score"
    TEAM_RIGHT_SCORE = "team_r_score"
    MAX_PLAYERS = "10"
    # PENALTY_TO_LEFT = "penalty_ready_l"
    # PENALTY_TO_RIGHT = "penalty_ready_r"
    # FK_LEFT = "free_kick_l"
    # FK_RIGHT = "free_kick_r"
    # GOAL_SCORED_L = "goal_l"
    # GOAL_SCORED_R = "goal_r"

    def __str__(self):
        return self.value

class LandmarksSSL:
    BOTTOM_LEFT = Point(-4500, -3000)
    BOTTOM_RIGHT = Point(4500, -3000)
    TOP_LEFT = Point(-4500, 3000)
    TOP_RIGHT = Point(-4500, 3000) 
    CENTER = Point (0, 0)
    TOP_CENTER = Point(0, 3000)
    BOTTOM_CENTER = Point (0, -3000)