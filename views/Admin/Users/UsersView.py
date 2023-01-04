from PyQt5 import QtCore, QtGui, QtWidgets
from Helpers.Helpers import Helpers
from PyQt5.QtWidgets import QLabel, QRadioButton, QDateEdit, QLineEdit,QWidget


class UsersView(QtWidgets.QWidget):

    def __init__(self, parent=None) -> None:
        super().__init__()
        self.setWindowTitle("Users")
        self.setMinimumSize(100, 600)
        self.setMaximumSize(600, 600)
        self.centerWidget()
        # self.move(parent.rect().center())
        self.setGeometry(
            QtCore.QRect(0, 96, 16777214, 16777214))
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
        self.formLayout.setAlignment(QtCore.Qt.AlignTop)

        self.text_userLayout = QtWidgets.QVBoxLayout()
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
        self.text_userLayout.addWidget(QLabel(" First name"))
        self.text_userLayout.addWidget(self.txtFirstName)
        self.text_userLayout.addWidget(QLabel("Last name"))
        self.text_userLayout.addWidget(self.txtLastName)
        self.text_userLayout.addWidget(QLabel("User name"))
        self.text_userLayout.addWidget(self.txtUsername)
        self.text_userLayout.addWidget(QLabel("User Email"))
        self.text_userLayout.addWidget(self.txtEmail)
        self.text_userLayout.addWidget(QLabel("user Adress"))
        self.text_userLayout.addWidget(self.txtAdress)
        self.text_userLayout.addWidget(QLabel("user Phone"))
        self.text_userLayout.addWidget(self.txtPhone)
        self.text_userLayout.addWidget(QLabel("Sexe"))
        self.text_userLayout.addLayout(self.q_gender_LYT)
        self.text_userLayout.addWidget(QLabel("Date of birth"))
        self.text_userLayout.addWidget(self.txtDateOfBirth)

        self.text_userLayout.addWidget(QLabel("user Nif"))
        self.text_userLayout.addWidget(self.txtNif)


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

        # load image
        # pixmap = QtGui.QPixmap("./assets/images/teams/fcb.png")
        
        # # Création du widget qui affichera l'image
        # self.imgText_QLB.setText("Image")
        # self.img_QLB.setPixmap(pixmap)

        # self.title_LBL.setText("Titre")
        # self.level_LBL.setText("Niveau")
        # self.teamCategory_LBL.setText("Categorie d'equipe")
        # # list combobox
        # level_list = list(["10", "100", "1000"])
        # self.level_CBB.addItems(level_list)
        # self.level_CBB.setStyleSheet("color: #FAFAFA;\n"
        #                             "background-color: #2C2C2C;\n"
        #                            "border-radius: 10px;\n"
        #                            "padding: 10px 15px;")

        # # type de matchs
        # self.groupTeamCategory = QtWidgets.QListWidget()
        # self.groupTeamCategory.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)    
        
        # self.vLayout4ChBx = QtWidgets.QVBoxLayout()
    
        # # self.vLayout4ChBx.addWidget(self.teamCategory_CHB)

        # # action btn        
        # hLayout4Btn = QtWidgets.QHBoxLayout()
        
        # self.saveBtn = QtWidgets.QPushButton("Enregistrer")
        # self.saveBtn.setStyleSheet("background-color: #106327;\n"
        #                            "color: #FAFAFA;\n"
        #                            "border-radius: 10px;\n"
        #                            "padding: 10px 15px;")
        # self.updateBtn = QtWidgets.QPushButton("Modifier")
        # self.updateBtn.setEnabled(False)
        # self.updateBtn.setStyleSheet("background-color: #2C2C2C;\n"
        #                            "color: #FAFAFA;\n"
        #                            "border-radius: 10px;\n"
        #                            "padding: 10px 15px;")
        # self.deleteBtn = QtWidgets.QPushButton("Supprimer")
        # self.deleteBtn.setStyleSheet("background-color: #2C2C2C;\n"
        #                            "color: #FAFAFA;\n"
        #                            "border-radius: 10px;\n"
        #                            "padding: 10px 15px;")
        # self.deleteBtn.setEnabled(False)
        # # add btn horizontal
        # hLayout4Btn.addWidget(self.saveBtn)
        # hLayout4Btn.addWidget(self.updateBtn)
        # hLayout4Btn.addWidget(self.deleteBtn)
        
        # # add QLineEdit & QComboBox to formLayout
        # self.formLayout.addWidget(self.imgText_QLB)
        # self.formLayout.addWidget(self.img_QLB)
        # self.formLayout.addWidget(self.title_LBL)
        # self.formLayout.addWidget(self.title_QLE)
        # self.formLayout.addWidget(self.level_LBL)
        # self.formLayout.addWidget(self.level_CBB)
        # self.formLayout.addWidget(self.teamCategory_LBL)
        # self.formLayout.addLayout(self.vLayout4ChBx)
        # self.formLayout.addLayout(hLayout4Btn)

        # add form layout to central Layout
        mainLayout.addLayout(self.text_userLayout)
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
        self.table_WDG.cellClicked.connect(lambda:self.eventOnTable())
        self.formLayout.addWidget(self.table_WDG)

    
    def loadDatas(self,list):

        # image to load
        imgTable_LBL = QtWidgets.QLabel()
        # end image to load
        self.table_WDG.setRowCount(len(list))
        self.table_WDG.setStyleSheet(
          "background-color: #2C2C2C;\n"
           "color: #42b883;\n"
           
        )
        row=0
        for i in list:
            # imgTable_LBL.setPixmap(QtGui.QPixmap(str(i[1])))
            # self.table_WDG.setItem(row,0,QtWidgets.QTableWidgetItem(imgTable_LBL))
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


    def eventOnTable(self):
        index=self.table_WDG.currentRow()
        
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


    # def listTypeOfMatch(self, list):

    #     for row in list:
    #         id, title, ratio, visible = row
    #         self.el_ChBx = QtWidgets.QListWidgetItem(f"{title}")
    #         self.el_ChBx.setBackground(QtGui.QColor("#2C2C2C"))
    #         self.el_ChBx.setForeground(QtGui.QColor("#FAFAFA"))
            
    #         # self.el_ChBx.setObjectName(f"{title}")
    #         self.groupTeamCategory.addItem(self.el_ChBx)
    #         self.vLayout4ChBx.addWidget(self.groupTeamCategory)
    #     # end listTypeMatch
