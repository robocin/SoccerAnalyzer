import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QListWidget, QLabel, QMenuBar, QAction
from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

import numpy as np
import pandas as pd

#import teamClass
#import robocinClass

STATISTICS = "EXTRACTIONS FIELDS" 
LIST_MINIMUM_HEIGHT = 300
LIST_MAXIMUM_HEIGHT = 600
LIST_MINIMUM_WIDTH = 181
LIST_MAXIMUM_WIDTH = 180

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.VIEW_FILLED = False

        ##### SCREEN INILIALIZATION #####
        #getting CURRENT monitor screen size
        #CHANGE:self.dimensions = QApplication(sys.argv)
        self.application = QApplication(sys.argv)
        self.screen = self.application.primaryScreen()
        self.rect = self.screen.availableGeometry()
        
        #declaring variables that holds the screen title and dimensions   
        self.title = 'RobôCIn statistics extractor'
        self.width = self.rect.width()
        self.height = self.rect.height()
        self.top = (self.rect.height()/2) - (self.height/2) 
        self.left = (self.rect.width()/2) -  (self.width/2) 
        
        #setting the title, icon image, dimensions(geometry), statusBar
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon('./files/robocin-03-small.png'))
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.statusBar().showMessage("Statusbar - awaiting user control")
        ##### END OF SCREEN INITIALIZATION #####

        #setting the main layout to be horizontal
        self.main_hbox = QHBoxLayout()

        #creating the elements of the window (calling custom functions)
        self.init_Menu() # main menu at the top of the screen
        self.init_List() # left side list
        self.create_View(False,"Escolha uma das opções na lista à esquerda") # right side graph area
        self.define_Log()
        #creating central widget and putting it in the main window as a central widget
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_hbox)
        self.setCentralWidget(self.main_widget)
        
        #turns main window visible
        self.show()

    ##### Definition of custom functions #####
    def init_Menu(self):
        '''
        Creates the main menu and connects its actions to
        the respective function calls
        '''
        #creates the main menu at the top 
        self.mainMenu = self.menuBar()
        fileMenu = self.mainMenu.addMenu("File")
        editMenu = self.mainMenu.addMenu("Edit")
        selectionMenu = self.mainMenu.addMenu("Selection")
        viewMenu = self.mainMenu.addMenu("View")
        terminalMenu = self.mainMenu.addMenu("Terminal")
        helpMenu = self.mainMenu.addMenu("Help")
        #creates the "clear" action inside the "edit" option on the main menu 
        clearAction = QAction("Clear", self)
        editMenu.addAction(clearAction)
        #connects the "clear" action to the clear_View() function 
        clearAction.triggered.connect(self.clear_View) # when calling clear_View without specifying parameters, False is given as parameter to graphType
 

    def init_List(self):
        '''
        Creates the selection list
        '''
        # creates the selection list
        self.main_list = QListWidget()
        # defines the maximum and minimum dimensions of the list
        self.main_list.setMinimumHeight(LIST_MINIMUM_HEIGHT)
        self.main_list.setMaximumHeight(LIST_MAXIMUM_HEIGHT)
        self.main_list.setMaximumWidth(LIST_MAXIMUM_WIDTH)
        self.main_list.setMinimumWidth(LIST_MINIMUM_WIDTH)
        # creates the list items
        self.main_list.insertItem(0,"TEST PIE")
        self.main_list.insertItem(1,"TEST BAR")
        self.main_list.insertItem(2,"Faltas absolutas")
        self.main_list.insertItem(3,"Faltas relativas")
        self.main_list.insertItem(4,STATISTICS)
        self.main_list.insertItem(5,STATISTICS)
        self.main_list.insertItem(6,STATISTICS)
        self.main_list.insertItem(7,STATISTICS)
        self.main_list.insertItem(8,STATISTICS)
        self.main_list.insertItem(9,STATISTICS)
        # adds the list to the main_hbox
        self.main_hbox.addWidget(self.main_list)
        # when an item is clicked on, sends a signal to the itemSelected() function 
        self.main_list.itemClicked.connect(self.itemSelected)
    
    def itemSelected(self, item):
        stat = item.text()
        self.create_View(stat, stat)

    def create_View(self, graphType, title):  
        '''
        Creates the area, on the right side of the screen, where the plot the graphs on.
        '''
        # creates the view_groupBox (area where to plot the graphs on)
        self.view_groupBox = QGroupBox()
        # creates the layout of view_groupBox 
        self.layout = QVBoxLayout()
        # cleans the graph area, if there's already a graph being displayed  
        if self.VIEW_FILLED == True:
            self.clear_View(title)
        # creates the area where to plot the graphs
        self.plot_Area = self.create_Plot(graphType, title)
        # defines the layout of view_groupBox
        self.view_groupBox.setLayout(self.plot_Area)
        # adds the view_groupBox to the main_hbox 
        self.main_hbox.addWidget(self.view_groupBox) 
        self.VIEW_FILLED = True



    #TODO: ENTENDER O FUNCIONAMENTO INERNO DE CLEAR_VIEW
    def clear_View(self, graphType):
        for i in reversed(range(self.main_hbox.count())): 
            if i > 0:
                self.main_hbox.itemAt(i).widget().setParent(None)  
        self.VIEW_FILLED = False
        # if the clear_View function was called by a signal from: MainMenu -> edit -> clear, 
        if (graphType == False):
            self.create_View(False,"Escolha uma das opções na lista à esquerda")
    
    def create_Plot(self, graphType, title):
        '''
        Creates figure, cavas, navigationToolbar, and configures the layout.
        Calls the function to plot the graph.
        '''
        # creates a 'figure', where to plot the graphs on 
        self.figure = Figure()

        # creates a canvas widget, which displays the figure 
        self.canvas = FigureCanvas(self.figure)

        # creates the navigationToolbar widget  
        if(graphType != False): 
            self.toolbar = NavigationToolbar(self.canvas, self)

        # customizes the toolbar and canvas layout 
        
        space = QVBoxLayout()
             
        if(graphType != False): #if graphType is not none
            space.addWidget(self.toolbar)
        else:
            # creates the encouraging message at the top 
            self.view_title = QLabel(title) 
            self.view_title.setAlignment(Qt.AlignCenter)
            self.view_title.setFont(QtGui.QFont("Arial",25,QtGui.QFont.Bold))
            space.addWidget(self.view_title) 
        space.addWidget(self.canvas) 

        # calls the function responsable of plotting the graph 
        if(graphType == "Faltas absolutas" or graphType == "Faltas relativas"):
            # get the names of the teams 
            teamL = self.log.iloc[0,2]
            teamR = self.log.iloc[0,3]
            # creates the variables which will hold the number of foul_charge
            faltasTeamL = 0
            faltasTeamR = 0
            # increments the number of foul_charge for team for every "block" of foul_charge in the log
            for i in range(self.log.shape[0]):
                if(self.log.iloc[i,1] == "foul_charge_l" and self.log.iloc[i+1,1] != "foul_charge_l"):
                    faltasTeamL += 1
                elif(self.log.iloc[i,1] == "foul_charge_r" and self.log.iloc[i+1,1] != "foul_charge_r"):
                    faltasTeamR += 1
            
            # defines the data list based on the graphType, absolute or relative(percentage)
            if(graphType == "Faltas absolutas"):
                xLabel = "Nome do time"
                yLabel = "Total de faltas cometidas"
                data = [2,teamL,teamR,faltasTeamL,faltasTeamR,xLabel,yLabel]
            else:
                xLabel = "Nome do time"
                yLabel = "Porcentagem de faltas cometidas"
                faltasTotal = faltasTeamL + faltasTeamR
                data = [2,teamL,teamR,(100*faltasTeamL)/faltasTotal,(100*faltasTeamR)/faltasTotal,xLabel,yLabel]  
            # calls the function to plot the graph 
            self.plot_Bar(title,data)
        
        elif(graphType == "Quantidade absoluta de gols"):
            pass
        elif(graphType == "Quantidade relativa de gols"):
            pass
        #TEST PIE e TEST BAR deverão ser excluídos, inclusive da lista, estão aqui apenas para servir de referência durante o desenvolvimento.
        elif(graphType == "TEST PIE"):
            self.plot_Pie("TEST PIE - APENAS PARA REFERÊNCIA ")
        elif(graphType == "TEST BAR"):
            self.plot_Bar("TEST BAR - APENAS PARA REFERÊNCIA",[2,2,2,10,20,"xLabel","yLabel"])
        '''(...)'''
        
        return space


    #TODO: implementar, xlabel, ylabel e labels individuais de cada bar e imbutir esses dados em `data`
    def plot_Bar(self, title, data):
       
        # TODO: documentar o funcionamento disto daqui
        # treating the data list to pass to the matplotlib methods
            
            # gets the xAxis values and yAxis values  
        xAxis = []
        yAxis = []
        cursor = 0 
        for i in range (1,data[0]+1):
            xAxis.append(data[i])
            cursor = i
        NUMBER_OF_FEATURES = 2
        for i in range (cursor+1,len(data)-NUMBER_OF_FEATURES):
            yAxis.append(data[i])
            cursor = i 
            
            # gets the xLabel and yLabel from the data list
        xLabel = data[cursor+1]
        yLabel = data[cursor+2]
        cursor += 2
       
        # setting the graph  
            # create an axis
        ax = self.figure.add_subplot(111) 
            # sets the axis labels
        ax.set_xlabel(xLabel) 
        ax.set_ylabel(yLabel)
            # plot data
        bar1 = ax.bar(xAxis[0],yAxis[0],label = "label1")
        bar2 = ax.bar(xAxis[1],yAxis[1],label = "label1")
            # set title
        ax.set_title(title)


        #TODO: is this necessary?
        # discards the old graph
        #ax.clear()
 
        #TODO: is this necessary?
        # refresh canvas
        #self.canvas.draw()
        

    def plot_Pie(self, title):

        data = [50,50]
        label = ["A","B"]

        # create an axis
        ax = self.figure.add_subplot(111)

        # plot data
        ax.pie(data, labels = label)

        # set title
        ax.set_title(title)

        #TODO: is this necessary?
        # discards the old graph
        #ax.clear()
 
        #TODO: is this necessary?
        # refresh canvas
        #self.canvas.draw()
   
    def define_Log(self):
        self.log = pd.read_csv('./files/t1.rcg.csv')

    def get_Score(self): 
        placar = [self.log['team_score_l'].max(),self.log['team_score_r'].max()]
        team_left = self.log.iloc[0].team_name_l
        team_right = self.log.iloc[0].team_name_r
        equipes = [team_left,team_right]
        eixox = np.arange(len(equipes))
    
    def getOut(self):
        sys.exit()


if __name__ == "__main__":
    Application = QApplication(sys.argv)
    Main = MainWindow()
    sys.exit(Application.exec())