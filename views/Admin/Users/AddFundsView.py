from PyQt5 import QtCore, QtGui, QtWidgets
from Helpers.Helpers import Helpers

class AddFundsView(QtWidgets.QDialog):

    def __init__(self, parent=None) -> None:
        super().__init__()
        self.setWindowTitle("Users")
        self.setMinimumSize(300, 200)
        self.setMaximumSize(350, 250)
        self.centerWidget()
        # self.move(parent.rect().center())
        # self.setGeometry(
        #     QtCore.QRect(0, 96, 16777214, 16777214))
        # self.setModal(True)
        self.setStyleSheet("background: #2C2C2C")
        
        # call methods
        self.ui()
        self.createFormRegister()
        

    def centerWidget(self):	
        # Ajout de cette méthode pour centrer la fenêtre        
        frameGm = self.frameGeometry()        
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())        
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()        
        frameGm.moveCenter(centerPoint)        
        self.move(frameGm.topLeft())
    # end centerWidget


    def ui(self):
        mainLayout = QtWidgets.QVBoxLayout()

        # add another widget to contain tabs value
        self.mainContainer_WDG = QtWidgets.QTabWidget()
        # add mainContainer_WDG to main main widget
        mainLayout.addWidget(self.mainContainer_WDG)
        
        self.setLayout(mainLayout)


    def createFormRegister(self):
        # layout
        mainLayout = QtWidgets.QVBoxLayout()
        
        #
        self.formLayout = QtWidgets.QVBoxLayout()
        self.formLayout.setAlignment(QtCore.Qt.AlignTop)
        
        self.vLayout_Form = QtWidgets.QVBoxLayout()
        # =========== fields for add fund
        doubleValidator = QtGui.QDoubleValidator()
        self.lbl_code_user = QtWidgets.QLabel("Code de l'utilisateur:")
        self.lbl_code_user.setStyleSheet("color:#FAFAFA")
        self.code_user_QLE = QtWidgets.QLineEdit()
        self.code_user_QLE.setStyleSheet("color:#FAFAFA; height: 60px; border: 1px solid #FAFAFA; border-radius:5px;")
        self.lbl_amount_increase = QtWidgets.QLabel("Montant de la recharge:")
        self.lbl_amount_increase.setStyleSheet("color:#FAFAFA")
        self.amount_increase_QLE = QtWidgets.QLineEdit()
        self.amount_increase_QLE.setValidator(doubleValidator)
        self.amount_increase_QLE.setStyleSheet("color:#FAFAFA; height: 60px; border: 1px solid #FAFAFA; border-radius:5px;")
        
        # add to layout
        self.vLayout_Form.addWidget(self.lbl_code_user)
        self.vLayout_Form.addWidget(self.code_user_QLE)        
        self.vLayout_Form.addWidget(self.lbl_amount_increase)
        self.vLayout_Form.addWidget(self.amount_increase_QLE)
        
         # action btn        
        self.hLayout4Btn = QtWidgets.QHBoxLayout()
        
        self.btn_increase_amount_QPB = QtWidgets.QPushButton("Enregistrer")
        self.btn_increase_amount_QPB.setStyleSheet("background-color: #106327;\n"
                                   "color: #FAFAFA;\n"
                                   "border-radius: 10px;\n"
                                   "padding: 10px 15px;")
                                   
        # add btn horizontal
        self.hLayout4Btn.addWidget(self.btn_increase_amount_QPB)
        
        # create elements will be in the forms

        # add form layout to central Layout
        mainLayout.addLayout(self.vLayout_Form)
        mainLayout.addLayout(self.hLayout4Btn)
        mainLayout.addLayout(self.formLayout)
        self.mainContainer_WDG.setLayout(mainLayout)

    def clearFields(self):
        # TODO will be clear all fields
        self.code_user_QLE.clear()
        self.amount_increase_QLE.clear()

