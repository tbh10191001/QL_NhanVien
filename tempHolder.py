# Form implementation generated from reading ui file 'Product.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(854, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableSanpham = QtWidgets.QTableWidget(self.centralwidget)
        self.tableSanpham.setGeometry(QtCore.QRect(0, 0, 853, 341))
        self.tableSanpham.setObjectName("tableSanpham")
        self.tableSanpham.setColumnCount(7)
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
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableSanpham.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableSanpham.setHorizontalHeaderItem(6, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 360, 58, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(253, 360, 31, 16))
        self.label_2.setObjectName("label_2")
        self.labelIddoan = QtWidgets.QLabel(self.centralwidget)
        self.labelIddoan.setGeometry(QtCore.QRect(80, 360, 41, 16))
        self.labelIddoan.setObjectName("labelIddoan")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(284, 355, 351, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(21, 390, 91, 16))
        self.label_3.setObjectName("label_3")
        self.startDay = QtWidgets.QDateEdit(self.centralwidget)
        self.startDay.setGeometry(QtCore.QRect(110, 388, 110, 22))
        self.startDay.setObjectName("startDay")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(21, 420, 91, 16))
        self.label_4.setObjectName("label_4")
        self.expDay = QtWidgets.QDateEdit(self.centralwidget)
        self.expDay.setGeometry(QtCore.QRect(111, 418, 110, 22))
        self.expDay.setObjectName("expDay")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(21, 450, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(354, 390, 81, 16))
        self.label_6.setObjectName("label_6")
        self.cmbEmployee = QtWidgets.QComboBox(self.centralwidget)
        self.cmbEmployee.setGeometry(QtCore.QRect(420, 385, 215, 27))
        self.cmbEmployee.setObjectName("cmbEmployee")
        self.exitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitBtn.setGeometry(QtCore.QRect(749, 353, 91, 32))
        self.exitBtn.setObjectName("exitBtn")
        self.resetBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetBtn.setGeometry(QtCore.QRect(354, 446, 91, 32))
        self.resetBtn.setObjectName("resetBtn")
        self.deleteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteBtn.setGeometry(QtCore.QRect(630, 446, 91, 32))
        self.deleteBtn.setObjectName("deleteBtn")
        self.editBtn = QtWidgets.QPushButton(self.centralwidget)
        self.editBtn.setGeometry(QtCore.QRect(750, 446, 91, 31))
        self.editBtn.setObjectName("editBtn")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(354, 420, 61, 16))
        self.label_7.setObjectName("label_7")
        self.cmbRating = QtWidgets.QComboBox(self.centralwidget)
        self.cmbRating.setGeometry(QtCore.QRect(420, 416, 124, 27))
        self.cmbRating.setObjectName("cmbRating")
        self.labelSubmitDay = QtWidgets.QLabel(self.centralwidget)
        self.labelSubmitDay.setGeometry(QtCore.QRect(115, 450, 58, 16))
        self.labelSubmitDay.setObjectName("labelSubmitDay")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(490, 446, 91, 32))
        self.addBtn.setObjectName("addBtn")
        self.openBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openBtn.setGeometry(QtCore.QRect(750, 400, 91, 32))
        self.openBtn.setObjectName("openBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        item = self.tableSanpham.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Đánh giá"))
        item = self.tableSanpham.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "ID Nhân viên"))
        self.label.setText(_translate("MainWindow", "ID Đồ án:"))
        self.label_2.setText(_translate("MainWindow", "Tên:"))
        self.labelIddoan.setText(_translate("MainWindow", "1"))
        self.label_3.setText(_translate("MainWindow", "Ngày bắt đầu:"))
        self.label_4.setText(_translate("MainWindow", "Ngày kết thúc:"))
        self.label_5.setText(_translate("MainWindow", "Ngày nộp:"))
        self.label_6.setText(_translate("MainWindow", "Nhân viên:"))
        self.exitBtn.setText(_translate("MainWindow", "Thoát"))
        self.resetBtn.setText(_translate("MainWindow", "Reset"))
        self.deleteBtn.setText(_translate("MainWindow", "Xoá"))
        self.editBtn.setText(_translate("MainWindow", "Sửa"))
        self.label_7.setText(_translate("MainWindow", "Đánh giá:"))
        self.labelSubmitDay.setText(_translate("MainWindow", "2000-01-01"))
        self.addBtn.setText(_translate("MainWindow", "Thêm"))
        self.openBtn.setText(_translate("MainWindow", "Xem đồ án"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
