import numpy as np
import pandas as pd

from Team import Team
from Event import Event
from Player import Player
from Position import Position

class DataCollector():
	def __init__(self,log_path):
		self.__log_path = log_path

		#instaciates the teams
		
		self.__team_l = None # By instanciating the team, all the computing is made inside the __init__ of the class Team()
		self.__team_r = None
		self.__teams = []
		self.__allEvents = []
		self.__allFaults = []
		self.__allGoals = []
		self.__allPenalties = []


		# calls for data computing
		self.initialize()

	
	# Creates the Setters and Getters methods   

	def set_log_path(self,log_path):
		self.__log_path = log_path 		

	def setAllGoals(self, allGoals):
		self.__allGoals = allGoals

	def setAllFaults(self, allFaults):
		self.__allFaults = 	allFaults

	
	# Getters
	
	def getTeam(self, teamSide):
		
		if(teamSide == "l"):
			return self.__team_l
		elif(teamSide == "r"):
			return self.__team_r

	
	# Does the general initialization
	def initialize(self):
		
		# The data will be collected from this dataframe
		self.__dataFrame = pd.read_csv(self.__log_path)

		# Teams:

		self.__team_l = Team(self.__dataFrame,"l")
		self.__team_r = Team(self.__dataFrame,"r")
		self.__teams.append(self.__team_l)
		self.__teams.append(self.__team_r)

		# Goals:

		self.__score = [self.__dataFrame['team_score_l'].max(),self.__dataFrame['team_score_r'].max()]
		
		self.__team_l.setGoalsMade = [] # need implementation
		self.__team_r.setGoalsMade = [] # need implementation

		self.__team_l.setNumberOfGoalsMade(self.__score[0])
		self.__team_r.setNumberOfGoalsMade(self.__score[1])

		# Faults:
		
		self.__foulChargeLeft = self.__dataFrame['playmode'].str.count('foul_charge_l').sum()
		self.__freeKickLeft = self.__dataFrame['playmode'].str.count('free_kick_l').sum()
		self.__team_l.setNumberOfFaultsCommited(self.__foulChargeLeft)
		self.__team_l.setNumberOfFreeKicks(self.__freeKickLeft)
		
		
		self.__foulChargeRight = self.__dataFrame['playmode'].str.count('foul_charge_r').sum()
		self.__freeKickRight = self.__dataFrame['playmode'].str.count('free_kick_r').sum()
		self.__team_r.setNumberOfFaultsCommited(self.__foulChargeRight)
		self.__team_r.setNumberOfFreeKicks(self.__freeKickRight)


		# Penalties:
		#
		#	code here

		# Corners:
		#
		#	code here

		# Ball out:
		#
		#	code here

		# parse the __all_goals list, giving, for each goal, it's reference to the team and player that made it
