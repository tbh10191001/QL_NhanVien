# Form implementation generated from reading ui file 'ai.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import traceback

import pyodbc
from PyQt6 import QtCore, QtGui, QtWidgets
import pandas as pd
from  sklearn.tree import DecisionTreeClassifier
import pickle
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(369, 223)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 70, 187, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 180, 100, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 361, 20))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.calRating)
        self.pushButton_2.clicked.connect(self.buildtree)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(self.openadmin)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Cập nhật rating Nhân viên"))
        self.pushButton_2.setText(_translate("MainWindow", "Train AI"))
        self.pushButton_3.setText(_translate("MainWindow", "Thoát"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">AI</span></p></body></html>"))


    def calRating(self):
        sever = 'localhost'
        database = 'HTTM'
        conn = pyodbc.connect("DRIVER={SQL Server Native Client 11.0};"
                              "Server=localhost;"
                              "Database=HTTM;"
                              "Trusted_connection=yes;"
                              "MARS_Connection=yes")
        cursor=conn.cursor()
        cursor.execute("SELECT IDEMP FROM EMPLOYEE")
        listID=[]
        for row in cursor.fetchall():
            listID.append(row[0])
            print(row)
        for x in listID:
            result=0
            try:
                cursor.execute("SELECT RATING FROM PRODUCT WHERE IDEMP=?",x)
                print(x)
                temp=cursor.fetchall()
                print(len(temp))
                if(len(temp)!=0):
                    stringresult = ""
                    trungbinh = len(temp)
                    for row in temp:

                        if(row[0]=="Kha"): result+=6
                        if(row[0]=="Tot"): result+=10
                        result=result//trungbinh

                        if(result>=3):
                            if(result>=7):
                                stringresult="Tot"
                            else:
                                stringresult="Kha"
                        else:
                            stringresult="Kem"
                    print(stringresult)
                    print(x)
                    try:
                        print("xxxxxx")
                        cursor.execute("UPDATE EMPLOYEE SET AVGRATING = ? WHERE IDEMP = ?",stringresult,x)
                        cursor.commit()
                    except:
                        traceback.print_exc()
            except:
                traceback.print_exc()

    def buildtree(self):
        CV=[]
        sever = 'localhost'
        database = 'HTTM'
        conn = pyodbc.connect("DRIVER={SQL Server Native Client 11.0};"
                              "Server=localhost;"
                              "Database=HTTM;"
                              "Trusted_connection=yes;"
                              "MARS_Connection=yes")
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT EDUCATIONLEVEL, FOREIGNLANGUAGES, TEAMWORKSKILLS, COMMUNICATIONSKILLS, EXPERIENCE, IDEMP FROM CV")
            for row in cursor.fetchall():
                temp = [elem for elem in row]


                CV.append(temp)
            y=[]
            print(CV)
            for x in CV:
                cursor.execute("Select AVGRATING FROM EMPLOYEE WHERE IDEMP=?",x[5])
                y.append(cursor.fetchone()[0])
                del x[5]
            print(CV)
            df = pd.DataFrame(CV,
                              columns=['Hoc van', 'TD Tieng Anh', 'Lam viec nhom', 'KN Giao Tiep', 'Experience'])
            df2=pd.DataFrame(y,columns=['RATING'])
            print(df.shape)
            print(df2.shape)
            df['Hoc van'].replace(['THPT', 'TC nghe', 'Cao dang', 'Dai hoc', 'Cao hoc'], [1, 2, 3, 4, 5, ],
                                  inplace=True)
            df['TD Tieng Anh'].replace(['Beginner', 'Elementary', 'Intermediate', 'Upper-Intermediate', 'Advanced'],
                                       [1, 2, 3, 4, 5], inplace=True)
            df['Lam viec nhom'].replace(['Kem', 'Kha', 'Tot'], [1, 2, 3], inplace=True)
            df['KN Giao Tiep'].replace(['Kem', 'Kha', 'Tot'], [1, 2, 3], inplace=True)
            df['Experience'].replace(['Fresher', 'Junior', 'Senior', 'Manager'], [1, 2, 3, 4], inplace=True)
            df2['RATING'].replace(['Kem', 'Kha', 'Tot'], [1, 2, 3], inplace=True)
            print(df)
            print(df2)
            my_tree=DecisionTreeClassifier()
            my_tree.fit(df,df2)
            pickle.dump(my_tree,open('tree.h5','wb'))
        except:
            traceback.print_exc()

    def openadmin(self):
        try:
            import admin
            self.windowProject = QtWidgets.QMainWindow()
            self.ui = admin.Ui_MainWindow()
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
