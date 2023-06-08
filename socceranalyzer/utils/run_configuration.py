from socceranalyzer.common.enums.sim2d import SIM2D
class RunConfiguration:
    def __init__(self) -> False:
        self.logs_dir = None
        self.file_path = None
        self.tester_2d = False
        self.ball_possession = False
        self.tester_free_kick = False
        self.foul_charge = False
        self.penalty = False
        self.playmodes = False
        self.corners_occurrencies = False
        self.intercept_counter = False
        self.passing_accuracy = False
        self.time_after_events = False
        self.ball_history = False
        self.stamina = False
        self.shooting = False
        self.heatmap = False
        self.speed = False
        self.goalkeeper = False
        self.find_goals = False

    def parse(self, info):
        if info["category"].upper() == "SIM2D":
            self.category = SIM2D

        self.logs_dir = info["logs_folder"]
        self.file_path = info["file_path"]
        self.tester_2d = self.is_enabled(info["analysis"]["tester_2d"])
        self.ball_possession = self.is_enabled(info["analysis"]["ball_possession"])
        self.tester_free_kick = self.is_enabled(info["analysis"]["tester_free_kick"])
        self.foul_charge = self.is_enabled(info["analysis"]["foul_charge"])
        self.penalty = self.is_enabled(info["analysis"]["penalty"])
        self.playmodes = self.is_enabled(info["analysis"]["playmodes"])
        self.corners_occurrencies = self.is_enabled(info["analysis"]["corners_occurrencies"])
        self.intercept_counter = self.is_enabled(info["analysis"]["intercept_counter"])
        self.passing_accuracy = self.is_enabled(info["analysis"]["passing_accuracy"])
        self.time_after_events = self.is_enabled(info["analysis"]["time_after_events"])
        self.ball_history = self.is_enabled(info["analysis"]["ball_history"])
        self.stamina = self.is_enabled(info["analysis"]["stamina"])
        self.shooting = self.is_enabled(info["analysis"]["shooting"])
        self.heatmap = self.is_enabled(info["analysis"]["heatmap"])
        self.speed = self.is_enabled(info["analysis"]["speed"])
        self.goalkeeper = self.is_enabled(info["analysis"]["goalkeeper"])
        self.find_goals = self.is_enabled(info["analysis"]["find_goals"])

    def is_enabled(self, parameter):
        if parameter != True:
            return False
