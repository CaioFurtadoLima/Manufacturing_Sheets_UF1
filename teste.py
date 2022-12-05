import importlib
from PyQt6 import QtGui, QtCore, QtWidgets


class MyDelegate(QtWidgets.QItemDelegate):
    def __init__(self, parent=None):
        QtWidgets.QItemDelegate.__init__(self, parent)


class Model(QtCore.QAbstractTableModel):
    def __init__(self):
        QtCore.QAbstractTableModel.__init__(self)
        self.tableList = ["Item %02d" % (i+1) for i in range(5)]

    def rowCount(self, parent):
        return len(self.tableList)

    def columnCount(self, parent):
        return 1

    def data(self, index, role):
        if (role == QtCore.Qt.DisplayRole):
            return self.tableList[index.row()]

        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignVCenter

        if role == QtCore.Qt.TextColorRole:
            return QtGui.QColor(255, 255, 255)

        if role == QtCore.Qt.BackgroundRole:
            return QtGui.QColor(255, 25+30*index.row(), 75)


class TableView(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        tableModel = Model()
        tableView = QtWidgets.QTableView()
        tableView.setModel(tableModel)
        mydelegate = MyDelegate(self)
        tableView.setItemDelegate(mydelegate)

        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(tableView)
        self.setLayout(hbox)

        try:
            import hou
            self.setParent(hou.ui.mainQtWindow(), QtCore.Qt.Window)
        except:
            pass


dialog = TableView()
dialog.show()
