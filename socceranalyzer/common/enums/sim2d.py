from enum import Enum

class SIM2D(Enum):
    GAME_TIME = "show_time"
    PLAYMODE = 'playmode'
    FAULT_COMMITED_L = "foul_charge_l"
    FAULT_COMMITED_R = "foul_charge_r"
    BALL_X = 'ball_x'
    BALL_Y = 'ball_y'
    TEAM_LEFT = "team_name_l"
    TEAM_RIGHT = "team_name_r"
    TEAM_LEFT_SCORE = "team_score_l"
    TEAM_RIGHT_SCORE = "team_score_r"
    TEAM_LEFT_CORNER = "corner_kick_l"
    TEAM_RIGHT_CORNER = "corner_kick_r"
    PENALTY_TO_LEFT = "penalty_ready_l"
    PENALTY_TO_RIGHT = "penalty_ready_r"

    def __str__(self):
        return self.value

