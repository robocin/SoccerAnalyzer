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
    def __init__(self, position=None, owner=None):
        self.__position = position
        self.__owner = owner


    # set and get methods

    def set_position(self, x):
        self.__position = x 
    def set_owner(self, x):
        self.__owner = x
    def get_position(self):
        return self.__position
    def get_owner(self):
        return self.__owner
