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
    def __init__(self, etype = None):

        # all types
        self.__etype = etype #type is a reserved word
        self.__position = None
        self.__chronological_id = None

        # foul
        if(self.__etype == "foul"):
            self.__offender = None
            self.__defender = None
        
        # goal
        if(self.__etype == "goal"):
            self.__who_scored = None


    # set and get methods

        # all types
    def set_position(self, position):
        self.__position = position
    def set_chronological_id(self, id):
        self.__chronological_id = id
    def get_position(self):
        return self.__position
    def get_chronological_id(self):
        return self.__chronological_id

        # foul
    def set_offender(self, offender):
        self.__offender = offender
    def set_defender(self, defender):
        self.__defender = defender
    def get_offender(self):
        return self.__offender
    def get_defender(self):
        return self.__defender

        # goal
    def set_who_scored(self, player):
        self.__who_scored = player
    def get_who_scored(self):
        return self.__who_scored