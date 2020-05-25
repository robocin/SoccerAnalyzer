import numpy as np
import pandas as pd

import playerClass
import positionClass

class Event:
    def __init__(self, etype = "No type", etime = 0, kicker = None, 
    offender = None, defender = None, eposition = None):

        self.__etype = etype #type is a reserved word
        self.__etime = etime
        self.__kicker = kicker
        self.__offender = offender
        self.__defender = defender 
        self.__eposition = eposition

    #set methods
    def setEventType(self, etype):
        self.__etype = etype

    def setETime(self, etime):
        self.__etime = etime
    
    def setKicker(self, kicker):
        self.__kicker = kicker

    def setOffender(self, offender):
        self.__offender = offender

    def setDefender(self, defender):
        self.__defender = defender

    def setEPosition(self, eposition):
        self.__eposition = eposition

    #get methods
    def getEventType(self):
        return self.__etype

    def getETime(self):
        return self.__etime

    def getKicker(self):
        return self.__kicker

    def getOffender(self):
        return self.__offender
    
    def getDefender(self):
        return self.__defender

    def getEPosition(self):
        return self.__eposition