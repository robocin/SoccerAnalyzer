import numpy as np
import pandas as pd

import Player
import Position

# This class is a generalization of any kind game related event like: goals, faults
#
# A fault and a penalty would have (V0.3):
#   
#   A string, telling it is a fault: etype
#   A Positon, telling in which cicle the Event happened and where(x,y in the field).
#   A Player that infflicted the fault: offender
#   A Player that suffered the fault: defender
#   A Player that took the kick: ekicker 
#   A bool telling if the offender recieved a yellow card
#   A bool telling if the offender recieved a red card
#
# ----------------------------------------------------------------------------------------------
#
# A ball and a corner would have (V0.3):
#      
#   A Position, telling in which cicle the Event happened and where(x,y int the field); 
#   The last player to touch the ball.
#
# ----------------------------------------------------------------------------------------------
# 
# A goal would have (V0.3):
#   
#   A Position, telling in which cicle the Event happened and where(x,y int the field); 
#   A Position, telling from where the kick was taken.
#   A Player who had the kick. [NEED IMPLEMENTATION]
#
# ----------------------------------------------------------------------------------------------

class Event:
    def __init__(self, etype = "No type", etime = 0, ekicker = None, 
    eoffender = None, edefender = None, eposition = None, yellow_card = False, red_card = False):

        self.__etype = etype #type is a reserved word
        self.__etime = etime
        self.__ekicker = ekicker
        self.__eoffender = eoffender
        self.__edefender = edefender 
        self.__eposition = eposition
        self.__yellow_card = yellow_card
        self.__red_card = red_card

    #set methods

    def set_event_type(self, etype):
        self.__etype = etype

    def set_etime(self, etime):
        self.__etime = etime
    
    def set_kicker(self, kicker):
        self.__kicker = kicker

    def set_offender(self, offender):
        self.__offender = offender

    def set_defender(self, defender):
        self.__defender = defender

    def set_eposition(self, eposition):
        self.__eposition = eposition

    def set_yellow_card(self, yellow_card):
        self.__yellow_card = yellow_card

    def set_red_card(self, red_card):
        self.__redcard = red_card


    #get methods

    def get_event_type(self):
        return self.__etype

    def get_etime(self):
        return self.__etime

    def get_kicker(self):
        return self.__ekicker

    def get_offender(self):
        return self.__eoffender
    
    def get_defender(self):
        return self.__edefender

    def get_eposition(self):
        return self.__eposition

    def get_yellow_card(self):
        return self.__yellow_card

    def get_red_card(self):
        return self.__red_card









        ############# codigo que já existia  ##############
'''

BALL_X_COLUMN = 10 
BALL_Y_COLUMN = 11


class Goal:
	def __init__(self, logDataFrame, teams, row, goalId):
		self.__teams = teams
		self.__logDataFrame = logDataFrame
		self.__row = row	
		self.__id = goalId
		self.__team_tackler_side
		self.__tackler
		self.__tackle_position
		self.__goal_position

		# calls for computing
		self.compute()


	
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
		tackle_informations = computing.getMostRecentTacklerAndPosition(self.__logDataFrame, self.__teams, self.__row)	
		tackler = tackle_informations[0]
		tackle_position = tackle_informations[1]	
		
        # tackler (player who scored the goal)
		self.setTackler(tackler)	
		
        # position the tackle was scored
		self.setTacklePosition(tackle_position)	

		# the team whose the player is the tackler
		setTeamTacklerSide(getTackler().getTeamSide)

		# position the goal was scored
		goal_x_pos = self.__logDataFrame.iloc(self.__row, BALL_X_COLUMN) 
		goal_y_pos = self.__logDataFrame.iloc(self.__row, BALL_Y_COLUMN) 
		goal_timestamp = self.__logDataFrame.iloc(self.__row, 0)

		self.setGoalPosition(Position(goal_x_pos,goal_y_pos,goal_timestamp))

'''