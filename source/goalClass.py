import computingFunctions as computing
import positionClass

BALL_X_POS_COLUMN = 10 
BALL_Y_POS_COLUMN = 11

class Goal():
	def __init__(self, logDataFrame, teams, row, goalId):
		self.__teams = teams
		self.__log_data_frame = logDataFrame
		self.__row = row	
		self.__id = goalId
		self.__team_tackler_side
		self.__tackler
		self.__tackle_position
		self.__goal_position

		# calls for computing
		self.compute()


	# Getters and Setters
		# Setters
	def setTackler(self, tackler):
		self.__tackler = tackler
	def setTeamTacklerSide(self, team_tackler_side):
		self.__team_tackler_side = team_tackler_side
	def setTacklePosition(self, tacklePosition):
		self.__tacklePosition = tacklePosition	
	def setGoalPosition(self, goalPosition):
		self.__goal_position = goalPosition


		# Getters	
	def getId(self):
		return self.__goal_id
	def getTackler(self):
		return self.__tackler
	def getTeamTackler(self):
		return self.__team_tackler
	def getTacklePosition(self):
		return self.__tackle_position
	def getGoalPosition(self):
		return self.__goal_position

	# Data Computing
	def compute(self):
		
		# the tackler and the time of the tackle			
		tackle_informations = computing.getMostRecentTacklerAndPosition(self.__log_data_frame, self.__teams, self.__row)	
		tackler = tackle_informations[0]
		tackle_position = tackle_informations[1]	
			# tackler (player who made the goal)
		self.setTackler(tackler)	
			# position the tackle was made
		self.setTacklePosition(tackle_position)	

		# the team whose the player is the tackler
		setTeamTacklerSide(getTackler().getTeamSide)

		# position the goal was made
		goal_x_pos = self.__log_data_frame.iloc(self.__row, BALL_X_POS_COLUMN) 
		goal_y_pos = self.__log_data_frame.iloc(self.__row, BALL_Y_POS_COLUMN) 
		goal_timestamp = self.__log_data_frame.iloc(self.__row, 0)
		self.setGoalPosition(positionClass.Position(goal_x_pos,goal_y_pos,goal_timestamp))

