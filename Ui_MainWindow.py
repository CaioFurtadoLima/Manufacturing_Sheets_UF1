
from ctypes import sizeof
from winreg import QueryInfoKey
from Libs_APP import *

class Page_main(object):
    def setup_page_1(self, MainWindow):
        
        #Add all your things here
        
        #Creating a menu bar
        menu = self.menuBar()
        file_menu = menu.addMenu("Menu")

        #Creating a toolbar
        self.toolbar = QToolBar("API toolbar")
        self.addToolBar(self.toolbar)
        
        self.toolbar_main_screen = QAction(QIcon(Global_Variables.icon_main_screen),"main screen", self)
        self.toolbar_main_screen.setStatusTip("Return to the main screen")
        self.toolbar.addAction(self.toolbar_main_screen)

        self.toolbar_insert_data_db = QAction(QIcon(Global_Variables.icon_db),"main data", self)
        self.toolbar_insert_data_db.setStatusTip("Insert main data into database")
        self.toolbar.addAction(self.toolbar_insert_data_db)
        
        #Head Title
        self.LB_Title = QLabel("Manufacturing Sheets")
        self.LB_Title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.LB_Title.setStyleSheet("""font: 700 16pt Segoe UI; color: "#818181" """)

        ###################################################
        #                  Main Page                      #
        ###################################################

        #Products Checklist Side
        self.TB_Products_List = QTableWidget()
        # self.TB_Products_List = QTableView()
        # self.TB_Products_List.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection) # Forbid multiselection into QTableview
        # self.TB_Products_List.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows) # When select a single cell, the QtableView will select all row
        # self.TB_Products_List.setSizePolicy(QSizePolicy.Policy.MinimumExpanding,QSizePolicy.Policy.Expanding)

        #self.BTN_validate = QPushButton("Validate")
        #self.BTN_not_validate = QPushButton("Not Validate")
        self.BTN_Edit_Save = QPushButton("Save/Update")
        self.BTN_clear_filter = QPushButton("Clear filter")
        
        self.layout_BTN_validation = QHBoxLayout()
        # self.layout_BTN_validation.addWidget(self.BTN_validate)
        # self.layout_BTN_validation.addWidget(self.BTN_not_validate)
        self.layout_BTN_validation.addWidget(self.BTN_Edit_Save)
        self.layout_BTN_validation.addWidget(self.BTN_clear_filter)

        self.spacer_products = QSpacerItem(20,40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_product_checklist = QVBoxLayout()
        
        self.layout_product_checklist.addWidget(self.TB_Products_List)
        self.layout_product_checklist.addLayout(self.layout_BTN_validation)

        self.layout_product_checklist.addSpacerItem(self.spacer_products)
        

        #Manufacturing Sheets Side
        self.TB_manufacturing_sheets = QTableView()

        self.BTN_Edit_bom = QPushButton("Edit BOM")
        
        self.BTN_Export_PDF = QPushButton("Export to PDF")
        self.BTN_Export_XLXS = QPushButton("Export to XLXS")

        self.layout_BTN_export = QHBoxLayout()
        self.layout_BTN_export.addWidget(self.BTN_Export_PDF)
        self.layout_BTN_export.addWidget(self.BTN_Export_XLXS)
        
        self.layout_manufacturing_sheets = QVBoxLayout()
        self.layout_manufacturing_sheets.addWidget(self.BTN_Edit_bom)
        self.layout_manufacturing_sheets.addWidget(self.TB_manufacturing_sheets)
        self.layout_manufacturing_sheets.addLayout(self.layout_BTN_export)       

        self.layout_prod_manufac = QHBoxLayout()
        self.layout_prod_manufac.addLayout(self.layout_product_checklist)
        self.layout_prod_manufac.addLayout(self.layout_manufacturing_sheets)

        ###################
        #To show up
        
        # adding to layout page_01
        self.layout_main = QVBoxLayout()
        self.layout_main.addWidget(self.LB_Title)
        self.layout_main.addLayout(self.layout_prod_manufac)
        self.main_page = QWidget()
        self.main_page.setLayout(self.layout_main)

        #MainWindow.setCentralWidget(self.main_page)   

class Page_insert_db(object):
    def setup_page_2(self, MainWindow):
        
        #Add all your things here

        ###################################################
        #                  Insert data database Page      #
        ###################################################

        self.label_products = QLabel("Products file") 
        self.lineEdit_product = QLineEdit()
        self.btn_confirm_prod = QPushButton("Confirm")
        self.btn_cancel_prod = QPushButton("Cancel")
        self.btn_tool_prod = QToolButton()
        self.btn_tool_prod.setIcon(QIcon(Global_Variables.icon_folder))
        self.layout_btn_controls_prod_DB = QHBoxLayout()
        self.layout_btn_controls_prod_DB.addWidget(self.btn_confirm_prod)
        self.layout_btn_controls_prod_DB.addWidget(self.btn_cancel_prod)
        self.layout_btn_controls_prod_DB.addSpacerItem(QSpacerItem(20,40,QSizePolicy.Policy.Expanding))       
        self.layout_head_product_DB = QHBoxLayout()
        self.layout_head_product_DB.addWidget(self.label_products)
        self.layout_head_product_DB.addWidget(self.lineEdit_product)
        self.layout_head_product_DB.addWidget(self.btn_tool_prod)
        self.layout_insert_control_prod = QVBoxLayout()
        self.layout_insert_control_prod.addLayout(self.layout_head_product_DB)
        self.layout_insert_control_prod.addLayout(self.layout_btn_controls_prod_DB)
        #self.layout_insert_control_prod.addSpacerItem(QSpacerItem(20,40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.label_acessories = QLabel("Accessories file")
        self.lineEdit_accessories = QLineEdit()
        self.btn_confirm_ace = QPushButton("Confirm")
        self.btn_cancel_ace = QPushButton("Cancel")
        self.btn_tool_ace = QToolButton()
        self.btn_tool_ace.setIcon(QIcon(Global_Variables.icon_folder))
        self.layout_btn_controls_ace_DB = QHBoxLayout()
        self.layout_btn_controls_ace_DB.addWidget(self.btn_confirm_ace)
        self.layout_btn_controls_ace_DB.addWidget(self.btn_cancel_ace)
        self.layout_btn_controls_ace_DB.addSpacerItem(QSpacerItem(20,40,QSizePolicy.Policy.Expanding))       
        self.layout_head_accessories_DB = QHBoxLayout()
        self.layout_head_accessories_DB.addWidget(self.label_acessories)
        self.layout_head_accessories_DB.addWidget(self.lineEdit_accessories)
        self.layout_head_accessories_DB.addWidget(self.btn_tool_ace)
        self.layout_insert_control_ace = QVBoxLayout()
        self.layout_insert_control_ace.addLayout(self.layout_head_accessories_DB)
        self.layout_insert_control_ace.addLayout(self.layout_btn_controls_ace_DB)
        #self.layout_insert_control_ace.addSpacerItem(QSpacerItem(20,40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.label_profiles = QLabel("Profiles file")
        self.lineEdit_profiles = QLineEdit()
        self.btn_confirm_prof = QPushButton("Confirm")
        self.btn_cancel_prof = QPushButton("Cancel")
        self.btn_tool_prof = QToolButton()
        self.btn_tool_prof.setIcon(QIcon(Global_Variables.icon_folder))
        self.layout_btn_controls_prof_DB = QHBoxLayout()
        self.layout_btn_controls_prof_DB.addWidget(self.btn_confirm_prof)
        self.layout_btn_controls_prof_DB.addWidget(self.btn_cancel_prof)
        self.layout_btn_controls_prof_DB.addSpacerItem(QSpacerItem(20,40,QSizePolicy.Policy.Expanding))       
        self.layout_head_profiles_DB = QHBoxLayout()
        self.layout_head_profiles_DB.addWidget(self.label_profiles)
        self.layout_head_profiles_DB.addWidget(self.lineEdit_profiles)
        self.layout_head_profiles_DB.addWidget(self.btn_tool_prof)
        self.layout_insert_control_prof = QVBoxLayout()
        self.layout_insert_control_prof.addLayout(self.layout_head_profiles_DB)
        self.layout_insert_control_prof.addLayout(self.layout_btn_controls_prof_DB)
        #self.layout_insert_control_prof.addSpacerItem(QSpacerItem(20,40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.label_bom =  QLabel("BOM file")
        self.lineEdit_bom = QLineEdit()
        self.btn_confirm_bom = QPushButton("Confirm")
        self.btn_cancel_bom = QPushButton("Cancel")
        self.btn_tool_bom = QToolButton()
        self.btn_tool_bom.setIcon(QIcon(Global_Variables.icon_folder))
        self.layout_btn_controls_bom_DB = QHBoxLayout()
        self.layout_btn_controls_bom_DB.addWidget(self.btn_confirm_bom)
        self.layout_btn_controls_bom_DB.addWidget(self.btn_cancel_bom)
        self.layout_btn_controls_bom_DB.addSpacerItem(QSpacerItem(20,40,QSizePolicy.Policy.Expanding))       
        self.layout_head_bom_DB = QHBoxLayout()
        self.layout_head_bom_DB.addWidget(self.label_bom)
        self.layout_head_bom_DB.addWidget(self.lineEdit_bom)
        self.layout_head_bom_DB.addWidget(self.btn_tool_bom)
        self.layout_insert_control_bom = QVBoxLayout()
        self.layout_insert_control_bom.addLayout(self.layout_head_bom_DB)
        self.layout_insert_control_bom.addLayout(self.layout_btn_controls_bom_DB)
        #self.layout_insert_control_bom.addSpacerItem(QSpacerItem(20,40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        ###################
        #To show up
        
        # adding to layout page_02
        self.layout_db_insert = QVBoxLayout()
        self.layout_db_insert.addLayout(self.layout_insert_control_ace)
        self.layout_db_insert.addLayout(self.layout_insert_control_prof)
        self.layout_db_insert.addLayout(self.layout_insert_control_prod)
        self.layout_db_insert.addLayout(self.layout_insert_control_bom)
        self.layout_db_insert.addSpacerItem(QSpacerItem(20,40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        
        self.insert_db_page = QWidget()
        self.insert_db_page.setLayout(self.layout_db_insert)

class edition_bom_window(object):
    def setup_page_3(self, MainWindow):

        #Information about select SKU

        self.label_title_sku_name = QLabel("SKU |")
        self.label_title_sku_name.setStyleSheet("font-weight: bold")
        self.label_answer_sku_name = QLabel("None")
        self.layout_name = QHBoxLayout()
        self.layout_name.addWidget(self.label_title_sku_name)
        self.layout_name.addWidget(self.label_answer_sku_name)
        self.layout_name.addSpacerItem(QSpacerItem(20,5, QSizePolicy.Policy.Expanding))

        self.label_title_sku_description = QLabel("Description |")
        self.label_title_sku_description.setStyleSheet("font-weight: bold")
        self.label_answer_sku_description = QLabel("None")
        self.layout_description = QHBoxLayout()
        self.layout_description.addWidget(self.label_title_sku_description)
        self.layout_description.addWidget(self.label_answer_sku_description)
        self.layout_description.addSpacerItem(QSpacerItem(20,5, QSizePolicy.Policy.Expanding))

        self.label_title_sku_color = QLabel("Color |")
        self.label_title_sku_color.setStyleSheet("font-weight: bold")
        self.label_answer_sku_color = QLabel("None")
        self.layout_color = QHBoxLayout()
        self.layout_color.addWidget(self.label_title_sku_color)
        self.layout_color.addWidget(self.label_answer_sku_color)
        self.layout_color.addSpacerItem(QSpacerItem(20,5, QSizePolicy.Policy.Expanding))

        self.label_title_sku_observations = QLabel("Observations |")
        self.label_title_sku_observations.setStyleSheet("font-weight: bold")
        self.label_answer_sku_observations = QLabel("None")
        self.layout_observations = QHBoxLayout()
        self.layout_observations.addWidget(self.label_title_sku_observations)
        self.layout_observations.addWidget(self.label_answer_sku_observations)
        self.layout_observations.addSpacerItem(QSpacerItem(20,5, QSizePolicy.Policy.Expanding))

        self.layout_info_sku_edition = QVBoxLayout()
        self.layout_info_sku_edition.addLayout(self.layout_name)
        self.layout_info_sku_edition.addLayout(self.layout_description)
        self.layout_info_sku_edition.addLayout(self.layout_color)
        self.layout_info_sku_edition.addLayout(self.layout_observations)

        #Information about a new component to insert
        self.checkbox_filter_ace = QCheckBox('Accessory')
        self.checkbox_filter_profile = QCheckBox('Profile')
        self.layout_filter_controls = QHBoxLayout()
        self.layout_filter_controls.addWidget(self.checkbox_filter_ace)
        self.layout_filter_controls.addWidget(self.checkbox_filter_profile)
        self.layout_filter_controls.addSpacerItem(QSpacerItem(20,5, QSizePolicy.Policy.Expanding))

        self.combobox_insert_components = QComboBox()
        self.combobox_insert_components.setMinimumSize(100,10)
        self.label_insert_description = QLabel("Component descripition")
        self.layout_insert_new_sku = QHBoxLayout()
        self.layout_insert_new_sku.addWidget(self.combobox_insert_components)
        self.layout_insert_new_sku.addWidget(self.label_insert_description)

        self.layout_insert_new_sku_2 = QVBoxLayout()
        self.layout_insert_new_sku_2.addLayout(self.layout_filter_controls)
        self.layout_insert_new_sku_2.addLayout(self.layout_insert_new_sku)
        
        self.spinbox_insert_quantity = QDoubleSpinBox()
        self.label_insert_quantity = QLabel("Quantity")
        self.layout_insert_quantity = QVBoxLayout()
        self.layout_insert_quantity.addWidget(self.label_insert_quantity)
        self.layout_insert_quantity.addWidget(self.spinbox_insert_quantity)

        self.spinbox_insert_level = QSpinBox() 
        self.label_insert_level = QLabel("Level")
        self.layout_insert_level = QVBoxLayout()
        self.layout_insert_level.addWidget(self.label_insert_level)
        self.layout_insert_level.addWidget(self.spinbox_insert_level)

        self.layout_insert_level_quantity = QHBoxLayout()
        self.layout_insert_level_quantity.addLayout(self.layout_insert_quantity)
        self.layout_insert_level_quantity.addLayout(self.layout_insert_level) 
        
        self.layout_insert_controls = QVBoxLayout()
        #self.layout_insert_controls.addLayout(self.layout_insert_new_sku)
        self.layout_insert_controls.addLayout(self.layout_insert_new_sku_2)
        self.layout_insert_controls.addLayout(self.layout_insert_level_quantity)
        self.btn_confirm_add_row = QPushButton("Add component")
        self.layout_insert_controls.addWidget(self.btn_confirm_add_row)

        self.layout_insert_top_board = QHBoxLayout()
        self.layout_insert_top_board.addLayout(self.layout_info_sku_edition)
        self.layout_insert_top_board.addLayout(self.layout_insert_controls)
        self.layout_insert_top_board.addSpacerItem(QSpacerItem(20,5, QSizePolicy.Policy.Expanding))

        #Information about buttons (delete, confirm, cancel)
        self.btn_delete_row = QPushButton("Delete row")
        self.btn_confirm_edit = QPushButton("Confirm")
        
        self.btn_cancel_edit = QPushButton("Cancel")
        self.layout_btn_controls_edition = QHBoxLayout()
        self.layout_btn_controls_edition.addWidget(self.btn_delete_row)
        self.layout_btn_controls_edition.addWidget(self.btn_confirm_edit)
        self.layout_btn_controls_edition.addWidget(self.btn_cancel_edit)
        self.layout_btn_controls_edition.addSpacerItem(QSpacerItem(20,5, QSizePolicy.Policy.Expanding))

        #Information about Qtable
        self.TB_MBOM_Editon = QTableWidget()   
        #self.TB_MBOM_Editon = QTableView()     

        #Structuring  the page
        self.layout_main_edition_bom = QVBoxLayout()
        
        #self.layout_main_edition_bom.addLayout(self.layout_info_sku_edition)
        self.layout_main_edition_bom.addLayout(self.layout_insert_top_board)
        
        self.layout_main_edition_bom.addLayout(self.layout_btn_controls_edition)
        self.layout_main_edition_bom.addWidget(self.TB_MBOM_Editon)
        
        self.MBOM_edition_page = QWidget()
        self.MBOM_edition_page.setLayout(self.layout_main_edition_bom)


        

