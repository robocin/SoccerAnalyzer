import sys
from PyQt5 import QtWidgets
from Classes import MainWindow


if __name__ == "__main__":
    Application = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow.MainWindow(Application) 
    sys.exit(Application.exec())