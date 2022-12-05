from Libs_APP import *
from Models import *

class Functions_Message(object):
    
    def standard_notification(self, window_title, message, icon_type):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(str(window_title))
        msg_box.setText(str(message))
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)

        if icon_type == 'No_icon':
            icon_type = QMessageBox.Icon.NoIcon
        elif icon_type == 'Warning':
            icon_type = QMessageBox.Icon.Warning 
        elif icon_type == 'Critical':
            icon_type = QMessageBox.Icon.Critical
        elif icon_type == 'Question':
            icon_type = QMessageBox.Icon.Question
        elif icon_type == 'Information':
            icon_type = QMessageBox.Icon.Information

        msg_box.setIcon(icon_type)
        msg_box.exec()

        # button = msg_box.exec()
        # if button == QMessageBox.StandardButton.Ok:
        #     print("OK!")

class Function_APP(object):

    def reset_quantity_level(self):
        self.spinbox_insert_quantity.setValue(0.00)
        self.spinbox_insert_level.setValue(0)


    def clean_insert_db(self, line_type):
        if line_type == 'ace':
            self.lineEdit_accessories.clear()
        elif line_type == 'prof':
            self.lineEdit_profiles.clear()
        elif line_type == 'prod':
            self.lineEdit_product.clear()
        elif line_type == 'bom':
            self.lineEdit_bom.clear()
    
    def get_file_name(self, line_type):
        file_name  = Functions_data_set.window_get_file_name()
        
        if line_type == 'ace':
            self.lineEdit_accessories.setText(file_name[0])
        elif line_type == 'prof':
            self.lineEdit_profiles.setText(file_name[0])
        elif line_type == 'prod':
            self.lineEdit_product.setText(file_name[0])
        elif line_type == 'bom':
            self.lineEdit_bom.setText(file_name[0])
    
    def go_to_page(self, page_selected):
        
        if page_selected == 'main_screen':
            self.stacked_pages_layout.setCurrentIndex(0)
        elif page_selected == 'insert_db_data':
            self.stacked_pages_layout.setCurrentIndex(1)
        elif page_selected == 'MBOM_edition':
            self.stacked_pages_layout.setCurrentIndex(2)
    
    def retieve_data(self, format):
        try:
            rows = self.proxy_model.rowCount()
            columns = self.proxy_model.columnCount()

            sku_info = []
            for column in range(2,self.TB_Products_List.columnCount()):
                item = self.TB_Products_List.item(self.TB_Products_List.currentRow(), column).text()
                sku_info.append(item)

        except:
            self.data_MBOM = Functions_data_set.tb_bom_all(self)
            self.Model_MBOM = PandasModel(self.data_MBOM)
            self.proxy_model = QSortFilterProxyModel()
            self.proxy_model.setSourceModel(self.Model_MBOM)
            rows = self.proxy_model.rowCount()
            columns = self.proxy_model.columnCount()

            sku_info = ['All_products', 'All accessories and profiles registration', 'all', '-']

        finally:  
            data_filtered_MBOM = pd.DataFrame()
            for column in range(columns):
                row_list = []
                for row in range(rows):
                    data_set = self.proxy_model.data(self.proxy_model.index(row,column))
                    row_list.append(data_set)

                data_filtered_MBOM[column]  = row_list 

            data_filtered_MBOM.rename(columns={0:'SKU_Product', 1:'SKU_Component', 2:'Type' , 3:'Quantity',4: 'Level', 5:'Component_Description'}, inplace=True)
            
            if format == 'XLXS':
                Functions_data_set.create_MBOM_file(self, sku_info, data_filtered_MBOM)
                format = 'Excel' 
            elif format == 'PDF':
                print('PDF')
                format = 'PDF'
            
            Functions_Message.standard_notification(
                            self,
                            'File export completed', 
                            ("A new {} file was created for your desktop area").format(format),
                            'Information' 
                            )
    def change_color_unsaved(self):   
        col_validation = self.TB_Products_List.item(self.TB_Products_List.currentRow(),1).text()
        combobox = self.TB_Products_List.item(self.TB_Products_List.currentRow(),0).text()
        if combobox != col_validation:
            row = self.TB_Products_List.currentRow()
            for column in range(self.TB_Products_List.columnCount()):
                self.TB_Products_List.item(row, column).setBackground(QColor('#ffffda'))

    # def change_color_unsaved_edition(self):   
    #     col_validation = self.TB_MBOM_Editon.item(self.TB_MBOM_Editon.currentRow(),1).text()
    #     combobox = self.TB_MBOM_Editon.item(self.TB_MBOM_Editon.currentRow(),0).text()
    #     if combobox != col_validation:
    #         row = self.TB_MBOM_Editon.currentRow()
    #         for column in range(self.TB_MBOM_Editon.columnCount()):
    #             self.TB_MBOM_Editon.item(row, column).setBackground(QColor('#ffffda'))
    
    def filter_MBOM(self, answer): 
        self.Model_MBOM = PandasModel(self.data_MBOM)
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.Model_MBOM)
        self.proxy_model.setFilterKeyColumn(0)
        if answer == 'Yes':
            SKU_filter = self.TB_Products_List.item(self.TB_Products_List.currentRow(),2).text()
            self.proxy_model.setFilterFixedString(SKU_filter)
        # elif answer == 'No':
        #     self.proxy_model.setFilterFixedString(None)

        self.TB_manufacturing_sheets.setModel(self.proxy_model)

        return self.proxy_model
    
    def confirm_insert_db(self, line_type):
        if line_type == 'ace':
            Functions_SQL.bulk_insert_db(self, self.lineEdit_accessories.text())
            
        elif line_type == 'prof':
            self.lineEdit_profiles.clear()
        elif line_type == 'prod':
            self.lineEdit_product.clear()
        elif line_type == 'bom':
            self.lineEdit_bom.clear()   
    
    def edit_bom(self):    
        try:
            proxy_model = Function_APP.filter_MBOM(self, 'Yes')
            rows = proxy_model.rowCount()
            columns = proxy_model.columnCount()

            sku_info = []
            for column in range(2,self.TB_Products_List.columnCount()):
                item = self.TB_Products_List.item(self.TB_Products_List.currentRow(), column).text()
                sku_info.append(item)
            
            data_filtered_MBOM = pd.DataFrame()
            for column in range(columns):
                row_list = []
                for row in range(rows):
                    data_set = proxy_model.data(proxy_model.index(row,column))
                    row_list.append(data_set)

                data_filtered_MBOM[column]  = row_list 

            data_filtered_MBOM.rename(columns={0:'SKU_Product', 1:'SKU_Component', 2:'Type' , 3:'Quantity',4: 'Level', 5:'Component_Description'}, inplace=True)
            
            self.label_answer_sku_name.setText(sku_info[0])
            self.label_answer_sku_description.setText(sku_info[1])
            self.label_answer_sku_color.setText(sku_info[2])
            self.label_answer_sku_observations.setText(sku_info[3])
            
            #print(data_filtered_MBOM)
            Function_APP.Create_MBOM_edition(self,data_filtered_MBOM)
            Function_APP.go_to_page(self,'MBOM_edition')
        except:
            Functions_Message.standard_notification(
                            self,
                            'BOM edition', 
                            "You didn't select a BOM",
                            'Warning' 
                            )
    
    def Create_MBOM_edition(self, data_frame):

        self.TB_MBOM_Editon.setRowCount(data_frame.shape[0])
        self.TB_MBOM_Editon.setColumnCount(data_frame.shape[1])
        self.TB_MBOM_Editon.horizontalHeader().setStretchLastSection(True)
        self.TB_MBOM_Editon.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        count = 0
        for column in data_frame.columns:
            self.TB_MBOM_Editon.setHorizontalHeaderItem(count, QTableWidgetItem(column))
            if count != 3 and count != 4: 
                self.TB_MBOM_Editon.setItemDelegateForColumn(count, ReadOnlyDelegate(self))
            count += 1

        for row in  range(data_frame.shape[0]):
            for column in range(data_frame.shape[1]):
                item  = QTableWidgetItem(data_frame.iloc[row, column])
                self.TB_MBOM_Editon.setItem(row, column, item)
                
                # if data_frame.iloc[row, 0] == 'Yes':
                #     item.setBackground(QColor('#e7fff3'))

    def Create_Product_List(self):

        data_SKU = Functions_data_set.tb_products_sku_all(self)

        self.TB_Products_List.setRowCount(data_SKU.shape[0])
        self.TB_Products_List.setColumnCount(data_SKU.shape[1])
        self.TB_Products_List.horizontalHeader().setStretchLastSection(True)
        self.TB_Products_List.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        count = 0
        for column in data_SKU.columns:
            self.TB_Products_List.setHorizontalHeaderItem(count, QTableWidgetItem(column))
            if count != 0 and count != 5: 
                self.TB_Products_List.setItemDelegateForColumn(count, ReadOnlyDelegate(self))
            count += 1

        for row in  range(data_SKU.shape[0]):
            for column in range(data_SKU.shape[1]):
                item  = QTableWidgetItem(data_SKU.iloc[row, column])
                if data_SKU.iloc[row, 0] == 'Yes':
                    item.setBackground(QColor('#e7fff3'))
                else:
                    item.setBackground(QColor('#ffc0c1'))
                self.TB_Products_List.setItem(row, column, item)
    
    def validation_save(self):
        data_SKU_change = pd.DataFrame()
        for column in range(self.TB_Products_List.columnCount()):
            row_list = []
            for row in range(self.TB_Products_List.rowCount()):
                new_status = self.TB_Products_List.item(row, 0).text()
                old_status = self.TB_Products_List.item(row, 1).text()
                if new_status != old_status:
                    data_set = self.TB_Products_List.item(row, column).text()
                    row_list.append(data_set)      
            data_SKU_change[self.TB_Products_List.horizontalHeaderItem(column).text()] = row_list

        if data_SKU_change.empty:
            Functions_Message.standard_notification(
                        self,
                        'Validation SKU product change', 
                        "You didn't do it any change",
                        'Warning' 
                        )
        else:
            Functions_SQL.func_update_SKU_Validation_df(self,data_SKU_change)
            Functions_Message.standard_notification(
                        self,
                        'Validation SKU product change', 
                        "The changes to Product SKU checklists have been saved",
                        'Information' 
                        )

        Function_APP.Create_Product_List(self)
    
    def cancel_edition(self):
        Function_APP.go_to_page(self,'main_screen')
        Function_APP.filter_MBOM(self,'No')

    def add_items_components(self):
        
        query_profile = """SELECT PERFIL_SKU, PERFIL_DESCRICAO_DEP FROM TB_PROFILES"""
        tb_data_set_profiles = pd.DataFrame(Functions_SQL.func_select(self,query_profile))
        tb_data_set_profiles['Type'] = 'Profile'
        query_ace = """SELECT ACE_ACESSORIO_SKU, ACE_DESCRICAO FROM TB_ACESSORIOS"""
        tb_data_set_ace = pd.DataFrame(Functions_SQL.func_select(self,query_ace))
        tb_data_set_ace['Type'] = 'Accessory'

        frames = [tb_data_set_ace, tb_data_set_profiles]
        TB_components = pd.concat(frames)
        TB_components.rename(columns={0:'SKU_Component', 1:'Description', 2:'Type'}, inplace=True)
        
        combobox_TB_components = TB_components['SKU_Component'].values.tolist()

        self.combobox_insert_components.addItem('None')
        self.combobox_insert_components.addItems(combobox_TB_components)
        
        return TB_components

    def items_components_filter(self):
        
        Status_filter = [self.checkbox_filter_ace.checkState(), self.checkbox_filter_profile.checkState()]
                
        #01 Statment - No filter
        if Status_filter == [Qt.CheckState.Checked, Qt.CheckState.Checked] or  Status_filter == [Qt.CheckState.Unchecked, Qt.CheckState.Unchecked]:
            query_df = ('Type == "Accessory" or Type == "Profile"')
        #02 Statment - Just accessory
        elif Status_filter == [Qt.CheckState.Checked, Qt.CheckState.Unchecked]:
            query_df = ('Type == "Accessory"')
        #02 Statment - Just profile
        elif Status_filter == [Qt.CheckState.Unchecked, Qt.CheckState.Checked]:
            query_df = ('Type == "Profile"')

        Filtered_list = self.TB_components.query(query_df)
        Filtered_list = Filtered_list['SKU_Component'].values.tolist()

        self.combobox_insert_components.clear()
        self.combobox_insert_components.addItem('None')
        self.combobox_insert_components.addItems(Filtered_list)
    
    def insert_component_description(self):
        Current_sku = self.combobox_insert_components.currentText()
        if Current_sku == 'None' or bool(Current_sku) == False :
            self.label_insert_description.setText("Component descripition")
        else:
            query_df = ('SKU_Component == "{}"').format(Current_sku)
            result = self.TB_components.query(query_df) 
            result = result.iloc[0,1]

            self.label_insert_description.setText(result)

    def Edition_delete_row(self):
        row = self.TB_MBOM_Editon.currentRow()
        columns = self.TB_MBOM_Editon.columnCount()
        for column in range(columns):
            self.TB_MBOM_Editon.item(row, column).setBackground(QColor('#ffc0c1'))     

    def Edition_add_row(self):
        SKU_name = self.combobox_insert_components.currentText()
        SKU_quantity = self.spinbox_insert_quantity.value()
        SKU_level = self.spinbox_insert_level.value()

        if SKU_name != 'None' or bool(SKU_name) == True:
            if SKU_quantity <= 0 or SKU_level <= 0:
                Functions_Message.standard_notification(self,
                    'Edition MBOM', 
                    "You didn't insert a correct amount or level", 
                    "Warning")
            else:
                query_df = ('SKU_Component == "{}"').format(SKU_name)
                result = self.TB_components.query(query_df) 

                Last_row = self.TB_MBOM_Editon.rowCount()
            
                self.TB_MBOM_Editon.insertRow(Last_row)
                self.TB_MBOM_Editon.setRowCount(Last_row+1)

                row_list = [self.label_answer_sku_name.text(), 
                            result.iloc[0,0], 
                            result.iloc[0,2], 
                            str(SKU_quantity), 
                            str(SKU_level), 
                            result.iloc[0,1]
                            ]

                for column in range(len(row_list)):
                    item = QTableWidgetItem(row_list[column])
                    item.setBackground(QColor('#e7fff3'))
                    self.TB_MBOM_Editon.setItem(Last_row, column, item)

        Function_APP.reset_quantity_level(self) 
    
    def edit_existing_components(self):
        row = self.TB_MBOM_Editon.currentRow()
        column  = self.TB_MBOM_Editon.currentColumn()
        item  = self.TB_MBOM_Editon.item(row, column)
        if item:
            color = colors.to_hex(item.background().color().getRgbF())
            if color != "#e7fff3" and  color != "#ffc0c1":
                columns_count = self.TB_MBOM_Editon.columnCount()
                row_current = self.TB_MBOM_Editon.currentRow()
                for column in range(columns_count):
                    self.TB_MBOM_Editon.item(row_current, column).setBackground(QColor("#ffffda"))
         
    
    def insertion_confirm(self):
        #Structuring the edited MBOM information
        all_rows = self.TB_MBOM_Editon.rowCount()
        all_columns = self.TB_MBOM_Editon.columnCount()

        MBOM_edited = []
        for row in range(all_rows):
            row_list = []
            for column in range(all_columns):
                row_list.append(self.TB_MBOM_Editon.item(row, column).text())
                
            color_row_hex = colors.to_hex(self.TB_MBOM_Editon.item(row, 0).background().color().getRgbF())
            row_list.append(color_row_hex)
            MBOM_edited.append(row_list)

        MBOM_edited = pd.DataFrame(MBOM_edited)
        MBOM_edited.rename(columns={0:'SKU_product', 1:'SKU_component' , 2:'Type' ,3: 'Quantity' , 4:'Level' , 5:'Description', 6:'Background_color'}, inplace=True)
        #Editing the MBOM into DB
        try:
            sku_product = MBOM_edited['SKU_product'].iloc[0]
            query = ("""DELETE FROM tb_bom WHERE bom_produto_sku = '{}'""").format(sku_product)
            Functions_SQL.func_delete_sku(self, query)
            #Inserting data 
            MBOM_edited = MBOM_edited.query('Background_color != "#ffc0c1"')
            for row in range(MBOM_edited.shape[0]):
                query = ("""INSERT INTO tb_bom (bom_produto_sku, bom_componente_sku, bom_componente_type, bom_componente_quantidade, bom_componente_level)
                                VALUES ('{}', '{}', '{}', {}, {})""").format(
                                    MBOM_edited.iloc[row][0], MBOM_edited.iloc[row][1], MBOM_edited.iloc[row][2], float(MBOM_edited.iloc[row][3]), MBOM_edited.iloc[row][4])
                Functions_SQL.func_insert_sku(self,query)
            
            Functions_Message.standard_notification(
                self, 
                'MBOM edition', 
                'MBOM edition done!',
                'Information')
        except:
            Functions_Message.standard_notification(
                self, 
                'MBOM edition', 
                'Something went wrong!',
                'Warning')
    
