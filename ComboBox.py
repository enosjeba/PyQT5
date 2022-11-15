import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__() 
        # Add a Title
        self.setWindowTitle("Folder Bag")

        #set Vertical layout
        self.setLayout(qtw.QVBoxLayout())

        #Create Label
        my_label = qtw.QLabel("Folder Bag")
        #set font
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)

        #Create A Entry Box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("Enter Project Name")
        self.layout().addWidget(my_entry)

        #Create a Combo Box
        my_combo = qtw.QComboBox(self)
        #Add Items to Combo Box
        my_combo.addItem("Premiere Pro", "Something")
        my_combo.addItem("Photoshop", 2)
        my_combo.addItem("After Effects", qtw.QWidget)
        my_combo.addItem("Premiere2")
        my_combo.addItem("Audition")
        #Put Combo Box on Screen
        self.layout().addWidget(my_combo)
    
        #Create a Button
        my_button = qtw.QPushButton("Create Project", 
        clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        def press_it():
            my_label.setText(f'{my_combo.currentText()} Project Created')
            #clear entry box
            my_entry.setText("")

        self.show()


app = qtw.QApplication([])
mw = MainWindow()

#Run the app
app.exec_()