from PyQt5 import QtWidgets
from utility_functions import clear_main_mdi_area
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas 

def fouls_proportion(MainWindow, game_data):
    # configure the plot
    figure = plt.figure()
    axes = figure.add_subplot(111)
    canvas = FigureCanvas(figure)

    # add the mdiSubwindow with the plot as its inner widget
    sub_window = MainWindow.mdiArea.addSubWindow(canvas)
    MainWindow.mdiArea_sub_windows_list.append(sub_window)
    sub_window.showMaximized() 

    # organize the data
        # general
    pie_explode_value = (0.06, 0)
    autopct_value = '%2.2f%%'
    shadow_value = True
    startangle_value = 90
        #
    fouls_commited_by_l = game_data.get_team(0).get_number_of_fouls_commited()
    fouls_commited_by_r = game_data.get_team(1).get_number_of_fouls_commited()
    total_number_of_fouls = fouls_commited_by_l + fouls_commited_by_r 
        # data for the sector 1
    sector_1_color = "#7da67d" #TODO: with this and all features: make the color be green if it's the robocin team else make it be red
    sector_1_label = game_data.get_team(0).get_name()
    sector_1_value = (fouls_commited_by_l*100)/total_number_of_fouls #TODO:should this computation be done in the computation module?
        # data for the sector 2
    sector_2_color = "#ffa1a1" #TODO: with this and all features: make the color be green if it's the robocin team else make it be red
    sector_2_label = game_data.get_team(1).get_name()
    sector_2_value = (fouls_commited_by_r*100)/total_number_of_fouls

    # call plotting functions
    axes.pie([sector_1_value, sector_2_value], explode=pie_explode_value, labels=[sector_1_label, sector_2_label], colors=[sector_1_color, sector_2_color], autopct = autopct_value, shadow=shadow_value, startangle=startangle_value)
