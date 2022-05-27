from cProfile import label
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import seaborn as sns
import os

import socceranalyzer
from socceranalyzer.common.chore.match_analyzer import MatchAnalyzer


class AdapterHelper:
    def __init__(self, config) -> None:
        self.__team_side_altered: str = ""
        self.__initial_color: str = ""
        self.__config: dict[str, str] = config


    def valid_player_unum(self, player_list) -> bool:
        if player_list == []:
            print(f'socceranalyzer: player_unum list is empty.')
            return False

        if(len(player_list) > 11):
            print(f'socceranalyzer: player_unum list is too big.')
            return False
        
        for unum in player_list:
            if unum <= 0 or unum >= 12:
                print(f'socceranalyzer: {unum} out of bounds.')
                return False

        return True


    def team_color_validate(self) -> None:
        alt_color = self.__config["alt_color"]

        if self.__config["left_color"] == "green":
            self.__team_side_altered = "left"
            self.__initial_color = "green"
            self.__config["left_color"] = self.__config["alt_color"]
        elif self.__config["right_color"] == "green":
            self.__team_side_altered = "right"
            self.__initial_color = "green"
            self.__config["right_color"] = self.__config["alt_color"]

        if self.__team_side_altered != "":
            print(f'socceranalyzer: The {self.__team_side_altered} team has the same color of the field, changing {self.__team_side_altered}_color to {alt_color}.')


    def team_color_restore(self) -> None:
        if self.__team_side_altered == "":
            return
        else:
            if self.__team_side_altered == "left":
                self.__config["left_color"] = self.__initial_color
            else:
                self.__config["right_color"] = self.__initial_color

            print(f'socceranalyzer: Restored {self.__team_side_altered} team to it\'s initial color: {self.__initial_color}.')

        self.__initial_color = ""
        self.__team_side_altered = ""

class JupyterAdapter:
    def __init__(self, match_analyzer: MatchAnalyzer) -> None:
        self.__match_analyzer = match_analyzer
        self.__config: dict[str, str] = {}
        self._helper: AdapterHelper = AdapterHelper(self.__config)

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
            self.__config["alt_color"] = 'yellow'
            self.__config["autopct"] = '%.1f%%'


    def ball_possession(self, width: int, height: int, title: str = "Ball Possession") -> None:
        sns.set()
        left_possession, right_possession = self.__match_analyzer.ball_possession.results()
        
        _, ax = plt.subplots(figsize=(width, height))
        ax.pie([left_possession, right_possession], 
                colors = [self.__config["left_color"], self.__config["right_color"]],
                labels = [self.__config["left_label"], self.__config["right_label"]],
                shadow = self.__config["shadow"],
                startangle = self.__config["startangle"],
                autopct= self.__config["autopct"])
        
        ax.set_title(title)

        plt.show()


    def fault_position(self, width: int = 10, height: int = 10, title: str = "Foul charges"):
        self._helper.team_color_validate()
    
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

        self._helper.team_color_restore()


    def playmodes(self, width: int = 15, height: int = 10, title: str = "Playmodes"):
        sns.set()
        data = self.__match_analyzer.playmodes.results()

        _, ax = plt.subplots(figsize =(width, height))
        ax.barh(data[0], data[1])

        ax.xaxis.set_tick_params(pad = 5)
        ax.yaxis.set_tick_params(pad = 10)

        # Cosmetic config
        ax.grid(visible = True, color ='grey',
                linestyle ='-.', linewidth = 0.5,
                alpha = 0.5)
        ax.invert_yaxis()
        ax.set_title(title)

        plt.show()


    def stamina(self, left_players_unum: list[int] = [], right_players_unum: list[int] = [], width: int = 20 , height: int = 10, title: str = "Stamina"):
        sns.set()
        left_players = self.__match_analyzer.stamina.stamina_left
        right_players = self.__match_analyzer.stamina.stamina_right

        if self._helper.valid_player_unum(left_players_unum) == True:

            _, ax = plt.subplots(figsize=(width, height))

            for ith_player in left_players_unum:
                plt.plot(left_players[ith_player - 1], label=f'Player {ith_player}')

            ax.set_title(title)
            plt.legend()
            plt.show()

        if self._helper.valid_player_unum(right_players_unum) == True:

            _, ax = plt.subplots(figsize=(width, height))

            for ith_player in right_players_unum:
                plt.plot(right_players[ith_player - 1], label=f'Player {ith_player}')
            
            ax.set_title(title)
            plt.legend()
            plt.show()