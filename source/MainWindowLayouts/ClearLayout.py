

def set_clear_layout(MainWindow):
    # erases any docker currently in the mainWindow
    for docker in MainWindow.dockers_list:
        MainWindow.removeDockWidget(docker)
    # erases the central widget
    MainWindow.takeCentralWidget()