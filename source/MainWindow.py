import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QMessageBox, QWidget, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QListWidget, QLabel, QMenuBar, QAction, QFileDialog
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
LIST_MINIMUM_HEIGHT = 150
LIST_MAXIMUM_HEIGHT = 151
#LIST_MINIMUM_WIDTH = 181
#LIST_MAXIMUM_WIDTH = 180
LIST_MINIMUM_WIDTH = 210
LIST_MAXIMUM_WIDTH = 211

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
            # Log selection PopUp
        self.category = self.selectorScreenPopUp()
        self.log_path = self.select_file()

            # MainScreen
        self.game_info = DataCollector(self.log_path)
        self.mainScreen(self.category)

        #creating central widget and putting it in the main window as a central widget
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_hbox)
        self.setCentralWidget(self.main_widget)
        
        #turns main window visible
        self.show()


    ## Screen type functions ##
    def selectorScreenPopUp(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Log type selection")
        msgBox.setText("Select the log type") 
        msgBox.setIcon(QMessageBox.Question)

        button1 = msgBox.addButton("2D",QMessageBox.ActionRole)
        button2 = msgBox.addButton("VSS",QMessageBox.ActionRole)
        button3 = msgBox.addButton("SSL",QMessageBox.ActionRole)

        x = msgBox.exec_()

        if (msgBox.clickedButton() == button1):
            category = "2D"
        if (msgBox.clickedButton() == button2):
            category = "VSS"
        if (msgBox.clickedButton() == button2):
            category = "SSL"

        return category

    def mainScreen(self, category):
        # All log types
        self.init_Menu() # main menu at the top of the screen
        # 2D
        if(category == "2D"):
            self.init_List("2D") # left side list
            self.create_view(False,"Escolha uma das opções na lista à esquerda") # right side graph area
        # vss
        if(category == "VSS"):
            pass
            #self.init_List("VSS") # left side list
            #self.create_view(False,"Escolha uma das opções na lista à esquerda") # right side graph area
        # ssl
        if(category == "SSl"):
            pass
    
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
        
        #Actions inside fileMenu
        findFile = QAction("File", self)
        fileMenu.addAction(findFile)
        findFile.triggered.connect(self.select_file)

        #creates the "clear" action inside the "edit" option on the main menu 
        clearAction = QAction("Clear", self)
        editMenu.addAction(clearAction)
        
        #connects the "clear" action to the clear_View() function 
        clearAction.triggered.connect(self.clear_View) # when calling clear_View without specifying parameters, False is given as parameter to graph_type
 
    def init_List(self, category):
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
        
        # Based on the category, creates the correspondent list and list items
            # 2D
        if(category == "2D"):
            self.main_list.insertItem(0, "Quantidade de faltas")
            self.main_list.insertItem(1, "Proporção de faltas")
            self.main_list.insertItem(2, "Posição das faltas")
            self.main_list.insertItem(3, "Quantidade de gols")
            self.main_list.insertItem(4, "Proporção de gols")
            self.main_list.insertItem(5, "Posição dos gols")
            self.main_list.insertItem(6, "Heatmap: ball position")
            #self.main_list.insertItem(7,)
            #self.main_list.insertItem(8,)
            #self.main_list.insertItem(9,)

            # vss
        elif(category == "VSS"):
            self.main_list.insertItem(0, "Mapa de calor: posição dos jogadores")

            # ssl
        elif(category == "SSL"):
            pass
        
        self.main_list.setWordWrap(True)

        # adds the list to the main_hbox
        self.main_hbox.addWidget(self.main_list)
        
        # when an item is clicked on, sends a signal to the itemSelected() function 
        self.main_list.itemClicked.connect(self.itemSelected)
    
    def itemSelected(self, item):
        stat = item.text()
        self.create_view(stat, stat)

    def select_file(self): 
        filename, _trash = QFileDialog.getOpenFileName(self, "*.")
        return filename

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

        # Creates the scoreboard widget
        if(graph_type != False):
            placar = self.game_info.get_team("l").get_name() + " " + str(self.game_info.get_team("l").get_number_of_goals_scored()) + " X " + str(self.game_info.get_team("r").get_number_of_goals_scored()) + " "+ self.game_info.get_team("r").get_name()
            self.scoreboard = QLabel(placar) 
            self.scoreboard.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
            self.scoreboard.setAlignment(QtCore.Qt.AlignCenter |QtCore.Qt.AlignVCenter)

        # creates the navigationToolbar widget  
        if(graph_type != False): 
            self.toolbar = NavigationToolbar(self.canvas, self)

        # customizes the toolbar and canvas layout 
        
        space = QVBoxLayout()
             
        if(graph_type != False): #if graph_type is not none
            space.addWidget(self.scoreboard)
            space.addWidget(self.toolbar)
        else:
            # creates the encouraging message at the top 
            self.view_title = QLabel(title) 
            self.view_title.setAlignment(Qt.AlignCenter)
            self.view_title.setFont(QtGui.QFont("Arial",25,QtGui.QFont.Bold))
            space.addWidget(self.view_title) 
            # Note: here we add the matplotlib canvas to the qvbox
        space.addWidget(self.canvas) 

        # calls the function responsable of plotting the graph 
        if(graph_type == "Quantidade de faltas"):
            self.game_info.plot_faults_quantity(self,"Quantidade de faltas")                

        elif(graph_type == "Proporção de faltas"):
            self.game_info.plot_faults_percentage(self,"Proporção de faltas")

        elif(graph_type == "Posição das faltas"):
            self.game_info.plot_faults_position(self, "Posição das faltas")
        elif(graph_type == "Quantidade de gols"):
            self.game_info.plot_goals_quantity(self, "Quantidade de gols")
        
        elif(graph_type == "Proporção de gols"):
            self.game_info.plot_goals_percentage(self, "Proporção de gols") 

        elif(graph_type == "Posição dos gols"):
            self.game_info.plot_goals_position(self, "Posição dos gols")
        
        elif(graph_type == "Heatmap: ball position"):
            self.game_info.plot_heatmap_ball_position(self, "Heatmap: ball position")

        return space
    

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
