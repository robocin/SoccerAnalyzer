from PyQt5 import QtWidgets
from PyQt5 import QtGui

#TODO: solve: popup not closing when pressin the x button or using shortcut Alt+f4.


def open_most_recent_file_or_ask_if_there_is_none():
    return file_selector()
    # if(is_the_most_recently_opened_file_txt_file_empty() == False):
    #     return get_most_recently_opened_file()
    # else:
    #     return file_selector()

def file_selector(): # returns the file_path
        txt_file = ask_for_file_and_save_it()
        return txt_file

def ask_for_file_and_save_it():
        file_path = ask_for_file()
        set_most_recently_opened_file(file_path)
        return file_path


def ask_for_file():
    category = ask_tipe_of_file()
    filename = select_file_path(category)
    if (is_valid(filename)):
        return filename
    else:
        warning_message_popup("Invalid File Format!", "File must be a .csv")
        return None


def ask_tipe_of_file():
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

def is_the_most_recently_opened_file_txt_file_empty():
    txt_file = open("../files/stored_data/most_recently_opened_file_path.txt", "r")
    line = txt_file.readline()
    txt_file.close()
    if(line == ''):
        return True
    else:
        return False

def get_most_recently_opened_file():
    txt_file = open("../files/stored_data/most_recently_opened_file_path.txt", "r")
    line = txt_file.readline()
    txt_file.close()
    return line

def set_most_recently_opened_file(file_path):
    txt_file = open("../files/stored_data/most_recently_opened_file_path.txt", "r+")
    txt_file.truncate(0) # clears the .txt
    txt_file.write(file_path)
    txt_file.close()

def select_file_path(category):
    if(category=="2D"): 
        filename, _trash = QtWidgets.QFileDialog.getOpenFileName()
        return filename    

# TODO: write a better validating function
def is_valid(filename):
    if '.csv' in filename:
        return True
    return False

def warning_message_popup(title, message):
        warning_message = QtWidgets.QMessageBox()
        warning_message.setWindowTitle(title)
        warning_message.setText(message)
        font = QtGui.QFont()
        font.setPointSize(12)
        warning_message.setFont(font)
        warning_message.exec_()

