from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from Helpers.Helpers import Helpers

from views.AuthView import AuthView
# models
from Models.LoginModel import LoginModel
from Models.RegisterModel import RegisterModel

class AuthController():

    def __init__(self, parent) -> None:
        self.parent = parent
        # views
        self.authView = AuthView()
        # models
        self.login_model = LoginModel()
        self.register_model = RegisterModel()
        self.isSignUp = False
        # helpers
        self.util = Helpers()

    def start(self, ):
        self.authView.show()
        self.toggleAuthScreen()
    # end start Controller

    def endAuth(self):
        self.authView.close()
        # is define in parent (__init__.py)
        self.parent.connected_user=True
        self.parent.user_id=self.user_id
        # end define in parent
        self.parent.toggleConnection()
    # end auth

    def toggleAuthScreen(self):
        if not self.isSignUp:
            self.setupLoginFunc()
        else:
            self.setupRegisterFunc()

    # end toggleAuthScreen()

    def setupLoginFunc(self):
        self.authView.displayLogin()
        
        # invite
        self.authView.inviteSignUpBtn.clicked.connect(
            lambda: self.toggle())

        self.authView.login_QPB.clicked.connect(lambda: self.loginTraitement())

    # end setupLoginFunc()

    def setupRegisterFunc(self):
        self.authView.displayRegister()
        # invite login
        self.authView.inviteLogin_QPB.clicked.connect(lambda: self.toggle())

        self.authView.loginbtn.clicked.connect(lambda: self.signUpTraitement())
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
            if isConnexionSuccess:
                self.user_id = isConnexionSuccess
                self.endAuth()

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
        firstname = self.authView.txtFirstName.text()
        lastname = self.authView.txtLastName.text()
        email = self.authView.txtEmail.text()
        tel = self.authView.txtPhone.text()
        adresse = self.authView.txtAdress.text()
        username = self.authView.txtUsername.text()
        nif = self.authView.txtNif.text()
        sexe = None
        if self.authView.rdFemale.isChecked():
            sexe = self.authView.rdFemale.text()
        else:
            sexe = self.authView.rdMale.text()

        dateNais = self.authView.txtDateOfBirth.date().toPyDate()
        password = self.authView.txtPassword_QLE.text()
        confirmpasswrd = self.authView.txtConfirmPassword.text()
        
        validation = self.validationSignUp(firstname, lastname, email, tel, adresse ,username, nif, sexe,dateNais, password,confirmpasswrd)
        
        if validation:
            self.register_model.firstname = firstname
            self.register_model.lastname = lastname
            self.register_model.username = username
            self.register_model.email = email
            self.register_model.sexe = sexe
            self.register_model.date_nais = dateNais
            self.register_model.tel = tel
            self.register_model.address = adresse
            self.register_model.nif = nif
            self.register_model.password = password
            isConnexionSuccess= self.register_model.enregistrer()
            
            if isConnexionSuccess:
                self.user_id = isConnexionSuccess
                self.endAuth()

    def validationSignUp(self, firstname: str, lastname: str, email: str, tel: str, adresse: str, username: str, nif: str, sexe: str ,datenaiss: str,password : str, confirmpasswrd: str ):
        result = False
        if self.util.is_not_empty(username) and self.util.valid_str(username):
            if self.util.validate_password(password):
                result = True
            else:
                self.authView.lbl_errorMessage.setText(
                    f"Veuillez entrer un mot de passe correct")
                self.authView.lbl_errorMessage.setVisible(True)
            if self.util.validate_password(password) == self.util.validate_password(confirmpasswrd):
                result = True
            else:
                self.authView.lbl_errorMessage.setText(
                    f" les mots de passe ne correspondent pas")
                self.authView.lbl_errorMessage.setVisible(True)
        else:
           self.authView.lbl_errorMessage.setText(
                f"Veuillez entrer un username correct ")
           self.authView.lbl_errorMessage.setVisible(True) 
        if self.util.is_not_empty(firstname) and self.util.valid_str(firstname):
            result = True
        else:
           self.authView.lbl_errorMessage.setText(
                f"Veuillez entrer un firstname correct ")
        if self.util.is_not_empty(lastname) and self.util.valid_str(lastname):
            result = True
        else:
           self.authView.lbl_errorMessage.setText(
                f"Veuillez entrer un lastname correct ")
        if self.util.is_not_empty(email) and self.util.valid_str(email):
            result = True
        else:
           self.authView.lbl_errorMessage.setText(
                f"Veuillez entrer un email correct ")
        if self.util.is_not_empty(tel) and self.util.valid_str(tel):
            result = True
        else:
           self.authView.lbl_errorMessage.setText(
                f"Veuillez entrer un telephone correct ")
        if self.util.is_not_empty(adresse) and self.util.valid_str(adresse):
            result = True
        else:
           self.authView.lbl_errorMessage.setText(
                f"Veuillez entrer un adresse correct ")
        if self.util.is_not_empty(nif) and self.util.valid_str(nif):
            result = True
        else:
           self.authView.lbl_errorMessage.setText(
                f"Veuillez entrer un Nif correct ")
        if self.util.is_not_empty(sexe) and self.util.valid_str(sexe):
            result = True
        else:
           self.authView.lbl_errorMessage.setText(
                f"Veuillez entrer un sexe correct ")

        return result