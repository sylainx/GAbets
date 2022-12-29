from PyQt5 import QtCore, QtGui, QtWidgets
from Helpers.Helpers import Helpers


class MatchsView(QtWidgets.QWidget):

    def __init__(self, parent=None) -> None:
        super().__init__()
        self.setWindowTitle("Matchs")
        # self.move(parent.rect().center())
        # self.setModal(True)
        self.setStyleSheet("background-color: #1E1E1E")
        
        self.teamCategory_LBL = QtWidgets.QLabel("Veuillez choisir le type de match")
        self.team_on_category_LBL = QtWidgets.QLabel("List des équipes dans ce championnat")
        
        # call methods
        self.ui()
        self.createFormRegister()
        self.listOfDatas()

    def ui(self):
        mainLayout = QtWidgets.QVBoxLayout()

        # add another widget to contain tabs value
        self.mainContainer_WDG = QtWidgets.QWidget()

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

        # will get Categories of team
        self.category_teams_CbBx = QtWidgets.QComboBox()
        
        self.team_on_category_CbBx = QtWidgets.QComboBox()
        self.team_on_category_CbBx.addItem("Liste des equipes:")
        self.team_on_category_CbBx.setStyleSheet("background-color: #2C2C2C; color: #FAFAFA")


        # action btn        
        hLayout4Btn = QtWidgets.QHBoxLayout()
        
        self.saveBtn = QtWidgets.QPushButton("Enregistrer")
        self.saveBtn.setStyleSheet("background-color: #106327;\n"
                                   "color: #FAFAFA;\n"
                                   "border-radius: 10px;\n"
                                   "padding: 10px 15px;")
        
        self.cancelBtn = QtWidgets.QPushButton("Annuler")
        self.cancelBtn.setStyleSheet("background-color: #2C2C2C;\n"
                                   "color: #FAFAFA;\n"
                                   "border-radius: 10px;\n"
                                   "padding: 10px 15px;")
        self.cancelBtn.setEnabled(False)
        # add btn horizontal
        hLayout4Btn.addWidget(self.saveBtn)
        hLayout4Btn.addWidget(self.cancelBtn)
        
        # add QLineEdit & QComboBox to formLayout
        self.formLayout.addWidget(self.teamCategory_LBL)
        self.formLayout.addWidget(self.category_teams_CbBx)
        
        self.formLayout.addWidget(self.team_on_category_LBL)
        self.formLayout.addWidget(self.team_on_category_CbBx)
        
        self.formLayout.addLayout(hLayout4Btn)

        # add form layout to central Layout
        mainLayout.addLayout(self.formLayout)
        self.mainContainer_WDG.setLayout(mainLayout)

    def clearFields(self):
        # TODO will be clear all fields
        self.teamCategory_LBL.text()
        self.el_CbBx.setCurrentIndex(0)


    def listOfDatas(self):
        
        self.table_WDG = QtWidgets.QTableWidget()
        header=("Equipe 1", "Championnat","Equipe 2")

        self.table_WDG.setColumnCount(len(header))
        self.table_WDG.setHorizontalHeaderLabels(header)
        # add a signal on the QTableWidget
        # self.table_WDG.cellClicked.connect(lambda:self.eventOnTable())
        self.formLayout.addWidget(self.table_WDG)

    
    def loadDatas(self,list):

        self.table_WDG.setRowCount(len(list))
        row=0
        for i in list:
            self.table_WDG.setItem(row, 0, QtWidgets.QTableWidgetItem(str(i[1])))
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
        # self.cancelBtn.setEnabled(True)
        self.cancelBtn.setStyleSheet("background-color: #E62641;\n"
                                   "color: #FAFAFA;\n"
                                   "border-radius: 10px;\n"
                                   "padding: 10px 15px;")


    def listTypeOfMatch(self, list):
        
        for row in list:
            id, title, ratio, visible = row
            self.el_CbBx = QtWidgets.QComboBox()
            self.el_CbBx.addItem(f"{title}")
            self.el_CbBx.setStyleSheet("background-color: #2C2C2C; color: #FAFAFA")            
            self.el_CbBx.setObjectName(f"{title}")
            self.category_teams_CbBx.addItem(f"{title}")
        # end listTypeMatch

    def listTeamOnCategory(self, teams):
        
        for row in teams:
            
            self.team_on_category_CbBx.addItem(f"{row[2]}")
            self.team_on_category_CbBx.setStyleSheet("background-color: #2C2C2C; color: #FAFAFA")
            self.team_on_category_CbBx.setObjectName(f"{row[2]}")
            
        # end listTypeMatch
