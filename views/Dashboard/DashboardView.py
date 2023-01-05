from PyQt5 import QtCore, QtGui, QtWidgets

from Helpers.Helpers import Helpers


class Ui_DashboardView(QtWidgets.QWidget):

    def setupUi(self, MainWindow: QtWidgets.QMainWindow):

        MainWindow.setObjectName("mainWindow")
        MainWindow.setWindowTitle("AG BETS SPORTS")
        MainWindow.setMinimumSize(1235, 600)
        MainWindow.setStyleSheet("#title{\n"
                                 "    font-size: 18px;\n"
                                 "    font-weight:bold;\n"
                                 "    margin-top:10px;\n"
                                 "}\n"
                                 "\n"

                                 "*{ margin: 0px;padding:0px;}\n"
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
                                 "QRadioButton{ color: #FAFAFA;}"
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
        self.centralwidget.setStyleSheet("background:#2C2C2C")
        self.centerWidget()
        self.MainContentFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainContentFrame.setGeometry(
            QtCore.QRect(0, 96, 1250, 1650))

        self.MainContentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainContentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainContentFrame.setObjectName("MainContentFrame")
        # self.MainContentFrame.setStyleSheet("background:blue")

        self.hMainLayout = QtWidgets.QHBoxLayout(self.MainContentFrame)
        self.hMainLayout.setObjectName("hMainLayout")
        self.MainContentFrame.setLayout(self.hMainLayout)

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

    def centerWidget(self):
        # Ajout de cette méthode pour centrer la fenêtre
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(
            QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
    # end centerWidget

    def headerContentFunc(self,):

        # start HEADER LAYOUT
        self.HeaderFrame = QtWidgets.QFrame(self.centralwidget)
        self.HeaderFrame.setMinimumSize(1250, 86)

        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(14)
        self.HeaderFrame.setFont(font)
        # self.HeaderFrame.setStyleSheet("background-color: pink;border-radius:10px")
        self.HeaderFrame.setContentsMargins(0, 0, 0, 0)
        self.HeaderFrame.setObjectName("HeaderFrame")

        self.hLayout_MainHeader_FRM = QtWidgets.QHBoxLayout(self.HeaderFrame)
        # self.hLayout_MainHeader_FRM.setSizeConstraint(
        #     QtWidgets.QLayout.SetDefaultConstraint)

        self.hLayout_MainHeader_FRM.setContentsMargins(0, 0, 0, 0)
        self.hLayout_MainHeader_FRM.setObjectName("hLayout_MainHeader_FRM")

        self.leftHeaderFrame = QtWidgets.QFrame(self.HeaderFrame)
        self.leftHeaderFrame.setContentsMargins(0, 0, 0, 0)

        self.leftHeaderFrame.setMinimumSize(QtCore.QSize(352, 0))
        self.leftHeaderFrame.setStyleSheet("border-radius: 10px")
        self.leftHeaderFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftHeaderFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftHeaderFrame.setContentsMargins(0, 0, 0, 0)
        self.leftHeaderFrame.setObjectName("leftHeaderFrame")

        self.hLayout_LeftHeader_FRM = QtWidgets.QHBoxLayout(
            self.leftHeaderFrame)
        self.hLayout_LeftHeader_FRM.setContentsMargins(0, 0, 0, 0)

        self.lbl_user_name = QtWidgets.QLabel("")
        self.lbl_user_name.setStyleSheet(
            "font-size: 22px;color: #42b883; font-weight: bold")
        self.lbl_user_name.setMaximumWidth(100)

        self.hLayout_LeftHeader_FRM.addWidget(self.lbl_user_name)
        self.hLayout_MainHeader_FRM.addWidget(
            self.leftHeaderFrame, alignment=QtCore.Qt.AlignLeft)

        self.centerHeaderFrame = QtWidgets.QFrame(self.HeaderFrame)
        self.centerHeaderFrame.setContentsMargins(0, 0, 0, 0)

        self.centerHeaderFrame.setMinimumSize(QtCore.QSize(352, 0))
        self.centerHeaderFrame.setStyleSheet("border-radius: 10px")
        self.centerHeaderFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.centerHeaderFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.centerHeaderFrame.setObjectName("centerHeaderFrame")

        self.hLayout_centerHeader_FRM = QtWidgets.QHBoxLayout(
            self.centerHeaderFrame)

        self.matchQPB = QtWidgets.QPushButton(self.centerHeaderFrame)
        self.matchQPB.setStyleSheet("background-color: #1E1E1E;\n"
                                    "color: #FAFAFA;\n"
                                    "border-radius: 10px;\n"
                                    "padding: 10px 15px;")
        self.matchQPB.setObjectName("matchQPB")
        self.matchQPB.setText("Matchs")
        self.hLayout_centerHeader_FRM.addWidget(self.matchQPB)
        self.matchQPB.clicked.connect(lambda: self.printHello())
        # end Match BTN

        # start Bet BTN
        self.betsQPBtn = QtWidgets.QPushButton(self.centerHeaderFrame)
        self.betsQPBtn.setStyleSheet("background-color: #1E1E1E;\n"
                                     "color: #FAFAFA;\n"
                                     "border-radius: 10px;\n"
                                     "padding: 10px 15px;")
        self.betsQPBtn.setObjectName("betsQPB")
        self.betsQPBtn.setText("Pariages")
        self.hLayout_centerHeader_FRM.addWidget(self.betsQPBtn)
        self.betsQPBtn.clicked.connect(lambda: self.printBet())
        # END match bets BTN

        # start payment BTN
        self.paymentQPB = QtWidgets.QPushButton(self.centerHeaderFrame)
        self.paymentQPB.setStyleSheet("background-color: #1E1E1E;\n"
                                      "color: #FAFAFA;\n"
                                      "border-radius: 10px;\n"
                                      "padding: 10px 15px;\n"
                                      "")
        self.paymentQPB.setObjectName("paymentQPB")
        self.paymentQPB.setText("Paiement")
        self.hLayout_centerHeader_FRM.addWidget(self.paymentQPB)

        # end team BTN
        self.hLayout_centerHeader_FRM.setObjectName("hLayout_centerHeader_FRM")

        self.hLayout_MainHeader_FRM.addWidget(
            self.centerHeaderFrame, alignment=QtCore.Qt.AlignJustify)

        # TODO: Right Header

        self.RightHeaderFrame = QtWidgets.QFrame(self.HeaderFrame)
        self.RightHeaderFrame.setStyleSheet("border: none;\n"
                                            "background-color: none;")
        self.RightHeaderFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RightHeaderFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RightHeaderFrame.setObjectName("RightHeaderFrame")

        self.hLayout_RightHeaderAside = QtWidgets.QHBoxLayout(
            self.RightHeaderFrame)
        self.hLayout_RightHeaderAside.setObjectName("hLayout_RightHeaderAside")

        self.balance = QtWidgets.QPushButton(self.RightHeaderFrame)

        self.balance.setStyleSheet("background-color: #1E1E1E;\n"
                                   "color: #FAFAFA;\n"
                                   "opacity: 50%;\n"
                                   "border-radius: 10px;\n"
                                   "padding: 10px 15px;\n"
                                   "")
        self.balance.setObjectName("balance")
        self.balance.setText(f"Balance: {0} HTG")
        self.hLayout_RightHeaderAside.addWidget(self.balance)

        #
        self.adminQPB = QtWidgets.QPushButton(self.RightHeaderFrame)
        self.adminQPB.setStyleSheet("background-color: #42b883;\n"
                                    "color: #FAFAFA;\n"
                                    "opacity: 50%;\n"
                                    "border-radius: 10px;\n"
                                    "padding: 10px 15px;\n"
                                    "")
        self.adminQPB.setObjectName("adminQPB")
        self.adminQPB.setText(f"Admin")
        self.adminQPB.setVisible(False)
        self.hLayout_RightHeaderAside.addWidget(self.adminQPB)

        self.logoutQPB = QtWidgets.QPushButton(self.RightHeaderFrame)

        self.logoutQPB.setStyleSheet("background-color: #E62641;\n"
                                     "color: #FAFAFA;\n"
                                     "opacity: 50%;\n"
                                     "border-radius: 10px;\n"
                                     "padding: 10px 15px;\n"
                                     "")
        self.logoutQPB.setObjectName("logoutQPB")
        self.logoutQPB.setText("Logout")
        self.hLayout_RightHeaderAside.addWidget(self.logoutQPB)
        # self.hLayout_RightHeaderAside.addWidget("Logout")
        self.hLayout_MainHeader_FRM.addWidget(
            self.RightHeaderFrame, alignment=QtCore.Qt.AlignRight)
    # end headerContentFunc()

    def showLeftAside(self, match_type) -> None:
        MAX_WIDTH = 300

        self.LeftAsideFrame = QtWidgets.QFrame(self.MainContentFrame)
        self.LeftAsideFrame.setStyleSheet("background-color: #1E1E1E;\n"
                                          "border-radius: 10px")
        self.LeftAsideFrame.setEnabled(True)
        self.LeftAsideFrame.setFixedWidth(MAX_WIDTH)

        vLayout_LeftAsideFrame = QtWidgets.QVBoxLayout(self.LeftAsideFrame)
        vLayout_LeftAsideFrame.setObjectName("verticalLeftAsideFrameLayout")

        central_FRM = QtWidgets.QFrame(self.LeftAsideFrame)

        vLayout_LeftAsideFrame.addWidget(central_FRM)

        self.title = QtWidgets.QLabel(central_FRM)
        self.title.setText("Catégories")
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        # font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.title.setStyleSheet(
            "margin-bottom: 10px; color:#FAFAFA; padding: 5px;")

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
            self.chb_radio.setStyleSheet("color: #FAFAFA;")
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
        MIN_WIDTH = 1000
        MAX_WIDTH = 600
        self.centralAsideFrame = QtWidgets.QFrame(self.MainContentFrame)
        self.centralAsideFrame.setStyleSheet("background-color: #1E1E1E;\n"
                                             "border-radius: 10px")
        self.centralAsideFrame.setEnabled(True)
        self.centralAsideFrame.setContentsMargins(0, 0, 0, 0)
        self.centralAsideFrame.setMinimumWidth(MIN_WIDTH)

        self.vLayoutCenterAside = QtWidgets.QVBoxLayout(self.centralAsideFrame)
    # end centerAsideFunc()

    def showListMatch(self):

        #  FRAME: START RIGHT ASIDE
        self.ListMatchContent_FRM = QtWidgets.QFrame(self.MainContentFrame)

        self.ListMatchContent_FRM.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ListMatchContent_FRM.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ListMatchContent_FRM.setContentsMargins(0, 0, 0, 0)
        self.ListMatchContent_FRM.setObjectName("ListMatchContent_FRM")
        #
        self.hLayout_ListMatchContent_FRM = QtWidgets.QHBoxLayout(
            self.ListMatchContent_FRM)
        self.hLayout_ListMatchContent_FRM.setObjectName(
            "hLayout_ListMatchContent_FRM")
        self.hLayout_ListMatchContent_FRM.setContentsMargins(0, 0, 0, 0)

        # start left match content
        self.Left_MatchContent_WDG = QtWidgets.QWidget(
            self.ListMatchContent_FRM)
        self.Left_MatchContent_WDG.setObjectName("Left_MatchContent_WDG")
        self.vLayout_MatchContent = QtWidgets.QVBoxLayout(
            self.Left_MatchContent_WDG)
        self.vLayout_MatchContent.setContentsMargins(0, 0, 0, 0)
        # self.vLayout_MatchContent.setSpacing(10)
        self.vLayout_MatchContent.setObjectName("vLayout_MatchContent")

        self.images_WDG = QtWidgets.QWidget(self.Left_MatchContent_WDG)
        self.images_WDG.setMaximumSize(QtCore.QSize(600, 200))
        self.images_WDG.setStyleSheet("background-image: url(./assets/images/panorama.jpeg);\n"
                                      "border-radius: 15px;")
        self.images_WDG.setObjectName("images_WDG")

        self.vLayout_Image_WDG = QtWidgets.QVBoxLayout(self.images_WDG)
        self.vLayout_Image_WDG.setContentsMargins(0, 0, 0, 0)
        self.vLayout_Image_WDG.setSpacing(0)
        self.vLayout_Image_WDG.setObjectName("vLayout_Image_WDG")
        self.lbl_coverImage = QtWidgets.QLabel(self.images_WDG)
        self.lbl_coverImage.setObjectName("label")

        self.vLayout_Image_WDG.addWidget(self.lbl_coverImage)
        self.vLayout_MatchContent.addWidget(self.images_WDG)

        self.LineUpsContainer_WDG = QtWidgets.QWidget(
            self.Left_MatchContent_WDG)

        self.LineUpsContainer_WDG.setStyleSheet(
            "background-color: #1E1E1E;"
            "border-radius: 15px;"
        )
        self.LineUpsContainer_WDG.setObjectName("lineupsContainer")

        # TODO: content list of matchs
        self.vLayout_ToLineUpContainer = QtWidgets.QVBoxLayout(
            self.LineUpsContainer_WDG)
        self.vLayout_ToLineUpContainer.setObjectName(
            "vLayout_ToLineUpContainer")
        self.vLayout_ToLineUpContainer.setAlignment(QtCore.Qt.AlignTop)

        self.vLayout_MatchContent.addWidget(self.LineUpsContainer_WDG)
        self.hLayout_ListMatchContent_FRM.addWidget(
            self.Left_MatchContent_WDG, )
        # end head to head

    def printTest(self):
        print("match is clicked")
        # exit()

    def printHello(self):
        print("teams is clicked")
        # exit()

    def printBet(self):
        print("Bet sport")
        # exit()
