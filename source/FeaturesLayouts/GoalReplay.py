from PyQt5 import QtWidgets
from utility_functions import clear_main_mdi_area, find_unique_event_ocurrences, copy_dataframe_subset_by_rows
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import seaborn as sb

def goal_replay(MainWindow, game_data):
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
    for i in range(1, total_score+1):
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

    # organize the data
    dataframe = game_data.get_dataframe() 

    # isso aqui ta meio gambiarrado. TODO: desgambiarrar

    # background image
    # draw_background_image("../files/images/soccerField.png", axes) 
    
    # plot graph
    item_changed(0, game_data, axes, figure)

def draw_background_image(file_path, axes): 
    img = plt.imread(file_path)
    axes.imshow(img, zorder = -1, extent=[-56, 56, -34, 34])


def plot_ball_replay(dataframe, initial_row, final_row, ax_value):
    cut_dataframe = copy_dataframe_subset_by_rows.copy_dataframe_subset_by_rows(dataframe, initial_row, final_row)
    print(cut_dataframe)
    cut_dataframe.plot(title = "Goal Replay", x="ball_x", y="ball_y", label="Ball trajectory 100 cycles before the goal", ax = ax_value)

def item_changed(index, game_data, axes, figure):
    plt.cla()
    draw_background_image("../files/images/soccerField.png", axes)
    all_goals_rows = find_unique_event_ocurrences.find_unique_event_ocurrences(game_data.get_dataframe(), "goal")
    plot_ball_replay(game_data.get_dataframe(), all_goals_rows[index-1]-100, all_goals_rows[index-1], axes) 