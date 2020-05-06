import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QListWidget, QLabel, QMenuBar, QAction
from PyQt5 import QtGui, QtCore

STATISTICS = "EXTRACTION_FIELDS"

class Canvas(QWidget):
    def __init__(self):
        super().__init__()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.VIEW_FILLED = False


##################################################### SCREEN INITIALIZATION ###################################################
        #getting CURRENT monitor screen size
        self.dimensions = QApplication(sys.argv)
        self.screen = self.dimensions.primaryScreen()
        self.rect = self.screen.availableGeometry()
    
        self.title = 'RobôCIn statistics extractor'
        self.width = self.rect.width()
        self.height = self.rect.height()
        self.top = (self.rect.height()/2) - (self.height/2) 
        self.left = (self.rect.width()/2) -  (self.width/2) 

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon('robocin-03-small.png'))
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.statusBar().showMessage("Statusbar - awaiting user control")
    

############################################ END OF SCREEN INITIALIZATION ####################################################

        #setting the main layout to be horizontal
        self.main_hbox = QHBoxLayout()

        #creating the elements of the window
        self.init_Menu()
        self.init_List()
        self.create_View("")

        #creating central widget and putting it int the main window as a central widget
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_hbox)
        self.setCentralWidget(self.main_widget)


        self.show()

    def init_Menu(self):
        self.mainMenu = self.menuBar()
        fileMenu = self.mainMenu.addMenu("File")
        editMenu = self.mainMenu.addMenu("Edit")
        selectionMenu = self.mainMenu.addMenu("Selection")
        viewMenu = self.mainMenu.addMenu("View")
        terminalMenu = self.mainMenu.addMenu("Terminal")
        helpMenu = self.mainMenu.addMenu("Help")

        clearAction = QAction("Clear", self)
        editMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear_View)




    
    def init_List(self):
        self.main_list = QListWidget()
        self.main_list.setMinimumHeight(300)
        self.main_list.setMaximumHeight(600)
        self.main_list.setMaximumWidth(181)
        self.main_list.setMinimumWidth(180)
        self.main_list.insertItem(0,"T1")
        self.main_list.insertItem(1,"T2")
        self.main_list.insertItem(2,STATISTICS)
        self.main_list.insertItem(3,STATISTICS)
        self.main_list.insertItem(4,STATISTICS)
        self.main_list.insertItem(5,STATISTICS)
        self.main_list.insertItem(6,STATISTICS)
        self.main_list.insertItem(7,STATISTICS)
        self.main_list.insertItem(8,STATISTICS)
        self.main_list.insertItem(9,STATISTICS)

        self.main_list.itemClicked.connect(self.itemSelected)

        self.main_hbox.addWidget(self.main_list)


    def itemSelected(self, item):
        stat = item.text()
        self.create_View(stat)
   

    def create_View(self, text):
        
        self.view_groupBox = QGroupBox()
        self.layout = QVBoxLayout()

        if self.VIEW_FILLED == False:
            self.view_Title = QLabel(text)
            self.layout.addWidget(self.view_Title)
            self.view_groupBox.setLayout(self.layout)
            self.main_hbox.addWidget(self.view_groupBox)
            self.VIEW_FILLED = True
        else:
            self.clear_View(text)

    
    def clear_View(self, text):
        
        for i in reversed(range(self.main_hbox.count())): 
            if i > 0:
                self.main_hbox.itemAt(i).widget().setParent(None)
        
        self.VIEW_FILLED = False
        self.create_View(text)

    def getOut(self):
        sys.exit()


if __name__ == "__main__":
    Application = QApplication(sys.argv)
    Main = MainWindow()
    sys.exit(Application.exec())

