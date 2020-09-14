from PyQt5 import QtWidgets
from PyQt5 import QtGui

#TODO: solve: popup not closing when pressin the x button or using shortcut Alt+f4.
def fileSelectorPopUp():
    # category = askTipeOfFile()
    # filename = select_file(category)
    # if (is_valid(filename)):
    #     print(filename) 
    #     return filename
    # else:
    #     warning_message_popup("Invalid File Format!", "File must be a .csv")
    #     return None
    return "/home/mateus/pastas/git/log-analyzer/files/logs/t1.rcg.csv"
 

# TODO: write a better validating function
def is_valid(filename):
    if '.csv' in filename:
        return True
    return False

def askTipeOfFile():
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Log type selection")
        msgBox.setText("Select the log type") 
        msgBox.setIcon(QtWidgets.QMessageBox.Question)

        button1 = msgBox.addButton("2D",QtWidgets.QMessageBox.ActionRole)
        button2 = msgBox.addButton("VSS",QtWidgets.QMessageBox.ActionRole)
        button3 = msgBox.addButton("SSL",QtWidgets.QMessageBox.ActionRole)

        x = msgBox.exec_()

        if (msgBox.clickedButton() == button1):
            category = "2D"
        elif (msgBox.clickedButton() == button2):
            category = None
            warning_message_popup("Not yet implemented :(", "Category not yet implemented!")
        elif (msgBox.clickedButton() == button3):
            category = None
            warning_message_popup("Not yet implemented :(", "Category not yet implemented!")

        return category

def select_file(category):
    if(category=="2D"): 
        filename, _trash = QtWidgets.QFileDialog.getOpenFileName()
        return filename    

def warning_message_popup(title, message):
        warning_message = QtWidgets.QMessageBox()
        warning_message.setWindowTitle(title)
        warning_message.setText(message)
        font = QtGui.QFont()
        font.setPointSize(12)
        warning_message.setFont(font)
        warning_message.exec_()

