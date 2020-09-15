from PyQt5 import QtWidgets
from utility_functions import clear_main_mdi_area
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar  
import seaborn as sb

def stamina_tracker(MainWindow, game_data):
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
    sub_window.showMaximized()    # organize the data
    plot_stamina(game_data, "l", 1)


def plot_stamina(game_data, side, player_number): 
    player_row_stamina = "player_{}{}_attribute_stamina".format(side,player_number) 

    player_stamina = []
    x_coordinate = []

    for i in range(0, 6000):
        player_stamina.append(game_data.get_dataframe().loc[i, player_row_stamina])
        x_coordinate.append(i)

    # call plotting functions
    sb.lineplot(x_coordinate,player_stamina)

def item_changed(index, game_data, axes, figure):
    plt.cla()
    if(index<11):
        plot_stamina(game_data, "l", index)
    else:
        plot_stamina(game_data, "r", index-11)
