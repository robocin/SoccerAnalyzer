import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from MainWindowLayouts import DefaultLayout
from PopUpWindows import fileSelector 


#MainWindow = QtWidgets.QMainWindow 

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, application):
        super().__init__()

        # gets the QApplication object passed as a parameter for this QMainWIndow  
        self.application = application

        # Main Window initializations 
        self.initialize_main_window("RobôCIn statistics extractor", '../files/images/robocin-03-small.png')
        self.initialize_menu_bar()

        # initialize the default layout()
        DefaultLayout.set_default_layout(self)

    def initialize_main_window(self, window_title, icon_path):
        # creates the array that will hold all the current mainWIndow dockers 
        self.dockers_list = [] # This is only needed until we find how to get all children of QMainWindowWidget
        self.mdiArea_sub_windows_list = []

        # gets the current monitor screen size
        self.screen = self.application.primaryScreen()
        self.rect = self.screen.availableGeometry()

        # declare variables that holds the screen title, window icon image and dimensions
        self.title = window_title
        self.icon_path = icon_path 
        self.width = int(self.rect.width())
        self.height = int(self.rect.height())

        # sets the title, icon image, dimensions(geometry), statusBar
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon_path))
        self.setGeometry(0, 0, self.width, self.height)

        # turns the main window visible
        self.show()

    def initialize_menu_bar(self):
         # adds the main window menuBar
        self.menu_bar = self.menuBar()
            # 'File' menu
        self.menu_bar_file_menu = self.menu_bar.addMenu("File") 
        self.menu_bar_file_menu_open_action = QtWidgets.QAction("Open")
        self.menu_bar_file_menu.addAction(self.menu_bar_file_menu_open_action)
        self.menu_bar_file_menu.triggered.connect(fileSelector.fileSelectorPopUp)
            # 'Edit' menu 
        self.menu_bar_edit_menu = self.menu_bar.addMenu("Edit") 
        self.menu_bar_edit_menu_layout_menu =  self.menu_bar_edit_menu.addMenu("Layout")
        self.menu_bar_edit_menu_layout_menu_default_action = self.menu_bar_edit_menu_layout_menu.addAction("Default") 
        self.menu_bar_edit_menu_layout_menu_default_action.triggered.connect(lambda: DefaultLayout.set_default_layout(self))
            # 'About' menu 
        self.menu_bar_about_menu = self.menu_bar.addMenu("About") 
                # 'About Qt' Action
        self.menu_bar_about_menu_about_qt_action = QtWidgets.QAction("About Qt")
        self.menu_bar_about_menu.addAction(self.menu_bar_about_menu_about_qt_action)
        self.menu_bar_about_menu_about_qt_action.triggered.connect(self.application.aboutQt)

    def exit(self): 
        sys.exit()