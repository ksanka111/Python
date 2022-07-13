from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog, QAction, QMessageBox, QStackedWidget

import sys
import pandas as pd
import numpy as np

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Обработчик Excel")
        self.setGeometry(100,100,800, 550)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.name_col = QtWidgets.QComboBox(self.centralwidget)
        self.name_col.setGeometry(QtCore.QRect(150, 20, 201, 22))
        self.name_col.setObjectName("name_col")

        self.col_after = QtWidgets.QCheckBox(self.centralwidget)
        self.col_after.setGeometry(QtCore.QRect(10, 80, 211, 17))
        self.col_after.setText("Добавить столбец в конец таблицы")
        self.col_after.setObjectName("col_after")

        self.col_ind = QtWidgets.QCheckBox(self.centralwidget)
        self.col_ind.setGeometry(QtCore.QRect(10, 150, 281, 17))
        self.col_ind.setText("Добавить столбец после определенного столбца")
        self.col_ind.setObjectName("col_ind")

        self.znachenie = QtWidgets.QTextEdit(self.centralwidget)
        self.znachenie.setGeometry(QtCore.QRect(460, 20, 211, 21))
        self.znachenie.setObjectName("znachenie")

        self.action_2 = QtWidgets.QComboBox(self.centralwidget)
        self.action_2.setGeometry(QtCore.QRect(370, 20, 69, 22))
        self.action_2.setObjectName("action_2")
        self.action_2.addItem("")
        self.action_2.addItem("")
        self.action_2.addItem("")
        self.action_2.addItem("")
        self.action_2.addItem("")
        self.action_2.addItem("")
        self.action_2.addItem("")
        self.action_2.setItemText(0, "Выбрать")
        self.action_2.setItemText(1, ">")
        self.action_2.setItemText(2, "<")
        self.action_2.setItemText(3, "=")
        self.action_2.setItemText(4, ">=")
        self.action_2.setItemText(5, "<=")
        self.action_2.setItemText(6,  "≠")

        self.otbor = QtWidgets.QCheckBox(self.centralwidget)
        self.otbor.setGeometry(QtCore.QRect(10, 20, 141, 31))
        self.otbor.setText("Отбор по значению")
        self.otbor.setObjectName("otbor")

        self.name_col_end = QtWidgets.QTextEdit(self.centralwidget)
        self.name_col_end.setGeometry(QtCore.QRect(240, 80, 231, 31))
        self.name_col_end.setObjectName("name_col_end")


        self.name_col_2 = QtWidgets.QComboBox(self.centralwidget)
        self.name_col_2.setGeometry(QtCore.QRect(310, 150, 201, 22))
        self.name_col_2.setObjectName("name_col_2")

        self.znachenie_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.znachenie_2.setGeometry(QtCore.QRect(530, 150, 211, 21))
        self.znachenie_2.setObjectName("znachenie")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 210, 91, 31))
        self.pushButton.setText("Отправить")
        self.pushButton.clicked.connect(self.new_data)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 250, 781, 221))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 480, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Сохранить")
        self.pushButton_3.clicked.connect(self.exportToExcel)

        self.setCentralWidget(self.centralwidget)
        self.menuBar()
        self.fname = None

    def menuBar(self):
        self.menu = QMenuBar(self)
        self.setMenuBar(self.menu)

        fileMenu = QMenu("&Файл", self)
        self.menu.addMenu(fileMenu)

        fileMenu.addAction('Загрузить', self.action_clicked)



    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        if action.text() == 'Загрузить':
            open_file = QFileDialog.getOpenFileName(self, "Выбрать файл",'','Excel files(*.xlsx , *.xls)')
            print(open_file)
            global path_open_file
            path_open_file = open_file[0]
            print(path_open_file)

            if len(path_open_file) > 0: # читаем загрузенный файл
                input_table = pd.read_excel(path_open_file)
                input_table.to_excel('./user_file.xlsx') # записываем к себе загруженный файл
                print(input_table)

                self.tableWidget.setRowCount(input_table.shape[0])  # сохраняем и выводим таблицу
                self.tableWidget.setColumnCount(input_table.shape[1])
                self.tableWidget.setHorizontalHeaderLabels(input_table.columns)

                for row in input_table.iterrows():  # сохраняем и выводим значения в таблице
                    values = row[1]
                    for col_index, value in enumerate(values):
                        if isinstance(value, (float, int)):
                            value = '{0:0,.0f}'.format(value)
                        tableItem = QtWidgets.QTableWidgetItem(str(value))
                        self.tableWidget.setItem(row[0], col_index, tableItem)
                self.tableWidget.setColumnWidth(2, 300)

                x = input_table.columns     # названия столбцов в переменную
                x_n = ' '.join(x).split(' ')
                print(x_n)

                for i in x_n:   # добавляем названия столбцов из файла в ComboBox
                    self.name_col.addItem(i)
                    self.name_col.setItemText(-1, i)
                    self.name_col_2.addItem(i)
                    self.name_col_2.setItemText(-1, i)

    def new_data(self): # получаем значения после заполнения формы
        userfile = pd.read_excel('./user_file.xlsx')
        print(userfile)
        if self.otbor.isChecked():
            namecol = self.name_col.currentText()  # значение из Combobox в переменную
            print(namecol)
            action2 = self.action_2.currentText()  # значение из Combobox в переменную
            print(action2)
            znachenie_n = self.znachenie.toPlainText()  # значение из строки для ввода
            print(znachenie_n)
            if action2 == '>':
                filter = userfile[namecol] > int(znachenie_n)
                new_table = userfile.loc[filter]
                new_table.to_excel('./user_file_new.xlsx')
            elif action2 == '<':
                filter = userfile[namecol] < int(znachenie_n)
                new_table = userfile.loc[filter]
                new_table.to_excel('./user_file_new.xlsx')
            elif action2 == '>=':
                filter = userfile[namecol] >= int(znachenie_n)
                new_table = userfile.loc[filter]
                new_table.to_excel('./user_file_new.xlsx')
            elif action2 == '<=':
                filter = userfile[namecol] <= int(znachenie_n)
                new_table = userfile.loc[filter]
                new_table.to_excel('./user_file_new.xlsx')
            elif action2 == '=':
                filter = userfile[namecol] = int(znachenie_n)
                new_table = userfile.loc[filter]
                new_table.to_excel('./user_file_new.xlsx')
            else:
                filter = userfile[namecol] == znachenie_n
                new_table = userfile.loc[filter]
                new_table.to_excel('./user_file_new.xlsx')

        if self.col_after.isChecked():
            namecolend = self.name_col_end.toPlainText()
            if namecolend != '':
                new_table = userfile
                new_table[namecolend] = ''
                new_table.to_excel('./user_file_new.xlsx')

        if self.col_ind.isChecked():
            namecol2 = self.name_col_2.currentText()
            znachenie_n_2 = self.znachenie_2.toPlainText()
            if namecol2 != '':
                new_table = userfile
                ind = new_table.columns.get_loc(namecol2)
                print(ind)
                new_table.insert(ind +1, znachenie_n_2, 'nan')
                new_table.to_excel('./user_file_new.xlsx')

        # обновляет таблицу согласно выбранной обработке
        newtable = pd.read_excel('./user_file_new.xlsx')
        self.tableWidget.setRowCount(newtable.shape[0])  # сохраняем и выводим таблицу
        self.tableWidget.setColumnCount(newtable.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(newtable.columns)

        for row in newtable.iterrows():  # сохраняем и выводим значения в таблице
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0,.0f}'.format(value)
                tableItem = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(row[0], col_index, tableItem)
        self.tableWidget.setColumnWidth(2, 300)


    def exportToExcel(self):
        path, _ = QFileDialog.getSaveFileName(self, 'Save Excel', '.', 'Excel(*.xlsx)')
        if not path:
            mes = QMessageBox.information(self, 'Внимание', 'Не указан файл для сохранения.')
            return

        columnHeaders = []
        # создаем список заголовков столбцов
        for j in range(self.tableWidget.model().columnCount()):
            columnHeaders.append(self.tableWidget.horizontalHeaderItem(j).text())

        df = pd.DataFrame(columns=columnHeaders)

        # создаем набор записей объекта dataframe
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                df.at[row, columnHeaders[col]] = self.tableWidget.item(row, col).text()

        df.to_excel(path, index=False)
        msg = QMessageBox.information(self, 'Ok', 'Файл сохранен')


def application():
    apl = QtWidgets.QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(apl.exec_())

if __name__ == "__main__":
    application()



