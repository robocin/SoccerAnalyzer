import numpy as np
import pandas as pd

from Team import Team
from Event import Event
from Player import Player
from Position import Position

#Constants
TOTAL_NUMBER_OF_PLAYERS = 22
NUMBER_OF_PLAYERS_PER_TEAM = TOTAL_NUMBER_OF_PLAYERS/2
PLAYER_L1_COUNTING_KICK_LOG_DATA_FRAME_COLUMN_POSITION = 34
FIRST_COUNTING_KICK_COLUMN_L = 34
NUMBER_OF_COLUMNS_BETWEEN_COUNTING_KICKS_PLUS_ONE = 31
NUMBER_OF_COLUMNS_BETWEEN_PLAYER_X_POS_AND_PLAYER_COUNTING_KICKS_PLUS_ONE = 16
NUMBER_OF_COLUMNS_BETWEEN_PLAYER_Y_POS_AND_PLAYER_COUNTING_KICKS_PLUS_ONE = 15


class DataCollector():
	def __init__(self,log_path):
		self.__log_path = log_path

            #instaciates the teams
	

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

	def set_log_path(self,log_path):
		self.__log_path = log_path 		

	def set_all_goals(self, all_goals):
		self.__all_goals = all_goals

	def set_all_faults(self, all_faults):
		self.__all_faults =	all_faults

	
	# Getters
	
	def get_team(self, team_side):
		if(team_side == "l"):
			return self.__team_l
		elif(team_side == "r"):
			return self.__team_r

	
	# Does the general initialization
	def initialize(self):
		
		# The data will be collected from this dataframe
		self.__data_frame = pd.read_csv(self.__log_path)

		# Teams:
		
		self.__team_l = Team(self.__data_frame,"l")
		self.__team_r = Team(self.__data_frame,"r")
		self.__teams.append(self.__team_l)
		self.__teams.append(self.__team_r)

		
		# Goals:

		self.__score = [self.__data_frame['team_score_l'].max(),self.__data_frame['team_score_r'].max()]
		
		self.__team_l.set_goals_scored = [] # need implementation
		self.__team_r.set_goals_scored = [] # need implementation

		self.__team_l.set_number_of_goals_scored(self.__score[0])
		self.__team_r.set_number_of_goals_scored(self.__score[1])

		# Faults:
		
		self.__foul_charge_left = self.__data_frame['playmode'].str.count('foul_charge_l').sum()
		self.__free_kick_left = self.__data_frame['playmode'].str.count('free_kick_l').sum()
		self.__team_l.set_number_of_faults_commited(self.__foul_charge_left)
		self.__team_l.set_number_of_free_kicks(self.__free_kick_left)
		
		
		self.__foul_charge_right = self.__data_frame['playmode'].str.count('foul_charge_r').sum()
		self.__free_kick_right = self.__data_frame['playmode'].str.count('free_kick_r').sum()
		self.__team_r.set_number_of_faults_commited(self.__foul_charge_right)
		self.__team_r.set_number_of_free_kicks(self.__free_kick_right)


		# Penalties:
		#
		#	code here

		# Corners:
		#
		#	code here

		# Ball out:
		#
		#	code here

		# parse the __all_goals list, giving, for each goal, it's reference to the team and player that scored it

	# Definition of computing functions

	def statChanged(self, logDataFrame, rowNumber, columnNumber):
		if(logDataFrame.iloc[rowNumber, columnNumber] == logDataFrame.iloc[rowNumber-1, columnNumber]):
			return False
		else:
			return True

	#												, teams, rowNumber):
	def getMostRecentTacklerAndPosition(sellf, logDataFrame, rowNumber):
		#TODO: ver como funciona retornar dois valores de uma vez para esta função
		'''
		Return a list containing the most recent tackler's id, and the position (int time and space) of where the tackle was scored
		return << [int:recent_tackler_id, positionClass.Position: recent_tackler_tackle_position]	
		'''


		tackler_and_position = []
		recent_tackler_tackle_position = None
		recent_tackler_id = None
		recent_tackler_indicator = " " #holds the name id of the most recent player to make a tackle (kick)
		rowCursor = rowNumber+1 # +1 because of the subtraction inside the while(True)
		columnCursor = PLAYER_L1_COUNTING_KICK_LOG_DATA_FRAME_COLUMN_POSITION
		# search the most recent player to have its counting_kick stat changed and sets the recent_tackler_indicator and recent_tackler_tackle_position
		while(True):
			# regress the cursor one row
			rowCursor -= 1
			# some auxiliar variables	
			playerTeam = "l"
			playerId = 1
			# for each player in this showTime (row)
			for i in range(0, TOTAL_NUMBER_OF_PLAYERS - 1):		
				# if the stat in the cell (that the cursor is pointing to) changed, it's player is the most recent tackler
				if(statChanged(logDataFrame, rowNumber,columnCursor)):
					# sets the tackler indicator and position (in space and time)
					recent_tackler_indicator = playerTeam + str(playerId) #i.e.: "l5" for the fifth player of the left team
					
					#TODO: descomentar e debuggar essas linhas abaixo
					#recent_tackler_tackle_time = int(logDataFrame.iloc[rowCursor, 0]) # timestamp
					#recent_tackler_tackle_xPos = logDataFrame.iloc[rowCursor, columnCursor - NUMBER_OF_COLUMNS_BETWEEN_PLAYER_X_POS_AND_PLAYER_COUNTING_KICKS_PLUS_ONE] # x position  
					#recent_tackler_tackle_yPos = logDataFrame.iloc[rowCursor, columnCursor - NUMBER_OF_COLUMNS_BETWEEN_PLAYER_Y_POS_AND_PLAYER_COUNTING_KICKS_PLUS_ONE] # y position
					#recent_tackler_tackle_position = positionClass.Position(recent_tackler_tackle_xPos, recent_tackler_tackle_yPos, None)#TODO: trocar Nonerecent_tackler_tackle_time) # instaciates a position object of the most recent tackle scored
					recent_tackler_tackle_position = Position(0, 0, None)#TODO: trocar Nonerecent_tackler_tackle_time) # instaciates a position object of the most recent tackle scored
					break
				playerId += 1
				if(playerId > NUMBER_OF_PLAYERS_PER_TEAM):
					playerTeam = "r"
				columnCursor += 1

		'''
		# gets the most recent tackler id
		if (playerTeam == "l"):
			recent_tackler_id = teams[0].get_player(playerId)
		elif (playerTeam == "r"):
			recent_tackler_id = teams[1].get_player(playerId)	
		'''

		recent_tackler_id = self.playerId

		# puts the id in the tackler_and_time list
		tackler_and_time.append(recent_tackler_id)

		# puts the time in the tackler_and_time list
		tackler_and_time.append(recent_tackler_tackle_position)

		# returns the tackler and the position objects
		return tackler_and_time 

				

		while ("kick" not in showTime): 
			rowCursor -= 1
			showTime = logDataFrame.iloc(rowCursor, 0)
		# when the row where of most recent tackle (kick) is found, return the player closest to the ball

	def computeAllGoals(logDataFrame, teams):
		'''
		Computes all the goals and instaciates an object of the goal class for each, storing all the information about it.
		Returns a list: [goalClass.Goal: allGoals[], total_number_of_goals_scored]		
		Gives to the tackle player and its team a reference for this goal object
		'''

		all_goals_and_total_number = []
		allGoals = []
		total_number_of_goals_scored = 0
		print(logDataFrame.index.stop)
		for row in range(0,len(logDataFrame.index)): #for each row of the .csv file,
			showTime = logDataFrame.iloc[0,600] #TODO: 600 ERA PRA SER row 
			if (showTime == "goal_l" or showTime == "goal_r"): #if a goal was scored
				total_number_of_goals_scored += 1
				allGoals.append(Event(logDataFrame, teams, row, total_number_of_goals_scored))#creates an instace representative of this goal with all the informations about it, and appends it to the allGoals list
			
		teams[(0 if showTime=="goal_l" else 1)].set_goals_scored(allGoals)#passes this goalObject reference to the team and player that scored it 

		# appends the list with all goals and the total number of goals to the all_goals_and_total_number variable (which will be returned!)
		all_goals_and_total_number.append(allGoals)	
		all_goals_and_total_number.append(total_number_of_goals_scored)		
		
		return all_goals_and_total_number


	def computeFaults(logDataFrame):
		pass