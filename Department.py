# Form implementation generated from reading ui file 'Department.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import traceback

import pyodbc
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(652, 349)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnEditDep = QtWidgets.QPushButton(self.centralwidget)
        self.btnEditDep.setGeometry(QtCore.QRect(420, 210, 100, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnEditDep.setFont(font)
        self.btnEditDep.setObjectName("btnEditDep")
        self.btnAddDep = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddDep.setGeometry(QtCore.QRect(420, 160, 100, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnAddDep.setFont(font)
        self.btnAddDep.setObjectName("btnAddDep")
        self.btnDelDep = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelDep.setGeometry(QtCore.QRect(540, 160, 100, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnDelDep.setFont(font)
        self.btnDelDep.setObjectName("btnDelDep")
        self.btnExitDep = QtWidgets.QPushButton(self.centralwidget)
        self.btnExitDep.setGeometry(QtCore.QRect(530, 300, 100, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnExitDep.setFont(font)
        self.btnExitDep.setObjectName("btnExitDep")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(3, 12, 651, 20))
        self.label.setObjectName("label")
        self.tableDep = QtWidgets.QTableWidget(self.centralwidget)
        self.tableDep.setGeometry(QtCore.QRect(10, 60, 401, 271))
        self.tableDep.setObjectName("tableDep")
        self.tableDep.setColumnCount(2)
        self.tableDep.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableDep.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableDep.setHorizontalHeaderItem(1, item)
        self.tableDep.horizontalHeader().setDefaultSectionSize(200)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(420, 60, 221, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.inputDep = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.inputDep.setObjectName("inputDep")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputDep)
        self.idDep = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.idDep.setFont(font)
        self.idDep.setObjectName("idDep")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.idDep)
        self.btnResetDep = QtWidgets.QPushButton(self.centralwidget)
        self.btnResetDep.setGeometry(QtCore.QRect(540, 210, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnResetDep.setFont(font)
        self.btnResetDep.setObjectName("btnResetDep")
        MainWindow.setCentralWidget(self.centralwidget)

        self.loadData()
        self.tableDep.clicked.connect(self.clickToShowData)
        self.btnEditDep.clicked.connect(self.clickToEdit)
        self.btnAddDep.clicked.connect(self.clickToAdd)
        self.btnDelDep.clicked.connect(self.clickToDel)
        self.btnResetDep.clicked.connect(self.clickToReset)
        try:
            self.btnExitDep.clicked.connect(MainWindow.close)
            self.btnExitDep.clicked.connect(self.openAdmin)
        except:
            traceback.print_exc()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def loadData(self):
        try:
            sever = 'localhost'
            database = 'HTTM'
            conn = pyodbc.connect("DRIVER={SQL Server Native Client 11.0};"
                                  "Server=localhost;"
                                  "Database=HTTM;"
                                  "Trusted_connection=yes;"
                                  "MARS_Connection=yes")
            cursor = conn.cursor()
            sql = cursor.execute("SELECT * FROM DEPARTMENT")
            for rowData in sql:
                rowNumber = self.tableDep.rowCount()
                self.tableDep.insertRow(rowNumber)
                for colName, data in enumerate(rowData):
                    self.tableDep.setItem(rowNumber, colName, QtWidgets.QTableWidgetItem(str(data)))
        except:
            traceback.print_exc()

    def setTableRow(self):
        while self.tableDep.rowCount() > 0:
            self.tableDep.removeRow(0)

    def clickToShowData(self):
        try:
            selectedRow = self.tableDep.currentRow()
            self.idDep.setText(self.tableDep.item(selectedRow, 0).text())
            self.inputDep.setText(self.tableDep.item(selectedRow, 1).text())
        except:
            traceback.print_exc()

    def clickToEdit(self):
        try:
            sever = 'localhost'
            database = 'HTTM'
            conn = pyodbc.connect("DRIVER={SQL Server Native Client 11.0};"
                                  "Server=localhost;"
                                  "Database=HTTM;"
                                  "Trusted_connection=yes;"
                                  "MARS_Connection=yes")
            idDep = self.idDep.text()
            inputNew = self.inputDep.text()
            cursor = conn.cursor()
            cursor.execute("UPDATE DEPARTMENT SET DEPNAME = '" + inputNew + "' WHERE DEPARTMENT.IDDEP = '" + str(idDep) + "'")
            cursor.commit()
            self.setTableRow()
            self.loadData()
        except:
            traceback.print_exc()

    def clickToAdd(self):
        try:
            sever = 'localhost'
            database = 'HTTM'
            conn = pyodbc.connect("DRIVER={SQL Server Native Client 11.0};"
                                  "Server=localhost;"
                                  "Database=HTTM;"
                                  "Trusted_connection=yes;"
                                  "MARS_Connection=yes")
            inputDep = self.inputDep.text()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO DEPARTMENT(DEPNAME) VALUES(?)", (inputDep))
            cursor.commit()
            self.setTableRow()
            self.loadData()
        except:
            traceback.print_exc()

    def clickToDel(self):
        try:
            sever = 'localhost'
            database = 'HTTM'
            conn = pyodbc.connect("DRIVER={SQL Server Native Client 11.0};"
                                  "Server=localhost;"
                                  "Database=HTTM;"
                                  "Trusted_connection=yes;"
                                  "MARS_Connection=yes")
            idDep = self.idDep.text()
            print(idDep)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM DEPARTMENT WHERE DEPARTMENT.IDDEP = '" + idDep + "'")
            cursor.commit()
            self.setTableRow()
            self.loadData()
        except:
            traceback.print_exc()

    def clickToReset(self):
        try:
            self.inputDep.setText("")
            self.idDep.setText("")
        except:
            traceback.print_exc()

    def openAdmin(self):
        try:
            import admin
            self.windowProject = QtWidgets.QMainWindow()
            self.ui = admin.Ui_MainWindow()
            self.ui.setupUi(self.windowProject)
            self.windowProject.show()
        except:
            traceback.print_exc()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnEditDep.setText(_translate("MainWindow", "Sửa"))
        self.btnAddDep.setText(_translate("MainWindow", "Thêm"))
        self.btnDelDep.setText(_translate("MainWindow", "Xoá"))
        self.btnExitDep.setText(_translate("MainWindow", "Thoát"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">THÔNG TIN PHÒNG BAN</span></p></body></html>"))
        item = self.tableDep.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID Phòng ban"))
        item = self.tableDep.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên"))
        self.label_4.setText(_translate("MainWindow", "ID:"))
        self.label_3.setText(_translate("MainWindow", "Tên:"))
        self.btnResetDep.setText(_translate("MainWindow", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
