from PyQt5 import QtWidgets
from utility_functions import clear_main_mdi_area
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas 

def stamina_tracker(MainWindow, game_data):
    # configure the plot
    figure = plt.figure()
    axes = figure.add_subplot(111)
    canvas = FigureCanvas(figure)

    # add the mdiSubwindow with the plot as its inner widget
    sub_window = MainWindow.mdiArea.addSubWindow(canvas)
    MainWindow.mdiArea_sub_windows_list.append(sub_window)
    sub_window.showMaximized() 

    # organize the data

    # call plotting functions


