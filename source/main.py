import sys
from PyQt5 import QtWidgets
from Classes import MainWindow
from PopUpWindows import fileSelector
from utility_functions import organize_data


if __name__ == "__main__":

   # Starts the Qt application
   Application = QtWidgets.QApplication(sys.argv)

   # Asks for the log file
   file_path = None
   while(file_path==None):
      file_path = fileSelector.open_most_recent_file_or_ask_if_there_is_none()

   # data extraction and data computing
   game_data = organize_data.organize_data(file_path)

   # Call the main window
   MainWindow = MainWindow.MainWindow(Application, game_data)#, game_statistics) 
   
   # Exit if system asks for it
   sys.exit(Application.exec())