from PyQt5 import QtCore, QtGui, QtWidgets

from Helpers.Helpers import Helpers


class Ui_DashboardView(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("mainWindow")
        MainWindow.setWindowTitle("AG BETS SPORTS")
        MainWindow.resize(1135, 600)
        MainWindow.setStyleSheet("#title{\n"
                                 "    font-size: 18px;\n"
                                 "    font-weight:bold;\n"
                                 "    margin-top:10px;\n"
                                 "}\n"
                                 "\n"
                                 "QLabel{\n"
                                 "    font: 22pt \"JetBrains Mono\";\n"
                                 "    color: rgb(255, 255, 255);\n"
                                 "    margin-top:20px;    \n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit{\n"
                                 "    height: 35px;\n"
                                 "    font-weight: bold;\n"
                                 "    margin-top:10px;\n"
                                 "    padding: 5px 15px;\n"
                                 "    border: 2px solid gray;\n"
                                 "}\n"
                                 "QLineEdit:focus{\n"
                                 "    border:1px solid green;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox{\n"
                                 "    font: 14pt \"JetBrains Mono\";\n"
                                 "    color: rgb(255, 255, 255);\n"
                                 "\n"
                                 "}\n"
                                 "#loginbtn{\n"
                                 "    margin-top:15px;\n"
                                 "    height:50px;\n"
                                 "    width:100px;\n"
                                 "    color:white;\n"
                                 "    background-color:green;\n"
                                 "    border-radius:15px;\n"
                                 "    font-size:18px;\n"
                                 "}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainContentFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainContentFrame.setGeometry(
            QtCore.QRect(0, 96, 16777214, 16777214))

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(
            self.MainContentFrame.sizePolicy().hasHeightForWidth())
        self.MainContentFrame.setSizePolicy(sizePolicy)
        self.MainContentFrame.setMinimumSize(QtCore.QSize(16777214, 16777214))
        self.MainContentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainContentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainContentFrame.setObjectName("MainContentFrame")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.MainContentFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # Left aside
        self.LeftAside = QtWidgets.QFrame(self.MainContentFrame)
        self.LeftAside.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.LeftAside.sizePolicy().hasHeightForWidth())
        
        self.LeftAside.setSizePolicy(sizePolicy)
        self.LeftAside.setMinimumSize(QtCore.QSize(180, 0))
        self.LeftAside.setStyleSheet("background-color: #1E1E1E;\n"
                                     "border-radius: 10px")
        self.LeftAside.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LeftAside.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LeftAside.setObjectName("LeftAside")

        
        # datas will be load here
        

        self.horizontalLayout_3.addWidget(self.LeftAside)
        # end left aside


        # TODO: FUNCTION RIGHT ASIDE
        self.rightAsideFrameFunc()

        # TABLE: PAYMENTS HISTORY
        # self.verticalLayout_6.addWidget(self.tabPayment_QTW)

        self.verticalLayout_7.addWidget(self.BottomBox)

        self.horizontalLayout_3.addWidget(self.RightAside)

        # TODO: FUCNTION TO CALL HEADER
        self.headerContentFunc(MainWindow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1135, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def headerContentFunc(self, MainWindow):

        # start HEADERLAYOUT

        self.HeaderFrame = QtWidgets.QFrame(self.centralwidget)
        self.HeaderFrame.setGeometry(QtCore.QRect(0, 0, 1131, 86))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(
            self.HeaderFrame.sizePolicy().hasHeightForWidth())
        self.HeaderFrame.setSizePolicy(sizePolicy)
        self.HeaderFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.HeaderFrame.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(14)
        self.HeaderFrame.setFont(font)
        self.HeaderFrame.setStyleSheet("")
        self.HeaderFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HeaderFrame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.HeaderFrame.setObjectName("HeaderFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.HeaderFrame)
        self.horizontalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LeftHeaderFrame = QtWidgets.QFrame(self.HeaderFrame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.LeftHeaderFrame.sizePolicy().hasHeightForWidth())
        self.LeftHeaderFrame.setSizePolicy(sizePolicy)
        self.LeftHeaderFrame.setMinimumSize(QtCore.QSize(352, 0))
        self.LeftHeaderFrame.setStyleSheet("background-color: #1E1E1E;\n"
                                           "border-radius: 10px")
        self.LeftHeaderFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LeftHeaderFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LeftHeaderFrame.setObjectName("LeftHeaderFrame")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(
            self.LeftHeaderFrame)

        # match button
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.matchQPB = QtWidgets.QPushButton(self.LeftHeaderFrame)
        self.matchQPB.setStyleSheet("background-color: #2C2C2C;\n"
                                    "color: #FAFAFA;\n"
                                    "border-radius: 10px;\n"
                                    "padding: 10px 15px;")
        self.matchQPB.setObjectName("matchQPB")
        self.horizontalLayout_2.addWidget(self.matchQPB)
        self.matchQPB.clicked.connect(lambda: self.printHello())
        

        # end Match BTN

        # start Bet BTN
        self.betsQPBtn = QtWidgets.QPushButton(self.LeftHeaderFrame)
        self.betsQPBtn.setStyleSheet("background-color: #2C2C2C;\n"
                                     "color: #FAFAFA;\n"
                                     "border-radius: 10px;\n"
                                     "padding: 10px 15px;")
        self.betsQPBtn.setObjectName("betsQPB")
        self.horizontalLayout_2.addWidget(self.betsQPBtn)
        self.betsQPBtn.clicked.connect(lambda: self.printBet())
        

        # END match bets BTN

        # start team BTN
        self.teamQPB = QtWidgets.QPushButton(self.LeftHeaderFrame)
        self.teamQPB.setStyleSheet("background-color: #2C2C2C;\n"
                                   "color: #FAFAFA;\n"
                                   "border-radius: 10px;\n"
                                   "padding: 10px 15px;\n"
                                   "")
        self.teamQPB.setObjectName("teamQPB")
        self.teamQPB.clicked.connect(lambda: self.printTest())
       
        self.horizontalLayout_2.addWidget(self.teamQPB)
        # end team BTN

        self.horizontalLayout.addWidget(self.LeftHeaderFrame)

        # TODO: Right Header

        self.RightHeaderFrame = QtWidgets.QFrame(self.HeaderFrame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.RightHeaderFrame.sizePolicy().hasHeightForWidth())
        self.RightHeaderFrame.setSizePolicy(sizePolicy)
        self.RightHeaderFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.RightHeaderFrame.setStyleSheet("border: none;\n"
                                            "background-color: none;")
        self.RightHeaderFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RightHeaderFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RightHeaderFrame.setObjectName("RightHeaderFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.RightHeaderFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logoutQPB = QtWidgets.QPushButton(self.RightHeaderFrame)
        self.logoutQPB.setMaximumSize(QtCore.QSize(200, 16777215))
        self.logoutQPB.setStyleSheet("background-color: #E62641;\n"
                                     "color: #FAFAFA;\n"
                                     "opacity: 50%;\n"
                                     "border-radius: 10px;\n"
                                     "padding: 10px 15px;\n"
                                     "")
        self.logoutQPB.setObjectName("logoutQPB")
        self.verticalLayout_2.addWidget(self.logoutQPB)
        # self.verticalLayout_2.addWidget("Logout")
        self.horizontalLayout.addWidget(self.RightHeaderFrame)
        self.retranslateUi(MainWindow)



    def rightAsideFrameFunc(self):

        #  FRAME: START RIGHT ASIDE
        self.RightAside = QtWidgets.QFrame(self.MainContentFrame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.RightAside.sizePolicy().hasHeightForWidth())
        self.RightAside.setSizePolicy(sizePolicy)
        self.RightAside.setStyleSheet("background-color: #1E1E1E;\n"
                                      "border-radius: 10px")
        self.RightAside.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RightAside.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RightAside.setProperty("border-radius", "")
        self.RightAside.setObjectName("RightAside")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.RightAside)

        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 20)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.TopBox = QtWidgets.QFrame(self.RightAside)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.TopBox.sizePolicy().hasHeightForWidth())
        self.TopBox.setSizePolicy(sizePolicy)
        self.TopBox.setMaximumSize(QtCore.QSize(16777215, 120))
        self.TopBox.setAutoFillBackground(False)
        self.TopBox.setStyleSheet("background-color: #2C2C2C;\n"
                                  "border-radius: 10px")
        self.TopBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TopBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TopBox.setObjectName("TopBox")
        self.ExpensesBox = QtWidgets.QFrame(self.TopBox)
        self.ExpensesBox.setGeometry(QtCore.QRect(4194101, 34, 150, 50))
        self.ExpensesBox.setMaximumSize(QtCore.QSize(150, 50))
        self.ExpensesBox.setBaseSize(QtCore.QSize(150, 50))
        self.ExpensesBox.setStyleSheet("background-color: #1E1E1E;\n"
                                       "border-radius: 10px")
        self.ExpensesBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ExpensesBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ExpensesBox.setObjectName("ExpensesBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.ExpensesBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.expenses_Lbl = QtWidgets.QLabel(self.ExpensesBox)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(14)
        self.expenses_Lbl.setFont(font)
        self.expenses_Lbl.setStyleSheet("color: #fafafa;\n"
                                        "text-align:center;")
        self.expenses_Lbl.setObjectName("expenses_Lbl")
        self.verticalLayout_4.addWidget(self.expenses_Lbl)
        self.expensesAmount_Lbl = QtWidgets.QLabel(self.ExpensesBox)
        self.expensesAmount_Lbl.setStyleSheet("color: #E62641;\n"
                                              "font: 18pt \"JetBrains Mono\";")
        self.expensesAmount_Lbl.setObjectName("expensesAmount_Lbl")
        self.verticalLayout_4.addWidget(self.expensesAmount_Lbl)
        self.betsQtyBox = QtWidgets.QFrame(self.TopBox)
        self.betsQtyBox.setGeometry(QtCore.QRect(8388363, 34, 200, 50))
        self.betsQtyBox.setMaximumSize(QtCore.QSize(200, 50))
        self.betsQtyBox.setBaseSize(QtCore.QSize(200, 50))
        self.betsQtyBox.setStyleSheet("background-color: #1E1E1E;\n"
                                      "border-radius: 10px")
        self.betsQtyBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.betsQtyBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.betsQtyBox.setObjectName("betsQtyBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.betsQtyBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.betsAmountQty_Lbl = QtWidgets.QLabel(self.betsQtyBox)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(14)
        self.betsAmountQty_Lbl.setFont(font)
        self.betsAmountQty_Lbl.setStyleSheet("color: #fafafa;\n"
                                             "text-align:center;")
        self.betsAmountQty_Lbl.setObjectName("betsAmountQty_Lbl")
        self.verticalLayout_5.addWidget(self.betsAmountQty_Lbl)
        self.betQtyAmount_Lbl = QtWidgets.QLabel(self.betsQtyBox)
        self.betQtyAmount_Lbl.setStyleSheet("color: #E62641;\n"
                                            "font: 18pt \"JetBrains Mono\";")
        self.betQtyAmount_Lbl.setObjectName("betQtyAmount_Lbl")
        self.verticalLayout_5.addWidget(self.betQtyAmount_Lbl)
        self.IncomeBox = QtWidgets.QFrame(self.TopBox)
        self.IncomeBox.setGeometry(QtCore.QRect(12582675, 22, 100, 75))
        self.IncomeBox.setMaximumSize(QtCore.QSize(200, 100))
        self.IncomeBox.setBaseSize(QtCore.QSize(200, 50))
        self.IncomeBox.setStyleSheet("background-color: #1E1E1E;\n"
                                     "border-radius: 10px")
        self.IncomeBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.IncomeBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.IncomeBox.setObjectName("IncomeBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.IncomeBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.incomeLbl = QtWidgets.QLabel(self.IncomeBox)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(14)
        self.incomeLbl.setFont(font)
        self.incomeLbl.setStyleSheet("color: #fafafa;\n"
                                     "text-align:center;")
        self.incomeLbl.setObjectName("incomeLbl")
        self.verticalLayout_3.addWidget(self.incomeLbl)
        self.label = QtWidgets.QLabel(self.IncomeBox)
        self.label.setStyleSheet("color: #E62641;\n"
                                 "font: 18pt \"JetBrains Mono\";")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_7.addWidget(self.TopBox)
        self.BottomBox = QtWidgets.QFrame(self.RightAside)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.BottomBox.sizePolicy().hasHeightForWidth())
        self.BottomBox.setSizePolicy(sizePolicy)
        self.BottomBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BottomBox.setFont(font)
        self.BottomBox.setStyleSheet("background-color: #2C2C2C;\n"
                                     "border-radius: 10px;\n"
                                     "")
        self.BottomBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BottomBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BottomBox.setObjectName("BottomBox")

        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.BottomBox)

        self.verticalLayout_6.setObjectName("verticalLayout_6")
        # END FRAME: RIGHT ASIDE



    def printTest(self):
        print("match is clicked")
        # exit()

    def printHello(self):
        print("teams is clicked")
        # exit()

    def printBet(self):
        print("Bet sport")
        # exit()

    def showLeftAside(self,MainWindow,match_type)->None:

        self.verticalLayout = QtWidgets.QVBoxLayout(self.LeftAside)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bottomAsideLFrame = QtWidgets.QFrame(self.LeftAside)
        self.bottomAsideLFrame.setStyleSheet("background-color: #E62641;\n"
        "color: #FAFAFA;\n"
        "opacity: 50%;\n"
        "border-radius: 10px;")
        self.bottomAsideLFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottomAsideLFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottomAsideLFrame.setObjectName("bottomAsideLFrame")

        self.title = QtWidgets.QLabel(self.bottomAsideLFrame)
        self.title.setGeometry(QtCore.QRect(30, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")

        self.typeMatchs_WDG = QtWidgets.QFrame(self.bottomAsideLFrame)
        self.typeMatchs_WDG.setGeometry(QtCore.QRect(0, 50, 161, 381))
        self.typeMatchs_WDG.setObjectName("typeMatchs_WDG")

        # Création du groupe de boutons radio
        self.match_type_grpe = QtWidgets.QButtonGroup(self.typeMatchs_WDG)
        
        # Création du layout vertical
        self.layout_CHB = QtWidgets.QVBoxLayout(self.typeMatchs_WDG)
        
        # Remplissage du layout avec les données
        for type_row in match_type:
            id_, name, prio, visibility = type_row

            self.chb_radio = QtWidgets.QRadioButton()
            self.chb_radio.setText(f"{name}")
            font = QtGui.QFont()
            font.setFamily("JetBrains Mono")
            font.setPointSize(14)
            font.setWeight(50)
            self.chb_radio.setFont(font)
            self.chb_radio.setObjectName(f"{name}")
            # Add RadioButton in Group
            self.match_type_grpe.addButton(self.chb_radio)
            # Add Checkbox to QVLayout
            self.layout_CHB.addWidget(self.chb_radio)
        # end loop
        
        # assigner
        self.typeMatchs_WDG.setLayout(self.layout_CHB)

        self.verticalLayout.addWidget(self.bottomAsideLFrame)
    # end func



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        
        self.expenses_Lbl.setText(_translate("MainWindow", "Revenu"))
        self.expensesAmount_Lbl.setText(_translate("MainWindow", "500 HTG"))
        self.betsAmountQty_Lbl.setText(_translate("MainWindow", "Revenu"))
        self.betQtyAmount_Lbl.setText(_translate("MainWindow", "500 HTG"))
        self.incomeLbl.setText(_translate("MainWindow", "Revenu"))
        self.label.setText(_translate("MainWindow", "500 HTG"))

        # TODO: TABLES ITEM CAN BE HERE

        self.matchQPB.setText(_translate("MainWindow", "Matchs"))
        self.betsQPBtn.setText(_translate("MainWindow", "Pariages"))
        self.teamQPB.setText(_translate("MainWindow", "Equipes"))
        self.logoutQPB.setText(_translate("MainWindow", "Logout"))
