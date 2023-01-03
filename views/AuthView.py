from PyQt5.QtWidgets import QDialog, QRadioButton, QDateEdit, QLineEdit, QSizePolicy, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
# local package
from Models.LoginModel import LoginModel
from Models.RegisterModel import RegisterModel
from Helpers.Helpers import Helpers
from datetime import date


class AuthView(QWidget):
    to_login = LoginModel()
    to_register = RegisterModel()
    util = Helpers()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Authentification")
        # features
        self.ui()

    # end init

    def ui(self):
        # conteneur principal.
        # QWidget io pemet u personalize page la
        # vLayout_MainContent = QVBoxLayout(self)
        self.content = QWidget(self)
        self.setMinimumSize(750, 400)
        self.content.setMinimumSize(800, 660)
        self.setMaximumSize(810, 750)
        self.content.setStyleSheet(
            "background-color: #2C2C2C;"
            "    font-size: 15px;\n"
            "    font-weight:bold;\n"
            "}\n"
            "\n"
            "QLabel{\n"
            "    font: 15px \"JetBrains Mono\";\n"
            "    color: #FAFAFA\n"
            # "    margin-top:5px;    \n"
            "}\n"
            "\n"
            "QLineEdit{\n"
            "    height: 30px;\n"
            "    font-weight: bold;\n"
            "    border: 1px solid white;\n"
            "}\n"
            "QLineEdit:focus{\n"
            "    border:0px solid white\n"
            "}\n"
            "")

        # Kom Layout io la pou pozisyone element io seulmn. siw bezwen ba yo style ou oblije metel nan
        # yon QWidget epi personalize QWidget la
        # QWidget sa pemet u personalize pati header an
        # idem2
        body_layout = QHBoxLayout()
        self.gridLayout = QGridLayout()

        # Label lan genyen imaj la ladann
        label_img = QLabel(self)
        pixmap = QPixmap("./assets/images/logo_gabets.png")
        label_img.setPixmap(pixmap)
        # self.setCentralWidget(label_league)
        label_img.setMinimumWidth(150)
        label_img.setMinimumHeight(252)

        sizePolicy = QSizePolicy(
            QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(
            label_img.sizePolicy().hasHeightForWidth())
        label_img.setSizePolicy(sizePolicy)

        # self.resize(pixmap.width(), pixmap.height())
        body_layout.addWidget(label_img)

        content_leftside = QWidget()
        content_leftside.setStyleSheet(
            "background-color: white;"
            "border-radius: 10px;"
        )
        content_leftside.setLayout(body_layout)
        self.gridLayout.addWidget(content_leftside, 1, 1)

        # methode sa pemet u di gridLayout la konbyn espas wap bay chak element
        # lipran an paramet indice ligne nan epi groseu a
        # ligne 3 lot elements io (2e ligne nan, pran 10 fois 1e ligne nan (1e ligne nan egal a 1))
        self.gridLayout.setRowStretch(1, 10)
        # methode sa pemet u di gridLayout la konbyn espas wap bay chak element
        # lipran an paramet indice colon nan epi groseu a
        # self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 4)
        self.gridLayout.setColumnStretch(2, 3)

        # end left aside

    def displayLogin(self):

        content_rightside = QWidget()

        rightside_layout = QHBoxLayout()
        content_rightside.setStyleSheet(
            "background-color: #2C2C2C;"
            "border-radius: 10px;"
        )
        content_rightside.setLayout(rightside_layout)

        # methode sa pemet ou retire marge GridLayout la. de base. Layout io tou vini ak marge
        # self.gridLayout.setContentsMargins(0,0,0,0)
        # Kom c QWidget io ki kenbe self.gridLayout ki pral kenbe lot element io, mw add QWidget io nan GridLayout la
        # 2e ligne, 2e colon
        # 2e ligne, 3e colon
        self.gridLayout.addWidget(content_rightside, 1, 2)

        # creating a form self.gridLayout
        # pass_layout = QHBoxLayout()
        form_layout = QVBoxLayout()
        self.login_QPB = QPushButton("Sign in")
        self.login_QPB.setCursor(Qt.PointingHandCursor)
        self.login_QPB.setStyleSheet("color: white;\n"
                                    "    margin-top:15px;\n"
                                    "    height:50px;\n"
                                    "    width:100px;\n"
                                    "color:white;\n"
                                    "text-align:center;\n"
                                    "background-color: #1E1E1E;\n"
                                    "border-radius:10px;\n"
                                    "font-size:15px;\n"
                                    )

        self.no_account_HLYT = QHBoxLayout()
        self.no_account = QLabel("Don't have an account?")
        self.no_account.setAlignment(QtCore.Qt.AlignCenter)
        self.no_account.setStyleSheet("font-size: 12px;\n"
                                      "    margin-top:10px;\n"
                                      "    text-align:center;\n"
                                      "    color: #FAFAFA;\n")
        self.inviteSignUpBtn = QPushButton("Create an account")
        self.inviteSignUpBtn.setCursor(Qt.PointingHandCursor)
        self.inviteSignUpBtn.setStyleSheet("font-size: 12px;\n"
                                           "    margin-top:10px;\n"
                                           "    text-align:center;\n"
                                           "    color: #42b883;\n")

        # create link back to login
        self.no_account_HLYT.addWidget(self.no_account)
        self.no_account_HLYT.addWidget(self.inviteSignUpBtn)
        form_layout.setAlignment(Qt.AlignTop)
        self.label_title = QLabel("Login")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setStyleSheet("    font-size: 20px;\n"
                                       "    font-weight:bold;\n"
                                       "    margin:10px 0px 35px 0px;\n"
                                       "    text-align:center;\n"
                                       "    color:#FAFAFA\n"
                                       )

        self.txtUsername_QLE = QLineEdit()
        self.txtPassword_QLE = QLineEdit()
        self.txtPassword_QLE.setEchoMode(QLineEdit.Password)

        self.lbl_errorMessage = QLabel()
        self.lbl_errorMessage.setVisible(False)
        self.lbl_errorMessage.setContentsMargins(0,0,0,0)
        self.lbl_errorMessage.setStyleSheet(
            "color: #E62641;"
            "font-size: 12px;"
            "text-align:center;"
            "margin: 10px 10px 0px 10px;"
        )

        # adding rows
        # for name and adding input text
        form_layout.addWidget(self.label_title)
        form_layout.addWidget(QLabel("Username"))
        form_layout.addWidget(self.txtUsername_QLE)
        form_layout.addWidget(QLabel("Password"))
        form_layout.addWidget(self.txtPassword_QLE)
        form_layout.addWidget(self.lbl_errorMessage)
        form_layout.addWidget(self.login_QPB)
        form_layout.addLayout(self.no_account_HLYT)
        #     Setting self.gridLayout
        rightside_layout.addLayout(form_layout)
        #
        self.content.setLayout(self.gridLayout)

    def clearFiels(self):
        # TODO will be prepare infos to submit login in Model

        # fill
        self.to_login.username = self.txtUsername_QLE.text()
        self.to_login.password = self.txtPassword_QLE.text()

        # verify if user is sucessfully connected
        id_user_connected = self.to_login.check_user_connect()

    # end clearFields


    def displayRegister(self):

        rightside_layout = QHBoxLayout()
        content_rightside = QWidget()
        content_rightside.setStyleSheet(
            "background-color: #1E1E1E;"
            "border-radius: 10px;"
        )
        content_rightside.setLayout(rightside_layout)

        # 2e ligne, 3e colon
        self.gridLayout.addWidget(content_rightside, 1, 2)

        # radioButton Layouts
        q_gender_LYT = QHBoxLayout()
        have_account_LYT = QHBoxLayout()
        # creating a form self.gridLayout
        form_layout = QVBoxLayout()
        self.loginbtn = QPushButton("Sign Up")
        self.loginbtn.setCursor(Qt.PointingHandCursor)
        self.loginbtn.setStyleSheet("color: white;\n"
                                    "    margin-top:5px;\n"
                                    "    height:30px;\n"
                                    "    width:100px;\n"
                                    "color:white;\n"
                                    "text-align:center;\n"
                                    "background-color: #1E1E1E;\n"
                                    "border-radius:10px;\n"
                                    "font-size:18px;\n"
                                    )
                                    
        self.have_account = QLabel("have an account?")
        self.have_account.setAlignment(QtCore.Qt.AlignCenter)
        self.have_account.setStyleSheet("font-size: 12px;\n"
                                        "    margin-top:5px;\n"
                                        "    color: #FAFAFA;\n"
                                        "    text-align:center;\n")

        self.inviteLogin_QPB = QPushButton("Login to account")
        self.inviteLogin_QPB.setCursor(Qt.PointingHandCursor)
        self.inviteLogin_QPB.setStyleSheet("font-size: 12px;\n"
                                           "    margin-top:5px;\n"
                                           "    text-align:center;\n"
                                           "    color: #42b883;\n")

        
        form_layout.setAlignment(Qt.AlignTop)
        self.label_title = QLabel("Sign Up Page")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setStyleSheet("    font-size: 15px;\n"
                                       "    font-weight:bold;\n"
                                       "    margin-top:5px;\n"
                                       "    text-align:center;\n"
                                       "    color: #FAFAFA;\n"
                                       )
        # create link back to login
        have_account_LYT.addWidget(self.have_account)
        have_account_LYT.addWidget(self.inviteLogin_QPB)
        # add radioButton to Widget
        self.rdMale = QRadioButton("Masculin")
        self.rdFemale = QRadioButton("Feminin")
        q_gender_LYT.addWidget(self.rdFemale)
        q_gender_LYT.addWidget(self.rdMale)
        # Create date
        self.txtDateOfBirth = QDateEdit()
        self.txtDateOfBirth.setDisplayFormat("dd/MM/yyyy")
        self.txtDateOfBirth.setCalendarPopup(True)
        self.txtDateOfBirth.setStyleSheet(
            "color: #FAFAFA;\n"
        )

        self.txtFirstName = QLineEdit()
        self.txtLastName = QLineEdit()
        self.txtUsername = QLineEdit()
        self.txtAdress = QLineEdit()
        self.txtEmail = QLineEdit()
        self.txtPhone = QLineEdit()
        self.txtNif = QLineEdit()
        self.txtPassword_QLE = QLineEdit()
        self.txtConfirmPassword = QLineEdit()
        self.txtConfirmPassword.setEchoMode(QLineEdit.Password)
        self.txtPassword_QLE.setEchoMode(QLineEdit.Password)

        # adding rows
        # for name and adding input text
        form_layout.addWidget(self.label_title)
        form_layout.addWidget(QLabel(" First name"))
        form_layout.addWidget(self.txtFirstName)
        form_layout.addWidget(QLabel("Last name"))
        form_layout.addWidget(self.txtLastName)
        form_layout.addWidget(QLabel("User name"))
        form_layout.addWidget(self.txtUsername)
        form_layout.addWidget(QLabel("User Email"))
        form_layout.addWidget(self.txtEmail)
        form_layout.addWidget(QLabel("user Adress"))
        form_layout.addWidget(self.txtAdress)
        form_layout.addWidget(QLabel("user Phone"))
        form_layout.addWidget(self.txtPhone)

        form_layout.addWidget(QLabel("Sexe"))
        form_layout.addLayout(q_gender_LYT)

        form_layout.addWidget(QLabel("Date of birth"))
        form_layout.addWidget(self.txtDateOfBirth)

        form_layout.addWidget(QLabel("user Nif"))
        form_layout.addWidget(self.txtNif)
        form_layout.addWidget(QLabel("Password"))
        form_layout.addWidget(self.txtPassword_QLE)
        form_layout.addWidget(QLabel("confirm Password"))
        form_layout.addWidget(self.txtConfirmPassword)
        form_layout.addWidget(self.loginbtn)

        form_layout.addLayout(have_account_LYT)

        #     Setting self.gridLayout
        form_layout.addLayout(q_gender_LYT)
        rightside_layout.addLayout(form_layout)
        #
        self.content.setLayout(self.gridLayout)

    # def clearFields(self):
    #     # TODO will be clear all fields
    #     self.txtUsername_QLE.clear()
    #     self.txtFirstname.clear()
    #     self.txtLastname.clear()
    #     self.txtAddress.clear()
    #     self.txtEmail.clear()
    #     self.txtNif.clear()
    #     self.txtPhone.clear()
    #     self.txtDateOfBirth.clear()
    #     self.txtPassword_QLE.clear()
    #     self.rdFemale.setChecked(False)
    #     self.rdMale.setChecked(False)
