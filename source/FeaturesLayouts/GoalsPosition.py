from PyQt5 import QtWidgets
from utility_functions import clear_main_mdi_area, is_robocin, find_unique_event_ocurrences, find_last_who_kicked
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas 
import numpy

BALL_X = 10
BALL_Y = 11

def goals_position(MainWindow, game_data):
    # configure the plot
    figure = plt.figure()
    axes = figure.add_subplot(111)
    canvas = FigureCanvas(figure)

    # add the mdiSubwindow with the plot as its inner widget
    sub_window = MainWindow.mdiArea.addSubWindow(canvas)
    MainWindow.mdiArea_sub_windows_list.append(sub_window)
    sub_window.showMaximized() 

    # Calculate goals array
    goals = list()
    goals_array = find_unique_event_ocurrences.find_unique_event_ocurrences(game_data.get_dataframe(), "goal")
    for item in goals_array:
        # goals.append("Player: {}\nShowTime: {}".format(str(item), find_last_who_kicked.find_last_who_kicked(item)))
        goals.append("Player: {}\nShowTime: {}".format(find_last_who_kicked.find_last_who_kicked(game_data.get_dataframe(), item),str(item)))
    goals_list_counter = 0

    # organize the data
    dataframe = game_data.get_dataframe()
    team_l_x_positions = []
    team_l_y_positions = []
    team_r_x_positions = []
    team_r_y_positions = []
    team_l_goals = []
    team_r_goals = []

    for i in range(len(dataframe)):
        if(dataframe.iloc[i,1] == "goal_l" and dataframe.iloc[i-1,1] != "goal_l"):
            team_l_x_positions.append(int(dataframe.iloc[i,BALL_X]))
            team_l_y_positions.append(int(dataframe.iloc[i,BALL_Y]))
            team_l_goals.append(goals[goals_list_counter])
            goals_list_counter += 1
        elif(dataframe.iloc[i,1] == "goal_r" and dataframe.iloc[i-1,1] != "goal_r"):
            team_r_x_positions.append(int(dataframe.iloc[i,BALL_X]))
            team_r_y_positions.append(int(dataframe.iloc[i,BALL_Y]))
            team_r_goals.append(goals[goals_list_counter])
            goals_list_counter += 1

    team_l_color = game_data.get_team(0).get_color()
    team_r_color = game_data.get_team(1).get_color()

    team_l_label = game_data.get_team(0).get_name()
    team_r_label = game_data.get_team(1).get_name()

    team_l_number_of_fouls = game_data.get_team(0).get_number_of_fouls_commited()
    team_r_number_of_fouls = game_data.get_team(1).get_number_of_fouls_commited()
    # total_number_of_fouls = team_l_number_of_fouls + team_r_number_of_fouls

    # call plotting functions

    # for i in range(0, total_number_of_fouls):
    #     axes.scatter(team_l_x_positions if i < team_l_number_of_fouls else team_r_x_positions, team_l_y_positions if i < team_l_number_of_fouls else team_r_y_positions, color = team_l_color if i<team_l_number_of_fouls else team_r_color, label = [team_l_label, team_r_label], marker = '.', s = 25)
 

        # plots the team l fouls
    for i in range(0, team_r_number_of_fouls):
        scatter_1 = axes.scatter(team_l_x_positions, team_l_y_positions, color = team_l_color, marker = 'o', s = 25, data = [1,2])
        # plots the team r fouls
    for i in range(0, team_l_number_of_fouls):
        scatter_2 = axes.scatter(team_r_x_positions, team_r_y_positions, color = team_r_color, marker = 'o', s = 25, data = [10, 20])

        # general customizing
    axes.set_title("Fouls Position")
    axes.set_xlabel('X')
    axes.set_ylabel('Y')	
    axes.legend((scatter_1, scatter_2),(team_l_label, team_r_label),scatterpoints=1)
    axes.margins(x = 1, y = 1)

        # background image
    img = plt.imread("../files/images/soccerField.png")
    axes.imshow(img, zorder = -1, extent=[-56, 56, -34, 34])

#------------------------------------------------------------


#-----------------------------------------------------------
# https://stackoverflow.com/questions/7908636/possible-to-make-labels-appear-when-hovering-over-a-point-in-matplotlib
# Sets up the hover annotations
    # names = numpy.array(list("AB"))
    names = numpy.array(goals)
    cmap = plt.cm.RdYlGn
    norm = plt.Normalize(1,4)
    c = numpy.random.randint(1,5,size=15)

    annot = axes.annotate("", xy=(0,0), xytext=(-20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

    def update_annot(ind, cont):
        if(cont == 1):
            position = ind["ind"][0]
            # position = ind["ind"][0] if cont==1 else (ind["ind"][0])
            pos = scatter_1.get_offsets()[position]
        else:
            position = ind["ind"][0]
            # position = ind["ind"][0] if cont==1 else (ind["ind"][0] + len(team_l_goals))
            pos = scatter_2.get_offsets()[position]
            
        annot.xy = pos
        text = "Goal: {}\n{}".format(str((1) + (position if cont==1 else (position + len(team_l_goals)))), names[position if cont==1 else (position + len(team_l_goals))])
        # text = "Goal: {}\n{}".format(str(1 + position), names[position])
        annot.set_text(text)
        annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
        annot.get_bbox_patch().set_alpha(0.4)


    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == axes:
            cont1, ind1 = scatter_1.contains(event)
            cont2, ind2 = scatter_2.contains(event)
            # print(ind1)
            # print("\n")
            # print(ind2)
            if (cont1 or cont2):
                update_annot(ind1 if cont1==True else ind2, 1 if cont1==True else 2)
                annot.set_visible(True)
                figure.canvas.draw_idle()
            else:
                if vis:
                    annot.set_visible(False)
                    figure.canvas.draw_idle()

    figure.canvas.mpl_connect("motion_notify_event", hover)