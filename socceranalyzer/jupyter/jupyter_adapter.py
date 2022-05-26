from matplotlib.axes import Axes
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import os

import socceranalyzer
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
        
        self.__config["name_left"] = team_l_name
        self.__config["name_right"] = team_r_name
        self.__config["left_label"] = team_l_name
        self.__config["right_label"] = team_r_name
        self.__config["shadow"] = True
        self.__config["startangle"] = 90
        self.__config["sim2d_field_img"] = f'{os.path.dirname(socceranalyzer.__file__)}/images/sim2d_field.png'

        # colorize my team
        if team_l_name == my_team_name:
            self.__config["left_color"] = 'green'
            self.__config["right_color"] = 'red'
        else:
            self.__config["left_color"] = 'green'
            self.__config["right_color"] = 'red'


    def ball_possession(self, width: int, height: int, title: str = "Ball Possession") -> None:
        
        left_possession, right_possession = self.__match_analyzer.ball_possession.results()
        
        _, ax = plt.subplots(figsize=(width, height))
        ax.pie([left_possession, right_possession], 
                colors = [self.__config["left_color"], self.__config["right_color"]],
                labels = [self.__config["left_label"], self.__config["right_label"]],
                shadow = self.__config["shadow"],
                startangle = self.__config["startangle"])
        
        ax.set_title(title)

        plt.show()

    def fault_position(self, width: int, height: int, title: str = "Ball Possession"):

        left_faults, right_faults = self.__match_analyzer.foul_charge.results(tuple=True)

        _, ax = plt.subplots(figsize=(width, height))

        # Left team
        lx_coordinates = [pos.x for pos in left_faults]
        ly_coordinates = [pos.y for pos in left_faults]

        # Right team
        rx_coordinates = [pos.x for pos in right_faults]
        ry_coordinates = [pos.y for pos in right_faults]

        scatter_left = ax.scatter(lx_coordinates, ly_coordinates, 
                                color = self.__config["left_color"],
                                marker = 'o',
                                s = 25)

        scatter_right = ax.scatter(rx_coordinates, ry_coordinates,
                                color = self.__config["right_color"],
                                marker = 'o',
                                s = 25)

        ax.set_title(title)
        ax.legend((scatter_left, scatter_right), (self.__config["name_left"], self.__config["name_right"]), scatterpoints = 1)
        ax.margins(x = 1, y = 1)

        img = plt.imread(self.__config["sim2d_field_img"])
        ax.imshow(img, zorder = -1, extent=[-56, 56, -34, 34])

        plt.show()
