import pandas
from Team import Team
from Event import Event
from Player import Player
from Posititon import Position


TOTAL_NUMBER_OF_PLAYERS = 22
NUMBER_OF_PLAYERS_PER_TEAM = TOTAL_NUMBER_OF_PLAYERS/2

PLAYER_L1_COUNTING_KICK_LOG_DATA_FRAME_COLUMN_POSITION = 34
FIRST_COUNTING_KICK_COLUMN_L = 34

NUMBER_OF_COLUMNS_BETWEEN_COUNTING_KICKS_PLUS_ONE = 31
NUMBER_OF_COLUMNS_BETWEEN_PLAYER_X_POS_AND_PLAYER_COUNTING_KICKS_PLUS_ONE = 16
NUMBER_OF_COLUMNS_BETWEEN_PLAYER_Y_POS_AND_PLAYER_COUNTING_KICKS_PLUS_ONE = 15

def statChanged(logDataFrame, rowNumber, columnNumber):
	if(logDataFrame.iloc[rowNumber, columnNumber] == logDataFrame.iloc[rowNumber-1, columnNumber]):
		return False
	else:
		return True	
#												, teams, rowNumber):
def getMostRecentTacklerAndPosition(logDataFrame, rowNumber):
	#TODO: ver como funciona retornar dois valores de uma vez para esta função
	'''
	Return a list containing the most recent tackler's id, and the position (int time and space) of where the tackle was made
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
				#recent_tackler_tackle_position = positionClass.Position(recent_tackler_tackle_xPos, recent_tackler_tackle_yPos, None)#TODO: trocar Nonerecent_tackler_tackle_time) # instaciates a position object of the most recent tackle made
				recent_tackler_tackle_position = Position(0, 0, None)#TODO: trocar Nonerecent_tackler_tackle_time) # instaciates a position object of the most recent tackle made
				break
			playerId += 1
			if(playerId > NUMBER_OF_PLAYERS_PER_TEAM):
				playerTeam = "r"
			columnCursor += 1

	'''
	# gets the most recent tackler id
	if (playerTeam == "l"):
		recent_tackler_id = teams[0].getPlayer(playerId)
	elif (playerTeam == "r"):
		recent_tackler_id = teams[1].getPlayer(playerId)	
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
	Returns a list: [goalClass.Goal: allGoals[], total_number_of_goals_made]		
	Gives to the tackle player and its team a reference for this goal object
	'''

	all_goals_and_total_number = []
	allGoals = []
	total_number_of_goals_made = 0
	print(logDataFrame.index.stop)
	for row in range(0,len(logDataFrame.index)): #for each row of the .csv file,
		showTime = logDataFrame.iloc[0,600] #TODO: 600 ERA PRA SER row 
		if (showTime == "goal_l" or showTime == "goal_r"): #if a goal was made
			total_number_of_goals_made += 1
			allGoals.append(Event(logDataFrame, teams, row, total_number_of_goals_made))#creates an instace representative of this goal with all the informations about it, and appends it to the allGoals list
   		
	teams[(0 if showTime=="goal_l" else 1)].setGoalsMade(allGoals)#passes this goalObject reference to the team and player that made it 

	# appends the list with all goals and the total number of goals to the all_goals_and_total_number variable (which will be returned!)
	all_goals_and_total_number.append(allGoals)	
	all_goals_and_total_number.append(total_number_of_goals_made)		
    
	return all_goals_and_total_number

def computeFaults(logDataFrame):
	pass

#def compute...
