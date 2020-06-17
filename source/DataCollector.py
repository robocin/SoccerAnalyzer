import numpy as numpy
import pandas as pandas

import ComputingFunctions as computing
import Team
import Event
import Player
import Position

class DataCollector():
	def __init__(self,log):
		self.__log = log
		self.__teams = []

		#instaciates the teams
		self.__team_l = Team.Team(log,"l") # By instanciating the team, all the computing is made inside the __init__ of the class Team()
		self.__team_r = Team.Team(log,"r") # ||
		self.__teams.append(self.__team_l)
		self.__teams.append(self.__team_r)

		#self.__allEvents = []
		#self.__numberOfEvents = []

		self.__all_goals = None
		self.__total_number_of_goals = None

		# calls for data computing
		self.compute()

	# Creates the Setters and Getters methods
		# Setters
	def setAllGoals(self, all_goals):
		self.__all_goals = all_goals
	def setTotalNumberOfGoals(self, total_number_of_goals):
		self.__total_number_of_goals = len(self.__all_goals)

		# Getters
	def getTeam(self, teamSide):
		if(teamSide == "l"):
			return self.__team_l
		elif(teamSide == "r"):
			return self.__team_r

	# Does the general computing
	def compute(self):
		# compute all goals and the total number of goals
		all_goals_informations = computing.computeAllGoals(self.__log, self.__teams)
		all_goals = all_goals_informations[0]
		total_number_of_goals = all_goals_informations[1] 
		self.setAllGoals(all_goals)
		self.setTotalNumberOfGoals(total_number_of_goals)

		# parse the __all_goals list, giving, for each goal, it's reference to the team and player that made it
