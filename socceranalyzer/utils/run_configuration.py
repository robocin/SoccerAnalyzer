from socceranalyzer.common.enums.sim2d import SIM2D
class RunConfiguration:
    def __init__(self) -> False:
        self.logs_dir = None
        self.file_path = None
        self.tester_2d = False
        self.ball_possession = False
        self.tester_free_kick = False
        self.foul_charge = False
        self.kick_in = False
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

    def parse(self, json_info):
        if json_info["category"].upper() == "SIM2D":
            self.category = SIM2D

        self.logs_dir = json_info["logs_folder"]
        self.file_path = json_info["file_path"]
        self.tester_2d = json_info["analysis"]["tester_2d"]
        self.ball_possession = json_info["analysis"]["ball_possession"]
        self.tester_free_kick = json_info["analysis"]["tester_free_kick"]
        self.foul_charge = json_info["analysis"]["foul_charge"]
        self.kick_in = json_info["analysys"]["kick_in"]
        self.penalty = json_info["analysis"]["penalty"]
        self.playmodes = json_info["analysis"]["playmodes"]
        self.corners_occurrencies = json_info["analysis"]["corners_occurrencies"]
        self.intercept_counter = json_info["analysis"]["intercept_counter"]
        self.passing_accuracy = json_info["analysis"]["passing_accuracy"]
        self.time_after_events = json_info["analysis"]["time_after_events"]
        self.ball_history = json_info["analysis"]["ball_history"]
        self.stamina = json_info["analysis"]["stamina"]
        self.shooting = json_info["analysis"]["shooting"]
        self.heatmap = json_info["analysis"]["heatmap"]
        self.speed = json_info["analysis"]["speed"]
        self.goalkeeper = json_info["analysis"]["goalkeeper"]
        self.find_goals = json_info["analysis"]["find_goals"]

