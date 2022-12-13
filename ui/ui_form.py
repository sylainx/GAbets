# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formVNdkYQ.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        if LoginForm.objectName():
            LoginForm.setObjectName(u"LoginForm")
        LoginForm.resize(400, 417)
        self.LoginFm = QFrame(LoginForm)
        self.LoginFm.setObjectName(u"LoginFm")
        self.LoginFm.setGeometry(QRect(-1, -1, 401, 381))
        self.LoginFm.setFrameShape(QFrame.StyledPanel)
        self.LoginFm.setFrameShadow(QFrame.Raised)
        self.formLayoutWidget = QWidget(self.LoginFm)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(60, 30, 281, 341))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.usernameLabel = QLabel(self.formLayoutWidget)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.usernameLabel)

        self.usernameLineEdit = QLineEdit(self.formLayoutWidget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.usernameLineEdit)

        self.firstnameLabel = QLabel(self.formLayoutWidget)
        self.firstnameLabel.setObjectName(u"firstnameLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.firstnameLabel)

        self.firstnameLineEdit = QLineEdit(self.formLayoutWidget)
        self.firstnameLineEdit.setObjectName(u"firstnameLineEdit")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.firstnameLineEdit)

        self.lastnameLabel = QLabel(self.formLayoutWidget)
        self.lastnameLabel.setObjectName(u"lastnameLabel")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lastnameLabel)

        self.lastnameLineEdit = QLineEdit(self.formLayoutWidget)
        self.lastnameLineEdit.setObjectName(u"lastnameLineEdit")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lastnameLineEdit)

        self.emailLabel = QLabel(self.formLayoutWidget)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.emailLabel)

        self.emailLineEdit = QLineEdit(self.formLayoutWidget)
        self.emailLineEdit.setObjectName(u"emailLineEdit")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.emailLineEdit)

        self.sexeLabel = QLabel(self.formLayoutWidget)
        self.sexeLabel.setObjectName(u"sexeLabel")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.sexeLabel)

        self.sexeComboBox = QComboBox(self.formLayoutWidget)
        self.sexeComboBox.addItem("")
        self.sexeComboBox.addItem("")
        self.sexeComboBox.setObjectName(u"sexeComboBox")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.sexeComboBox)

        self.dateNaissanceLabel = QLabel(self.formLayoutWidget)
        self.dateNaissanceLabel.setObjectName(u"dateNaissanceLabel")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.dateNaissanceLabel)

        self.dateNaissanceDateEdit = QDateEdit(self.formLayoutWidget)
        self.dateNaissanceDateEdit.setObjectName(u"dateNaissanceDateEdit")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.dateNaissanceDateEdit)

        self.telLabel = QLabel(self.formLayoutWidget)
        self.telLabel.setObjectName(u"telLabel")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.telLabel)

        self.telLineEdit = QLineEdit(self.formLayoutWidget)
        self.telLineEdit.setObjectName(u"telLineEdit")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.telLineEdit)

        self.addressLabel = QLabel(self.formLayoutWidget)
        self.addressLabel.setObjectName(u"addressLabel")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.addressLabel)

        self.addressLineEdit = QLineEdit(self.formLayoutWidget)
        self.addressLineEdit.setObjectName(u"addressLineEdit")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.addressLineEdit)

        self.nifLabel = QLabel(self.formLayoutWidget)
        self.nifLabel.setObjectName(u"nifLabel")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.nifLabel)

        self.nifLineEdit = QLineEdit(self.formLayoutWidget)
        self.nifLineEdit.setObjectName(u"nifLineEdit")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.nifLineEdit)

        self.passwordLabel = QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.passwordLabel)

        self.passwordLineEdit = QLineEdit(self.formLayoutWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.passwordLineEdit)

        self.confirmPasswordLabel = QLabel(self.formLayoutWidget)
        self.confirmPasswordLabel.setObjectName(u"confirmPasswordLabel")

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.confirmPasswordLabel)

        self.confirmPasswordLineEdit = QLineEdit(self.formLayoutWidget)
        self.confirmPasswordLineEdit.setObjectName(u"confirmPasswordLineEdit")

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.confirmPasswordLineEdit)

        self.pushButton = QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout_2.setWidget(11, QFormLayout.FieldRole, self.pushButton)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(12, QFormLayout.LabelRole, self.label)

        self.frame_2 = QFrame(self.LoginFm)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 10, 120, 80))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton_2 = QPushButton(LoginForm)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(110, 380, 161, 41))
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font-size: 20px;")

        self.retranslateUi(LoginForm)

        QMetaObject.connectSlotsByName(LoginForm)
    # setupUi

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"Form", None))
        self.usernameLabel.setText(QCoreApplication.translate("LoginForm", u"username", None))
        self.firstnameLabel.setText(QCoreApplication.translate("LoginForm", u"First name", None))
        self.lastnameLabel.setText(QCoreApplication.translate("LoginForm", u"Last name", None))
        self.emailLabel.setText(QCoreApplication.translate("LoginForm", u"email", None))
        self.sexeLabel.setText(QCoreApplication.translate("LoginForm", u"sexe", None))
        self.sexeComboBox.setItemText(0, QCoreApplication.translate("LoginForm", u"Masculin", None))
        self.sexeComboBox.setItemText(1, QCoreApplication.translate("LoginForm", u"F\u00e9minin", None))

        self.dateNaissanceLabel.setText(QCoreApplication.translate("LoginForm", u"Date Naissance", None))
        self.telLabel.setText(QCoreApplication.translate("LoginForm", u"Telephone", None))
        self.addressLabel.setText(QCoreApplication.translate("LoginForm", u"Address", None))
        self.nifLabel.setText(QCoreApplication.translate("LoginForm", u"nif", None))
        self.passwordLabel.setText(QCoreApplication.translate("LoginForm", u"password", None))
        self.confirmPasswordLabel.setText(QCoreApplication.translate("LoginForm", u"Confirm password", None))
        self.pushButton.setText(QCoreApplication.translate("LoginForm", u"Enregistrer", None))
        self.label.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("LoginForm", u"Login", None))
    # retranslateUi

