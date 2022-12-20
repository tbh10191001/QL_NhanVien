# Form implementation generated from reading ui file 'dialog_EditCV.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import traceback

import pyodbc
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    id = ""

    def init(self, id=''):
        self.id = id

    def set_id(self, id):
        self.id = id;

    def get_id(self):
        return self.id;

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 313)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setGeometry(QtCore.QRect(316, 270, 56, 17))
        self.cancelBtn.setObjectName("cancelBtn")
        self.okBtn = QtWidgets.QPushButton(self.centralwidget)
        self.okBtn.setGeometry(QtCore.QRect(246, 270, 56, 17))
        self.okBtn.setObjectName("okBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(6, 20, 401, 20))
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 50, 371, 201))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.idCV = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.idCV.setFont(font)
        self.idCV.setObjectName("idCV")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.idCV)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.FLCbb = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FLCbb.setFont(font)
        self.FLCbb.setObjectName("FLCbb")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.FLCbb)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.TSCbb = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TSCbb.setFont(font)
        self.TSCbb.setObjectName("TSCbb")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.TSCbb)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.ExpCbb = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ExpCbb.setFont(font)
        self.ExpCbb.setObjectName("ExpCbb")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.ExpCbb)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.ELCbb = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ELCbb.setFont(font)
        self.ELCbb.setObjectName("ELCbb")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.ELCbb)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.CSCbb = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CSCbb.setFont(font)
        self.CSCbb.setObjectName("CSCbb")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.CSCbb)
        MainWindow.setCentralWidget(self.centralwidget)
        self.loadForeignLanguages()
        self.loadTeamworkSkills()
        self.loadEducationLevels()
        self.loadExp()
        self.loadCommunicationSkills()
        self.loadData()
        self.okBtn.clicked.connect(self.okBtnClicked)
        self.okBtn.clicked.connect(MainWindow.close)
        self.cancelBtn.clicked.connect(MainWindow.close)

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
            idemp = self.get_id()
            cursor = conn.cursor()
            sql = cursor.execute("SELECT * FROM CV WHERE CV.IDEMP = '"+ idemp + "'")
            temp = sql.fetchone()
            fl = temp[1]
            ts = temp[2]
            exp = temp[3]
            el = temp[4]
            cs = temp[5]
            self.idCV.setText(self.get_id())
            self.FLCbb.setCurrentText(fl)
            self.TSCbb.setCurrentText(ts)
            self.ExpCbb.setCurrentText(exp)
            self.ELCbb.setCurrentText(el)
            self.CSCbb.setCurrentText(cs)
        except:
            traceback.print_exc()

    def okBtnClicked(self):
        try:
            sever = 'localhost'
            database = 'HTTM'
            conn = pyodbc.connect("DRIVER={SQL Server Native Client 11.0};"
                                  "Server=localhost;"
                                  "Database=HTTM;"
                                  "Trusted_connection=yes;"
                                  "MARS_Connection=yes")
            idemp = self.get_id()
            cursor = conn.cursor()
            fl = self.FLCbb.currentText()
            ts = self.TSCbb.currentText()
            exp = self.ExpCbb.currentText()
            el = self.ELCbb.currentText()
            cs = self.CSCbb.currentText()
            cursor.execute("UPDATE CV SET FOREIGNLANGUAGES = '" + str(fl) + "', TEAMWORKSKILLS = '" + str(ts) + "', EXPERIENCE = '" + str(exp) + "', EDUCATIONLEVEL = '" + str(el) + "', COMMUNICATIONSKILLS = '" + str(cs) + "' WHERE CV.IDEMP ='" + self.get_id() + "'")
            cursor.commit()
        except:
            traceback.print_exc()

    def loadForeignLanguages(self):
        try:
            fl = ["Beginner", "Elementary", "Intermediate", "Upper-Intermediate", "Advanced"]
            for i in fl:
                self.FLCbb.addItem(i)
        except:
            traceback.print_exc()

    def loadTeamworkSkills(self):
        try:
            ts = ["Kem", "Kha", "Tot"]
            for i in ts:
                self.TSCbb.addItem(i)
        except:
            traceback.print_exc()

    def loadExp(self):
        try:
            exp = ["Fresher", "Junior", "Senior", "Manager"]
            for i in exp:
                self.ExpCbb.addItem(i)
        except:
            traceback.print_exc()

    def loadEducationLevels(self):
        try:
            el = ["THPT", "Trung cap nghe", "Cao dang", "Dai hoc", "Cao hoc"]
            for i in el:
                self.ELCbb.addItem(i)
        except:
            traceback.print_exc()

    def loadCommunicationSkills(self):
        try:
            cs = ["Kem", "Kha", "Tot"]
            for i in cs:
                self.CSCbb.addItem(i)
        except:
            traceback.print_exc()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel"))
        self.okBtn.setText(_translate("MainWindow", "OK"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">CV</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">ID CV:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Trình độ ngoại ngữ:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Kĩ năng làm việc nhóm:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Kinh nghiệm:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Trình độ học vấn:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Kĩ năng giao tiếp:</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
