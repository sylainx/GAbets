from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QWidget, QRadioButton, QRadioButton, QHBoxLayout, QVBoxLayout, QTabWidget, QFormLayout, QTableWidgetItem, QPushButton, QDateEdit
from PyQt5.QtCore import Qt
# local package
from Models.LoginModel import LoginModel
from Models.RegisterModel import RegisterModel
from Helpers.Helpers import Helpers
from datetime import date


class LoginView(QDialog):
    to_login = LoginModel()
    to_register = RegisterModel()
    util = Helpers()

    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Login")
        self.setMinimumSize(600, 600)
        self.setMaximumSize(600, 600)
        self.setModal(True)
        # features
        self.createNewTab()
        self.createLoginForm()
        self.createRegisterForm()

    # end init

    def createNewTab(self):
        main_layout = QHBoxLayout()
        # table widget
        self.tabWidget = QTabWidget()
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)

        # widget
        self.wgLogin = QWidget()
        self.wgRegister = QWidget()

        # add widgets in Tab
        self.tabWidget.addTab(self.wgLogin, "Login")
        self.tabWidget.addTab(self.wgRegister, "Register")

        #
        main_layout.addWidget(self.tabWidget)
        self.setLayout(main_layout)
    # end createNewTab

    def createLoginForm(self):
        # create gridFormLayout
        main_login_layout = QVBoxLayout()

        # create gridFormLayout
        self.form_LYT = QFormLayout()
        self.form_LYT.setAlignment(Qt.AlignTop)

        hb_button_LYT = QHBoxLayout()
        hb_button_LYT.setAlignment(Qt.AlignTop)

        # push button
        # login button
        self.btnSubmitLogin = QPushButton("Login")
        self.btnSubmitLogin.clicked.connect(self.loginControl)
        # register
        self.btnGoToRegister = QPushButton("Register")
        self.btnGoToRegister.clicked.connect(self.goToRegisterForm)
        # self.btnGoToRegister.setEnabled(False)

        # add push button to widget
        hb_button_LYT.addWidget(self.btnSubmitLogin)
        hb_button_LYT.addWidget(self.btnGoToRegister)

        self.txtUsername = QLineEdit()
        self.txtPassword = QLineEdit()

        # add fields to Widget
        self.form_LYT.addRow("Username", self.txtUsername)
        self.form_LYT.addRow("Password", self.txtPassword)
        # button submit form
        self.form_LYT.addRow("", hb_button_LYT)

        main_login_layout.addLayout(self.form_LYT)
        self.wgLogin.setLayout(main_login_layout)

    # end createLoginFunc()

    def createRegisterForm(self):

        # define main Layouts
        main_login_layout = QVBoxLayout()

        # create gridFormLayout
        self.form_LYT = QFormLayout()
        self.form_LYT.setAlignment(Qt.AlignTop)

        hb_button_LYT = QHBoxLayout()
        hb_button_LYT.setAlignment(Qt.AlignTop)
        # radioButton Layouts
        q_gender_LYT = QHBoxLayout()

        # push button
        # Register
        self.btnGoToRegister = QPushButton("Register")
        self.btnGoToRegister.clicked.connect(self.goToRegisterForm)
        # self.btnGoToRegister.setEnabled(False)
        # login Button
        self.btnSubmitLogin = QPushButton("Login")
        self.btnSubmitLogin.clicked.connect(self.loginControl)

        # add push button to button layout widget
        hb_button_LYT.addWidget(self.btnGoToRegister)
        hb_button_LYT.addWidget(self.btnSubmitLogin)

        # add radioButton to Widget
        self.rdMale = QRadioButton("Masculin")
        self.rdFemale = QRadioButton("Feminin")
        q_gender_LYT.addWidget(self.rdFemale)
        q_gender_LYT.addWidget(self.rdMale)

        # Add date
        self.txtDateOfBirth = QDateEdit()
        self.txtDateOfBirth.setDisplayFormat("dd/MM/yyyy")
        self.txtDateOfBirth.setCalendarPopup(True)

        self.txtFirstname = QLineEdit()
        self.txtUsername = QLineEdit()
        self.txtLastname = QLineEdit()
        self.txtEmail = QLineEdit()
        self.txtPhone = QLineEdit()
        self.txtAddress = QLineEdit()
        self.txtNif = QLineEdit()
        self.txtPassword = QLineEdit()
        self.txtConfirmPassword = QLineEdit()

        # add fields to Widget
        self.form_LYT.addRow("Username", self.txtUsername)
        self.form_LYT.addRow("Lastname", self.txtLastname)
        self.form_LYT.addRow("Firstname", self.txtFirstname)
        self.form_LYT.addRow("Email", self.txtEmail)
        self.form_LYT.addRow("Phone", self.txtPhone)
        self.form_LYT.addRow("Address", self.txtAddress)
        self.form_LYT.addRow("Sexe", q_gender_LYT)
        self.form_LYT.addRow("Date of birth", self.txtDateOfBirth)
        self.form_LYT.addRow("Nif", self.txtNif)
        self.form_LYT.addRow("Password", self.txtPassword)
        self.form_LYT.addRow("ConfirmPassword", self.txtConfirmPassword)
        # button submit form
        self.form_LYT.addRow("", hb_button_LYT)

        main_login_layout.addLayout(self.form_LYT)
        self.wgRegister.setLayout(main_login_layout)

    # end createLoginFunc()

    def loginControl(self):
        # TODO will be prepare infos to submit login in Model

        # fill
        self.to_login.username = self.txtUsername.text()
        self.to_login.password = self.txtPassword.text()

        # verify if user is sucessfully connected
        id_user_connected = self.to_login.check_user_connect()

        #
        self.clearFields()

    def goToRegisterForm(self):
        # TODO will be ....
        gender = None
        errorMsg = ""

        self.to_register.username = self.txtUsername.text()
        self.to_register.lastname = self.txtLastname.text()
        self.to_register.firstname = self.txtFirstname.text()
        self.to_register.email = self.txtEmail.text()

        # save Gender
        if self.rdFemale.isChecked():
            gender = self.rdFemale.text()
        else:
            gender = self.rdMale.text()
        self.to_register.sexe = gender
        # end save Gender

        self.to_register.date_nais = self.txtDateOfBirth.date().toPyDate()
        self.to_register.tel = self.txtPhone.text()
        self.to_register.address = self.txtAddress.text()
        self.to_register.password = self.txtPassword.text()
        confirm_pwd= self.txtConfirmPassword.text()
        self.to_register.nif = self.txtNif.text()
        
        # before send | verify some things
        # check_email
        if self.util.check_email(self.to_register.email):
            # password
            if self.to_register.password == confirm_pwd:
                self.to_register.enregistrer()
                return True
            else:
                errorMsg="Password don't match"
        else:
            errorMsg="Email don't valid"
        
        

        # display error
        if errorMsg :
            QMessageBox.warning(
                None, "Error", errorMsg, QMessageBox.Ok)

        return False
        

    def clearFields(self):
        # TODO will be clear all fields
        self.txtUsername.clear()
        self.txtFirstname.clear()
        self.txtLastname.clear()
        self.txtAddress.clear()
        self.txtEmail.clear()
        self.txtNif.clear()
        self.txtPhone.clear()
        self.txtDateOfBirth.clear()
        self.txtPassword.clear()
        self.rdFemale.setChecked(False)
        self.rdMale.setChecked(False)
