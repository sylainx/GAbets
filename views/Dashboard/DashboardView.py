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
                                #  "    height: 35px;\n"
                                 "    font-weight: bold;\n"
                                #  "    margin-top:10px;\n"
                                #  "    padding: 5px 15px;\n"
                                #  "    border: 2px solid gray;\n"
                                 "}\n"
                                 "QLineEdit:focus{\n"
                                #  "    border:1px solid green;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox{\n"
                                 "    font: 14pt \"JetBrains Mono\";\n"
                                 "    color: rgb(255, 255, 255);\n"
                                 "\n"
                                 "}\n"
                                 "QPushButton{\n"
                                    "background-color: #2C2C2C;\n"
                                    "color: #FAFAFA;\n"
                                    "border-radius: 10px;\n"
                                    "padding: 10px 15px;"                            
                                 "}"
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
        # self.centralwidget.setStyleSheet("background-color: ")


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
        # self.LeftAside.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.LeftAside.setStyleSheet("background-color: #1E1E1E;")
        self.LeftAside.setObjectName("left_aside")

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

        
        # TODO: LEFT ASIDE -> initialization
        self.horizontalLayout_3.addWidget(self.LeftAside)
        # end left aside


        # TODO: FUNCTION RIGHT ASIDE
        # self.rightAsideFrameFunc()
        self.showListMatch()

        # TABLE: PAYMENTS HISTORY
        # self.verticalLayout_6.addWidget(self.tabPayment_QTW)


        self.RightAside = QtWidgets.QFrame(self.MainContentFrame)

        self.horizontalLayout_3.addWidget(self.RightAside)

        # TODO: FUCNTION TO CALL HEADER
        self.headerContentFunc()


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1135, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

       
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # END SETUPUI()

    def headerContentFunc(self,):

        # start HEADER LAYOUT
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

        self.matchQPB = QtWidgets.QPushButton(self.LeftHeaderFrame)
        self.matchQPB.setStyleSheet("background-color: #2C2C2C;\n"
                                    "color: #FAFAFA;\n"
                                    "border-radius: 10px;\n"
                                    "padding: 10px 15px;")
        self.matchQPB.setObjectName("matchQPB")
        self.matchQPB.setText("Matchs")
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
        self.betsQPBtn.setText("Pariages")
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
        self.teamQPB.setText("Equipes")
        
       
        self.horizontalLayout_2.addWidget(self.teamQPB)
        # end team BTN

        # TODO: START ADMIN button
        # if user isADMIN:
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.adminQPB = QtWidgets.QPushButton(self.LeftHeaderFrame)
        self.adminQPB.setStyleSheet("background-color: #42b883;\n"
                                    "color: #FAFAFA;\n"
                                    "border-radius: 10px;\n"
                                    "padding: 10px 15px;")
        self.adminQPB.setObjectName("adminQPB")
        self.adminQPB.setText("Admin")
        self.horizontalLayout_2.addWidget(self.adminQPB)
        # self.adminQPB.clicked.connect(lambda: self.callAdminDashboard())
        # END ADMIN BUTTON

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
        self.logoutQPB.setText("Logout")
        self.verticalLayout_2.addWidget(self.logoutQPB)
        # self.verticalLayout_2.addWidget("Logout")
        self.horizontalLayout.addWidget(self.RightHeaderFrame)
        

    def showLeftAside(self,MainWindow,match_type)->None:

        MAX_WIDTH= 200
        MAX_HEIGHT= 700
        self.LeftAsideFrame = QtWidgets.QFrame(self.MainContentFrame)
        self.LeftAsideFrame.setStyleSheet("background-color: #1E1E1E;\n"
                                     "border-radius: 10px")
        self.LeftAsideFrame.setEnabled(True)
        # self.LeftAsideFrame.setMinimumWidth(MAX_WIDTH)
        # self.LeftAsideFrame.setMinimumHeight(MAX_HEIGHT)
        # self.LeftAsideFrame.setMaximumSize(MAX_WIDTH,MAX_HEIGHT)
        self.LeftAsideFrame.setMinimumSize(QtCore.QSize(MAX_WIDTH, 500))
        # self.LeftAsideFrame.setMaximumWidth(200)

        vLayout_LeftAsideFrame = QtWidgets.QVBoxLayout(self.LeftAsideFrame)
        vLayout_LeftAsideFrame.setObjectName("verticalLeftAsideFrameLayout")
        
        central_FRM = QtWidgets.QFrame(self.LeftAsideFrame)
        central_FRM.setMinimumSize(QtCore.QSize(MAX_WIDTH, 500))    
        
        # central_FRM.setStyleSheet("background-color: pink")

        self.title = QtWidgets.QLabel(central_FRM)
        self.title.setText("Catégories")
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.title.setStyleSheet("margin-bottom: 10px;padding:5px")

        
        vLayout_Central_FRM = QtWidgets.QVBoxLayout(central_FRM)
        vLayout_Central_FRM.setAlignment(QtCore.Qt.AlignTop)

        vLayout_Central_FRM.addWidget(self.title)
        # Création du groupe de boutons radio
        self.match_type_grpe = QtWidgets.QButtonGroup()

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
            vLayout_Central_FRM.addWidget(self.chb_radio)
        # end loop

        # vLayout_Central_FRM.addLayout(vLayout_Central_FRM)

        self.LeftAsideFrame.setLayout(vLayout_Central_FRM)


    def centerAsideFunc(self):
        MAX_WIDTH=700
        self.centralAsideFrame = QtWidgets.QFrame(self.MainContentFrame)
        self.centralAsideFrame.setStyleSheet("background-color: #1E1E1E;\n"
                                     "border-radius: 10px")
        self.centralAsideFrame.setEnabled(True)
        # self.centralAsideFrame.setMinimumWidth(MAX_WIDTH)
        # self.centralAsideFrame.setMinimumHeight(MAX_HEIGHT)
        # self.centralAsideFrame.setMaximumSize(MAX_WIDTH,MAX_HEIGHT)
        self.centralAsideFrame.setMinimumSize(QtCore.QSize(MAX_WIDTH, 500))
        # self.centralAsideFrame.setMaximumWidth(200)

    def rightAsideFrameFunc(self):

        #  FRAME: START RIGHT ASIDE
        # self.verticalLayout_7.addWidget(self.BottomBox)
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



        # TODO: START TOPBOX CONTAINER

        self.TopBox = QtWidgets.QFrame(self.RightAside)
        # sizePolicy = QtWidgets.QSizePolicy(
        #     QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.TopBox.sizePolicy().hasHeightForWidth())
        self.TopBox.setSizePolicy(sizePolicy)
        # self.TopBox.setMaximumSize(QtCore.QSize(10, 120))
        self.TopBox.setAutoFillBackground(False)
        self.TopBox.setStyleSheet("background-color: #2C2C2C;\n"
                                  "border-radius: 10px")
        self.TopBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TopBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TopBox.setObjectName("TopBox")


        # START INCOMEBOX
        self.IncomeBox = QtWidgets.QFrame(self.TopBox)
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
        self.incomeLbl.setText("Revenu")
        self.incomeLbl.setStyleSheet("color: #fafafa;\n"
                                     "text-align:center;")
        self.incomeLbl.setObjectName("incomeLbl")
        self.verticalLayout_3.addWidget(self.incomeLbl)
        self.label = QtWidgets.QLabel(self.IncomeBox)
        self.label.setText("500 HTG")
        self.label.setStyleSheet("color: #E62641;\n"
                                 "font: 18pt \"JetBrains Mono\";")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_7.addWidget(self.TopBox)
        # END EXPENSESBOX

        # START EXPENSESBOX
        self.ExpensesBox = QtWidgets.QFrame(self.TopBox)
        # self.ExpensesBox.setGeometry(QtCore.QRect(10, 34, 150, 50))
        # self.ExpensesBox.setMaximumSize(QtCore.QSize(150, 50))
        self.ExpensesBox.setStyleSheet("background-color: #1E1E1E;\n"
                                       "border-radius: 10px")
        self.ExpensesBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ExpensesBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ExpensesBox.setObjectName("ExpensesBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.ExpensesBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.expenses_Lbl = QtWidgets.QLabel(self.ExpensesBox)
        self.expenses_Lbl.setText("Revenu")

        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(14)
        self.expenses_Lbl.setFont(font)
        self.expenses_Lbl.setStyleSheet("color: #fafafa;\n"
                                        "text-align:center;")
        self.expenses_Lbl.setObjectName("expenses_Lbl")
        self.verticalLayout_4.addWidget(self.expenses_Lbl)
        self.expensesAmount_Lbl = QtWidgets.QLabel(self.ExpensesBox)
        self.expensesAmount_Lbl.setText("500 HTG")
        self.expensesAmount_Lbl.setStyleSheet("color: #E62641;\n"
                                              "font: 18pt \"JetBrains Mono\";")
        self.expensesAmount_Lbl.setObjectName("expensesAmount_Lbl")
        self.verticalLayout_4.addWidget(self.expensesAmount_Lbl)
        # END EXPENSESBOX

        # START BETSSBOX
        self.betsQtyBox = QtWidgets.QFrame(self.TopBox)
        # self.betsQtyBox.setGeometry(QtCore.QRect(63, 34, 200, 50))
        # self.betsQtyBox.setMaximumSize(QtCore.QSize(200, 50))
        # self.betsQtyBox.setBaseSize(QtCore.QSize(200, 50))
        self.betsQtyBox.setStyleSheet("background-color: #1E1E1E;\n"
                                      "border-radius: 10px")
        self.betsQtyBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.betsQtyBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.betsQtyBox.setObjectName("betsQtyBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.betsQtyBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.betsAmountQty_Lbl = QtWidgets.QLabel(self.betsQtyBox)
        self.betsAmountQty_Lbl.setText("Revenu")
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(14)
        self.betsAmountQty_Lbl.setFont(font)
        self.betsAmountQty_Lbl.setStyleSheet("color: #fafafa;\n"
                                             "text-align:center;")
        self.betsAmountQty_Lbl.setObjectName("betsAmountQty_Lbl")
        self.verticalLayout_5.addWidget(self.betsAmountQty_Lbl)
        self.betQtyAmount_Lbl = QtWidgets.QLabel(self.betsQtyBox)
        self.betQtyAmount_Lbl.setText("500 HTG")        
        self.betQtyAmount_Lbl.setStyleSheet("color: #E62641;\n"
                                            "font: 18pt \"JetBrains Mono\";")
        self.betQtyAmount_Lbl.setObjectName("betQtyAmount_Lbl")
        self.verticalLayout_5.addWidget(self.betQtyAmount_Lbl)



        self.BottomBox = QtWidgets.QFrame(self.RightAside)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.BottomBox.sizePolicy().hasHeightForWidth())
        self.BottomBox.setSizePolicy(sizePolicy)
        self.BottomBox.setMaximumSize(QtCore.QSize(715, 1215))
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


    def showListMatch (self):

        #  FRAME: START RIGHT ASIDE
        self.RightAside = QtWidgets.QFrame(self.MainContentFrame)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.RightAside.sizePolicy().hasHeightForWidth())
        self.RightAside.setSizePolicy(sizePolicy)

        self.RightAside.setStyleSheet("background-color: red;\n"
                                      "border-radius: 10px")
        # self.RightAside.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.RightAside.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RightAside.setObjectName("RightAside")

        # mwen ranplase verticalLayout_7 pa hLayout_2
        self.hLayout_2 = QtWidgets.QHBoxLayout(self.RightAside)
        self.hLayout_2.setObjectName("hLayout_2")

        # start head to head
        self.head_to_head = QtWidgets.QWidget(self.RightAside)
        self.head_to_head.setObjectName("head_to_head")
        self.vLayout_4 = QtWidgets.QVBoxLayout(self.head_to_head)
        self.vLayout_4.setContentsMargins(0, 0, 0, 0)
        self.vLayout_4.setSpacing(10)
        self.vLayout_4.setObjectName("vLayout_4")
        self.images = QtWidgets.QWidget(self.head_to_head)
        self.images.setMaximumSize(QtCore.QSize(16777215, 201))
        self.images.setStyleSheet("background-image: url(./assets/images/tt.png);\n"
"border-radius: 15px;")
        self.images.setObjectName("images")
        self.vLayout_5 = QtWidgets.QVBoxLayout(self.images)
        self.vLayout_5.setContentsMargins(0, 0, 0, 0)
        self.vLayout_5.setSpacing(0)
        self.vLayout_5.setObjectName("vLayout_5")
        self.label = QtWidgets.QLabel(self.images)
        self.label.setText("")
        self.label.setObjectName("label")
        self.vLayout_5.addWidget(self.label)
        self.vLayout_4.addWidget(self.images)
        self.h2h = QtWidgets.QWidget(self.head_to_head)
        self.h2h.setStyleSheet("background-color: #1E1E1E; \n"
"border-radius: 15px;")
        self.h2h.setObjectName("h2h")
        self.vLayout_6 = QtWidgets.QVBoxLayout(self.h2h)
        self.vLayout_6.setObjectName("vLayout_6")
        self.lineups_container = QtWidgets.QWidget(self.h2h)
        self.lineups_container.setStyleSheet("background-color: #2C2C2C;\n"
"")
        self.lineups_container.setObjectName("lineups_container")
        self.hLayout_5 = QtWidgets.QHBoxLayout(self.lineups_container)
        self.hLayout_5.setObjectName("hLayout_5")
        self.home_team = QtWidgets.QFrame(self.lineups_container)
        self.home_team.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home_team.setFrameShadow(QtWidgets.QFrame.Raised)
        self.home_team.setObjectName("home_team")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.home_team)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.homteam_button = QtWidgets.QPushButton(self.home_team)
        self.homteam_button.setStyleSheet("color: #fff")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./assets/images/teams/ajax.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homteam_button.setIcon(icon)
        self.homteam_button.setIconSize(QtCore.QSize(32, 32))
        self.homteam_button.setObjectName("homteam_button")
        self.horizontalLayout_3.addWidget(self.homteam_button)
        self.hometeam_cote = QtWidgets.QLabel(self.home_team)
        self.hometeam_cote.setStyleSheet("color: #E62641;")
        self.hometeam_cote.setObjectName("hometeam_cote")
        self.horizontalLayout_3.addWidget(self.hometeam_cote)
        self.label_2 = QtWidgets.QLabel(self.home_team)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("color: #FAFAFA;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.hLayout_5.addWidget(self.home_team)
        self.home_team_2 = QtWidgets.QFrame(self.lineups_container)
        self.home_team_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home_team_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.home_team_2.setObjectName("home_team_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.home_team_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.home_team_2)
        self.label_3.setStyleSheet("color: #FAFAFA;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.hometeam_cote_2 = QtWidgets.QLabel(self.home_team_2)
        self.hometeam_cote_2.setStyleSheet("color: #E62641;")
        self.hometeam_cote_2.setObjectName("hometeam_cote_2")
        self.horizontalLayout_4.addWidget(self.hometeam_cote_2)
        self.pushButton_6 = QtWidgets.QPushButton(self.home_team_2)
        self.pushButton_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_6.setStyleSheet("color: #fff;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./assets/images/teams/fcb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        self.hLayout_5.addWidget(self.home_team_2)
        self.vLayout_6.addWidget(self.lineups_container)
        self.lineups_container_2 = QtWidgets.QWidget(self.h2h)
        self.lineups_container_2.setStyleSheet("background-color: #2C2C2C;\n"
"")
        self.lineups_container_2.setObjectName("lineups_container_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.lineups_container_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.home_team_3 = QtWidgets.QFrame(self.lineups_container_2)
        self.home_team_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home_team_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.home_team_3.setObjectName("home_team_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.home_team_3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.homteam_button_2 = QtWidgets.QPushButton(self.home_team_3)
        self.homteam_button_2.setStyleSheet("color: #fff")
        self.homteam_button_2.setIcon(icon)
        self.homteam_button_2.setIconSize(QtCore.QSize(32, 32))
        self.homteam_button_2.setObjectName("homteam_button_2")
        self.horizontalLayout_7.addWidget(self.homteam_button_2)
        self.hometeam_cote_3 = QtWidgets.QLabel(self.home_team_3)
        self.hometeam_cote_3.setStyleSheet("color: #E62641;")
        self.hometeam_cote_3.setObjectName("hometeam_cote_3")
        self.horizontalLayout_7.addWidget(self.hometeam_cote_3)
        self.label_4 = QtWidgets.QLabel(self.home_team_3)
        self.label_4.setStyleSheet("color: #FAFAFA;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.horizontalLayout_6.addWidget(self.home_team_3)
        self.home_team_4 = QtWidgets.QFrame(self.lineups_container_2)
        self.home_team_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home_team_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.home_team_4.setObjectName("home_team_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.home_team_4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.home_team_4)
        self.label_5.setStyleSheet("color: #FAFAFA;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.hometeam_cote_4 = QtWidgets.QLabel(self.home_team_4)
        self.hometeam_cote_4.setStyleSheet("color: #E62641;")
        self.hometeam_cote_4.setObjectName("hometeam_cote_4")
        self.horizontalLayout_8.addWidget(self.hometeam_cote_4)
        self.pushButton_7 = QtWidgets.QPushButton(self.home_team_4)
        self.pushButton_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_7.setStyleSheet("color: #fff;")
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_8.addWidget(self.pushButton_7)
        self.horizontalLayout_6.addWidget(self.home_team_4)
        self.vLayout_6.addWidget(self.lineups_container_2)
        self.vLayout_4.addWidget(self.h2h)
        self.hLayout_2.addWidget(self.head_to_head)
        # end head to head


        self.right_details = QtWidgets.QWidget(self.RightAside)
        self.right_details.setStyleSheet("background-color: #1E1E1E; ")
        self.right_details.setObjectName("right_details")
        self.hLayout_2.addWidget(self.right_details)
        # OR self.verticalLayout_6.addWidget(self.RightAside)
        self.hLayout_2.addWidget(self.RightAside)
        # TODO: end cent
       
       

    def printTest(self):
        print("match is clicked")
        # exit()

    def printHello(self):
        print("teams is clicked")
        # exit()

    def printBet(self):
        print("Bet sport")
        # exit()

    # end showLeftAside
