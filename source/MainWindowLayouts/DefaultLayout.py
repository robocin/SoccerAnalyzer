from PyQt5 import QtWidgets
from PyQt5 import QtCore
from MainWindowLayouts import ClearLayout
from PyQt5 import QtGui


def set_default_layout(MainWindow):
    # sets clean layout #
    ClearLayout.set_clear_layout(MainWindow)
    
    # creates an mdiArea and sets it as the MainWindow central widget 
    MainWindow.mdiArea = QtWidgets.QMdiArea()  
    MainWindow.setCentralWidget(MainWindow.mdiArea)

    # creates and customizes the QListWidget #
    create_features_list(MainWindow)

    # creates the dock widget and customizes it
    create_features_list_docker(MainWindow)

    # sets the list widget as child of the docker
    MainWindow.features_list_docker.setWidget(MainWindow.features_list)

    # creates the big message (subWindow of the mdiArea)#
    create_big_message(MainWindow)

def create_features_list(MainWindow):
    #TODO: make the width of the QListWidget be minimum
    # creates and customizes the QListWidget #
    MainWindow.features_list = QtWidgets.QListWidget()

    list_items = []
    font = QtGui.QFont()
    font.setPointSize(12)

        # creates the fouls quantity QListWidgetItem
    MainWindow.features_list_item_1 = QtWidgets.QListWidgetItem("Fouls Quantity")
    list_items.append(MainWindow.features_list_item_1) 
    MainWindow.features_list.addItem(MainWindow.features_list_item_1)

        # creates the fouls quantity QListWidgetItem
    MainWindow.features_list_item_2 = QtWidgets.QListWidgetItem("Fouls Proportion")
    list_items.append(MainWindow.features_list_item_2) 
    MainWindow.features_list.addItem(MainWindow.features_list_item_2)

        # creates the fouls quantity QListWidgetItem
    MainWindow.features_list_item_3 = QtWidgets.QListWidgetItem("Heatmaps")
    list_items.append(MainWindow.features_list_item_3) 
    MainWindow.features_list.addItem(MainWindow.features_list_item_3)

        # creates the fouls quantity QListWidgetItem
    MainWindow.features_list_item_4 = QtWidgets.QListWidgetItem("Goal Replay")
    list_items.append(MainWindow.features_list_item_4) 
    MainWindow.features_list.addItem(MainWindow.features_list_item_4)

        # creates the fouls quantity QListWidgetItem
    MainWindow.features_list_item_5 = QtWidgets.QListWidgetItem("Player Replay")
    list_items.append(MainWindow.features_list_item_5) 
    MainWindow.features_list.addItem(MainWindow.features_list_item_5)

        # creates the fouls quantity QListWidgetItem
    MainWindow.features_list_item_6 = QtWidgets.QListWidgetItem("Stamina Tracker")
    list_items.append(MainWindow.features_list_item_6) 
    MainWindow.features_list.addItem(MainWindow.features_list_item_6)

    for item in list_items:
        item.setFont(font)
        item.setTextAlignment(QtCore.Qt.AlignHCenter)

def create_features_list_docker(MainWindow):
    # creates the dock widget and customizes it
    MainWindow.features_list_docker = QtWidgets.QDockWidget(MainWindow)
    MainWindow.dockers_list.append(MainWindow.features_list_docker)
    MainWindow.features_list_docker.setFeatures(QtWidgets.QDockWidget.DockWidgetMovable)
        # creates, customizes and adds a QLabel widget to the list widget docker as the a custom title bar 
    MainWindow.features_list_docker_custom_title_bar = QtWidgets.QLabel("Features List")
    MainWindow.features_list_docker_custom_title_bar.setStyleSheet(" font-size: 25px; qproperty-alignment: AlignCenter; font-family: Arial;")
    MainWindow.features_list_docker.setTitleBarWidget(MainWindow.features_list_docker_custom_title_bar)
    # adds the list docker to de MainMenu
    MainWindow.addDockWidget(QtCore.Qt.LeftDockWidgetArea, MainWindow.features_list_docker)

def create_big_message(MainWindow):
    # creates the big message (subWindow of the mdiArea)#
    MainWindow.message_qlabel = QtWidgets.QLabel("Selecione uma das opções na lista à esquerda")
    MainWindow.message_qlabel.setStyleSheet(" font-size: 40px; qproperty-alignment: AlignCenter; font-family: Arial;")
    MainWindow.message_sub_window = MainWindow.mdiArea.addSubWindow(MainWindow.message_qlabel)
    MainWindow.mdiArea_sub_windows_list.append(MainWindow.message_sub_window)
    MainWindow.message_sub_window.showMaximized()
