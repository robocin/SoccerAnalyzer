class RunConfiguration:
    def __init__(self) -> None:
        self.logs_dir = None
        self.tester_2d = None
        self.ball_possession = None
        self.tester_free_kick = None
        self.foul_charge = None
        self.penalty = None
        self.playmodes = None
        self.corners = None
        self.intercept_counter = None
        self.passing_accuracy = None
        self.time_after_events = None
        self.ball_hisory = None
        self.stamina = None
        self.shooting = None
        self.heatmap = None
        self.speed = None
        self.goalkpeeper = None
        self.find_goals = None

    def parse(self, json_info):
        for key, value in json_info.items():
            print(key, value)
