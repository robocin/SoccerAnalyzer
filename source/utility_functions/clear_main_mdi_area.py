#TODO: generalizar isso para qq mdiArea passada como argumento.
def clear_main_mdi_area(MainWindow):
    for subWindow in MainWindow.mdiArea_sub_windows_list:
        MainWindow.mdiArea.removeSubWindow(subWindow)
    MainWindow.mdiArea_sub_windows_list = []

