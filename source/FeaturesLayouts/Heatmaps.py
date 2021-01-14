from PyQt5 import QtWidgets
from utility_functions import clear_main_mdi_area
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas 
import seaborn as sb
from PyQt5 import QtGui
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

def heatmaps(MainWindow, game_data):
    # configure the plot
    figure = plt.figure()
    axes = figure.add_subplot(111)
    canvas = FigureCanvas(figure)

        # matplotlib toolbox menu
    toolbox =  NavigationToolbar(canvas, MainWindow)
    #TODO: shrink the space occupied by the matplotlib navigation toolbar

        # entity selection combobox
    entity_combobox = QtWidgets.QComboBox()
    entity_combobox_items = []
    entity_combobox_items.append(entity_combobox.addItem("Ball"))
    for i in range(1, 12):
        entity_combobox_items.append(entity_combobox.addItem("Player_{}_{}".format(game_data.get_team(0).get_name(),i)))
    for i in range(1, 12):
        entity_combobox_items.append(entity_combobox.addItem("Player_{}_{}".format(game_data.get_team(1).get_name(),i)))

    entity_combobox.currentIndexChanged.connect(lambda index:item_changed(index, game_data, axes, figure))

        # horizontal space for the navigation toolbar and the custom buttons
    horizontal_space = QtWidgets.QHBoxLayout() 
    horizontal_space.addWidget(toolbox)
    horizontal_space.addWidget(entity_combobox)
    small_box = QtWidgets.QGroupBox()
    small_box.setLayout(horizontal_space)

        # vertical space for the canvas and the horizontal space
    vertical_space = QtWidgets.QVBoxLayout()
    vertical_space.addWidget(small_box)
    vertical_space.addWidget(canvas)
    box_layout = QtWidgets.QGroupBox()
    box_layout.setLayout(vertical_space)

    # add the mdiSubwindow with the plot as its inner widget
    sub_window = MainWindow.mdiArea.addSubWindow(box_layout)
    MainWindow.mdiArea_sub_windows_list.append(sub_window)
    sub_window.showMaximized()

    # plot the ball plot
    plot_position_heatmap(game_data, axes, "ball_x", "ball_y")

def plot_position_heatmap(game_data, axes, string1, string2):
    # organize the data
    data_frame = game_data.get_dataframe()

    heatmap_string_1 = string1 
    heatmap_string_2 = string2

    shade_value = True
    color_value = "green"
    n_levels_value = 10

    # call plotting functions
    sb.kdeplot(data_frame[heatmap_string_1], data_frame[heatmap_string_2], ax=axes, shade=shade_value, color=color_value, n_levels=n_levels_value) #TODO: I think this computation of "data_frame[heatmap_string_1]" should be done in the computing module, so the program would only need to load anything on start

def item_changed(index, game_data, axes, figure):
    plt.cla()
    if(index==0):
        plot_position_heatmap(game_data, axes, "ball_x", "ball_y")
    elif(index<12):
        plot_position_heatmap(game_data, axes, "player_l{}_x".format(index), "player_l{}_y".format(index))
    else:
        plot_position_heatmap(game_data, axes, "player_r{}_x".format(index-11), "player_r{}_y".format(index-11))