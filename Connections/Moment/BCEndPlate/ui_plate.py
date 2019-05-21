# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_plate.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Plate(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(287, 179)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.plateHeight = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.plateHeight.setFont(font)
        self.plateHeight.setObjectName("plateHeight")
        self.gridLayout.addWidget(self.plateHeight, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.txt_plateHeight = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_plateHeight.setFont(font)
        self.txt_plateHeight.setReadOnly(True)
        self.txt_plateHeight.setObjectName("txt_plateHeight")
        self.gridLayout.addWidget(self.txt_plateHeight, 0, 1, 1, 1)
        self.txt_plateDemand = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_plateDemand.setFont(font)
        self.txt_plateDemand.setReadOnly(True)
        self.txt_plateDemand.setObjectName("txt_plateDemand")
        self.gridLayout.addWidget(self.txt_plateDemand, 2, 1, 1, 1)
        self.txt_plateWidth = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_plateWidth.setFont(font)
        self.txt_plateWidth.setReadOnly(True)
        self.txt_plateWidth.setObjectName("txt_plateWidth")
        self.gridLayout.addWidget(self.txt_plateWidth, 1, 1, 1, 1)
        self.label_163 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_163.setFont(font)
        self.label_163.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_163.setObjectName("label_163")
        self.gridLayout.addWidget(self.label_163, 2, 0, 1, 1)
        self.txt_plateCapacity = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_plateCapacity.setFont(font)
        self.txt_plateCapacity.setReadOnly(True)
        self.txt_plateCapacity.setObjectName("txt_plateCapacity")
        self.gridLayout.addWidget(self.txt_plateCapacity, 3, 1, 1, 1)
        self.label_164 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_164.setFont(font)
        self.label_164.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_164.setObjectName("label_164")
        self.gridLayout.addWidget(self.label_164, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Plate"))
        self.plateHeight.setText(_translate("Dialog", "Height (mm)"))
        self.label_2.setText(_translate("Dialog", "Width (mm)"))
        self.label_163.setText(_translate("Dialog", "<html><head/><body><p>Moment demand (kNm)</p></body></html>"))
        self.label_164.setText(_translate("Dialog", "<html><head/><body><p>Moment capacity (kNm)</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Plate()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

