import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QListWidget, QLabel, QMenuBar, QAction
from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # window config
        title = "Log type selector"
        left = 500
        top = 200
        width = 300
        height = 250
        icon_name  = "files/robocin-03-small.png"
        message_text = "Selecione o tipo de log a ser analisado"


        # window inicialization
        self.setWindowTitle(title)
        self.setGeometry(left, top, width, height) 
        self.setWindowIcon(QtGui.QIcon(icon_name))
        self.main_vbox = QVBoxLayout()
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_vbox)
        self.setCentralWidget(self.main_widget)
        self.message = QLabel(message_text)
        self.message.setFont(QtGui.QFont("Sanserif ", 20))
        self.message.setAlignment(Qt.AlignCenter)

        self.UiComponents()
        self.main_vbox.addWidget(self.message)
        self.main_vbox.addWidget(self.button1)
        self.main_vbox.addWidget(self.button2)
        self.main_vbox.addWidget(self.button3)

        #turns main window visible
        self.show()

    def UiComponents(self):
        self.button1 = QPushButton("2D", self)
        self.button2 = QPushButton("VSS", self)
        self.button3 = QPushButton("SSL", self)
        self.button1.clicked.connect(self.clicked1)

    def clicked1(self):
        self.button1.setText("açsldfjasçl")
         




if __name__ == "__main__":
    Application = QApplication(sys.argv)
    Main = MainWindow()
    sys.exit(Application.exec())
