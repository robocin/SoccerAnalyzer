from typing import Literal
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Arc

import seaborn as sns
import os

import socceranalyzer
from socceranalyzer.common.chore.match_analyzer import MatchAnalyzer
from socceranalyzer.common.enums.sim2d import Landmarks


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


    def heatmap(self, left_players_unum: list[int] = [], 
                        right_players_unum: list[int] = [],  
                        ball: int = bool,  
                        width: int = 15, 
                        height: int = 10, 
                        title: str = "Heatmap"):
        sns.set()
        left_players, right_players, ball_positions_dict = self.__match_analyzer.heatmap.data

        fig, ax = plt.subplots(figsize=(width, height))

        if ball:
            sns.kdeplot(ball_positions_dict['x'], ball_positions_dict['y'], shade="True", color="green", n_levels = 10)
            plt.title(f'{title}')
            plt.ylim(-35,35)
            plt.xlim(-55,55)
            plt.show()
            
        else:
            for player in left_players:
                sns.kdeplot(player[0], player[1], shade = "True", color = "green", n_levels = 10)
                plt.title(f'{title}')
                plt.ylim(-35,35)
                plt.xlim(-55,55)
                plt.show()

            for player in right_players:
                sns.kdeplot(player[0], player[1], shade = "True", color = "green", n_levels = 10)
                plt.title(f'{title}')
                plt.ylim(-35,35)
                plt.xlim(-55,55)
                plt.show()

    
    def draw_pitch(self, figsize: (tuple[float, float])=(10, 6), color: Literal['green', 'white']='white') -> tuple[Figure, Axes]:
        """
        Creates a plot of the offical Robocup 2D soccer pitch with size 105x68 meters.

            Parameters:
                figsize(tuple[float, float]): Width, height in inches
                color('green' | 'white'): Color of the pitch
            Returns:
                fig: `matplotlib.figure.Figure`
                ax: `matplotlib.axes.Axes` or array of Axes
        """
        fig, ax = plt.subplots(1, figsize=figsize)
        linecolor = ''
        pitch_color = ''
        if color == 'green':
            linecolor = 'white'
            pitch_color='darkgreen'
            rect = Rectangle((Landmarks.LEFT_BOTTOM.value[0]-4., Landmarks.LEFT_BOTTOM.value[1]-4.), 
                                Landmarks.PITCH_SIZE.value[0]+8., Landmarks.PITCH_SIZE.value[1]+8.,
                                linewidth=0.1, edgecolor='r', facecolor=pitch_color, zorder=0)
            ax.add_patch(rect)            
        elif color == 'white':
            linecolor = 'black'
            pitch_color = 'white'
        else:
            raise ValueError(f'color argument must be either \'green\' or \'white\', but \'{color}\' was given.')

        # Pitch outline
        ax.plot([Landmarks.LEFT_BOTTOM.value[0], Landmarks.RIGHT_BOTTOM.value[0]], 
                [Landmarks.LEFT_BOTTOM.value[1], Landmarks.RIGHT_BOTTOM.value[1]], color=linecolor)
        ax.plot([Landmarks.LEFT_TOP.value[0], Landmarks.RIGHT_TOP.value[0]], 
                [Landmarks.LEFT_TOP.value[1], Landmarks.RIGHT_TOP.value[1]], color=linecolor)
        ax.plot([Landmarks.LEFT_BOTTOM.value[0], Landmarks.LEFT_TOP.value[0]], 
                [Landmarks.LEFT_BOTTOM.value[1], Landmarks.LEFT_TOP.value[1]], color=linecolor)
        ax.plot([Landmarks.RIGHT_BOTTOM.value[0], Landmarks.RIGHT_TOP.value[0]], 
                [Landmarks.RIGHT_BOTTOM.value[1], Landmarks.RIGHT_TOP.value[1]], color=linecolor)
        ax.plot([Landmarks.CENTER_BOTTOM.value[0], Landmarks.CENTER_TOP.value[0]], 
                [Landmarks.CENTER_BOTTOM.value[1], Landmarks.CENTER_TOP.value[1]], color=linecolor)        
        center_circle = Circle(Landmarks.CENTER.value, 9.15, edgecolor=linecolor, facecolor=pitch_color)
        center_spot = Circle(Landmarks.CENTER.value, .3, color=linecolor)
        ax.add_patch(center_circle)
        ax.add_patch(center_spot)

        # Goal boxes
        ax.plot([Landmarks.L_PEN_BOTTOM.value[0], Landmarks.L_PEN_TOP.value[0]], 
                [Landmarks.L_PEN_BOTTOM.value[1], Landmarks.L_PEN_TOP.value[1]], color=linecolor)
        ax.plot([Landmarks.L_PEN_BOTTOM.value[0], Landmarks.LEFT_BOTTOM.value[0]], 
                [Landmarks.L_PEN_BOTTOM.value[1], Landmarks.L_PEN_BOTTOM.value[1]], color=linecolor)
        ax.plot([Landmarks.L_PEN_TOP.value[0], Landmarks.LEFT_TOP.value[0]], 
                [Landmarks.L_PEN_TOP.value[1], Landmarks.L_PEN_TOP.value[1]], color=linecolor)
        left_arc = Arc(Landmarks.L_PEN_C.value, 9.15, 16, theta1=270.0, theta2=90.0, color=linecolor)
        left_pen_spot = Circle(Landmarks.L_PEN_SPOT.value, 0.3, color=linecolor)
        ax.add_patch(left_arc)
        ax.add_patch(left_pen_spot)

        ax.plot([Landmarks.R_PEN_BOTTOM.value[0], Landmarks.R_PEN_TOP.value[0]], 
                [Landmarks.R_PEN_BOTTOM.value[1], Landmarks.R_PEN_TOP.value[1]], color=linecolor)
        ax.plot([Landmarks.R_PEN_BOTTOM.value[0], Landmarks.RIGHT_BOTTOM.value[0]], 
                [Landmarks.R_PEN_BOTTOM.value[1], Landmarks.R_PEN_BOTTOM.value[1]], color=linecolor)
        ax.plot([Landmarks.R_PEN_TOP.value[0], Landmarks.RIGHT_TOP.value[0]], 
                [Landmarks.R_PEN_TOP.value[1], Landmarks.R_PEN_TOP.value[1]], color=linecolor)
        right_arc = Arc(Landmarks.R_PEN_C.value, 9.15, 16, theta1=90.0, theta2=270.0, color=linecolor)
        right_pen_spot = Circle(Landmarks.R_PEN_SPOT.value, 0.3, color=linecolor)
        ax.add_patch(right_arc)
        ax.add_patch(right_pen_spot)

        # Goals
        ax.plot([Landmarks.L_GOAL_BOTTOM_BAR.value[0], Landmarks.L_GOAL_BOTTOM_BAR.value[0]-2.], 
                [Landmarks.L_GOAL_BOTTOM_BAR.value[1], Landmarks.L_GOAL_BOTTOM_BAR.value[1]], color=linecolor)
        ax.plot([Landmarks.L_GOAL_TOP_BAR.value[0], Landmarks.L_GOAL_TOP_BAR.value[0]-2.], 
                [Landmarks.L_GOAL_TOP_BAR.value[1], Landmarks.L_GOAL_TOP_BAR.value[1]], color=linecolor)
        ax.plot([Landmarks.L_GOAL_BOTTOM_BAR.value[0]-2., Landmarks.L_GOAL_TOP_BAR.value[0]-2.], 
                [Landmarks.L_GOAL_BOTTOM_BAR.value[1], Landmarks.L_GOAL_TOP_BAR.value[1]], color=linecolor)
        ax.plot([Landmarks.R_GOAL_BOTTOM_BAR.value[0], Landmarks.R_GOAL_BOTTOM_BAR.value[0]+2.], 
                [Landmarks.R_GOAL_BOTTOM_BAR.value[1], Landmarks.R_GOAL_BOTTOM_BAR.value[1]], color=linecolor)
        ax.plot([Landmarks.R_GOAL_TOP_BAR.value[0], Landmarks.R_GOAL_TOP_BAR.value[0]+2.], 
                [Landmarks.R_GOAL_TOP_BAR.value[1], Landmarks.R_GOAL_TOP_BAR.value[1]], color=linecolor)
        ax.plot([Landmarks.R_GOAL_BOTTOM_BAR.value[0]+2., Landmarks.R_GOAL_TOP_BAR.value[0]+2.], 
                [Landmarks.R_GOAL_BOTTOM_BAR.value[1], Landmarks.R_GOAL_TOP_BAR.value[1]], color=linecolor)
        
        
        plt.axis('off')
        plt.tight_layout()
        plt.gca().set_aspect('equal', adjustable='box')

        return fig, ax


    def __draw_pitch(self, fig_size: tuple[int, int]=(15, 4), amount=2, stack_horizontally=True) -> tuple[Figure, Axes]:
        """
        Draws specified amount of pitches and returns a figure and axes with the drawn pitches.

            Parameters:
                    fig_size (tuple[int, int]): Tuple indicating total figure size
                    amount (int): Amount of pitches to draw
                    stack_horizontally (bool): Stack pitches horizontally or vertically
            Returns:
                    fig, axs (tuple[Figure, Axes]): Figure and Axes drawn
        """
        fig, axs=plt.subplots(1, amount, figsize=fig_size) if stack_horizontally else plt.subplots(amount, 1, figsize=fig_size)
        linecolor='black'

        for ax in axs:
            ax.plot([0,68],[0,0], color=linecolor)
            ax.plot([68,68],[52.5,0], color=linecolor)
            ax.plot([0,0],[52.5,0], color=linecolor)
            
            #Left Penalty Area
            ax.plot([13.84,13.84],[0,16.5],color=linecolor)
            ax.plot([13.84,54.16],[16.5,16.5],color=linecolor)
            ax.plot([54.16,54.16],[0,16.5],color=linecolor)    
            
            #Goal
            ax.plot([41.01,41.01],[-2,0],color=linecolor)
            ax.plot([26.99,41.01],[-2,-2],color=linecolor)
            ax.plot([26.99,26.99],[0,-2],color=linecolor)
        
            #Prepare Circles
            leftPenSpot = plt.Circle((68/2,11),0.4,color=linecolor)
            
            #Draw Circles
            ax.add_patch(leftPenSpot)

            #Prepare Arcs
            leftArc = Arc((34,11),height=18,width=18,angle=0,theta1=38,theta2=142,color=linecolor)
            
            #Draw Arcs
            ax.add_patch(leftArc)
            
            #Tidy Axes
            ax.axis('off')
        
        return fig, axs

    
    def plot_shot_frequency(self) -> tuple[Figure, Axes]:
        """
        Plots shot frequency hexbin graph in the pitch and returns figure and axes where it was drawn.

            Returns:
                    fig, axs (tuple[Figure, Axes]): Figure and Axes drawn
        """
        (fig, axs) = self.__draw_pitch(fig_size=(10, 4))
        chart_data = self.__match_analyzer.shooting.results_as_dataframe()[['team', 'x', 'y']]
        for i,shot in chart_data.iterrows():
            chart_data.at[i,'x']=52.5-shot['x']
            chart_data.at[i,'y']=34+shot['y']
        for ax, team, team_name in zip(axs,['l', 'r'],[self.__config["name_left"], self.__config["name_right"]]):
            team_data=chart_data[chart_data['team'] == team]
            pos=ax.hexbin(data=team_data, x='y', y='x',zorder=1,cmap='OrRd',gridsize=(25,10),alpha=.7,extent=(0,68,0,52.5))
            ax.set_xlim(-1, 69)
            ax.set_ylim(-3,52.5)
            ax.set_title(f'Frequency of shots: {team_name}')
            plt.colorbar(pos, ax=ax)
            plt.tight_layout()
            plt.gca().set_aspect('equal', adjustable='box')
        return fig, axs

    
    def plot_shot_log(self) -> tuple[Figure, Axes]:
        """
        Plots all shots registered in a scatter graph of the pitch and returns figure and axes where
        it was drawn.

            Returns:
                    fig, axs (tuple[Figure, Axes]): Figure and Axes drawn
        """
        (fig, axs) = self.__draw_pitch(fig_size=(10, 4))
        chart_data = self.__match_analyzer.shooting.results_as_dataframe()[['team', 'x', 'y', 'goal']]
        for i,shot in chart_data.iterrows():
            chart_data.at[i,'x']=52.5-shot['x']
            chart_data.at[i,'y']=34+shot['y']
        for ax, team, team_name in zip(axs, ['l', 'r'], [self.__config['name_left'], self.__config['name_right']]):
            team_data = chart_data[chart_data['team'] == team]
            goals = team_data[team_data['goal']==True]
            shots = team_data[team_data['goal']==False]
            ax.plot(shots['y'], shots['x'], 'rx', label='misses', alpha=0.5)
            ax.plot(goals['y'], goals['x'], 'go', label='goals', alpha=0.5)
            ax.set_title(f'Shots: {team_name}')
            ax.legend()
            plt.xlim(-1, 69)
            plt.ylim(-3, 52.5)
            plt.tight_layout()
            plt.gca().set_aspect('equal', adjustable='box')
        return fig, axs

    
    def plot_shot_quality(self) -> tuple[Figure, Axes]:        
        """
        Plots all shots registered in a scatter graph where the size of the of the pitch means the 
        shot quality and returns figure and axes where it was drawn.

            Returns:
                    fig, axs (tuple[Figure, Axes]): Figure and Axes drawn
        """
        (fig, axs) = self.__draw_pitch(fig_size=(10, 4))
        chart_data = self.__match_analyzer.shooting.results_as_dataframe()[['team', 'x', 'y', 'xG','goal']]
        for i,shot in chart_data.iterrows():
            chart_data.at[i,'x']=52.5-shot['x']
            chart_data.at[i,'y']=34+shot['y']
        for ax, team, team_name in zip(axs, ['l', 'r'], [self.__config['name_left'], self.__config['name_right']]):
            team_data = chart_data[chart_data['team'] == team]
            goals = team_data[team_data['goal']==True]
            shots = team_data[team_data['goal']==False]
            ax.scatter(shots['y'], shots['x'], s=150*shots['xG'], c='#7e7272', label='misses', alpha=0.5)
            ax.scatter(goals['y'], goals['x'], s=150*goals['xG'], c='#981717', label='goals', alpha=0.5)
            ax.set_title(f'Shot quality {team_name}')
            ax.legend()
            plt.xlim(-1, 69)
            plt.ylim(-3, 52.5)
            plt.tight_layout()
            plt.gca().set_aspect('equal', adjustable='box')
        return fig, axs

    def passing_accuracy(self):
        sns.set()
        labels = [self.__config["left_label"], self.__config["right_label"]]
        acc_left, acc_right, total_passes_left, total_passes_right = self.__match_analyzer.passing_accuracy.results()

        correct_passes = [int(total_passes_left*acc_left), int(total_passes_right*acc_right)]
        wrong_passes = [total_passes_left-correct_passes[0], total_passes_right-correct_passes[1]]

        width = 0.5

        fig, ax = plt.subplots(figsize=(6,6))

        ax.bar(labels, correct_passes, width, label='certos', color='#36FF51', align='center')
        rects2 = ax.bar(labels, wrong_passes, width, label='errados', bottom=correct_passes, color='#FF2222')

        for i, rect in enumerate(rects2):
            text = f"{100*correct_passes[i]/(wrong_passes[i]+correct_passes[i]):2.2f}%"
            height = rect.get_height()
            ax.text(s=text, x=rect.get_x()+rect.get_width()/2,y=correct_passes[i]+wrong_passes[i], ha="center", va="bottom", color="#3ED452", fontsize=13, fontweight='bold')

        ax.set_ylabel('passes')
        ax.set_title('Passing accuracy')

        ax.legend()

        plt.show()