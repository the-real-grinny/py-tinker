# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'countCalculator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.checkBox = QtWidgets.QCheckBox(dialog)
        self.checkBox.setGeometry(QtCore.QRect(10, 37, 81, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 60, 81, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 80, 81, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(dialog)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 100, 91, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.textEdit = QtWidgets.QTextEdit(dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 140, 31, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 190, 31, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(50, 140, 16, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 190, 16, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(dialog)
        self.buttonBox.accepted.connect(dialog.accept)
        self.buttonBox.rejected.connect(dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Dialog"))
        self.checkBox.setText(_translate("dialog", "Permutation"))
        self.checkBox_2.setText(_translate("dialog", "Combination"))
        self.checkBox_3.setText(_translate("dialog", "Repeats?"))
        self.checkBox_4.setText(_translate("dialog", "No Repeats?"))
        self.label.setText(_translate("dialog", "n"))
        self.label_2.setText(_translate("dialog", "r"))

