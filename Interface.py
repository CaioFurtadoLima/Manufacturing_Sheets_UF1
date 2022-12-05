

from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QListView
from PyQt6 import QtCore, QtGui, QtWidgets

class Interface(object):
    def setupUi(self, MainWindow):
        
        #Add all your things here


        #self.setWindowTitle("My todo list App")
        self.table_view = QListView()
        
        self.btn_delete = QPushButton("Delete")
        self.btn_complete = QPushButton("Complete")
        self.layout_Del_Comp = QHBoxLayout()
        self.layout_Del_Comp.addWidget(self.btn_delete)
        self.layout_Del_Comp.addWidget(self.btn_complete)

        self.btn_add = QPushButton("Add Todo")
        self.line_txt = QLineEdit()
        self.layout_btnAdd_linetxt = QVBoxLayout()
        self.layout_btnAdd_linetxt.addWidget(self.table_view)
        self.layout_btnAdd_linetxt.addWidget(self.line_txt)
        self.layout_btnAdd_linetxt.addWidget(self.btn_add)
        self.layout_btnAdd_linetxt.addLayout(self.layout_Del_Comp)
        
        self.layout_main = QVBoxLayout()

        self.layout_main.addLayout(self.layout_Del_Comp)
        self.layout_main.addLayout(self.layout_btnAdd_linetxt)
        

        self.widget = QWidget()
        self.widget.setLayout(self.layout_main)

    	#To show up
        MainWindow.setCentralWidget(self.widget)



         

