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

from DataCollector import DataCollector 
from PlotData import PlotData
from Team import Team 
from Event import Event
from Player import Player
from Position import Position

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
        self.create_view(False,"Escolha uma das opções na lista à esquerda") # right side graph area
        self.define_log()
        self.game_info = DataCollector()

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
        clearAction.triggered.connect(self.clear_View) # when calling clear_View without specifying parameters, False is given as parameter to graph_type
 
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
        self.main_list.insertItem(0, "Faltas absolutas")
        self.main_list.insertItem(1, "Faltas relativas")
        self.main_list.insertItem(2, "Posição das faltas")
        self.main_list.insertItem(3, "[TODO]Quantidade absoluta de gols")
        self.main_list.insertItem(4, "[TODO]Quantidade relativa de gols")
        #self.main_list.insertItem(5,)
        #self.main_list.insertItem(6,)
        #self.main_list.insertItem(7,)
        #self.main_list.insertItem(8,)
        #self.main_list.insertItem(9,)
        
        # adds the list to the main_hbox
        self.main_hbox.addWidget(self.main_list)
        
        # when an item is clicked on, sends a signal to the itemSelected() function 
        self.main_list.itemClicked.connect(self.itemSelected)
    
    def itemSelected(self, item):
        stat = item.text()
        self.create_view(stat, stat)

    def create_view(self, graph_type, title):  
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
        self.plot_Area = self.create_Plot(graph_type, title)
        # defines the layout of view_groupBox
        self.view_groupBox.setLayout(self.plot_Area)
        # adds the view_groupBox to the main_hbox 
        self.main_hbox.addWidget(self.view_groupBox) 
        self.VIEW_FILLED = True

    def clear_View(self, graph_type):
        #for widget in main_hbox,
        for i in reversed(range(self.main_hbox.count())): 
            if i > 0:
                self.main_hbox.itemAt(i).widget().setParent(None)  
        self.VIEW_FILLED = False
        # if the clear_View function was called by a signal from: MainMenu -> edit -> clear, 
        if (graph_type == False):
            self.create_view(False,"Escolha uma das opções na lista à esquerda")
   
    def create_Plot(self, graph_type, title):
        '''
        Creates figure, cavas, navigationToolbar, and configures the layout.
        Calls the function to plot the graph.
        '''
        # creates a 'figure', where to plot the graphs on 
        self.figure = Figure()

        # creates a canvas widget, which displays the figure 
        self.canvas = FigureCanvas(self.figure)

        # creates the navigationToolbar widget  
        if(graph_type != False): 
            self.toolbar = NavigationToolbar(self.canvas, self)

        # customizes the toolbar and canvas layout 
        
        space = QVBoxLayout()
             
        if(graph_type != False): #if graph_type is not none
            space.addWidget(self.toolbar)
        else:
            # creates the encouraging message at the top 
            self.view_title = QLabel(title) 
            self.view_title.setAlignment(Qt.AlignCenter)
            self.view_title.setFont(QtGui.QFont("Arial",25,QtGui.QFont.Bold))
            space.addWidget(self.view_title) 
        space.addWidget(self.canvas) 

        # calls the function responsable of plotting the graph 
        if(graph_type == "Faltas absolutas" or graph_type == "Faltas relativas" or graph_type == "Posição das faltas"):
            # defines the data list based on the graph_type, absolute or relative(percentage)
            if(graph_type == "Faltas absolutas"):
                self.game_info.plot_faults_quantity(self,"Faltas absolutas")                

            elif(graph_type == "Faltas relativas"):
                self.game_info.plot_faults_percentage(self,"Faltas Relativas")

            elif(graph_type == "Posição das faltas"):
                self.game_info.plot_faults_position(self, "Posição das faltas")

        elif(graph_type == "Quantidade absoluta de gols"):
            self.game_info.plot_goals_quantity()
        
        elif(graph_type == "Quantidade relativa de gols"):
            self.game_info.plot_goals_percentage() 

        return space
    

    def define_log(self):
        self.log_path = './files/t1.rcg.csv'

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
