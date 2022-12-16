# Form implementation generated from reading ui file 'employeeProduct.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

from PyQt6.QtWidgets import QMessageBox
from datetime import datetime, date
import pyodbc
import traceback
import re
import employeeMain

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, idEmpPara):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(866, 325)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableSanpham = QtWidgets.QTableWidget(self.centralwidget)
        self.tableSanpham.setGeometry(QtCore.QRect(0, 50, 621, 261))
        self.tableSanpham.setObjectName("tableSanpham")
        self.tableSanpham.setColumnCount(5)
        self.tableSanpham.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableSanpham.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableSanpham.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableSanpham.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableSanpham.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableSanpham.setHorizontalHeaderItem(4, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 791, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(640, 60, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(704, 60, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(640, 90, 31, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(674, 90, 181, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(640, 120, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(733, 120, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(640, 150, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(740, 150, 71, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(640, 180, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(710, 180, 71, 16))
        self.label_11.setObjectName("label_11")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(710, 210, 100, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 10, 100, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(640, 250, 71, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lbl_fileSubmitName = QtWidgets.QLabel(self.centralwidget)
        self.lbl_fileSubmitName.setGeometry(QtCore.QRect(710, 250, 201, 31))
        self.lbl_fileSubmitName.setText("")
        self.lbl_fileSubmitName.setObjectName("lbl_fileSubmitName")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.filePathSubmit = ""
        self.idEmp = idEmpPara
        self.mainWindowCopy = MainWindow

        self.tableSanpham.setColumnWidth(0, 65)
        self.tableSanpham.setColumnWidth(1, 239)
        self.tableSanpham.setColumnWidth(2, 98)
        self.tableSanpham.setColumnWidth(3, 102)
        self.tableSanpham.setColumnWidth(4, 98)

        self.loadDataFromDB()
        self.hideButton()

        #listenerFunctions
        self.pushButton.clicked.connect(self.askDirectory)
        self.pushButton_2.clicked.connect(self.clickToBackMainEmpWindow)
        self.tableSanpham.clicked.connect(self.clickTableShowInfo)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableSanpham.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID Đồ án"))
        item = self.tableSanpham.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên"))
        item = self.tableSanpham.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ngày bắt đầu"))
        item = self.tableSanpham.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ngày kết thúc"))
        item = self.tableSanpham.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Ngày nộp"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">ĐỒ ÁN CÁ NHÂN</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "ID Đồ án:"))
        self.label_3.setText(_translate("MainWindow", ""))
        self.label_4.setText(_translate("MainWindow", "Tên:"))
        self.label_5.setText(_translate("MainWindow", ""))
        self.label_6.setText(_translate("MainWindow", "Ngày bắt đầu:"))
        self.label_7.setText(_translate("MainWindow", ""))
        self.label_8.setText(_translate("MainWindow", "Ngày kết thúc:"))
        self.label_9.setText(_translate("MainWindow", ""))
        self.label_10.setText(_translate("MainWindow", "Ngày nộp:"))
        self.label_11.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "Nộp"))
        self.pushButton_2.setText(_translate("MainWindow", "Thoát"))
        self.label_12.setText(_translate("MainWindow", "Tên file nộp:"))

    def askDirectory(self):
        try:
            import os
            import shutil

            self.filePathSubmit = \
                str(QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Hey! Select a File')).split("'")[1]
            if self.filePathSubmit == "":
                return
            fileName = self.filePathSubmit.split(r"/")[len(self.filePathSubmit.split(r"/")) - 1]
            fileType = fileName.split(".")[1]
            accentedProjectName = str(self.tableSanpham.item(self.tableSanpham.currentRow(), 1).text())
            idProject = str(self.tableSanpham.item(self.tableSanpham.currentRow(), 0).text())
            assignProjectYear = str(self.tableSanpham.item(self.tableSanpham.currentRow(), 2).text()).split("-")[0]
            if self.showMessageConfirm("Are you sure to want to submit this file?", "Your file name: " + fileName):
                unsignedProjectName = self.convertAccentedToUnsigned(accentedProjectName)
                fileNameToSubmit = f"{idProject}_{self.idEmp}_{unsignedProjectName}.{fileType}"
                # print(fileNameToSubmit)
                dst_path = os.path.join(".\\Project Management", assignProjectYear, fileNameToSubmit)
                print(dst_path)
                shutil.copy(self.filePathSubmit, dst_path)
                print('Copied')
                try:
                    conn = pyodbc.connect("DRIVER={SQL Server Native Client 11.0};"
                                          "Server=localhost;"
                                          "Database=HTTM;"
                                          "Trusted_connection=yes;"
                                          "MARS_Connection=yes")
                    idProject = self.label_3.text()
                    submitDate = date.today().strftime("%Y-%m-%d")
                    cursorExc = conn.cursor()
                    cursorExc.execute("""UPDATE PRODUCT SET SUBMITDAY= (?) WHERE IDPRODUCT = (?)""",(submitDate, idProject))
                    cursorExc.commit()
                    cursorExc.close()
                except:
                    traceback.print_exc()
                self.loadDataFromDB()
        except:
            traceback.print_exc()
    def loadDataFromDB(self):
        self.tableSanpham.setRowCount(0)
        try:
            conn = pyodbc.connect("DRIVER={SQL Server Native Client 11.0};"
                                  "Server=localhost;"
                                  "Database=HTTM;"
                                  "Trusted_connection=yes;"
                                  "MARS_Connection=yes")
            cursor = conn.cursor()
            sqlQuery = cursor.execute("""SELECT IDPRODUCT, PRODUCTNAME, STARTDAY, EXPDAY, SUBMITDAY FROM PRODUCT "
                                      "WHERE IDEMP = (?)""", self.idEmp)
            tableRow = 0
            for rowData in sqlQuery:
                # print(rowData)
                rowNumber = self.tableSanpham.rowCount()
                self.tableSanpham.insertRow(rowNumber)
                for colNumber, data in enumerate(rowData):
                    if colNumber == 4 and data is None:
                        self.tableSanpham.setItem(rowNumber, colNumber, QtWidgets.QTableWidgetItem("Chưa nộp"))
                        continue
                    self.tableSanpham.setItem(rowNumber, colNumber, QtWidgets.QTableWidgetItem(str(data)))
        except():
            import traceback
            traceback.print_exc()

    def clickTableShowInfo(self):
        try:
            currentRowNum = self.tableSanpham.currentRow()
            self.label_3.setText(str(self.tableSanpham.item(currentRowNum, 0).text()))
            self.label_5.setText(str(self.tableSanpham.item(currentRowNum, 1).text()))
            self.label_7.setText(str(self.tableSanpham.item(currentRowNum, 2).text()))
            expDateStr = str(self.tableSanpham.item(currentRowNum, 3).text())
            self.label_9.setText(expDateStr)
            expDate = datetime.strptime(expDateStr, "%Y-%m-%d")
            submitDate = self.tableSanpham.item(currentRowNum, 4).text()
            self.label_11.setText(submitDate)
            if submitDate == "Chưa nộp":
                self.showButton("Nộp")
            elif expDate.date() >= date.today():
                self.showButton("Nộp lại")
        except:
            import traceback
            traceback.print_exc()

    def hideButton(self):
        self.pushButton.hide()
        self.label_12.hide()
        self.lbl_fileSubmitName.hide()

    def showButton(self, message):
        self.pushButton.setText(message)
        self.pushButton.show()

    def showMessageConfirm(self, message, information):
        msg = QMessageBox()
        msg.setWindowTitle("Confirm!")
        msg.setText(message)
        msg.setInformativeText(information)
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        result = msg.exec()
        return result == QMessageBox.StandardButton.Ok

    def convertAccentedToUnsigned(self, text):
        patterns = {
            '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
            '[đ]': 'd',
            '[èéẻẽẹêềếểễệ]': 'e',
            '[ìíỉĩị]': 'i',
            '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
            '[ùúủũụưừứửữự]': 'u',
            '[ỳýỷỹỵ]': 'y'
            }
        output = text
        for regex, replace in patterns.items():
            output = re.sub(regex, replace, output)
            # deal with upper case
            output = re.sub(regex.upper(), replace.upper(), output)
        return output

    def clickToBackMainEmpWindow(self):
        try:
            self.windowEmployeeMain = QtWidgets.QMainWindow()
            self.ui = employeeMain.Ui_MainWindow()
            self.ui.setupUi(self.windowEmployeeMain, self.idEmp)
            self.windowEmployeeMain.show()
            self.mainWindowCopy.close()
        except:
            traceback.print_exc()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, "7")
    MainWindow.show()
    sys.exit(app.exec())
