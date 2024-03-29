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

        #Create a Text Box
        my_text = qtw.QTextEdit(self,

        plainText = "Real Text",
        acceptRichText = True, 
        lineWrapMode = qtw.QTextEdit.FixedColumnWidth,
        lineWrapColumnOrWidth = 50,
        placeholderText = "Type Here",
        readOnly = False,

        )

        #Change Font Size of Spin Box
        #my_spin.setFont(qtg.QFont('Helvetica',14))

        #Put Combo Box on Screen
        self.layout().addWidget(my_text)
    
        #Create a Button
        my_button = qtw.QPushButton("Create Project", 
        clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        def press_it():
            my_label.setText(f'{my_text.toPlainText()} typed')
            my_text.setPlainText("You Pressed the Button!")
            #clear entry box
            my_entry.setText("")

        self.show()


app = qtw.QApplication([])
mw = MainWindow()

#Run the app
app.exec_()