class Functions_SQL(object):

    def func_insert_sku(self, query):
        try:
            connection = psycopg2.connect(**Global_Variables.param_DB_API)
            cursor = connection.cursor()
            #Fetch result
            cursor.execute(query)
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print(error)
            Functions_Message.standard_notification(self, 'Something gone wrong',error,'Warning')
        finally:
            if connection:
                    cursor.close()
                    connection.close()

    
    def func_delete_sku(self, query):
        try:
            connection = psycopg2.connect(**Global_Variables.param_DB_API)
            cursor = connection.cursor()
            #Fetch result
            cursor.execute(query)
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print(error)
            Functions_Message.standard_notification(self, 'Something gone wrong',error,'Warning')
        finally:
            if connection:
                    cursor.close()
                    connection.close()

    def func_select(self, query):
        try:
            connection = psycopg2.connect(**Global_Variables.param_DB_API)
            cursor = connection.cursor()
            #Fetch result
            cursor.execute(query)
            DB_DATASET = cursor.fetchall()

        except (Exception, psycopg2.Error) as error:
            #print(error)
            Functions_Message.standard_notification(self,'Something gone wrong',error,'Warning')
        finally:
            if connection:
                    cursor.close()
                    connection.close()
        
        return DB_DATASET
    
    def func_update_SKU_Validation_df(self, data_frame):
        try:
            connection = psycopg2.connect(**Global_Variables.param_DB_API)
            cursor = connection.cursor()
            #Fetch result
            for row in range(len(data_frame)):
                query = ("""UPDATE tb_produtos 
                            SET validation_status = '{}',  observations_validation = '{}' 
                            WHERE prod_produto_sku = '{}' """).format(data_frame.iloc[row,0], data_frame.iloc[row, 5],data_frame.iloc[row, 2] )
                cursor.execute(query)
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print(error)
            Functions_Message.standard_notification(self, 'Something gone wrong',error,'Warning')
        finally:
            if connection:
                    cursor.close()
                    connection.close()
    
    def bulk_insert_db_ace(self, data_frame_path):
        df = pd.read_csv(self.lineEdit_accessories.text())
        df = df.values.tolist()
        try:
            connection = psycopg2.connect(**Global_Variables.param_DB_API)
            cursor = connection.cursor()
            #Fetch result
            args = ','.join(cursor.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s)", i).decode('utf-8') for i in df)
            cursor.execute("INSERT INTO tb_acessorios VALUES " + (args))
            connection.commit()          
        except (Exception, psycopg2.Error) as error:
            print('ERRO!')
            print(error)
        finally:
            if connection:
                    cursor.close()
                    connection.close()
    
    def bulk_insert_db_prof(self, data_frame_path):
        df = pd.read_csv(self.lineEdit_profiles.text())
        df = df.values.tolist()
        try:
            connection = psycopg2.connect(**Global_Variables.param_DB_API)
            cursor = connection.cursor()
            #Fetch result

            args = ','.join(cursor.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s)", i).decode('utf-8') for i in df)

            cursor.execute("INSERT INTO tb_profiles VALUES " + (args))
            connection.commit()
            

        except (Exception, psycopg2.Error) as error:
            print('ERRO!')
            print(error)
        finally:
            if connection:
                    cursor.close()
                    connection.close()

    def bulk_insert_db_prod(self, data_frame_path):
        df = pd.read_csv(self.lineEdit_products.text())
        df = df.values.tolist()
        try:
            connection = psycopg2.connect(**Global_Variables.param_DB_API)
            cursor = connection.cursor()
            #Fetch result
            args = ','.join(cursor.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s, %s, %s)", i).decode('utf-8') for i in df)
            cursor.execute("INSERT INTO tb_produtos VALUES " + (args))
            connection.commit()
        
        except (Exception, psycopg2.Error) as error:
            print('ERRO!')
            print(error)
        finally:
            if connection:
                    cursor.close()
                    connection.close()
    
    def bulk_insert_db_bom(self, data_frame_path):
        df = pd.read_csv(self.lineEdit_bom.text())
        df = df.values.tolist()
        try:
            connection = psycopg2.connect(**Global_Variables.param_DB_API)
            cursor = connection.cursor()
            #Fetch result
            args = ','.join(cursor.mogrify("(%s,%s,%s,%s,%s,%s)", i).decode('utf-8') for i in df)

            cursor.execute("INSERT INTO tb_bom VALUES " + (args))
            connection.commit()
            
        except (Exception, psycopg2.Error) as error:
            print('ERRO!')
            print(error)
        finally:
            if connection:
                    cursor.close()
                    connection.close()

