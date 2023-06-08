from socceranalyzer.common.enums.sim2d import SIM2D
from enum import Enum

class ExecutionType(Enum):
    RUN = 1
    TESTER = 2
    UNSPECIFIED = 0

class RunConfiguration:
    def __init__(self) -> False:
        self.execution = None
        self.logs_dir = None
        self.file_path = None
        self.output_results = False
        self.output_file_name = "output.txt"
        self.enable_analysis = False
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

        if info["execution"].upper() == "RUN":
            self.execution = ExecutionType.RUN
        elif info["execution"].upper() == "TESTER":
            self.execution = ExecutionType.TESTER
        else:
            self.execution = ExecutionType.UNSPECIFIED

        self.logs_dir = info["logs_folder"]
        self.file_path = info["file_path"]
        self.output_results = self.handle_input(info["output_results"])
        self.output_file_name = info["output_file_name"]
        self.enable_analysis = self.handle_input(info["enable_analysis"])
        if self.enable_analysis:
            self.tester_2d = self.handle_input(info["analysis"]["tester_2d"])
            self.ball_possession = self.handle_input(info["analysis"]["ball_possession"])
            self.tester_free_kick = self.handle_input(info["analysis"]["tester_free_kick"])
            self.foul_charge = self.handle_input(info["analysis"]["foul_charge"])
            self.penalty = self.handle_input(info["analysis"]["penalty"])
            self.playmodes = self.handle_input(info["analysis"]["playmodes"])
            self.corners_occurrencies = self.handle_input(info["analysis"]["corners_occurrencies"])
            self.intercept_counter = self.handle_input(info["analysis"]["intercept_counter"])
            self.passing_accuracy = self.handle_input(info["analysis"]["passing_accuracy"])
            self.time_after_events = self.handle_input(info["analysis"]["time_after_events"])
            self.ball_history = self.handle_input(info["analysis"]["ball_history"])
            self.stamina = self.handle_input(info["analysis"]["stamina"])
            self.shooting = self.handle_input(info["analysis"]["shooting"])
            self.heatmap = self.handle_input(info["analysis"]["heatmap"])
            self.speed = self.handle_input(info["analysis"]["speed"])
            self.goalkeeper = self.handle_input(info["analysis"]["goalkeeper"])
            self.find_goals = self.handle_input(info["analysis"]["find_goals"])

    def handle_input(self, parameter):
        """Misspelling check from user input on boolean params"""
        if parameter != True:
            return False

        return True