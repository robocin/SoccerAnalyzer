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

import dataCollector 
import plotBarData
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
        self.width = int(self.rect.width())
        self.height = int(self.rect.height())
        self.top = int((self.rect.height()/2) - (self.height/2))
        self.left = int((self.rect.width()/2) -  (self.width/2))
        
        #setting the title, icon image, dimensions(geometry), statusBar
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon('./files/robocin-03-small.png'))
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.statusBar().showMessage("Statusbar - awaiting user control")
        ##### END OF SCREEN INITIALIZATION #####

        #setting the main layout to be horizontal
        self.main_hbox = QHBoxLayout()

        #creating the elements of the window and calling some computing functions
        self.init_Menu() # main menu at the top of the screen
        self.init_List() # left side list
        self.create_View(False,"Escolha uma das opções na lista à esquerda") # right side graph area
        self.define_Log()
        self.dataCollector = dataCollector.DataCollector(self.log)

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
        self.main_list.insertItem(4,"Posição das faltas")
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

        # TODO: check with 2D-veterans if the metod of getting the foul positinos is precise 
        # calls the function responsable of plotting the graph 
        if(graphType == "Faltas absolutas" or graphType == "Faltas relativas" or graphType == "Posição das faltas"):
            # defines the data list based on the graphType, absolute or relative(percentage)
            if(graphType == "Faltas absolutas"):
                #xLabel = "Nome do time"
                #yLabel = "Total de faltas cometidas"
                #data = [2,teamL,teamR,faltasTeamL,faltasTeamR,xLabel,yLabel]
                data_to_plot = plotBarData.PlotBarData()
                    # set data for graph
                data_to_plot.setXLabel(self.dataCollector.getTeam("l").getName())
                data_to_plot.setYLabel(self.dataCollector.getTeam("r").getName())
                data_to_plot.appendBars(2,["team_l_absolute_faults","team_r_absolute_faults"])                    


                    # set data for bar 1 
                bar1 =  data_to_plot.getBar(0)
                bar1.setName(self.dataCollector.getTeam("l").getName())
                bar1.setValue(self.dataCollector.getTeam("l").getNumberOfFaultsCommited()) 
                    # set data for bar 2 
                bar2 = data_to_plot.getBar(1) 
                bar2.setName(self.dataCollector.getTeam("r").getName())
                bar2.setValue(self.dataCollector.getTeam("r").getNumberOfFaultsCommited()) 
                
                # calls the function to plot the graph 
                self.plot_Bar(title,data_to_plot) 

            elif(graphType == "Faltas relativas"):
                pass 
                #TODO: refactor 
                #xLabel = "Nome do time"
                #yLabel = "Porcentagem de faltas cometidas"
                #faltasTotal = faltasTeamL + faltasTeamR
                #data = [2,teamL,teamR,(100*faltasTeamL)/faltasTotal,(100*faltasTeamR)/faltasTotal,xLabel,yLabel]  
                # calls the function to plot the graph 
                #self.plot_Bar(title,data)
            elif(graphType == "Posição das faltas"):
                pass 
                #TODO: refactor 
                xLabel = "x"
                yLabel = "y" 
                #(HARDCODED TO DEBUG) 
                data = [20,10,10,14,15,37,46,24,25,26,19,33]
                #data = [team1NumberOfFouls,team2NumberOfFouls,x1,x2,y1,y2,X1,X2,X3,Y1,Y2,Y3,]
                #data = [team1NumberOfFouls,team2NumberOfFouls,fatalsPostitions=[[team,x,y],[team,x,y] ... ]
                #data = [faltasTeamL,faltasTeamR,faltasPositions]
                self.plot_Scatter(title)

        elif(graphType == "Quantidade absoluta de gols"):
            pass
        elif(graphType == "Quantidade relativa de gols"):
            pass
        #TEST PIE e TEST BAR deverão ser excluídos, inclusive da lista, estão aqui apenas para servir de referência durante o desenvolvimento.
        elif(graphType == "TEST PIE"):
            self.plot_Pie("TEST PIE - APENAS PARA REFERÊNCIA ")
        elif(graphType == "TEST BAR"):
            data = plotBarData.PlotBarData()
            data.appendBars(1,["test bar"])
            data.setXLabel("x label")
            data.setYLabel("y label")
            bar = data.getBar(0) 
            bar.setName("Bar name")
            bar.setValue(100) 
            bar.setLabel("Bar label")
            self.plot_Bar("TEST BAR - APENAS PARA REFERÊNCIA",data)
        '''(...)'''
        
        return space

    #TODO: generalizar função
    #TODO: labels individuais de cada bar e imbutir esses dados em `data`
    def plot_Bar(self, title, data):
       
        # setting the graph  
            # create an axis
        ax = self.figure.add_subplot(111) 
            # sets the axis labels
        #print(type(data))
        ax.set_xlabel(data.getXLabel()) 
        ax.set_ylabel(data.getYLabel())
            # plot data
        bars = [] 
        for barIndex in range(0,len(data.getBars())):
            bars.append(ax.bar(data.getBar(barIndex).getName(), data.getBar(barIndex).getValue(), label = data.getBar(barIndex).getLabel()))
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

    #TODO: generalizar função
    def plot_Scatter(self, title):
        #TODO: Terminar esta implementação

        #data = [team1NumberOfFouls,team2NumberOfFouls,fatalsPostitions=[[team,x,y],[team,x,y] ... ]
        #data = [team1NumberOfFouls,team2NumberOfFouls,x1,x2,y1,y2,X1,X2,X3,Y1,Y2,Y3,]
        
        team1NumberOfFouls = 2
        team2NumberOfFouls = 3
     
        data = [team1NumberOfFouls,team2NumberOfFouls,10,15,10,15,35,40,45,35,40,45]
        
        #xPositionsTeam1 = [10,15]
        #yPositionsTeam1 = [10,15]
        #xPositionsTeam2 = [35,40,45]
        #yPositionsTeam2 = [35,40,45]

        xPositionsTeam1 = []
        yPositionsTeam1 = []
        xPositionsTeam2 = []
        yPositionsTeam2 = []


        for i in range(0, data[0]):
            xPositionsTeam1.append(data[i+2])
            yPositionsTeam1.append(data[i+4])
        for i in range(6, data[1]+6):
            xPositionsTeam2.append(data[i])
            yPositionsTeam2.append(data[i+3])

        team1 = (xPositionsTeam1,yPositionsTeam1) 
        team2 = (xPositionsTeam2,yPositionsTeam2)
        data = (team1,team2)
        
        colorTeam1 = "green"
        colorTeam2 = "red"
        colors = (colorTeam1,colorTeam2)
        
        team1Name = "team1"
        team2Name = "team2"
        groups = (team1Name,team2Name)

        # create an axis
        ax = self.figure.add_subplot(111)        
        
        
       
        for data, color, group in zip(data, colors, groups):
            x, y = data
            ax.scatter(x, y, alpha=1, c=color, edgecolors="none", s=30, label=group)
        
        # set title
        ax.set_title(title) 

        # set legend
        ax.legend(loc=2)

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

    ##### Computing #####


    ##### Showing #####


if __name__ == "__main__":
    Application = QApplication(sys.argv)
    Main = MainWindow()
    sys.exit(Application.exec())
