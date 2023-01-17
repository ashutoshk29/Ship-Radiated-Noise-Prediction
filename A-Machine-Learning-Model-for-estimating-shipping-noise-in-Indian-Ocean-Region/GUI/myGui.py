from tkinter import Y
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import *
import joblib
import tensorflow as tf
from pickle import load

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1040, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 40, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 115, 150, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 155, 160, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 195, 150, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 235, 150, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(150, 275, 150, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.frequency = QtWidgets.QLineEdit(self.centralwidget)
        self.frequency.setGeometry(QtCore.QRect(340, 110, 111, 30))
        self.frequency.setObjectName("frequency")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frequency.setFont(font)
        self.onlyDouble = QDoubleValidator()
        self.frequency.setValidator(self.onlyDouble)

        self.speed = QtWidgets.QLineEdit(self.centralwidget)
        self.speed.setGeometry(QtCore.QRect(340, 150, 111, 30))
        self.speed.setObjectName("speed")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.speed.setFont(font)
        self.onlyDouble = QDoubleValidator()
        self.speed.setValidator(self.onlyDouble)

        self.dwt = QtWidgets.QLineEdit(self.centralwidget)
        self.dwt.setGeometry(QtCore.QRect(340, 190, 111, 30))
        self.dwt.setObjectName("dwt")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dwt.setFont(font)
        self.onlyDouble = QDoubleValidator()
        self.dwt.setValidator(self.onlyDouble)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(340, 230, 111, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)

        self.length = QtWidgets.QLineEdit(self.centralwidget)
        self.length.setGeometry(QtCore.QRect(340, 270, 111, 30))
        self.length.setObjectName("length")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.length.setFont(font)
        self.onlyDouble = QDoubleValidator()
        self.length.setValidator(self.onlyDouble)

        new_model = tf.keras.models.load_model('my_model.h5')
        sc = load(open('scaler.pkl', 'rb'))
        le = joblib.load('labelEncoder.joblib')
        pt = load(open('power_transform.pkl', 'rb'))

        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.calculate(new_model, sc, le, pt))
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(615, 180, 100, 40))
        self.pushButton.setObjectName("pushButton")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet('background-color:blue; color:white; font-weight:bold;')

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clear())
        self.pushButton2.setEnabled(True)
        self.pushButton2.setGeometry(QtCore.QRect(745, 180, 100, 40))
        self.pushButton2.setObjectName("pushButton2")
        font.setPointSize(10)
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet('background-color:grey; color:white; font-weight:bold;')

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(655, 120, 180, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(600, 250, 260, 50))
        self.textBrowser.setObjectName("textBrowser")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setPlaceholderText("Predicted Noise Value Will Appear In This Box.")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1040, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def clear(self):
        self.frequency.setText('')
        self.speed.setText('')
        self.dwt.setText('')
        self.comboBox.setCurrentText('--Select--')
        self.length.setText('')
        self.textBrowser.setText('')
        
    def calculate(self, new_model, sc, le, pt):
        F = self.frequency.text()
        S = self.speed.text()
        D = self.dwt.text()
        T = self.comboBox.currentText()   
        L = self.length.text()
        if(F=='' or S=='' or D=='' or L=='' or T=='--Select--'):
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setWindowIcon(QtGui.QIcon('logo.png'))
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Enter Correct Details!")
            msg.setStyleSheet('color:black;')
            x = msg.exec_()
        else:
            types = ['Tanker', 'Cargo', 'Other', 'Tug', 'Container']
            type_index = types.index(T)
            types = le.fit_transform(types)
            T = types[type_index]
            arr = pt.transform([[D]])
            ans = new_model.predict(sc.transform([[F, S, arr[0][0], L, T]]))
            self.textBrowser.setText("Noise = %f dB" %ans)
            self.textBrowser.setAlignment(QtCore.Qt.AlignCenter)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "URN Prediction"))
        MainWindow.setWindowIcon(QtGui.QIcon('logo.png'))
        self.label.setText(_translate("MainWindow", "Enter Some of these Details for Getting Noise Prediction"))
        self.label_2.setText(_translate("MainWindow", "Frequency (in Hz)"))
        self.label_3.setText(_translate("MainWindow", "Ship Speed (in Knots)"))
        self.label_4.setText(_translate("MainWindow", "DWT (in t)"))
        self.label_5.setText(_translate("MainWindow", "Ship Type"))
        self.label_6.setText(_translate("MainWindow", "Ship Length (in m)"))
        self.pushButton.setText(_translate("MainWindow", "SUBMIT"))
        self.pushButton2.setText(_translate("MainWindow", "CLEAR"))
        self.label_7.setText(_translate("MainWindow", "Press Submit Button"))

        self.comboBox.setItemText(0, _translate("MainWindow", "--Select--"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Cargo"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Container"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Tanker"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Tug"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Other"))


stylesheet = """
    QMainWindow {
        background-image: url("image.jpg");
        background-repeat: no-repeat;
        background-position: center;
        opacity: 0;
    }
    QLabel{
        color:white;
    }
    QLineEdit{
        border-radius:4px;
    }
    QPushButton{
        border-radius:10px;
    }
"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
