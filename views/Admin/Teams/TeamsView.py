from PyQt5 import QtCore, QtGui, QtWidgets
from Helpers.Helpers import Helpers


class TeamsView(QtWidgets.QDialog):

    def __init__(self, parent=None) -> None:
        super().__init__()
        self.setWindowTitle("Team")
        self.setMinimumSize(100, 600)
        self.setMaximumSize(600, 600)
        self.centerWidget()
        # self.move(parent.rect().center())
        self.setGeometry(
            QtCore.QRect(0, 96, 16777214, 16777214))
        # self.setModal(True)
        self.setStyleSheet("background-color: #1E1E1E")
        
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

        # create elements will be in the forms

        # load image
        pixmap = QtGui.QPixmap("./assets/images/teams/fcb.png")
        
        # Création du widget qui affichera l'image
        self.imgText_QLB.setText("Image")
        self.img_QLB.setPixmap(pixmap)

        self.title_LBL.setText("Titre")
        self.title_LBL.setStyleSheet("color: #FAFAFA")
        self.level_LBL.setText("Niveau")
        self.level_CBB.setStyleSheet("color: #FAFAFA")
        self.teamCategory_LBL.setText("Categorie d'equipe")
        self.teamCategory_LBL.setStyleSheet("color: #FAFAFA")
        # list combobox
        level_list = list(["10", "100", "1000"])
        self.level_CBB.addItems(level_list)
        self.level_CBB.setStyleSheet("color: #FAFAFA;\n"
                                    "background-color: #2C2C2C;\n"
                                   "border-radius: 10px;\n"
                                   "padding: 10px 15px;")

        # type de matchs
        self.groupTeamCategory = QtWidgets.QListWidget()
        self.groupTeamCategory.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)    
        
        self.vLayout4ChBx = QtWidgets.QVBoxLayout()
    
        # self.vLayout4ChBx.addWidget(self.teamCategory_CHB)

        # action btn        
        hLayout4Btn = QtWidgets.QHBoxLayout()
        
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
        hLayout4Btn.addWidget(self.saveBtn)
        hLayout4Btn.addWidget(self.updateBtn)
        hLayout4Btn.addWidget(self.deleteBtn)
        
        # add QLineEdit & QComboBox to formLayout
        # self.formLayout.addWidget(self.imgText_QLB)
        # self.formLayout.addWidget(self.img_QLB)
        self.formLayout.addWidget(self.title_LBL)
        self.formLayout.addWidget(self.title_QLE)
        self.formLayout.addWidget(self.level_LBL)
        self.formLayout.addWidget(self.level_CBB)
        self.formLayout.addWidget(self.teamCategory_LBL)
        self.formLayout.addLayout(self.vLayout4ChBx)
        self.formLayout.addLayout(hLayout4Btn)

        # add form layout to central Layout
        mainLayout.addLayout(self.formLayout)
        self.mainContainer_WDG.setLayout(mainLayout)

    def clearFields(self):
        # TODO will be clear all fields
        self.title_QLE.clear()
        self.level_CBB.setCurrentIndex(0)



    def listOfDatas(self):
        
        self.table_WDG = QtWidgets.QTableWidget()
        header=("ID","Nom de l'équipe","Niveau")

        self.table_WDG.setColumnCount(len(header))
        self.table_WDG.setHorizontalHeaderLabels(header)
        self.table_WDG.setStyleSheet("color: #FAFAFA")
        # add a signal on the QTableWidget
        self.table_WDG.cellClicked.connect(lambda:self.eventOnTable())
        self.formLayout.addWidget(self.table_WDG)

    
    def loadDatas(self,list):

        # image to load
        imgTable_LBL = QtWidgets.QLabel()
        # end image to load
        self.table_WDG.setRowCount(len(list))
        row=0
        for i in list:
            # imgTable_LBL.setPixmap(QtGui.QPixmap(str(i[1])))
            # self.table_WDG.setItem(row,0,QtWidgets.QTableWidgetItem(imgTable_LBL))
            self.table_WDG.setItem(row, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.table_WDG.setItem(row, 1, QtWidgets.QTableWidgetItem(str(i[2])))
            self.table_WDG.setItem(row, 2, QtWidgets.QTableWidgetItem(str(i[3])))         
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


    def listTypeOfMatch(self, list):

        for row in list:
            id, title, ratio, visible = row
            self.el_ChBx = QtWidgets.QListWidgetItem(f"{title}")
            self.el_ChBx.setBackground(QtGui.QColor("#2C2C2C"))
            self.el_ChBx.setForeground(QtGui.QColor("#FAFAFA"))
            
            # self.el_ChBx.setObjectName(f"{title}")
            self.groupTeamCategory.addItem(self.el_ChBx)
            self.vLayout4ChBx.addWidget(self.groupTeamCategory)
        # end listTypeMatch
