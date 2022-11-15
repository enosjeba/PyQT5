import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        #Add Title
        self.setWindowTitle("Hello World")

        #Set Layout - Vertical
        self.setLayout(qtw.QVBoxLayout())

        #Label
        my_label = qtw.QLabel("Pick Something")
        #Label Font Size
        my_label.setFont(qtg.QFont('Helvetica', 24))
        self.layout().addWidget(my_label)

        #Combo Box
        my_combo = qtw.QComboBox(self,
        editable = True,
        insertPolicy = qtw.QComboBox.InsertAtBottom)

        #Items to ComboBox
        my_combo.addItem("Item1", "Something1")
        my_combo.addItem("Item2", "Something2")
        my_combo.addItem("Item3", "Something3")

        #Add it to screen
        self.layout().addWidget(my_combo)

        #Button
        my_button = qtw.QPushButton("Press Me!",
        clicked = lambda: press_it())
        self.layout().addWidget(my_button)
