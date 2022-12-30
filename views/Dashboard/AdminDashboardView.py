from PyQt5 import QtCore, QtGui, QtWidgets

from Helpers.Helpers import Helpers


class Ui_AdminDashboardView(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("mainWindow")
        MainWindow.setWindowTitle("ADMIN AG BETS SPORTS")
        # MainWindow.resize(1135, 600)
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
            QtCore.QRect(0, 96, 1150, 16777214))

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(
            self.MainContentFrame.sizePolicy().hasHeightForWidth())
        self.MainContentFrame.setSizePolicy(sizePolicy)
        self.MainContentFrame.setMaximumSize(QtCore.QSize(1150, 16777214))
        self.MainContentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainContentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainContentFrame.setObjectName("MainContentFrame")

        self.hMainLayout = QtWidgets.QHBoxLayout(self.MainContentFrame)
        self.hMainLayout.setObjectName("hMainLayout")
        self.MainContentFrame.setLayout(self.hMainLayout)

        # TODO: FUNCTION RIGHT ASIDE

        # TABLE: PAYMENTS HISTORY
        # self.verticalLayout_6.addWidget(self.tabPayment_QTW)

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
        self.LeftHeaderFrame.setStyleSheet(
            "background-color: #1E1E1E;border-radius: 10px")
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
    # end headerContentFunc

    def showLeftAside(self, match_type) -> None:
        MAX_WIDTH = 300
        MAX_HEIGHT = 700

        self.LeftAsideFrame = QtWidgets.QFrame()
        self.LeftAsideFrame.setStyleSheet("background-color: #1E1E1E;\n"
                                          "border-radius: 10px")
        self.LeftAsideFrame.setEnabled(True)
        # self.LeftAsideFrame.setMinimumWidth(MAX_WIDTH)
        # self.LeftAsideFrame.setMinimumHeight(MAX_HEIGHT)
        # self.LeftAsideFrame.setMaximumSize(MAX_WIDTH,MAX_HEIGHT)
        self.LeftAsideFrame.setMinimumSize(QtCore.QSize(MAX_WIDTH, 500))
        self.LeftAsideFrame.setMaximumWidth(200)

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

    # end showLeftAside

    def centerAsideFunc(self):
        MAX_WIDTH = 100
        self.centralAsideFrame = QtWidgets.QFrame()
        self.centralAsideFrame.setStyleSheet("background-color: #1E1E1E;\n"
                                             "border-radius: 10px")
        self.centralAsideFrame.setEnabled(True)
        # self.centralAsideFrame.setMinimumWidth(MAX_WIDTH)
        # self.centralAsideFrame.setMinimumHeight(MAX_HEIGHT)
        # self.centralAsideFrame.setMaximumSize(MAX_WIDTH,MAX_HEIGHT)
        # self.centralAsideFrame.setMinimumSize(QtCore.QSize(MAX_WIDTH, 500))
        # self.centralAsideFrame.setMaximumSize(10,0)

        self.vLayoutCenterAside = QtWidgets.QVBoxLayout(self.centralAsideFrame)
        
    # end centerAsideFunc

    def showListMatch(self):

        #  FRAME: START RIGHT ASIDE
        self.ListMatchContent_FRM = QtWidgets.QFrame(self.MainContentFrame)

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ListMatchContent_FRM.sizePolicy().hasHeightForWidth())
        self.ListMatchContent_FRM.setSizePolicy(sizePolicy)

        # self.ListMatchContent_FRM.setStyleSheet("background-color: pink;\n"
        #                                         "border-radius: 10px")
        self.ListMatchContent_FRM.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ListMatchContent_FRM.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ListMatchContent_FRM.setObjectName("ListMatchContent_FRM")

        #
        self.hLayout_2 = QtWidgets.QHBoxLayout(self.ListMatchContent_FRM)
        self.hLayout_2.setObjectName("hLayout_2")

        
        # start head to head
        self.head_to_head = QtWidgets.QWidget(self.ListMatchContent_FRM)
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
        self.lbl_coverImage = QtWidgets.QLabel(self.images)
        self.lbl_coverImage.setText("")
        self.lbl_coverImage.setObjectName("label")

        self.vLayout_5.addWidget(self.lbl_coverImage)
        self.vLayout_4.addWidget(self.images)

        self.h2h = QtWidgets.QWidget(self.head_to_head)
        
        self.h2h.setStyleSheet("background-color: #1E1E1E; \n"
                               "border-radius: 15px;")
        self.h2h.setObjectName("h2h")

        # TODO: content list of matchs
        self.vLayout_ToLineUpContainer = QtWidgets.QVBoxLayout(self.h2h)
        self.vLayout_ToLineUpContainer.setObjectName("vLayout_ToLineUpContainer")
        self.vLayout_ToLineUpContainer.setAlignment(QtCore.Qt.AlignTop)
        
        self.vLayout_4.addWidget(self.h2h)
        self.hLayout_2.addWidget(self.head_to_head)
        # end head to head



        self.right_details = QtWidgets.QWidget(self.ListMatchContent_FRM)
        self.right_details.setStyleSheet("background-color: #2C2C2C; ")
        self.right_details.setObjectName("right_details")
        self.hLayout_2.addWidget(self.right_details)

        # self.vLayout_ToLineUpContainer.addWidget(self.ListMatchContent_FRM)
        
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
