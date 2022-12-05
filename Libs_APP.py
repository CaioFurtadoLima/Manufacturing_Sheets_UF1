import sys, os

class Global_Variables:
    Desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']),'Desktop')

    # param_DB = {
    #     "user" : "postgres", 
    #     "password" : "123456ASD", 
    #     "host" : "localhost",
    #     "port" : "5432" ,
    #     "database" : "MRP_UF1"
    #     }
    
    param_DB_API = {
        "user" : "postgres", 
        "password" : "123456ASD", 
        "host" : "localhost",
        "port" : "5432" ,
        "database" : "API_fichas_fabrico"
        }
    
    icon_db = "C:/Users/Caio Lima/Desktop/PyQT Class/APPs/Manufacturing_Files_UF1/images/database_arrow.png"
    icon_folder = "C:/Users/Caio Lima/Desktop/PyQT Class/APPs/Manufacturing_Files_UF1/images/folder.png"
    icon_main_screen = "C:/Users/Caio Lima/Desktop/PyQT Class/APPs/Manufacturing_Files_UF1/images/main_screen.png"

import pandas as pd
import numpy as np
import psycopg2, xlsxwriter

from matplotlib import colors

from PyQt6.QtGui import QFont, QColor, QAction, QIcon

from PyQt6.QtCore import (
                            QAbstractTableModel, 
                            Qt, 
                            QSize, 
                            QSortFilterProxyModel,
                            QModelIndex,
                            )

from PyQt6.QtWidgets import (
                            QApplication,
                            QMainWindow,
                            QWidget, 
                            QVBoxLayout,
                            QHBoxLayout,
                            QGridLayout,
                            QTableView, 
                            QLabel, 
                            QPushButton,
                            QToolButton,
                            QSizePolicy, 
                            QSpacerItem,
                            QComboBox,
                            QLineEdit,
                            QAbstractItemView, 
                            QMessageBox,
                            QTableWidget,
                            QTableWidgetItem,
                            QHeaderView,
                            QStyledItemDelegate,
                            QComboBox,
                            QToolBar, 
                            QFileDialog, 
                            QDoubleSpinBox, 
                            QSpinBox,
                            QCheckBox,

                            QStackedLayout
                            )

#NOTES
# 01 - Color - White  - "#000000"
# 02 - Color - Green  - "#e7fff3"
# 03 - Color - Red    - "#ffc0c1"
# 04 - Color - Yellow - "#ffffda"

