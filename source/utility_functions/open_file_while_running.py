from PopUpWindows import fileSelector
from utility_functions import organize_data, clear_main_mdi_area
from MainWindowLayouts import ClearLayout, DefaultLayout

def open_file_while_running(MainWindow, game_data):
    file_path = fileSelector.file_selector()
    organize_data.organize_data(file_path, game_data) 
    clear_main_mdi_area.clear_main_mdi_area(MainWindow)
    DefaultLayout.create_big_message(MainWindow)
    MainWindow.setWindowTitle("RobôCIn statistics extractor - {} {} X {} {}".format(game_data.get_team(0).get_name(),game_data.get_team(0).get_number_of_goals_scored(), game_data.get_team(1).get_number_of_goals_scored(), game_data.get_team(1).get_name()))