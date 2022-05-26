from matplotlib.axes import Axes
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from pyparsing import col

from socceranalyzer.common.chore.match_analyzer import MatchAnalyzer


class JupyterAdapter:
    def __init__(self, match_analyzer: MatchAnalyzer) -> None:
        self.__match_analyzer = match_analyzer
        self.__config: dict[str, str] = {}

        self.__init_config()

    def __init_config(self):
        """
        config contains: 
            left_color:     str
            right_color:    str
            left_label:     str
            right_label:    str
            shadow:         Bool
            startangle:     int
        """

        my_team_name = "RobôCIn"

        team_l_name = self.__match_analyzer.match.team_left_name
        team_r_name = self.__match_analyzer.match.team_right_name

        # colorize my team
        if team_l_name == my_team_name:
            self.__config["left_color"] = 'green'
            self.__config["right_color"] = 'red'
        else:
            self.__config["left_color"] = 'green'
            self.__config["right_color"] = 'red'

        self.__config["left_label"] = team_l_name
        self.__config["right_label"] = team_r_name
        self.__config["shadow"] = True
        self.__config["startangle"] = 90

    def ball_possession_plot(self, width: int, height: int, title: str) -> None:
        
        left_possession, right_possession = self.__match_analyzer.ball_possession.results()
        
        _, ax = plt.subplots(figsize=(width, height))
        ax.pie([left_possession, right_possession], 
                colors = [self.__config["left_color"], self.__config["right_color"]],
                labels = [self.__config["left_label"], self.__config["right_label"]],
                shadow = self.__config["shadow"],
                startangle = self.__config["startangle"])
        
        ax.set_title(title)

        plt.show()

    def _build_sim2d(self):
        self.__ball_possession_plot(10, 5, "Ball Possession")

    def _build_ssl(self):
        pass

    def _build_vss(self):
        pass


    
    