from PyQt5 import QtWidgets
from utility_functions import clear_main_mdi_area
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas 

def fouls_quantity(MainWindow, game_data):
    # configure the plot
    figure = plt.figure()
    axes = figure.add_subplot(111)
    canvas = FigureCanvas(figure)


    # add the mdiSubwindow with the plot as its inner widget
    sub_window = MainWindow.mdiArea.addSubWindow(canvas)
    MainWindow.mdiArea_sub_windows_list.append(sub_window)
    sub_window.showMaximized() 

    # organize the data
        # axis
    x_label = "Team Name"
    y_label = "Number of fouls commited"
        # general bar
    bar_width = 1
        # bar 1
    bar1_color = "#7da67d"
    bar1_x_coordinate = game_data.get_team(0).get_name() 
    bar1_y_coordinate = game_data.get_team(0).get_number_of_fouls_commited()
        # bar 2
    bar2_color = "#ffa1a1"
    bar2_x_coordinate = game_data.get_team(1).get_name() 
    bar2_y_coordinate = game_data.get_team(1).get_number_of_fouls_commited()   
    
    # call plotting functions
        # bar1
    bar1_plot = axes.bar(bar1_x_coordinate, bar1_y_coordinate, bar_width, color = bar1_color)
        # bar 2
    bar2_plot = axes.bar(bar2_x_coordinate, bar2_y_coordinate, bar_width, color = bar2_color)
