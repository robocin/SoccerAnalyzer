import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QListWidget, QLabel, QMenuBar, QAction
from PyQt5 import QtGui, QtCore

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

import numpy as np
import pandas as pd

STATISTICS = "EXTRACTION_FIELDS"

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
        self.setWindowIcon(QtGui.QIcon('robocin-03-small.png'))
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.statusBar().showMessage("Statusbar - awaiting user control")
        ##### END OF SCREEN INITIALIZATION #####

        #setting the main layout to be horizontal
        self.main_hbox = QHBoxLayout()

        #creating the elements of the window (calling custom functions)
        self.init_Menu() #menu principal no topo da tela
        self.init_List() #lista lateral esquerda
        #self.create_View("bar") #área do gráfico, à direita da lista

        #creating central widget and putting it in the main window as a central widget
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_hbox)
        self.setCentralWidget(self.main_widget)
        
        #turns main window visible
        self.show()
    ##### Definition of custom functions #####
    def init_Menu(self):
        '''
        Cria o menu principal e conecta suas ações às 
        chamadas de funções respectivas
        '''
        #cria o menu principal no topo da janela
        self.mainMenu = self.menuBar()
        fileMenu = self.mainMenu.addMenu("File")
        editMenu = self.mainMenu.addMenu("Edit")
        selectionMenu = self.mainMenu.addMenu("Selection")
        viewMenu = self.mainMenu.addMenu("View")
        terminalMenu = self.mainMenu.addMenu("Terminal")
        helpMenu = self.mainMenu.addMenu("Help")
        #cria a ação "clear" na opção "edit" do menu principal
        clearAction = QAction("Clear", self)
        editMenu.addAction(clearAction)
            #conecta a ação "clear" à função clear_View()     
        clearAction.triggered.connect(self.clear_View)
    
    def init_List(self):
        '''
        Cria a lista de seleção da esquerda
        '''
        # cria a lista da esquerda 
        self.main_list = QListWidget()
        # define as dimensões máximas e mínimas da lista 
        self.main_list.setMinimumHeight(300)
        self.main_list.setMaximumHeight(600)
        self.main_list.setMaximumWidth(181)
        self.main_list.setMinimumWidth(180)
        # cria os itens da lista 
        self.main_list.insertItem(0,"pie")
        self.main_list.insertItem(1,"bar")
        self.main_list.insertItem(2,STATISTICS)
        self.main_list.insertItem(3,STATISTICS)
        self.main_list.insertItem(4,STATISTICS)
        self.main_list.insertItem(5,STATISTICS)
        self.main_list.insertItem(6,STATISTICS)
        self.main_list.insertItem(7,STATISTICS)
        self.main_list.insertItem(8,STATISTICS)
        self.main_list.insertItem(9,STATISTICS)
        # adiciona a lista à main_hbox 
        self.main_hbox.addWidget(self.main_list)
        # ao clicar num item, manda sinal para a função itemSelected
        self.main_list.itemClicked.connect(self.itemSelected)

    def itemSelected(self, item):
        stat = item.text()
        self.create_View(stat)

    def create_View(self, title):  
        '''
        Cria a região, à direita da tela, onde o gráfico será plotado.
        
        '''
        # cria o view_groupBox  (região do gráfico)
        self.view_groupBox = QGroupBox()
        # cria o layout do view_groupBox 
        self.layout = QVBoxLayout()
        # limpa a área do gráfico se já houver sendo mostrado 
        if self.VIEW_FILLED == True:
            self.clear_View(title)
        # cria a área do gráfico
        self.plot_Area = self.create_Plot(title)
                                        #TODO: o que é? tira? 
                                        #self.view_Title = QLabel(title)
                                        #self.layout.addWidget(self.plot_Area)
        # define o layout do view_groupBox 
        self.view_groupBox.setLayout(self.plot_Area)
        # adiciona o view_groupBox à main_hbox 
        self.main_hbox.addWidget(self.view_groupBox) 
        self.VIEW_FILLED = True



    #TODO: ENTENDER O FUNCIONAMENTO INERNO DE CLEAR_VIEW
    def clear_View(self, title):  
        for i in reversed(range(self.main_hbox.count())): 
            if i > 0:
                self.main_hbox.itemAt(i).widget().setParent(None)  
        self.VIEW_FILLED = False
        #self.create_View(title)

    def create_Plot(self, title):
        '''
        Cria o figure, o canvas, a barra de ferramentas de navegação,
        e organiza o layout.
        Chama a função de plotar o gráfico
        '''
        # cria uma 'figure', onde o gráfico será plotado
        self.figure = Figure()

        # cria o widget canvas, que "segura" o figure
        self.canvas = FigureCanvas(self.figure)

        # cria o widget da barra de ferramentas de navegação
        self.toolbar = NavigationToolbar(self.canvas, self)

        #(Bloco de código p/ se quiser plotar atravéz de um botão)
        # Just some button connected to `plot` method
        #self.button = QPushButton('Plot')
        #self.button.clicked.connect(self.plot)

        # organiza o layout do toolbar e do canvas 
        space = QVBoxLayout()
        space.addWidget(self.toolbar)
        space.addWidget(self.canvas) 

        # chama a função que vai plotar o gráfico  
        if(title == "pie"):
            self.plot_Pie()
        elif(title == "bar"):
            self.plot_Bar()

        return space

    def plot_Bar(self):
        
        data = [50,50]

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.clear()

        # plot data
        ax.bar(data,2)

        # refresh canvas
        self.canvas.draw()

    def plot_Pie(self):

        data = [50,50]
        label = ["A", "B"]

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.clear()

        # plot data
        ax.pie(data, labels = label)

        # refresh canvas
        self.canvas.draw()
   
    def define_Log(self):
        self.log = pd.read_csv('./t1.rcg.csv1')

    #TODO: essa função:
    def get_Score(self):
        pass

    def getOut(self):
        sys.exit()


if __name__ == "__main__":
    Application = QApplication(sys.argv)
    Main = MainWindow()
    sys.exit(Application.exec())
