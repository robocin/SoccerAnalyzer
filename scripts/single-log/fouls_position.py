import pandas as pd
import matplotlib.pyplot as plt
import sys

BALL_X = 10
BALL_Y = 11


# configure the plot
figure = plt.figure()
axes = figure.add_subplot(111)

# organize the data
    # gets a path as an argumment from the command the line
path = sys.argv[1]
dataframe = pd.read_csv(path)
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

team_l_color = "deepskyblue"
team_r_color = "tomato" 

team_l_label = dataframe.iloc[3][2]
team_r_label = dataframe.iloc[3][3]


# call plotting functions

    # plots the team l fouls
scatter_1 = axes.scatter(team_l_x_positions, team_l_y_positions, color = team_l_color, marker = 'o', s = 25)
    # plots the team r fouls
scatter_2 = axes.scatter(team_r_x_positions, team_r_y_positions, color = team_r_color, marker = 'o', s = 25)

    # general customizing
axes.set_title("Fouls Position")
axes.set_xlabel('X')
axes.set_ylabel('Y')	
axes.legend((scatter_1, scatter_2),(team_l_label, team_r_label),scatterpoints=1)
axes.margins(x = 1, y = 1)

    # background image
img = plt.imread("files/images/soccerField.png")
axes.imshow(img, zorder = -1, extent=[-56, 56, -34, 34])

plt.show()