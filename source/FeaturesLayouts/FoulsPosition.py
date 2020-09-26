from PyQt5 import QtWidgets
from utility_functions import clear_main_mdi_area, is_robocin
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas 

BALL_X = 10
BALL_Y = 11

def fouls_position(MainWindow, game_data):
    # configure the plot
    figure = plt.figure()
    axes = figure.add_subplot(111)
    canvas = FigureCanvas(figure)

    # add the mdiSubwindow with the plot as its inner widget
    sub_window = MainWindow.mdiArea.addSubWindow(canvas)
    MainWindow.mdiArea_sub_windows_list.append(sub_window)
    sub_window.showMaximized() 

    # organize the data
    dataframe = game_data.get_dataframe()
    team_l_x_positions = []
    team_l_y_positions = []
    team_r_x_positions = []
    team_r_y_positions = []

    for i in range(len(dataframe)):
        if(dataframe.iloc[i,1] == "foul_charge_l" and dataframe.iloc[i-1,1] != "foul_charge_l"):
            team_l_x_positions.append(int(dataframe.iloc[i,BALL_X]))
            team_l_y_positions.append(int(dataframe.iloc[i,BALL_Y]))
        elif(dataframe.iloc[i,1] == "foul_charge_r" and dataframe.iloc[i-1,1] != "foul_charge_r"):
            team_r_x_positions.append(int(dataframe.iloc[i,BALL_X]))
            team_r_y_positions.append(int(dataframe.iloc[i,BALL_Y]))

    team_l_color = game_data.get_team(0).get_color()
    team_r_color = game_data.get_team(1).get_color()

    team_l_label = game_data.get_team(0).get_name()
    team_r_label = game_data.get_team(1).get_name()

    team_l_number_of_fouls = game_data.get_team(0).get_number_of_fouls_commited()
    team_r_number_of_fouls = game_data.get_team(1).get_number_of_fouls_commited()
    total_number_of_fouls = team_l_number_of_fouls + team_r_number_of_fouls

    # call plotting functions

    # for i in range(0, total_number_of_fouls):
    #     axes.scatter(team_l_x_positions if i < team_l_number_of_fouls else team_r_x_positions, team_l_y_positions if i < team_l_number_of_fouls else team_r_y_positions, color = team_l_color if i<team_l_number_of_fouls else team_r_color, label = [team_l_label, team_r_label], marker = '.', s = 25)
 

        # plots the team l fouls
    for i in range(0, team_r_number_of_fouls):
        scatter_1 = axes.scatter(team_l_x_positions, team_l_y_positions, color = team_l_color, marker = 'o', s = 25)
        # plots the team r fouls
    for i in range(0, team_l_number_of_fouls):
        scatter_2 = axes.scatter(team_r_x_positions, team_r_y_positions, color = team_r_color, marker = 'o', s = 25)

        # general customizing
    axes.set_title("Fouls Position")
    axes.set_xlabel('X')
    axes.set_ylabel('Y')	
    axes.legend((scatter_1, scatter_2),(team_l_label, team_r_label),scatterpoints=1)
    axes.margins(x = 1, y = 1)

        # background image
    img = plt.imread("../files/images/soccerField.png")
    axes.imshow(img, zorder = -1, extent=[-56, 56, -34, 34])