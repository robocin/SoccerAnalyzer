class PlotBarData():
	def __init__(self):
		self.__bars = []	

		self.__xLabel = None
		self.__yLabel = None

	# Setters and Getters

	def appendBars(self, numberOfBars, referenceNamesList):
		for i in range(0,numberOfBars):	
			self.__bars.append(Bar(referenceNamesList[i]))
			self.__bars[i].setReferenceName(referenceNamesList[i])
	def setXLabel(self, label):
		self.__xLabel = label
	def setYLabel(self, label):
		self.__yLabel = label

	def getBars(self):
		return self.__bars
	def getBar(self, listIndex):
		return self.__bars[listIndex]
	def getXLabel(self):
		return self.__xLabel
	def getYLabel(self):
		return self.__yLabel
class Bar():
	def __init__(self, referenceName):
		self.__reference_name = referenceName
		self.__name = None
		self.__value = None
		self.__label = None

	# Setters and Getters
	def setName(self, name):
		self.__name = name
	def setReferenceName(self, refName):
		self.__reference_name = refName
	def setValue(self, value):
		self.__value = value
	def setLabel(self, label):
		self.__label = label
	

	def getName(self):
		return self.__name 
	def setReferenceName(self, refName):
		return self.__reference_name
	def getValue(self):
		return self.__value
	def getLabel(self):
		return self.__label