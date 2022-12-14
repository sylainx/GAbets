from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QWidget, QRadioButton, QRadioButton, QHBoxLayout, QVBoxLayout, QTabWidget, QFormLayout, QTableWidgetItem, QPushButton
from PyQt5.QtCore import Qt
# local package
from Models.LoginModel import LoginModel
from datetime import date


class LoginView(QDialog):
    to_login = LoginModel()

    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Login")
        self.setMinimumSize(600, 600)
        self.setMaximumSize(600, 600)
        self.setModal(True)
        # features
        self.createNewTab()
        self.createLoginForm()

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
        self.form = QFormLayout()
        self.form.setAlignment(Qt.AlignTop)

        hb_button = QHBoxLayout()
        hb_button.setAlignment(Qt.AlignTop)

        # push button
        # new
        self.btnSubmitLogin = QPushButton("Login")
        self.btnSubmitLogin.clicked.connect(self.loginControl)
        # save
        self.btnGoToRegister = QPushButton("Register")
        self.btnGoToRegister.clicked.connect(self.goToRegisterForm)
        # self.btnGoToRegister.setEnabled(False)

        # add push button to widget
        hb_button.addWidget(self.btnSubmitLogin)
        hb_button.addWidget(self.btnGoToRegister)

        self.rdStayConnect = QRadioButton("Oui")
        self.rdNotStayConnect = QRadioButton("Non")

        self.txtUsername = QLineEdit()
        self.txtPassword = QLineEdit()

        # add fields to Widget
        self.form.addRow("Username", self.txtUsername)
        self.form.addRow("Password", self.txtPassword)
        # button submit form
        self.form.addRow("", hb_button)

        main_login_layout.addLayout(self.form)
        self.wgLogin.setLayout(main_login_layout)

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
        pass

    def clearFields(self):
        # TODO will be clear all fields
        self.txtUsername.clear()
        self.txtPassword.clear()
