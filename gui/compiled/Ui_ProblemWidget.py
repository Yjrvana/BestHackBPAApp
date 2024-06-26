# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProblemWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProblemWidget(object):
    def setupUi(self, CardWidget):
        CardWidget.setObjectName("CardWidget")
        CardWidget.resize(707, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CardWidget.sizePolicy().hasHeightForWidth())
        CardWidget.setSizePolicy(sizePolicy)
        CardWidget.setMinimumSize(QtCore.QSize(200, 350))
        CardWidget.setStyleSheet("QWidget#DeckWidget {\n"
"    background-color: rgb(210, 210, 210);\n"
"}")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(CardWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.deletePushButton = QtWidgets.QPushButton(CardWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deletePushButton.sizePolicy().hasHeightForWidth())
        self.deletePushButton.setSizePolicy(sizePolicy)
        self.deletePushButton.setMinimumSize(QtCore.QSize(0, 60))
        self.deletePushButton.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.deletePushButton.setFont(font)
        self.deletePushButton.setStyleSheet("QPushButton#deletePushButton {\n"
"    border-radius: 0 px;\n"
"    background-color: rgb(210, 210, 210);\n"
"}\n"
"\n"
"QPushButton#deletePushButton:pressed {\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QPushButton#deletePushButton:hover {\n"
"    background-color: rgb(200, 200, 200);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deletePushButton.setIcon(icon)
        self.deletePushButton.setIconSize(QtCore.QSize(30, 30))
        self.deletePushButton.setObjectName("deletePushButton")
        self.horizontalLayout_4.addWidget(self.deletePushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(CardWidget)
        QtCore.QMetaObject.connectSlotsByName(CardWidget)

    def retranslateUi(self, CardWidget):
        _translate = QtCore.QCoreApplication.translate
        CardWidget.setWindowTitle(_translate("CardWidget", "Form"))
        self.deletePushButton.setText(_translate("CardWidget", "Принять задачу"))