class Functions_data_set(object):

    def window_get_file_name():
        initial_dir = Global_Variables.Desktop_path  # Empty uses current folder.
        
        dialog = QFileDialog()
        dialog.setWindowTitle('Select the accessories file')
        dialog.setDirectory(initial_dir)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)

        ok = dialog.exec()

        return dialog.selectedFiles()
  
    def tb_bom_all(self):
        
        query = """SELECT TB_BOM.bom_produto_sku, TB_BOM.bom_componente_sku, TB_BOM.bom_componente_type, TB_BOM.bom_componente_quantidade, TB_BOM.bom_componente_level, TB_ACESSORIOS.ace_descricao, TB_PROFILES.perfil_descricao_dep 
                    FROM TB_BOM
                    FULL OUTER JOIN TB_ACESSORIOS
                        ON TB_BOM.bom_componente_sku = TB_ACESSORIOS.ace_acessorio_sku 
                    FULL OUTER JOIN TB_PROFILES
                        ON TB_BOM.bom_componente_sku = TB_PROFILES.perfil_sku
					WHERE TB_BOM.bom_produto_sku IS NOT NULL"""

        tb_data_set = pd.DataFrame(Functions_SQL.func_select(self,query))
        tb_data_set.rename(columns={0:"SKU_Produtc", 1:"SKU_Component", 2:"Type" , 3: "Quantity",4: "Level", 5:"Description_ACE", 6:"Description_Profile"}, inplace=True)
        tb_data_set['Component_Description'] = tb_data_set['Description_ACE']
        tb_data_set.loc[tb_data_set['Type'] == 'Profile', 'Component_Description'] = tb_data_set['Description_Profile']
        tb_data_set = tb_data_set.drop(['Description_ACE', 'Description_Profile'], axis=1)
        tb_data_set = tb_data_set.round(2)
        #tb_bom = tb_bom.values.tolist()

        return tb_data_set
    
    def tb_products_sku_all(self):
        
        query = """SELECT prod_produto_sku, prod_descricao, prod_cor_sku, validation_status, observations_validation FROM tb_produtos"""

        tb_data_set = pd.DataFrame( Functions_SQL.func_select(self,query))
        tb_data_set.rename(columns={0:"SKU", 1:"Description",2: "Color", 3:'Validated', 4:'Observations'}, inplace=True)
        tb_data_set['DB_Validation'] = tb_data_set['Validated'] 
        tb_data_set = tb_data_set.reindex(columns= ["Validated", "DB_Validation", "SKU", "Description", "Color", "Observations"])
        
        return tb_data_set
    
    def create_MBOM_file(self, sku_info, MBOM_data_frame):
        
        file_name = '\MBOM_file_SKU_' + str(sku_info[0]) + '.xlsx'

        workbook  = xlsxwriter.Workbook(Global_Variables.Desktop_path + file_name)
        worksheet = workbook.add_worksheet('MBOM')

        #####################################################
        #Creating the Worksheet template
        format_GG = workbook.add_format({'bold': True, 'font_color':'black', 'font_size':20})
        format_MBOM = workbook.add_format({'bold': True, 'font_color':'black','font_size':18,  'bg_color': '#F2F2F2', 'align': 'center'})
        format_header = workbook.add_format({'bold': True, 'font_color':'black','font_size':11,  'bg_color': '#F2F2F2', 'align': 'center'})
        format_fields = workbook.add_format({'bold': True, 'font_color':'white','font_size':11,  'bg_color': '#808080', 'align': 'center'})

        worksheet.write(0, 0, 'Gardengate', format_GG)
        worksheet.merge_range('A3:E4','Manufacturing BOM',format_MBOM)

        worksheet.merge_range('A6:E6', 'Product',format_header)
        row_product_info = 6
        worksheet.write(row_product_info, 0, 'SKU', format_fields)
        #worksheet.merge_range('B7:E7', 'Product',format_header)
        worksheet.write(row_product_info+1, 0, 'Description', format_fields)
        #worksheet.merge_range('B8:E8', 'Product',format_header)
        worksheet.write(row_product_info+2, 0, 'Color', format_fields)
        #worksheet.merge_range('B9:B9', 'Product',format_header)
        worksheet.write(row_product_info+3, 0, 'Observations', format_fields)

        row_component = 12
        worksheet.merge_range('A12:E12', 'Acessories', format_header)
        worksheet.write(row_component, 0, 'SKU', format_fields)
        worksheet.write(row_component, 1, 'Type', format_fields)
        worksheet.write(row_component, 2, 'Quantity', format_fields)
        worksheet.write(row_component, 3, 'Level', format_fields)
        worksheet.write(row_component, 4, 'Description', format_fields)

        worksheet.set_column(0, 0, 18.89)
        worksheet.set_column(1, 3, 8.11)
        worksheet.set_column(4, 4, 43.78)

        worksheet.hide_gridlines(2)

        #####################################################
        #Filling the table data
        row = 0 
        for info in sku_info:
            worksheet.write(row_product_info + row, 1,info)
            row +=1

        for row in range(MBOM_data_frame.shape[0]):
            for column in range(1,MBOM_data_frame.shape[1]):
                worksheet.write((row_component+1)+row, column-1,MBOM_data_frame.iat[row, column]) 

        workbook.close()



