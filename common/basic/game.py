class Game:
    def __init__(self, dataFrame):
        self.__log = None
        self.__teamLeftName = None
        self.__teamRightName = None
        self.__winningTeam = None
        self.__losingTeam = None
        self.__faultQuantity = 0
        self.__cornerQuantity = 0
        self.__penaltyQuantity = 0
        self.__goalQuantity = 0
        
        self.__setLog(dataFrame)
        self.__setTeamLeftName()
        self.__setTeamRightName()
    
    def __setLog(self, dataFrame):
        self.__log = dataFrame
    
    def __setTeamLeftName(self):
        self.__teamLeftName = str(self.__log.iloc[0,2])
        
    def __setTeamRightName(self):
        self.__teamRightName = str(self.__log.iloc[0,3])
        
    def getTeamLeftName(self) -> str:
        return self.__teamLeftName
    
    def getTeamRightName(self) -> str:
        return self.__teamRightName
        
