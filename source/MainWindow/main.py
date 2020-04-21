import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QListWidget, QLabel, QMenuBar
from PyQt5 import QtGui, QtCore

STATISTICS = "EXTRACTION_FIELDS"

class Canvas(QWidget):
    def __init__(self):
        super().__init__()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

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
        self.init_View("")

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
        self.init_View(stat)
   

    def init_View(self, text):
        nullLabel = QLabel("NONE")
                
        if text != "":
            if text == 'T1':
                self.T1_SCREEN()
            elif text == 'T2':
                self.T2_SCREEN()
        else:
            self.main_hbox.addWidget(nullLabel)

   
   
    def clear_View(self):
        for widget in self.main_hbox.children():
            if isinstance(widget, QLabel):
                widget.deleteLater()


    def T1_SCREEN(self):
        label = QLabel("T1")
        self.clear_View()
        self.main_hbox.addWidget(label)


    def T2_SCREEN(self):
        label = QLabel("T2")
        self.clear_View()
        self.main_hbox.addWidget(label)


    def getOut(self):
        sys.exit()

if __name__ == "__main__":
    Application = QApplication(sys.argv)
    Main = MainWindow()
    sys.exit(Application.exec())

