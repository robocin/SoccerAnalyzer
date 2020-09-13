from PyQt5 import QtWidgets 

def fileSelectorPopUp():
    category = askTipeOfFile()
    filename = select_file(category)

def askTipeOfFile():
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Log type selection")
        msgBox.setText("Select the log type") 
        msgBox.setIcon(QtWidgets.QMessageBox.Question)

        button1 = msgBox.addButton("2D",QtWidgets.QMessageBox.ActionRole)
        button2 = msgBox.addButton("VSS",QtWidgets.QMessageBox.ActionRole)
        button3 = msgBox.addButton("SSL",QtWidgets.QMessageBox.ActionRole)

        x = msgBox.exec_()

        warning_message = QtWidgets.QMessageBox()
        warning_message.setWindowTitle("Ainda não implementado :(")
        warning_message.setText("Categoria ainda não implementada!")


        if (msgBox.clickedButton() == button1):
            category = "2D"
        elif (msgBox.clickedButton() == button2):
            category = None
            warning_message.exec_()
        elif (msgBox.clickedButton() == button3):
            category = None
            warning_message.exec_()

        return category

def select_file(category):
    if(category=="2D"): 
        filename, _trash = QtWidgets.QFileDialog.getOpenFileName()
        return filename    