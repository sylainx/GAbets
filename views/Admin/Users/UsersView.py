from PyQt5 import QtCore, QtGui, QtWidgets
from Helpers.Helpers import Helpers
from PyQt5.QtWidgets import QLabel, QRadioButton, QDateEdit, QLineEdit,QWidget


class UsersView(QtWidgets.QDialog):

    def __init__(self, parent=None) -> None:
        super().__init__()
        self.setWindowTitle("Users")
        self.setMinimumSize(750,640)
        self.setMaximumSize(1200, 700)
        self.centerWidget()
        
        # self.setModal(True)
        self.setStyleSheet("background-color: #1E1E1E"
        "QLabel{\n"
            " \"JetBrains Mono\";\n"
            "    color: #1E1E1E\n"
            "}\n"
            "\n"
            "QLineEdit{\n"
            "    border: 1px solid white;\n"
            "}\n"
            "QLineEdit:focus{\n"
            "    border:0px solid white\n"
            "}\n")
        
        self.imgText_QLB = QtWidgets.QLabel()
        self.img_QLB = QtWidgets.QLabel()
        self.title_LBL = QtWidgets.QLabel()
        self.title_QLE = QtWidgets.QLineEdit()    
        self.level_LBL = QtWidgets.QLabel()
        self.level_CBB = QtWidgets.QComboBox()
        self.teamCategory_LBL = QtWidgets.QLabel()
        # self.teamCategory_CHB = QtWidgets.QCheckBox()

        # call methods
        self.ui()
        self.createFormRegister()
        self.listOfDatas()


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
        # self.formLayout.setAlignment(QtCore.Qt.AlignTop)
        gridLayout = QtWidgets.QGridLayout()

        self.vLyt_FormView = QtWidgets.QVBoxLayout()
        self.q_gender_LYT = QtWidgets.QHBoxLayout()
        # add radioButton to Widget
        self.rdMale = QRadioButton("Masculin")
        self.rdFemale = QRadioButton("Feminin")
        
        self.q_gender_LYT.addWidget(self.rdFemale)
        self.q_gender_LYT.addWidget(self.rdMale)
        # Create date
        self.txtDateOfBirth = QDateEdit()
        self.txtDateOfBirth.setDisplayFormat("dd/MM/yyyy")
        self.txtDateOfBirth.setCalendarPopup(True)
        self.txtDateOfBirth.setStyleSheet(
            "color: #2C2C2C;\n"
        )

        self.txtCode = QLineEdit()
        self.txtCode.setEnabled(False)
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
        gridLayout.addWidget(QLabel(" First name"), 0,0)
        gridLayout.addWidget(self.txtFirstName, 0,1)
        gridLayout.addWidget(QLabel("Last name"), 0,2)
        gridLayout.addWidget(self.txtLastName, 0,3)

        gridLayout.addWidget(QLabel("User name"), 1,0)
        gridLayout.addWidget(self.txtUsername, 1,1)
        gridLayout.addWidget(QLabel("User Email"),1,2)
        gridLayout.addWidget(self.txtEmail,1,3)

        gridLayout.addWidget(QLabel("user Adress"),2,0)
        gridLayout.addWidget(self.txtAdress,2,1)
        gridLayout.addWidget(QLabel("user Phone"),2,2)
        gridLayout.addWidget(self.txtPhone,2,3)
        
        gridLayout.addWidget(QLabel("Sexe"),3,0)
        gridLayout.addLayout(self.q_gender_LYT,3,1)

        gridLayout.addWidget(QLabel("Date of birth"),4,0)
        gridLayout.addWidget(self.txtDateOfBirth,4,1)
        gridLayout.addWidget(QLabel("user Nif"),4,2)
        gridLayout.addWidget(self.txtNif,4,3)
        # grid
        self.vLyt_FormView.addLayout(gridLayout)


         # action btn        
        self.hLayout4Btn = QtWidgets.QHBoxLayout()
        
        self.saveBtn = QtWidgets.QPushButton("Enregistrer")
        self.saveBtn.setStyleSheet("background-color: #106327;\n"
                                   "color: #FAFAFA;\n"
                                   "border-radius: 10px;\n"
                                   "padding: 10px 15px;")
        self.updateBtn = QtWidgets.QPushButton("Modifier")
        self.updateBtn.setEnabled(False)
        self.updateBtn.setStyleSheet("background-color: #2C2C2C;\n"
                                   "color: #FAFAFA;\n"
                                   "border-radius: 10px;\n"
                                   "padding: 10px 15px;")
        self.deleteBtn = QtWidgets.QPushButton("Supprimer")
        self.deleteBtn.setStyleSheet("background-color: #2C2C2C;\n"
                                   "color: #FAFAFA;\n"
                                   "border-radius: 10px;\n"
                                   "padding: 10px 15px;")
        self.deleteBtn.setEnabled(False)
        # add btn horizontal
        self.hLayout4Btn.addWidget(self.saveBtn)
        self.hLayout4Btn.addWidget(self.updateBtn)
        self.hLayout4Btn.addWidget(self.deleteBtn)
        # create elements will be in the forms

       

        # add form layout to central Layout
        mainLayout.addLayout(self.vLyt_FormView)
        mainLayout.addLayout(self.hLayout4Btn)
        mainLayout.addLayout(self.formLayout)
       
        self.mainContainer_WDG.setLayout(mainLayout)

    def clearFields(self):
        # TODO will be clear all fields
        self.title_QLE.clear()
        self.level_CBB.setCurrentIndex(0)



    def listOfDatas(self):
        
        self.table_WDG = QtWidgets.QTableWidget()
        header=("ID","firstname","lastname","email","tel", "code_user","Adresse","Username","NIF","Sexe","DateNaissance")
        
        self.table_WDG.setColumnCount(len(header))
        self.table_WDG.setHorizontalHeaderLabels(header)
        # add a signal on the QTableWidget
        self.formLayout.addWidget(self.table_WDG)

    
    def loadDatas(self,list):

        # end image to load
        self.table_WDG.setRowCount(len(list))
        self.table_WDG.setStyleSheet(
          "background-color: #2C2C2C;\n"
           "color: #42b883;\n")
        row=0
        print(f"ROW: {list}")
        
        for i in list:
            self.table_WDG.setItem(row, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.table_WDG.setItem(row, 1, QtWidgets.QTableWidgetItem(str(i[1])))
            self.table_WDG.setItem(row, 2, QtWidgets.QTableWidgetItem(str(i[2])))         
            self.table_WDG.setItem(row, 3, QtWidgets.QTableWidgetItem(str(i[3])))         
            self.table_WDG.setItem(row, 4, QtWidgets.QTableWidgetItem(str(i[4])))         
            self.table_WDG.setItem(row, 5, QtWidgets.QTableWidgetItem(str(i[5])))         
            self.table_WDG.setItem(row, 6, QtWidgets.QTableWidgetItem(str(i[6])))         
            self.table_WDG.setItem(row, 7, QtWidgets.QTableWidgetItem(str(i[7])))         
            self.table_WDG.setItem(row, 8, QtWidgets.QTableWidgetItem(str(i[8])))         
            self.table_WDG.setItem(row, 9, QtWidgets.QTableWidgetItem(str(i[9])))         
            self.table_WDG.setItem(row, 10, QtWidgets.QTableWidgetItem(str(i[10])))         
            row+=1


    def changeBtnColor(self):
        
        self.saveBtn.setEnabled(False)
        self.saveBtn.setStyleSheet("background-color: #2C2C2C;\n"
                                   "color: #FAFAFA;\n"
                                   "border-radius: 10px;\n"
                                   "padding: 10px 15px;")
        # don't work for now
        # self.updateBtn.setEnabled(True)
        self.updateBtn.setStyleSheet("background-color: #106327;\n"
                                   "color: #FAFAFA;\n"
                                   "border-radius: 10px;\n"
                                   "padding: 10px 15px;")
        # don't work for now
        # self.deleteBtn.setEnabled(True)
        self.deleteBtn.setStyleSheet("background-color: #E62641;\n"
                                   "color: #FAFAFA;\n"
                                   "border-radius: 10px;\n"
                                   "padding: 10px 15px;")                           

      
    # 
