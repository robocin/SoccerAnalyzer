from enum import Enum

class SIM2D(Enum):
    PLAYMODE = 'playmode'
    BALL_X = 'ball_x'
    BALL_Y = 'ball_y'
    TEAM_LEFT = "team_name_l"
    TEAM_RIGHT = "team_name_r"
    TEAM_LEFT_SCORE = "team_score_l"
    TEAM_RIGHT_SCORE = "team_score_r"

    def __str__(self):
        return self.value

