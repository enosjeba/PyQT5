# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'todo_db.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(469, 436)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.additem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.add_it())
        self.additem_pushButton.setGeometry(QtCore.QRect(10, 50, 101, 31))
        self.additem_pushButton.setObjectName("additem_pushButton")
        self.deleteitem_pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.delete_it())
        self.deleteitem_pushButton_2.setGeometry(QtCore.QRect(130, 50, 101, 31))
        self.deleteitem_pushButton_2.setObjectName("deleteitem_pushButton_2")
        self.clearall_pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clear_it())
        self.clearall_pushButton_3.setGeometry(QtCore.QRect(250, 50, 101, 31))
        self.clearall_pushButton_3.setObjectName("clearall_pushButton_3")
        self.additem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.additem_lineEdit.setGeometry(QtCore.QRect(10, 10, 451, 31))
        self.additem_lineEdit.setObjectName("additem_lineEdit")
        self.mylist_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.mylist_listWidget.setGeometry(QtCore.QRect(10, 90, 451, 291))
        self.mylist_listWidget.setObjectName("mylist_listWidget")
        self.savedb_pushButton = QtWidgets.QPushButton(self.centralwidget,  clicked = lambda: self.save_it())
        self.savedb_pushButton.setGeometry(QtCore.QRect(370, 50, 91, 31))
        self.savedb_pushButton.setObjectName("savedb_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 469, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #all items from database
        self.grab_all()

    
    #add item
    def add_it(self):
        #Grab item from input
        item = self.additem_lineEdit.text()

        #add to list
        self.mylist_listWidget.addItem(item)

        #Clearing Input Field
        self.additem_lineEdit.setText("")

    #delete item
    def delete_it(self):
        #Grab Current Row 
        clicked = self.mylist_listWidget.currentRow()

        #Delete Selected Row
        self.mylist_listWidget.takeItem(clicked)

    #clear all
    def clear_it(self):
        self.mylist_listWidget.clear()

    #save to db
    def save_it(self):
        #connect to a database
        conn = sqlite3.connect('mylist.db')

        #create cursor 
        c = conn.cursor()

        #Delete Everything in database table
        c.execute('DELETE FROM todo_list;', )

        #blank dictonary
        items = []

        #loop through items and pull out each
        for index in range(self.mylist_listWidget.count()):
            items.append(self.mylist_listWidget.item(index))
        
        for item in items:
            # print(item.text())
            #add stuff to table
            c.execute("INSERT INTO todo_list VALUES (:item)",
            {
                'item': item.text(),
            })

        #comit
        conn.commit()

        #close
        conn.close()

    def grab_all():
                
        #Create or connect to a database
        conn = sqlite3.connect('mylist.db')

        #create cursor 
        c = conn.cursor()

        #Create Table
        records = c.execute("SELECT * FROM todo_list")
        records = c.fetchall()

        #comit
        conn.commit()

        #close
        conn.close()

        #find record and add to screen
        for record in records:
            self.mylist_listWidget.additem(str(record[0]))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TODO List"))
        self.additem_pushButton.setText(_translate("MainWindow", "Add Item"))
        self.deleteitem_pushButton_2.setText(_translate("MainWindow", "Delete Item"))
        self.clearall_pushButton_3.setText(_translate("MainWindow", "Clear All"))
        self.savedb_pushButton.setText(_translate("MainWindow", "Save"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
