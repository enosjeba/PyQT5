import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__() 
        # Add a Title
        self.setWindowTitle("Folder Bag")

        #set Qform layout
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)

        #Create Label
        my_label = qtw.QLabel("Folder Bag")
        #set font
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)

        #Stuff/Widget
        label_1 = qtw.QLabel("Cool Label Row")
        

        self.show()


app = qtw.QApplication([])
mw = MainWindow()

#Run the app
app.exec_()