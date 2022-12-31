from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from Helpers.Helpers import Helpers

from views.AuthView import AuthView
# models
from Models.LoginModel import LoginModel


class AuthController():

    def __init__(self, parent) -> None:
        self.parent = parent
        # views
        self.authView = AuthView()
        # models
        self.login_model = LoginModel()
        self.isSignUp = False
        # helpers
        self.util = Helpers()

    def start(self, ):
        self.authView.show()
        self.toggleAuthScreen()
    # end start Controller

    def toggleAuthScreen(self):
        if not self.isSignUp:
            self.setupLoginFunc()
        else:
            self.setupRegisterFunc()

        print(f"IS SIGNUP: {self.isSignUp}")
    # end toggleAuthScreen()

    def setupLoginFunc(self):
        self.authView.displayLogin()
        print("Mwen nan setupL")
        # invite
        self.authView.inviteSignUpBtn.clicked.connect(
            lambda: self.toggle())

        self.authView.login_QPB.clicked.connect(lambda: self.loginTraitement())

    # end setupLoginFunc()

    def setupRegisterFunc(self):
        self.authView.displayRegister()
        # invite login
        self.authView.inviteLogin_QPB.clicked.connect(lambda: self.toggle())
    # end setupRegisterFunc()

    def toggle(self):
        self.isSignUp = not self.isSignUp
        self.toggleAuthScreen()

    # ===================   T R A I T E M E N T S   L O G I N   ======================#

    def loginTraitement(self):
        username = self.authView.txtUsername_QLE.text()
        password = self.authView.txtPassword_QLE.text()

        validation = self.validateLogin(username, password)

        if validation:
            
            self.login_model.username = username
            self.login_model.password = password
            isConnexionSuccess= self.login_model.check_user_connect()
            print(f"IS SUCCESS: {isConnexionSuccess}")

    def validateLogin(self, username: str, password: str):
        result = False
        if self.util.is_not_empty(username) and self.util.valid_str(username):

            if self.util.validate_password(password):
                result = True
            else:
                self.authView.lbl_errorMessage.setText(
                    f"Veuillez entrer un mot de passe correct")
                self.authView.lbl_errorMessage.setVisible(True)
        else:
            self.authView.lbl_errorMessage.setText(
                f"Veuillez entrer un username correct")
            self.authView.lbl_errorMessage.setVisible(True)
            

        return result

    # ===================   T R A I T E M E N T S   R E G I S T E R   ======================#

    def signUpTraitement(self):
        pass
