# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'paymentWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PaymentManageWidget(object):
    def setupUi(self, PaymentManageWidget):
        if not PaymentManageWidget.objectName():
            PaymentManageWidget.setObjectName(u"PaymentManageWidget")
        PaymentManageWidget.resize(1142, 663)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PaymentManageWidget.sizePolicy().hasHeightForWidth())
        PaymentManageWidget.setSizePolicy(sizePolicy)
        PaymentManageWidget.setMinimumSize(QSize(770, 600))
        font = QFont()
        font.setFamily(u"JetBrains Mono")
        font.setPointSize(14)
        PaymentManageWidget.setFont(font)
        PaymentManageWidget.setStyleSheet(u"background-color: #2C2C2C;")
        self.verticalLayout = QVBoxLayout(PaymentManageWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.HeaderFrame = QFrame(PaymentManageWidget)
        self.HeaderFrame.setObjectName(u"HeaderFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(100)
        sizePolicy1.setHeightForWidth(self.HeaderFrame.sizePolicy().hasHeightForWidth())
        self.HeaderFrame.setSizePolicy(sizePolicy1)
        self.HeaderFrame.setMinimumSize(QSize(0, 0))
        self.HeaderFrame.setMaximumSize(QSize(16777215, 200))
        self.HeaderFrame.setFont(font)
        self.HeaderFrame.setFrameShape(QFrame.StyledPanel)
        self.HeaderFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.HeaderFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.LeftHeaderFrame = QFrame(self.HeaderFrame)
        self.LeftHeaderFrame.setObjectName(u"LeftHeaderFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.LeftHeaderFrame.sizePolicy().hasHeightForWidth())
        self.LeftHeaderFrame.setSizePolicy(sizePolicy2)
        self.LeftHeaderFrame.setMinimumSize(QSize(352, 0))
        self.LeftHeaderFrame.setStyleSheet(u"background-color: #1E1E1E;\n"
"border-radius: 10px")
        self.LeftHeaderFrame.setFrameShape(QFrame.StyledPanel)
        self.LeftHeaderFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.LeftHeaderFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.matchQPB = QPushButton(self.LeftHeaderFrame)
        self.matchQPB.setObjectName(u"matchQPB")
        self.matchQPB.setStyleSheet(u"background-color: #2C2C2C;\n"
"color: #FAFAFA;\n"
"border-radius: 10px;\n"
"padding: 10px 15px;")

        self.horizontalLayout_2.addWidget(self.matchQPB)

        self.betsQPB = QPushButton(self.LeftHeaderFrame)
        self.betsQPB.setObjectName(u"betsQPB")
        self.betsQPB.setStyleSheet(u"background-color: #2C2C2C;\n"
"color: #FAFAFA;\n"
"border-radius: 10px;\n"
"padding: 10px 15px;")

        self.horizontalLayout_2.addWidget(self.betsQPB)

        self.teamQPB = QPushButton(self.LeftHeaderFrame)
        self.teamQPB.setObjectName(u"teamQPB")
        self.teamQPB.setStyleSheet(u"background-color: #2C2C2C;\n"
"color: #FAFAFA;\n"
"border-radius: 10px;\n"
"padding: 10px 15px;\n"
"")

        self.horizontalLayout_2.addWidget(self.teamQPB)


        self.horizontalLayout.addWidget(self.LeftHeaderFrame)

        self.RightHeaderFrame = QFrame(self.HeaderFrame)
        self.RightHeaderFrame.setObjectName(u"RightHeaderFrame")
        sizePolicy2.setHeightForWidth(self.RightHeaderFrame.sizePolicy().hasHeightForWidth())
        self.RightHeaderFrame.setSizePolicy(sizePolicy2)
        self.RightHeaderFrame.setMinimumSize(QSize(352, 0))
        self.RightHeaderFrame.setStyleSheet(u"background-color: #1E1E1E;\n"
"border-radius: 10px")
        self.RightHeaderFrame.setFrameShape(QFrame.StyledPanel)
        self.RightHeaderFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.RightHeaderFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.logoutQPB = QPushButton(self.RightHeaderFrame)
        self.logoutQPB.setObjectName(u"logoutQPB")
        self.logoutQPB.setStyleSheet(u"background-color: #E62641;\n"
"color: #FAFAFA;\n"
"opacity: 50%;\n"
"border-radius: 10px;\n"
"padding: 10px 15px;\n"
"")

        self.verticalLayout_2.addWidget(self.logoutQPB)


        self.horizontalLayout.addWidget(self.RightHeaderFrame)


        self.verticalLayout.addWidget(self.HeaderFrame, 0, Qt.AlignTop)

        self.MainContentFrame = QFrame(PaymentManageWidget)
        self.MainContentFrame.setObjectName(u"MainContentFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.MainContentFrame.sizePolicy().hasHeightForWidth())
        self.MainContentFrame.setSizePolicy(sizePolicy3)
        self.MainContentFrame.setMinimumSize(QSize(16777214, 16777214))
        self.MainContentFrame.setFrameShape(QFrame.StyledPanel)
        self.MainContentFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.MainContentFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.LeftAside = QFrame(self.MainContentFrame)
        self.LeftAside.setObjectName(u"LeftAside")
        self.LeftAside.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.LeftAside.sizePolicy().hasHeightForWidth())
        self.LeftAside.setSizePolicy(sizePolicy4)
        self.LeftAside.setMinimumSize(QSize(180, 0))
        self.LeftAside.setStyleSheet(u"background-color: #1E1E1E;\n"
"border-radius: 10px")
        self.LeftAside.setFrameShape(QFrame.StyledPanel)
        self.LeftAside.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.LeftAside)

        self.RightAside = QFrame(self.MainContentFrame)
        self.RightAside.setObjectName(u"RightAside")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.RightAside.sizePolicy().hasHeightForWidth())
        self.RightAside.setSizePolicy(sizePolicy5)
        self.RightAside.setStyleSheet(u"background-color: #1E1E1E;\n"
"border-radius: 10px")
        self.RightAside.setFrameShape(QFrame.StyledPanel)
        self.RightAside.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.RightAside)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 20)
        self.TopBox = QFrame(self.RightAside)
        self.TopBox.setObjectName(u"TopBox")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.TopBox.sizePolicy().hasHeightForWidth())
        self.TopBox.setSizePolicy(sizePolicy6)
        self.TopBox.setMaximumSize(QSize(16777215, 120))
        self.TopBox.setAutoFillBackground(False)
        self.TopBox.setStyleSheet(u"background-color: #2C2C2C;\n"
"border-radius: 10px")
        self.TopBox.setFrameShape(QFrame.StyledPanel)
        self.TopBox.setFrameShadow(QFrame.Raised)
        self.ExpensesBox = QFrame(self.TopBox)
        self.ExpensesBox.setObjectName(u"ExpensesBox")
        self.ExpensesBox.setGeometry(QRect(4194101, 34, 150, 50))
        self.ExpensesBox.setMaximumSize(QSize(150, 50))
        self.ExpensesBox.setBaseSize(QSize(150, 50))
        self.ExpensesBox.setStyleSheet(u"background-color: #1E1E1E;\n"
"border-radius: 10px")
        self.ExpensesBox.setFrameShape(QFrame.StyledPanel)
        self.ExpensesBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.ExpensesBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.expenses_Lbl = QLabel(self.ExpensesBox)
        self.expenses_Lbl.setObjectName(u"expenses_Lbl")
        self.expenses_Lbl.setFont(font)
        self.expenses_Lbl.setStyleSheet(u"color: #fafafa;\n"
"text-align:center;")

        self.verticalLayout_4.addWidget(self.expenses_Lbl)

        self.expensesAmount_Lbl = QLabel(self.ExpensesBox)
        self.expensesAmount_Lbl.setObjectName(u"expensesAmount_Lbl")
        self.expensesAmount_Lbl.setStyleSheet(u"color: #E62641;\n"
"font: 18pt \"JetBrains Mono\";")

        self.verticalLayout_4.addWidget(self.expensesAmount_Lbl)

        self.betsQtyBox = QFrame(self.TopBox)
        self.betsQtyBox.setObjectName(u"betsQtyBox")
        self.betsQtyBox.setGeometry(QRect(8388363, 34, 200, 50))
        self.betsQtyBox.setMaximumSize(QSize(200, 50))
        self.betsQtyBox.setBaseSize(QSize(200, 50))
        self.betsQtyBox.setStyleSheet(u"background-color: #1E1E1E;\n"
"border-radius: 10px")
        self.betsQtyBox.setFrameShape(QFrame.StyledPanel)
        self.betsQtyBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.betsQtyBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.betsAmountQty_Lbl = QLabel(self.betsQtyBox)
        self.betsAmountQty_Lbl.setObjectName(u"betsAmountQty_Lbl")
        self.betsAmountQty_Lbl.setFont(font)
        self.betsAmountQty_Lbl.setStyleSheet(u"color: #fafafa;\n"
"text-align:center;")

        self.verticalLayout_5.addWidget(self.betsAmountQty_Lbl)

        self.betQtyAmount_Lbl = QLabel(self.betsQtyBox)
        self.betQtyAmount_Lbl.setObjectName(u"betQtyAmount_Lbl")
        self.betQtyAmount_Lbl.setStyleSheet(u"color: #E62641;\n"
"font: 18pt \"JetBrains Mono\";")

        self.verticalLayout_5.addWidget(self.betQtyAmount_Lbl)

        self.IncomeBox = QFrame(self.TopBox)
        self.IncomeBox.setObjectName(u"IncomeBox")
        self.IncomeBox.setGeometry(QRect(12582675, 22, 100, 75))
        self.IncomeBox.setMaximumSize(QSize(200, 100))
        self.IncomeBox.setBaseSize(QSize(200, 50))
        self.IncomeBox.setStyleSheet(u"background-color: #1E1E1E;\n"
"border-radius: 10px")
        self.IncomeBox.setFrameShape(QFrame.StyledPanel)
        self.IncomeBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.IncomeBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.incomeLbl = QLabel(self.IncomeBox)
        self.incomeLbl.setObjectName(u"incomeLbl")
        self.incomeLbl.setFont(font)
        self.incomeLbl.setStyleSheet(u"color: #fafafa;\n"
"text-align:center;")

        self.verticalLayout_3.addWidget(self.incomeLbl)

        self.label = QLabel(self.IncomeBox)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: #E62641;\n"
