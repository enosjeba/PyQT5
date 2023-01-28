from PyQt5.QtWidgets import QMainWindow, QApplication, QMdiSubWindow, QTextEdit, QPushButton, QMdiArea
from PyQt5 import uic
import sys

class UI(QMainWindow):
    count = 0
    def __init__(self):
        super(UI, self).__init__()

        #Load UI file
        uic.loadUi("new_win.ui", self)

        #Define Widget Push Button
        self.mdi = self.findChild(QMdiArea, "mdiArea")
        self.button = self.findChild(QPushButton, "pushButton")

        #Click Button
        self.button.clicked.connect(self.add_window)

        #Show App
        self.show()

    def add_window(self):
        UI.count = UI.count + 1

        #Sub window
        sub = QMdiSubWindow()

        #Do Stuff in sub window
        sub.setWidget(QTextEdit())
        sub.setWindowTitle("Subby Window" + str(UI.count))
        self.mdi.addSubWindow(sub)

        #show new subwindow
        sub.show()

        #Tile Windows
        self.mdi.tileSubWindows()

        #Cascade
        self.mdi.cascadeSubWindows()

        # #Close Active Subwindow
        # self.mdi.closeActiveSubWindow()

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_() 