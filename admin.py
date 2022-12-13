# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import traceback

from PyQt6 import QtCore, QtGui, QtWidgets
import Employee
import Product
import Major
import Role
import Department
import ai




class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindaaaaow")
        MainWindow.resize(431, 396)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 60, 271, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.QLNV = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.QLNV.setObjectName("QLNV")
        self.verticalLayout.addWidget(self.QLNV)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(310, 360, 100, 32))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 431, 20))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        # Nhan Vien
        try:
            self.QLNV.clicked.connect(self.OpenEmployee)
            self.QLNV.clicked.connect(MainWindow.close)
        except:
            traceback.print_exc()
        # Do an
        try:
            self.pushButton_3.clicked.connect(self.OpenProject)
            self.pushButton_3.clicked.connect(MainWindow.close)
        except:
            traceback.print_exc()
        # Chuyen nganh
        try:
            self.pushButton_4.clicked.connect(self.OpenMajor)
            self.pushButton_4.clicked.connect(MainWindow.close)
        except:
            traceback.print_exc()
        # Quyen
        try:
            self.pushButton.clicked.connect(self.OpenRole)
            self.pushButton.clicked.connect(MainWindow.close)
        except:
            traceback.print_exc()
        # Phong ban
        try:
            self.pushButton_5.clicked.connect(self.OpenDepartment)
            self.pushButton_5.clicked.connect(MainWindow.close)
        except:
            traceback.print_exc()
        # Chuc nang thong minh
        try:
            self.pushButton_7.clicked.connect(self.OpenAI)
            self.pushButton_7.clicked.connect(MainWindow.close)
        except:
            traceback.print_exc()

        try:
            self.pushButton_6.clicked.connect(self.Exit)
            self.pushButton_6.clicked.connect(MainWindow.close)
        except:
            traceback.print_exc()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.QLNV.setText(_translate("MainWindow", "Quản lí nhân viên"))
        self.pushButton_3.setText(_translate("MainWindow", "Quản lí đồ án"))
        self.pushButton_4.setText(_translate("MainWindow", "Quản lí chuyên ngành"))
        self.pushButton.setText(_translate("MainWindow", "Quản lí quyền"))
        self.pushButton_5.setText(_translate("MainWindow", "Quản lí phòng ban"))
        self.pushButton_7.setText(_translate("MainWindow", "Quản lí chức năng thông minh"))
        self.pushButton_6.setText(_translate("MainWindow", "Thoát"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">QUẢN LÍ</span></p></body></html>"))

    def OpenEmployee(self):
        try:
            #print(type(self.window))
            self.window = QtWidgets.QMainWindow()
            self.ui = Employee.Ui_admin()
            self.ui.setupUi(self.window)
            self.window.show()
        except:
            traceback.print_exc()
    def OpenProject(self):
        try:
            self.windowProject= QtWidgets.QMainWindow()
            self.ui = Product.Ui_MainWindow()
            self.ui.setupUi(self.windowProject)
            self.windowProject.show()
        except:
            traceback.print_exc()
    def OpenMajor(self):
        try:
            self.windowProject = QtWidgets.QMainWindow()
            self.ui = Major.Ui_MainWindow()
            self.ui.setupUi(self.windowProject)
            self.windowProject.show()
        except:
            traceback.print_exc()
    def OpenRole(self):
        try:
            self.windowProject = QtWidgets.QMainWindow()
            self.ui = Role.Ui_MainWindow()
            self.ui.setupUi(self.windowProject)
            self.windowProject.show()
        except:
            traceback.print_exc()
    def OpenDepartment(self):
        try:
            self.windowProject = QtWidgets.QMainWindow()
            self.ui = Department.Ui_MainWindow()
            self.ui.setupUi(self.windowProject)
            self.windowProject.show()
        except:
            traceback.print_exc()
    def OpenAI(self):
        try:
            self.windowProject = QtWidgets.QMainWindow()
            self.ui = ai.Ui_MainWindow()
            self.ui.setupUi(self.windowProject)
            self.windowProject.show()
        except:
            traceback.print_exc()
    def Exit(self):
        try:
            import dialog_Login
            self.windowProject = QtWidgets.QDialog()
            self.ui = dialog_Login.Ui_Dialog()
            self.ui.setupUi(self.windowProject)
            self.windowProject.show()
        except:
            traceback.print_exc()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
