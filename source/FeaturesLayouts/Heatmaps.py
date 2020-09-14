from PyQt5 import QtWidgets
from utility_functions import clear_main_mdi_area
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas 
import seaborn as sb

def heatmaps(MainWindow, game_data):
    # configure the plot
    figure = plt.figure()
    axes = figure.add_subplot(111)
    canvas = FigureCanvas(figure)

    # add the mdiSubwindow with the plot as its inner widget
    sub_window = MainWindow.mdiArea.addSubWindow(canvas)
    MainWindow.mdiArea_sub_windows_list.append(sub_window)
    sub_window.showMaximized() 

    # organize the data
    data_frame = game_data.get_dataframe()

    heatmap_string_1 = "ball_x"
    heatmap_string_2 = "ball_y"

    shade_value = True
    color_value = "green"
    n_levels_value = 10

    # call plotting functions
    sb.kdeplot(data_frame[heatmap_string_1], data_frame[heatmap_string_2], ax=axes, shade=shade_value, color=color_value, n_levels=n_levels_value) #TODO: I think this computation of "data_frame[heatmap_string_1]" should be done in the computing module, so the program would only need to load anything on start
    
    axes.set_xbound(lower=-56, upper=56)
    axes.set_xbound(lower=33, upper=-33)

