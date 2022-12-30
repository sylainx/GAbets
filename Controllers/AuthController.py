from PyQt5 import QtWidgets, QtCore, QtGui
import sys

from views.LoginView import LoginView
# models
from Models.LoginModel import LoginModel


class AuthController():

    def __init__(self, parent) -> None:
        self.parent = parent
        # views
        self.loginView = LoginView()
        # models
        self.login_model = LoginModel()

    def start(self, ):
        self.loginView.show()
        self.loginView.displayLogin()
        # self.loginView.displayRegister()

        # self.loginView.inviteSignUpBtn.clicked.connect(
        #     lambda: self.callSignUpFunc())

    # end start Controller

    def callSignUpFunc(self):
        self.loginView.close()
        # self.
