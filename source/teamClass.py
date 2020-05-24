class Team:

    def __init__(self, name = "No name", goalsPro = "0", goalsAgainst = "0", faultsPro = "0", 
    faultsAgainst = "0", penaltisPro = "0", penaltisAgainst = "0", seenOn = "1", substitutions = "0"):

        self.__name = name
        self.__goalsPro = goalsPro
        self.__goalsAgainst = goalsAgainst
        self.__faultsPro = faultsPro
        self.__faultsAgainst = faultsAgainst
        self.__penaltisPro = penaltisPro
        self.__penaltisAgainst = penaltisAgainst
        self.__seenOn = seenOn
        self.__substitutions = substitutions

    #set methods (interface)
    def setName(self):
        pass
    def setGoalsPro(self):
        pass
    def setGoalsAgainst(self):
        pass
    def setFaultsPro(self):
        pass
    def setFaultsAgainst(self):
        pass
    def setPenaltisPro(self):
        pass
    def setPenaltisAgainst(self):
        pass
    def setSeenOn(self):
        pass
    def setSubstitutions(self):
        pass

    #get methods
    def getName(self):
        print(self.__name)

    def getGoalsPro(self):
        return self.__goalsPro

    def getGoalsAgainst(self):
        return self.__goalsAgainst

    def getFaultsPro(self):
        return self.__faultsPro
    
    def getFaultsAgainst(self):
        return self.__faultsAgainst

    def getPenaltisPro(self):
        return self.__penaltisPro
    
    def getPenaltisAgainst(self):
        return self.__penaltisAgainst

