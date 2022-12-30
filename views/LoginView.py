from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import  QtCore
from PyQt5.QtGui import QPixmap
# local package
from Models.LoginModel import LoginModel
from Models.RegisterModel import RegisterModel
from Helpers.Helpers import Helpers
from datetime import date


class LoginView(QMainWindow):
    to_login = LoginModel()
    to_register = RegisterModel()
    util = Helpers()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login")
        self.setMaximumSize(800, 640)
        self.setMinimumSize(700, 400)
        # self.isModal(True)
        # features
        self.display()
        self.setCentralWidget(self.content)
        # self.createNewTab()
        # self.createLoginForm()
        # self.createRegisterForm()

    # end init

    def display(self):
        # conteneur principal.
        # QWidget io pemet u personalize page la
        self.content = QWidget()
        self.content.setStyleSheet(
            "background-color: #2C2C2C;"
            "    font-size: 15px;\n"
            "    font-weight:bold;\n"
            "}\n"
            "\n"
            "QLabel{\n"
            "    font: 15px \"JetBrains Mono\";\n"
            "    color: blue;\n"
            # "    margin-top:5px;    \n"
            "}\n"
            "\n"
            "QLineEdit{\n"
            "    height: 30px;\n"
            "    font-weight: bold;\n"
            "    border: 1px solid #1E1E1E;\n"
            "}\n"
            "QLineEdit:focus{\n"
            "    border:1px solid blue;\n"
            "}\n"
            "")
        # Kom Layout io la pou pozisyone element io seulmn. siw bezwen ba yo style ou oblije metel nan
        # yon QWidget epi personalize QWidget la
        # QWidget sa pemet u personalize pati header an
        # idem2
        body_layout = QHBoxLayout()
        # Label lan genyen logo ki league
        label_league = QLabel(self)
        pixmap = QPixmap('home-29.png')
        label_league.setPixmap(pixmap)
        self.setCentralWidget(label_league)
        self.resize(pixmap.width(), pixmap.height())
        body_layout.addWidget(label_league)
        content_leftside = QWidget()
        content_leftside.setStyleSheet(
            "background-color: white;"
            "border-radius: 10px;"
        )
        content_leftside.setLayout(body_layout)
        # idem3
        rightside_layout = QHBoxLayout()
        content_rightside = QWidget()
        content_rightside.setStyleSheet(
            "background-color: white;"
            "border-radius: 10px;"
        )
        content_rightside.setLayout(rightside_layout)
        layout = QGridLayout()
        # methode sa pemet ou retire marge GridLayout la. de base. Layout io tou vini ak marge
        # layout.setContentsMargins(0,0,0,0)
        # Kom c QWidget io ki kenbe layout ki pral kenbe lot element io, mw add QWidget io nan GridLayout la
        # 2e ligne, 2e colon
        layout.addWidget(content_leftside, 1, 1)
        # 2e ligne, 3e colon
        layout.addWidget(content_rightside, 1, 2)
        # methode sa pemet u di gridLayout la konbyn espas wap bay chak element
        # lipran an paramet indice ligne nan epi groseu a
        # ligne 3 lot elements io (2e ligne nan, pran 10 fois 1e ligne nan (1e ligne nan egal a 1))
        layout.setRowStretch(1, 10)
        # methode sa pemet u di gridLayout la konbyn espas wap bay chak element
        # lipran an paramet indice colon nan epi groseu a
        # layout.setColumnStretch(0, 2)
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 3)
        # creating a form layout
        # pass_layout = QHBoxLayout()
        form_layout = QVBoxLayout()
        self.loginbtn = QPushButton("Sign in")
        self.loginbtn.setCursor(Qt.PointingHandCursor)
        self.loginbtn.setStyleSheet("color: white;\n"
                                    "    margin-top:15px;\n"
                                    "    height:50px;\n"
                                    "    width:100px;\n"
                                    "color:white;\n"
                                    "text-align:center;\n"
                                    "background-color:blue;\n"
                                    "border-radius:15px;\n"
                                    "font-size:18px;\n"
                                    )
        self.no_account_LYT = QHBoxLayout()
        self.no_account = QLabel("D`ont have an account?")
        self.no_account.setAlignment(QtCore.Qt.AlignCenter);
        self.no_account.setStyleSheet("font-size: 12px;\n"
                                      "    margin-top:10px;\n"
                                      "    text-align:center;\n"
                                      "    color: #1E1E1E;\n")
        self.inviteSignUpBtn = QPushButton("Create an account")
        self.inviteSignUpBtn.setCursor(Qt.PointingHandCursor)
        self.inviteSignUpBtn.setStyleSheet("font-size: 12px;\n"
                                           "    margin-top:10px;\n"
                                           "    text-align:center;\n"
                                           "    color: blue;\n")
        self.inviteSignUpBtn.clicked.connect(lambda: self.clallSignUpFunc())
        # create link back to login
        self.no_account_LYT.addWidget(self.no_account)
        self.no_account_LYT.addWidget(self.inviteSignUpBtn)
        form_layout.setAlignment(Qt.AlignTop)
        self.label_title = QLabel("Login Page")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter);
        self.label_title.setStyleSheet("    font-size: 20px;\n"
                                       "    font-weight:bold;\n"
                                       "    margin:10px 0px 35px 0px;\n"
                                       "    text-align:center;\n"
                                       "    color:blue;\n"
                                       )
        
        self.txtUsername = QLineEdit()
        self.txtPassword = QLineEdit()
        self.txtPassword.setEchoMode(QLineEdit.Password)
        # adding rows
        # for name and adding input text
        form_layout.addWidget(self.label_title)
        form_layout.addWidget(QLabel("User name"))
        form_layout.addWidget(self.txtUsername)
        form_layout.addWidget(QLabel("Password"))
        form_layout.addWidget(self.txtPassword)
        form_layout.addWidget(self.loginbtn)
        form_layout.addLayout(self.no_account_LYT)
        #     Setting layout
        rightside_layout.addLayout(form_layout)
        #
        self.content.setLayout(layout)
    def clalSignUpFunc(self):
        LoginView.close()
        # li dwe yon widget
        print("Siiiiiiiiiiiiiiiiiiiiiiiiiiiiignnnnnnnnnnnnnnnnnn UUUUUUUUUUUp")

    def loginControl(self):
        # TODO will be prepare infos to submit login in Model

        # fill
        self.to_login.username = self.txtUsername.text()
        self.to_login.password = self.txtPassword.text()

        # verify if user is sucessfully connected
        id_user_connected = self.to_login.check_user_connect()

        #
        self.clearFields()

    # def goToRegisterForm(self):
    #     # TODO will be ....
    #     gender = None
    #     errorMsg = ""

    #     self.to_register.username = self.txtUsername.text()
    #     self.to_register.lastname = self.txtLastname.text()
    #     self.to_register.firstname = self.txtFirstname.text()
    #     self.to_register.email = self.txtEmail.text()

    #     # save Gender
    #     if self.rdFemale.isChecked():
    #         gender = self.rdFemale.text()
    #     else:
    #         gender = self.rdMale.text()
    #     self.to_register.sexe = gender
    #     # end save Gender

    #     self.to_register.date_nais = self.txtDateOfBirth.date().toPyDate()
    #     self.to_register.tel = self.txtPhone.text()
    #     self.to_register.address = self.txtAddress.text()
    #     self.to_register.password = self.txtPassword.text()
    #     confirm_pwd= self.txtConfirmPassword.text()
    #     self.to_register.nif = self.txtNif.text()
        
    #     # before send | verify some things
    #     # check_email
    #     if self.util.check_email(self.to_register.email):
    #         # password
    #         if self.to_register.password == confirm_pwd:
    #             self.to_register.enregistrer()
    #             return True
    #         else:
    #             errorMsg="Password don't match"
    #     else:
    #         errorMsg="Email don't valid"
        
        
    #     # display error
    #     if errorMsg :
    #         QMessageBox.warning(
    #             None, "Error", errorMsg, QMessageBox.Ok)

    #     return False
        

    # def clearFields(self):
    #     # TODO will be clear all fields
    #     self.txtUsername.clear()
    #     self.txtFirstname.clear()
    #     self.txtLastname.clear()
    #     self.txtAddress.clear()
    #     self.txtEmail.clear()
    #     self.txtNif.clear()
    #     self.txtPhone.clear()
    #     self.txtDateOfBirth.clear()
    #     self.txtPassword.clear()
    #     self.rdFemale.setChecked(False)
    #     self.rdMale.setChecked(False)
