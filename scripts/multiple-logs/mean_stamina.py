"""
This program gets all the .csv files in a given directory (as an argument) and outputs an image with the mean stamina plot for each team
Note that if a team is in more than one game, the mean stamina is calculated cumulatively
"""

import os
import sys

import pandas as pd
from matplotlib import pyplot as plt

PLAYER_L1_STAMINA_COLUMN = 29
PLAYER_R1_STAMINA_COLUMN = 370
COLUMNS_BETWEEN_EACH_PLAYER = 31

# gets a path as an argumment from the command the line
path = sys.argv[1]

# creates the time list
time = list(range(0, 5999))

# creates the list of mean_stamina_per_team (yet empty)
mean_stamina_per_team_x_time_names = [] # this will be a list of strings
mean_stamina_per_team_x_time = [] # this will be a list of lists

# for each .csv file,
counter = -1
for file in os.listdir(path):
    counter += 1

    # opens the given .csv file with pandas
    df = pd.read_csv(path + "/" + file) 

    # removes the duplicate lines (from halted game)
    df = df.drop_duplicates(subset=["show_time"])

    # gets the team's names
    team_l_name =  df.iloc[1][2] 
    team_r_name = df.iloc[1][3]

    # reduces and splits the df into two df's, with only the stamina data
    team_l_stamina_df = df.filter(regex="player_l.*_attribute_stamina$")
    team_r_stamina_df = df.filter(regex="player_r.*_attribute_stamina$")

    # takes the mean of each row (showtime)
    team_l_stamina_df["mean"] = team_l_stamina_df.mean(axis=1)
    team_r_stamina_df["mean"] = team_r_stamina_df.mean(axis=1)


    # adds this mean to the mean_stamina_per_team_x_time list (making the necessary operations)
    for team in [[team_l_name,team_l_stamina_df], [team_r_name, team_r_stamina_df]]:
        if (team[0] not in mean_stamina_per_team_x_time_names):
            mean_stamina_per_team_x_time_names.append(team[0])
            mean_stamina_per_team_x_time.append(team[1]["mean"].tolist())
        else:
            for i in range(0, len(mean_stamina_per_team_x_time_names)):
                if (mean_stamina_per_team_x_time_names[i] == team[0]):
                    mean_stamina_per_team_x_time[i] = [(x + y) / 2 for x, y in zip(mean_stamina_per_team_x_time[i], team[1]["mean"].tolist())]


# plots a graph with all the stuff
fig, ax = plt.subplots()
plt.subplots_adjust(left = 0.09, right = 0.99)
ax.set_title("Mean stamina of each team")
lines = []
for i in range(0, len(mean_stamina_per_team_x_time)):
    line, = ax.plot(time, mean_stamina_per_team_x_time[i], label=mean_stamina_per_team_x_time_names[i])
    lines.append(line)

leg = ax.legend(fancybox=True, shadow=True)

### the code below was adapted from official matplotlib docs to implement a clickable legend
lined = {} # will map legend lines to original lines
for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(True)    # enable picking on the legend line
    lined[legline] = origline

def on_pick(event):
    # On the pick event, find the original line corresponding to the legend proxy line, and toggle its visibility.
    legline = event.artist
    origline = lined[legline]
    visible = not origline.get_visible()
    origline.set_visible(visible)
    # change the alpha on the line in the legend so we can see what lines have been toggled
    legline.set_alpha(1.0 if visible else 0.2)
    fig.canvas.draw()

fig.canvas.mpl_connect("pick_event", on_pick)

plt.show()