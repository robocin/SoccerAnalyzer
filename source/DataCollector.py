import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sb

from Team import Team
from Event import Event
from Player import Player
from Position import Position
from PlotData import PlotData

from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

#Constants
BALL_X = 10
BALL_Y = 11
TOTAL_NUMBER_OF_PLAYERS = 22
NUMBER_OF_PLAYERS_PER_TEAM = TOTAL_NUMBER_OF_PLAYERS/2
PLAYER_L1_COUNTING_KICK_LOG_DATA_FRAME_COLUMN_POSITION = 34
FIRST_COUNTING_KICK_COLUMN_L = 34
NUMBER_OF_COLUMNS_BETWEEN_COUNTING_KICKS_PLUS_ONE = 31
NUMBER_OF_COLUMNS_BETWEEN_PLAYER_X_POS_AND_PLAYER_COUNTING_KICKS_PLUS_ONE = 16
NUMBER_OF_COLUMNS_BETWEEN_PLAYER_Y_POS_AND_PLAYER_COUNTING_KICKS_PLUS_ONE = 15

class DataCollector():
	def __init__(self, log_path): #sem log_path
		
		self.__log_path = log_path
		self.__data_frame = None	

		self.__team_l = None # By instanciating the team, all the computing is scored inside the __init__ of the class Team()
		self.__team_r = None
		self.__teams = []
		self.__all_events = []
		self.__all_faults = []
		self.__all_goals = []
		self.__all_penalties = []

		# calls for data computing
		self.initialize()

	
	# Creates the Setters and Getters methods   

	def set_team_l(self, team):
		self.__team_l = team
	
	def set_log_path(self,log_path):
		self.__log_path = log_path 		

	def set_all_goals(self, all_goals):
		self.__all_goals = all_goals

	def set_all_faults(self, all_faults):
		self.__all_faults =	all_faults

	def set_all_penalties(self, all_penalties):
		self.__all_penalties = all_penalties
	
	# Getters
	
	def get_team(self, team_side):
		
		if(team_side == "l"):
			return self.__team_l
		else:
			return self.__team_r
	
	#TODO: funcão redundante...    get_team(side).get_name() já retorna o nome do time
	def get_team_name(self, team_side):
		if(team_side == "l"):
			return self.__team_l.get_name()
		else:
			return self.__team_r.get_name()
		
	
	# Does the general initialization
	def initialize(self):
		
		# The data will be collected from this dataframe
		self.__data_frame = pd.read_csv(self.__log_path)

		# Getting teams names from the Data Frame
		team_left_name = self.__data_frame.iloc[0].team_name_l
		team_right_name = self.__data_frame.iloc[0].team_name_r
		
		# Players are initialized before the Teams because they are an attribute of them.
		# -> All Teams have an array of Players 
		left_players = self.starting_players(team_left_name, "l")
		right_players = self.starting_players(team_right_name, "r")
		
		# Teams:
		self.starting_teams(team_left_name, team_right_name, left_players, right_players)

		# Saving both teams in this DataCollector
		self.__teams.append(self.__team_l)
		self.__teams.append(self.__team_r)

	# Definition of computing functions
	'''
		#Funções getMostRecent... burras paliativas TODO: otimizar funções!!
	def getMostRecentKicker_x(self, row):
		i = row
		kicker_x = None
		while(kicker_x == None):
			for player_id in range(0,22):
				if(self.__data_frame.iloc[i, 34+(31*player_id)] != self.__data_frame.iloc[i-1, 34+(31*player_id)]):
					kicker_x = self.__data_frame.iloc[i, (34+(31*player_id) - 16)]
				
		return kicker_x
	
	def getMostRecentKicker_y(self, row):
		i = row
		kicker_y = None
		while(kicker_y == None):
			for player_id in range(0,22):
				if(self.__data_frame.iloc[i, 34+(31*player_id)] != self.__data_frame.iloc[i-1, 34+(31*player_id)]):
					kicker_y = self.__data_frame.iloc[i, (34+(31*player_id) - 15)]
				
		return kicker_y
	'''
	
	def find_unique_event_occurrences(self, event):
  		
		event_occurrences_index = []
  		
		for i in range(len(self.__data_frame)):
			if(self.__data_frame.iloc[i,1] == event and self.__data_frame.iloc[i-1,1] != event):
				event_occurrences_index.append(i)
		
		return event_occurrences_index

	def statChanged(self, logDataFrame, rowNumber, columnNumber):
		if(logDataFrame.iloc[rowNumber, columnNumber] == logDataFrame.iloc[rowNumber-1, columnNumber]):
			return False
		else:
			return True
	
	def starting_teams(self, team_left_name, team_right_name, left_players, right_players):
	
		self.__team_l = Team()
		self.__team_l.set_side("left")

		self.__team_r = Team()
		self.__team_r.set_side("right")
		
		# Setting team names from the Data Frame
		self.__team_l.set_name(team_left_name)
		self.__team_r.set_name(team_right_name)
		
		# Goals:

		self.__score = [self.__data_frame['team_score_l'].max(),self.__data_frame['team_score_r'].max()]
		
		self.__team_l.set_goals_scored = [] # need implementation
		self.__team_r.set_goals_scored = [] # need implementation

		self.__team_l.set_number_of_goals_scored(self.__score[0])
		self.__team_r.set_number_of_goals_scored(self.__score[1])
		
		self.__team_l.set_players(left_players)
		self.__team_r.set_players(right_players)
		
		# Setting goals scored
		l_goals = self.__data_frame['team_score_l'].max()
		r_goals = self.__data_frame['team_score_r'].max()
		
		self.__team_l.set_number_of_goals_scored(l_goals)
		self.__team_r.set_number_of_goals_scored(r_goals)
		
		# Setting free kicks
		r_free_kicks = self.__data_frame['playmode'].str.count('free_kick_l').sum()
		l_free_kicks = self.__data_frame['playmode'].str.count('free_kick_r').sum()
		
		self.__team_r.set_number_of_free_kicks(r_free_kicks)
		self.__team_l.set_number_of_free_kicks(l_free_kicks)

		#TODO: IMPLEMENTAR FUNÇÃO find_unique_event_count, e usá-la no lugar disto:
		#solução alternativa com output correto (mas mais lenta...)
		l_foul_charge = 0
		r_foul_charge = 0
		for i in range(len(self.__data_frame)):
			if(self.__data_frame.iloc[i,1] == "foul_charge_l" and self.__data_frame.iloc[i-1,1] != "foul_charge_l"):
				l_foul_charge += 1
			elif(self.__data_frame.iloc[i,1] == "foul_charge_r" and self.__data_frame.iloc[i-1,1] != "foul_charge_r"):
				r_foul_charge += 1

		self.__team_l.set_number_of_faults_commited(l_foul_charge)
		self.__team_r.set_number_of_faults_commited(r_foul_charge)

		# Setting foul_charges
			#TODO

		
		# Penalties:
		pen_r = self.__data_frame['team_pen_score_r'].max()
		pen_l = self.__data_frame['team_pen_score_l'].max()		
		
		self.__team_r.set_penaltis_scored(pen_r)
		self.__team_l.set_penaltis_scored(pen_l)

	def starting_players(self, team, side):	  
		players_array = [Player(team,side,1), Player(team,side,2), Player(team,side,3), Player(team,side,4), Player(team,side,5), Player(team,side,6), Player(team,side,7), Player(team,side,8), Player(team,side,9), Player(team,side,10), Player(team,side,11)]
		i = 1

		if side[0] == 'l' or side[0] == 'L':
			side = 'l'
		elif side[0] == 'r' or side[0] == 'R':
			side = 'r'
		
		for player in players_array:
			column = "player_{}{}_type".format(side,i)
			position = self.__data_frame.iloc[0][column] 
			player.set_pos(position)
			i = i + 1

		return players_array
		
	def copy_dataframe_subset_by_rows(self, dataframe, first_row, last_row):
		# Returns a copy of a subset of the given dataframe, delimited by first_row and last_row
			# Add one to each because of the first label row
		first_row += 1
		last_row += 1

		subset = dataframe.head(last_row)
		subset = subset.tail(last_row - first_row)

		return subset

		# Plotting of graphs:

	#TODO: procurar o valor por string e achar o valor showtime referente
	def goal_replay(self, goal_number, size):
		#Returns the start and end times of a replay of a gol
		start_time = 0
		end_time = 0
		number_of_goals = 0
		for row in self.__data_frame.index:
			if((self.__data_frame.iloc[row,1] == "goal_l" and self.__data_frame.iloc[row-1,1] != "goal_l") or (self.__data_frame.iloc[row,1] == "goal_r" and self.__data_frame.iloc[row-1,1] != "goal_r")):
				number_of_goals += 1
			if(number_of_goals == goal_number):
				break
		end_time = row
		start_time = row - size
		return [start_time, end_time]

	# Show features functions

	def show_feature_faults_quantity(self, mainWindowObject, feature_name, axes):
		data_to_plot = PlotData("bar", "Fouls Quantiti", 2)
			
			# sets data for graph
		data_to_plot.set_x_label("Team name")
		data_to_plot.set_y_label("Number of fouls commited")
			
			# sets data for bar 1 
		bar1 =  data_to_plot.get_entry(0)
		bar1.set_color("#7da67d")
		bar1.set_x_coordinate(self.get_team("l").get_name())
		bar1.set_y_coordinate(self.get_team("l").get_number_of_faults_commited()) 
			
			# sets data for bar 2 
		bar2 = data_to_plot.get_entry(1) 
		bar2.set_color("#ffa1a1")
		bar2.set_x_coordinate(self.get_team("r").get_name())
		bar2.set_y_coordinate(self.get_team("r").get_number_of_faults_commited()) 
		
			# calls the function to plot the graph 
		self.plot_bar(mainWindowObject, feature_name, data_to_plot, axes)

	def show_feature_faults_percentage(self, mainWindowObject, feature_name, axes):
		data_to_plot = PlotData("pie",number_of_entries=2)

		# aux variables for readability
		fouls_commited_by_l = self.get_team("l").get_number_of_faults_commited()
		fouls_commited_by_r = self.get_team("r").get_number_of_faults_commited()
		total_number_of_fouls = fouls_commited_by_l + fouls_commited_by_r

		# sets data for sector 1
		sector1 = data_to_plot.get_entry(0)
		sector1.set_color("#7da67d")
		sector1.set_label(self.get_team("l").get_name())

		sector1.set_value( (fouls_commited_by_l*100)/total_number_of_fouls)

		# sets data for sector 2
		sector2 = data_to_plot.get_entry(1)
		sector2.set_color("#ffa1a1")
		sector2.set_label(self.get_team("r").get_name())
		sector2.set_value( (fouls_commited_by_r*100)/total_number_of_fouls)


		self.plot_pie(mainWindowObject, feature_name, data_to_plot, axes)

	def show_feature_events_position(self, mainWindowObject, feature_name, axes):
		pass

	#merging this one onto show_feature_events_position
	def show_feature_faults_position(self, mainWindowObject, feature_name, axes):
		data_to_plot = PlotData("scatter",2)
		
		teamL = data_to_plot.get_entry(0)
		teamL_x_positions = []
		teamL_y_positions = []

		teamR = data_to_plot.get_entry(1)
		teamR_x_positions = []
		teamR_y_positions = []
		
		for i in range(len(self.__data_frame)):
			if(self.__data_frame.iloc[i,1] == "foul_charge_l" and self.__data_frame.iloc[i-1,1] != "foul_charge_l"):
				teamL_x_positions.append(int(self.__data_frame.iloc[i,BALL_X]))
				teamL_y_positions.append(int(self.__data_frame.iloc[i,BALL_Y]))
			elif(self.__data_frame.iloc[i,1] == "foul_charge_r" and self.__data_frame.iloc[i-1,1] != "foul_charge_r"):
				teamR_x_positions.append(int(self.__data_frame.iloc[i,BALL_X]))
				teamR_y_positions.append(int(self.__data_frame.iloc[i,BALL_Y]))

		teamL.set_x_positions(teamL_x_positions)
		teamL.set_y_positions(teamL_y_positions)
		teamR.set_x_positions(teamR_x_positions)
		teamR.set_y_positions(teamR_y_positions)

		data_to_plot.get_entry(0).set_label(self.get_team_name("l"))
		data_to_plot.get_entry(1).set_label(self.get_team_name("r"))

		data_to_plot.set_background_image(plt.imread("files/soccerField.png"))
		data_to_plot.show_background_image()

		team_l_name_to_lower = data_to_plot.get_entry(0).get_label().lower()

		if(team_l_name_to_lower == "robocin"):
			data_to_plot.get_entry(0).set_color("#7da67d")
			data_to_plot.get_entry(1).set_color("#ffa1a1")
		else:
			data_to_plot.get_entry(0).set_color("#ffa1a1")
			data_to_plot.get_entry(1).set_color("#7da67d")

		self.plot_scattter(mainWindowObject, feature_name, data_to_plot, axes)
	#mergin this one onto show_feature_events_position
	def show_feature_goals_position(self, mainWindowObject, feature_name, axes):

		data_to_plot = PlotData("scatter",2)
		
		teamL = data_to_plot.get_entry(0)
		teamL_x_positions = []
		teamL_y_positions = []

		teamR = data_to_plot.get_entry(1)
		teamR_x_positions = []
		teamR_y_positions = []
		
		for i in range(len(self.__data_frame)):
			if(self.__data_frame.iloc[i,1] == "goal_l" and self.__data_frame.iloc[i-1,1] != "goal_l"):
				teamL_x_positions.append(int(self.__data_frame.iloc[i,10]))
				teamL_y_positions.append(int(self.__data_frame.iloc[i,11]))
			elif(self.__data_frame.iloc[i,1] == "goal_r" and self.__data_frame.iloc[i-1,1] != "goal_r"):
				teamR_x_positions.append(int(self.__data_frame.iloc[i,10]))
				teamR_y_positions.append(int(self.__data_frame.iloc[i,11]))

		teamL.set_x_positions(teamL_x_positions)
		teamL.set_y_positions(teamL_y_positions)
		teamR.set_x_positions(teamR_x_positions)
		teamR.set_y_positions(teamR_y_positions)

		data_to_plot.get_entry(0).set_label(self.get_team_name("l"))
		data_to_plot.get_entry(1).set_label(self.get_team_name("r"))

		data_to_plot.set_background_image(plt.imread("files/soccerField.png"))
		data_to_plot.show_background_image()

		team_l_name_to_lower = data_to_plot.get_entry(0).get_label().lower()
		team_r_name_to_lower = data_to_plot.get_entry(1).get_label().lower()

		if(team_l_name_to_lower == "robocin"):
			data_to_plot.get_entry(0).set_color("#7da67d")
			data_to_plot.get_entry(1).set_color("#ffa1a1")
		else:
			data_to_plot.get_entry(0).set_color("#ffa1a1")
			data_to_plot.get_entry(1).set_color("#7da67d")

		self.plot_graph(mainWindowObject, "scatter", title, data_to_plot, axes)

	def show_feature_heatmap_position(self, mainWindowObject, feature_name, x_string, y_string, axes):
		pass
		
		# merge this with events position (maybe?)
	def show_feature_event_retrospective(self, mainWindowObject, feature_name, start_time, end_time, object, axes):
		pass

	def show_feature_stamina_tracker(self, mainWindowObject, feature_name, axes):
		pass

	# Plotting functions
	def plot_bar(self, mainWindowObject, title, data, axes):

		# sets axis labels
		axes.set_xlabel(data.get_x_label()) 
		axes.set_ylabel(data.get_y_label())
		# set title
		axes.set_title(title)
		# plot each bar
		for barIndex in range(0,len(data.get_entries())):
			axes.bar(data.get_entry(barIndex).get_x_coordinate(), data.get_entry(barIndex).get_y_coordinate(), width = data.get_entry(barIndex).get_width(), color = data.get_entry(barIndex).get_color())
		# Attach a text label above each bar in *rects*, displaying its height.
		#I don't understand this. It was adapted from matplotlib documentation.
		aux = 0
		for entry in data.get_entries():
			height = entry.get_y_coordinate()
			axes.annotate('{}'.format(height), xy=(aux, height), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
			aux += 1

	def plot_pie(self, mainWindowObject, title, data, axes):

		# set title
		axes.set_title(title)

		colors = []
		values = []
		labels = []
		for entry in data.get_entries():
			colors.append(entry.get_color())
			values.append(entry.get_value())
			labels.append(entry.get_label())

		# plot the graph
		axes.pie(values, explode =(0.06, 0), labels = labels, colors = colors, autopct='%1.1f%%', shadow=True, startangle=90)

	def plot_scatter(self, mainWindowObject, title, data, axes):
		pass