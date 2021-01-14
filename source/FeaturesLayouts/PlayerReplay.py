from PyQt5 import QtWidgets
from utility_functions import clear_main_mdi_area, find_unique_event_ocurrences
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import seaborn as sb


def player_replay(MainWindow, game_data):
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

    team_1_score = game_data.get_team(0).get_number_of_goals_scored()
    team_2_score = game_data.get_team(1).get_number_of_goals_scored()
    total_score = team_1_score + team_2_score
    for i in range(0, total_score):
        entity_combobox_items.append(entity_combobox.addItem("Goal_{}_{}".format(i, game_data.get_team(0).get_name())))

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

    # set data
    player_n = 1
    amount_of_cycles = 100
    dataframe = game_data.get_dataframe()

    side = "l" 
    goal_occurrences_l = find_unique_event_ocurrences.find_unique_event_ocurrences(dataframe, "goal_l")
    goal_occurrences_r = find_unique_event_ocurrences.find_unique_event_ocurrences(dataframe, "goal_r")

    end_time = goal_occurrences_l[0]
    start_time = goal_occurrences_r[0] - amount_of_cycles

    player_row_x = "player_{}{}_x".format(side,player_n)
    player_row_y = "player_{}{}_y".format(side,player_n)
    
    player_replay_x = []
    player_replay_y = []


    for i in range(0, amount_of_cycles):
        player_replay_x.append(dataframe.loc[start_time + i, player_row_x])
        player_replay_y.append(dataframe.loc[start_time + i, player_row_y])


    # background image
    img = plt.imread("../files/images/soccerField.png")
    axes.imshow(img, zorder = -1, extent=[-56, 56, -34, 34])

    # plot graph
    sb.lineplot(x = player_replay_x, y = player_replay_y, label = "Ball trajectory 100 cycles before the goal", ax=axes)

def item_changed(index, game_data, axes, figure):
    plt.cla()