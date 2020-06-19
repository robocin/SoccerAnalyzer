class PlotData:
    def __init__(self, plotType, numberOfEntries):
        # All types
        self.__name = None
        self.__entries = []
        self.__xLabel = None
        self.__yLabel = None


        # Specifc types 
        if(plotType == "bar"):
            for i in range(0, numberOfEntries):
                self.__entries.append(Entry("bar"))
        
        if(plotType == "pir"):
            pass
        
        if(plotType == "scatter"):
            pass

    # Setters and Getters
    def setXLabel(self, label):
        self.__xLabel = label
    def setYLabel(self, label):
        self.__yLabel = label
    
    def getXLabel(self):
        return self.__xLabel
    def getYLabel(self):
        return self.__yLabel
    def getEntries(self):
        return self.__entries

    def getEntry(self, entryId):
        print("--------------------------------------------------->")
        print(self.__entries)
        return self.__entries[entryId]



class Entry:
    def __init__(self, entryType):
        # All types
        self.__value = None
        self.__label = None

        # Specifc types
        if(entryType == "bar"):
            self.__xCoordinate = None
            self.__height = None
            self.__width = None

	# Setters and Getters (all types)
    def setValue(self, value):
        self.__value = value
    def setLabel(self, label):
        self.__label = label
	
    def getValue(self):
        return self.__value
    def getLabel(self):
        return self.__label


	# Setters and Getters (specifc types)
        #bar
    def setXCoordinate(self, xCoodinate):
        self.__xCoordinate = xCoodinate
    def setHeight(self, height):
        self.__height = height

    def getXCoordinate(self):
        return self.__xCoordinate
    def getHeight(self):
        return self.__height








'''
def getBars(self):
        return self.__bars
    def getBar(self, listIndex):
        return self.__bars[listIndex]
    def getXLabel(self):
        return self.__xLabel
    def getYLabel(self):
        return self.__yLabel



'''
