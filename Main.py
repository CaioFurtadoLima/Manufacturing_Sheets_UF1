from re import I
from Libs_APP import *
from Ui_MainWindow import Page_main, Page_insert_db , edition_bom_window
from Models import TB_Model_Manufacturing_sheets, TB_Model_Products_List, PandasModel
from Models import ReadOnlyDelegate as delegate
from Querys import Functions_data_set, Functions_SQL, Functions_Message, Function_APP

#TESTEHOJE

class MainWindow(QMainWindow, Page_main, Page_insert_db, edition_bom_window):
    def __init__(self):
        super().__init__()

        self.setup_page_1(self)
        self.setup_page_2(self)
        self.setup_page_3(self)

        self.setWindowTitle("Manufacturing BOM checklist")
        self.setMinimumSize(500,600)

        #################################

        self.stacked_pages_layout = QStackedLayout()
        self.main_widget_app = QWidget()
        self.main_widget_app.setLayout(self.stacked_pages_layout)
        self.setCentralWidget(self.main_widget_app)
        
        self.stacked_pages_layout.addWidget(self.main_page)
        self.stacked_pages_layout.addWidget(self.insert_db_page)
        self.stacked_pages_layout.addWidget(self.MBOM_edition_page)
        
        #################################
        #Switching pages app
        self.toolbar_main_screen.triggered.connect(lambda: Function_APP.go_to_page(self,'main_screen'))
        self.toolbar_insert_data_db.triggered.connect(lambda: Function_APP.go_to_page(self,'insert_db_data'))   
        
        ######################################################
        #Main Window Properties
        ######################################################
        
        #################################
        #Main Window inserting data

        self.data_MBOM = Functions_data_set.tb_bom_all(self)
        self.TB_manufacturing_model = TB_Model_Manufacturing_sheets(self.data_MBOM)
        self.TB_manufacturing_sheets.setModel(self.TB_manufacturing_model)
        self.TB_manufacturing_sheets.resizeColumnsToContents()  

        Function_APP.Create_Product_List(self)

        self.TB_Products_List.clicked.connect(lambda: Function_APP.filter_MBOM(self,'Yes'))
        self.TB_Products_List.cellChanged.connect(lambda: Function_APP.change_color_unsaved(self))
        self.BTN_Edit_Save.clicked.connect(lambda: Function_APP.validation_save(self))
        self.BTN_clear_filter.clicked.connect(lambda:Function_APP.filter_MBOM(self, 'No'))

        self.BTN_Edit_bom.clicked.connect(lambda: Function_APP.edit_bom(self))
        self.BTN_Export_PDF.clicked.connect(lambda: Function_APP.retieve_data(self,'PDF')) 
        self.BTN_Export_XLXS.clicked.connect(lambda: Function_APP.retieve_data(self,'XLXS')) 

        ######################################################
        #Insert data database Window Properties
        ######################################################

        self.btn_confirm_ace.clicked.connect(lambda: Function_APP.confirm_insert_db(self, 'ace'))
        self.btn_cancel_ace.clicked.connect(lambda: Function_APP.clean_insert_db(self,'ace'))
        self.btn_tool_ace.clicked.connect(lambda: Function_APP.get_file_name(self,'ace'))

        self.btn_confirm_prof.clicked.connect(lambda: Function_APP.confirm_insert_db(self, 'prof'))
        self.btn_cancel_prof.clicked.connect(lambda: Function_APP.clean_insert_db(self,'prof'))
        self.btn_tool_prof.clicked.connect(lambda: Function_APP.get_file_name(self,'prof'))

        self.btn_confirm_prod.clicked.connect(lambda: Function_APP.confirm_insert_db(self, 'prod'))
        self.btn_cancel_prod.clicked.connect(lambda: Function_APP.clean_insert_db(self,'prod'))
        self.btn_tool_prod.clicked.connect(lambda: Function_APP.get_file_name(self,'prod'))

        self.btn_confirm_bom.clicked.connect(lambda: Function_APP.confirm_insert_db(self, 'bom'))
        self.btn_cancel_bom.clicked.connect(lambda: Function_APP.clean_insert_db(self,'bom'))
        self.btn_tool_bom.clicked.connect(lambda: Function_APP.get_file_name(self,'bom'))

        ######################################################
        #Editon MBOM Window Properties
        ######################################################
        self.spinbox_insert_quantity.setRange(0,100)
        self.spinbox_insert_level.setRange(0,3)

        self.TB_components = Function_APP.add_items_components(self)

        self.btn_confirm_edit.clicked.connect(lambda: Function_APP.insertion_confirm(self))
        self.btn_cancel_edit.clicked.connect(lambda: Function_APP.cancel_edition(self))
        self.btn_delete_row.clicked.connect(lambda: Function_APP.Edition_delete_row(self))

        self.checkbox_filter_ace.stateChanged.connect(lambda:Function_APP.items_components_filter(self))
        self.checkbox_filter_profile.stateChanged.connect(lambda: Function_APP.items_components_filter(self))
        self.combobox_insert_components.currentTextChanged.connect(lambda: Function_APP.reset_quantity_level(self))

        self.combobox_insert_components.currentTextChanged.connect(lambda:Function_APP.insert_component_description(self))
        self.btn_confirm_add_row.clicked.connect(lambda: Function_APP.Edition_add_row(self))

        self.TB_MBOM_Editon.cellChanged.connect(lambda: Function_APP.edit_existing_components(self))
        
    #################################
    #Functions Mainwindow

    #################################
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    app.exec()


        