"font: 18pt \"JetBrains Mono\";")

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout_7.addWidget(self.TopBox)

        self.BottomBox = QFrame(self.RightAside)
        self.BottomBox.setObjectName(u"BottomBox")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.BottomBox.sizePolicy().hasHeightForWidth())
        self.BottomBox.setSizePolicy(sizePolicy7)
        self.BottomBox.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(14)
        self.BottomBox.setFont(font1)
        self.BottomBox.setStyleSheet(u"background-color: #2C2C2C;\n"
"border-radius: 10px;\n"
"")
        self.BottomBox.setFrameShape(QFrame.StyledPanel)
        self.BottomBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.BottomBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tabPayment_QTW = QTableWidget(self.BottomBox)
        if (self.tabPayment_QTW.columnCount() < 4):
            self.tabPayment_QTW.setColumnCount(4)
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font2);
        self.tabPayment_QTW.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font2);
        self.tabPayment_QTW.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font2);
        self.tabPayment_QTW.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font2);
        self.tabPayment_QTW.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tabPayment_QTW.rowCount() < 4):
            self.tabPayment_QTW.setRowCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabPayment_QTW.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabPayment_QTW.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabPayment_QTW.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabPayment_QTW.setVerticalHeaderItem(3, __qtablewidgetitem7)
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.NoBrush)
        brush1 = QBrush(QColor(232, 232, 233, 255))
        brush1.setStyle(Qt.NoBrush)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setBackground(brush1);
        __qtablewidgetitem8.setForeground(brush);
        self.tabPayment_QTW.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabPayment_QTW.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabPayment_QTW.setItem(0, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabPayment_QTW.setItem(0, 3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabPayment_QTW.setItem(1, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabPayment_QTW.setItem(1, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabPayment_QTW.setItem(1, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabPayment_QTW.setItem(1, 3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabPayment_QTW.setItem(2, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tabPayment_QTW.setItem(2, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tabPayment_QTW.setItem(2, 2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tabPayment_QTW.setItem(2, 3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tabPayment_QTW.setItem(3, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tabPayment_QTW.setItem(3, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tabPayment_QTW.setItem(3, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tabPayment_QTW.setItem(3, 3, __qtablewidgetitem23)
        self.tabPayment_QTW.setObjectName(u"tabPayment_QTW")
        sizePolicy4.setHeightForWidth(self.tabPayment_QTW.sizePolicy().hasHeightForWidth())
        self.tabPayment_QTW.setSizePolicy(sizePolicy4)
        self.tabPayment_QTW.setStyleSheet(u"")
        self.tabPayment_QTW.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tabPayment_QTW.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tabPayment_QTW.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tabPayment_QTW.setShowGrid(True)
        self.tabPayment_QTW.setSortingEnabled(True)
        self.tabPayment_QTW.setWordWrap(True)
        self.tabPayment_QTW.setRowCount(4)
        self.tabPayment_QTW.horizontalHeader().setVisible(True)
        self.tabPayment_QTW.horizontalHeader().setCascadingSectionResizes(True)
        self.tabPayment_QTW.horizontalHeader().setMinimumSectionSize(23)
        self.tabPayment_QTW.horizontalHeader().setDefaultSectionSize(200)
        self.tabPayment_QTW.horizontalHeader().setHighlightSections(True)
        self.tabPayment_QTW.horizontalHeader().setProperty("showSortIndicator", True)
        self.tabPayment_QTW.horizontalHeader().setStretchLastSection(False)
        self.tabPayment_QTW.verticalHeader().setHighlightSections(True)
        self.tabPayment_QTW.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_6.addWidget(self.tabPayment_QTW)


        self.verticalLayout_7.addWidget(self.BottomBox)


        self.horizontalLayout_3.addWidget(self.RightAside)


        self.verticalLayout.addWidget(self.MainContentFrame)


        self.retranslateUi(PaymentManageWidget)

        QMetaObject.connectSlotsByName(PaymentManageWidget)
    # setupUi

    def retranslateUi(self, PaymentManageWidget):
        PaymentManageWidget.setWindowTitle(QCoreApplication.translate("PaymentManageWidget", u"Form", None))
        self.matchQPB.setText(QCoreApplication.translate("PaymentManageWidget", u"Matchs", None))
        self.betsQPB.setText(QCoreApplication.translate("PaymentManageWidget", u"Pariages", None))
        self.teamQPB.setText(QCoreApplication.translate("PaymentManageWidget", u"Equipes", None))
        self.logoutQPB.setText(QCoreApplication.translate("PaymentManageWidget", u"Logout", None))
        self.RightAside.setProperty("border-radius", "")
        self.expenses_Lbl.setText(QCoreApplication.translate("PaymentManageWidget", u"Revenu", None))
        self.expensesAmount_Lbl.setText(QCoreApplication.translate("PaymentManageWidget", u"500 HTG", None))
        self.betsAmountQty_Lbl.setText(QCoreApplication.translate("PaymentManageWidget", u"Revenu", None))
        self.betQtyAmount_Lbl.setText(QCoreApplication.translate("PaymentManageWidget", u"500 HTG", None))
        self.incomeLbl.setText(QCoreApplication.translate("PaymentManageWidget", u"Revenu", None))
        self.label.setText(QCoreApplication.translate("PaymentManageWidget", u"500 HTG", None))
        ___qtablewidgetitem = self.tabPayment_QTW.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PaymentManageWidget", u"ID", None));
        ___qtablewidgetitem1 = self.tabPayment_QTW.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PaymentManageWidget", u"ID PARIAGE", None));
        ___qtablewidgetitem2 = self.tabPayment_QTW.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PaymentManageWidget", u"DATE", None));
        ___qtablewidgetitem3 = self.tabPayment_QTW.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PaymentManageWidget", u"MONTANT", None));
        ___qtablewidgetitem4 = self.tabPayment_QTW.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PaymentManageWidget", u"1", None));
        ___qtablewidgetitem5 = self.tabPayment_QTW.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PaymentManageWidget", u"2", None));
        ___qtablewidgetitem6 = self.tabPayment_QTW.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("PaymentManageWidget", u"3", None));
        ___qtablewidgetitem7 = self.tabPayment_QTW.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("PaymentManageWidget", u"4", None));

        __sortingEnabled = self.tabPayment_QTW.isSortingEnabled()
        self.tabPayment_QTW.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.tabPayment_QTW.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("PaymentManageWidget", u"33", None));
        ___qtablewidgetitem9 = self.tabPayment_QTW.item(0, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("PaymentManageWidget", u"72983", None));
        ___qtablewidgetitem10 = self.tabPayment_QTW.item(0, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("PaymentManageWidget", u"21/10/2022", None));
        ___qtablewidgetitem11 = self.tabPayment_QTW.item(0, 3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("PaymentManageWidget", u"450 HTG", None));
        ___qtablewidgetitem12 = self.tabPayment_QTW.item(1, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("PaymentManageWidget", u"34", None));
        ___qtablewidgetitem13 = self.tabPayment_QTW.item(1, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("PaymentManageWidget", u"47238", None));
        ___qtablewidgetitem14 = self.tabPayment_QTW.item(1, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("PaymentManageWidget", u"17/12/2022", None));
        ___qtablewidgetitem15 = self.tabPayment_QTW.item(1, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("PaymentManageWidget", u"823 HTG", None));
        ___qtablewidgetitem16 = self.tabPayment_QTW.item(2, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("PaymentManageWidget", u"42", None));
        ___qtablewidgetitem17 = self.tabPayment_QTW.item(2, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("PaymentManageWidget", u"37238", None));
        ___qtablewidgetitem18 = self.tabPayment_QTW.item(2, 2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("PaymentManageWidget", u"21/01/2023", None));
        ___qtablewidgetitem19 = self.tabPayment_QTW.item(2, 3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("PaymentManageWidget", u"732 HTG", None));
        ___qtablewidgetitem20 = self.tabPayment_QTW.item(3, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("PaymentManageWidget", u"32", None));
        ___qtablewidgetitem21 = self.tabPayment_QTW.item(3, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("PaymentManageWidget", u"82354", None));
        ___qtablewidgetitem22 = self.tabPayment_QTW.item(3, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("PaymentManageWidget", u"15/05/2022", None));
        ___qtablewidgetitem23 = self.tabPayment_QTW.item(3, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("PaymentManageWidget", u"50 HTG", None));
        self.tabPayment_QTW.setSortingEnabled(__sortingEnabled)

    # retranslateUi

