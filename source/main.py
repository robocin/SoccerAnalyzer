import sys
from PyQt5 import QtWidgets
from Classes import MainWindow
from PopUpWindows import fileSelector
import DataExtractor


if __name__ == "__main__":

    # Starts the Qt application
    Application = QtWidgets.QApplication(sys.argv)

    # Asks for the log file
    file_path = None
    while(file_path==None):
       file_path = fileSelector.fileSelectorPopUp()

    # Call for data extraction
    game_data = DataExtractor.data_extractor(file_path)

    # Call for data computing
    #game_statistics = DataExtractor.data_computing(game_data)

    # Call the main window
    MainWindow = MainWindow.MainWindow(Application, game_data)#, game_statistics) 
    
    # Exit if system asks for it
    sys.exit(Application.exec())