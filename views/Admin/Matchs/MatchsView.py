from PyQt5 import QtCore, QtGui, QtWidgets
from Helpers.Helpers import Helpers


class MatchsView(QtWidgets.QWidget):

    def __init__(self, parent=None) -> None:
        super().__init__()
        self.setWindowTitle("Matchs")
        # self.move(parent.rect().center())
        
        self.setStyleSheet("background-color: #1E1E1E")
        # self.minimumWidth(400)
        
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

    
    def loadDatas(self,list_of_match):

        self.table_WDG.setRowCount(len(list_of_match))
        row=0        
        for i in list_of_match:
            
            self.table_WDG.setItem(row, 0, QtWidgets.QTableWidgetItem(str(i['home_team'])))
            self.table_WDG.setItem(row, 1, QtWidgets.QTableWidgetItem(str(i['category'])))
            self.table_WDG.setItem(row, 2, QtWidgets.QTableWidgetItem(str(i['away_team'])))         
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


    def showLineUpFunc(self, list_match=None):
        """
            need to pass list_match
        """
        main_FRM = QtWidgets.QFrame()
        vLayout_LineUp = QtWidgets.QVBoxLayout(main_FRM)

        if list_match:

            for row in list_match: 
                print("mwen pase")

                self.lineups_container_FRM = QtWidgets.QFrame()
                # START ONE LINEUP
                # self.lineups_container_FRM.setStyleSheet("background-color: #2C2C2C;")
                self.lineups_container_FRM.setStyleSheet("background-color: red;")
                self.lineups_container_FRM.setObjectName(f"lineups_container_FRM")
                self.lineups_container_FRM.setMaximumWidth(350)
                sizePolicy = QtWidgets.QSizePolicy(
                    QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)

                sizePolicy.setHeightForWidth(
                    self.lineups_container_FRM.sizePolicy().hasHeightForWidth())
                self.lineups_container_FRM.setSizePolicy(sizePolicy)
                self.lineups_container_FRM.setMaximumHeight(100)
                self.hLayout_LineUpContainer = QtWidgets.QHBoxLayout(self.lineups_container_FRM)
                self.hLayout_LineUpContainer.setObjectName(f"{row['match_id']} hLayout_LineUpContainer")


                self.homeTeam_FRM = QtWidgets.QFrame(self.lineups_container_FRM)
                self.homeTeam_FRM.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.homeTeam_FRM.setFrameShadow(QtWidgets.QFrame.Raised)
                self.homeTeam_FRM.setObjectName(f"{row['match_id']} homeTeam_FRM")

                self.hLayout_HomeTeam = QtWidgets.QHBoxLayout(self.homeTeam_FRM)
                self.hLayout_HomeTeam.setObjectName(f"{row['match_id']} hLayout_HomeTeam")

                self.homeTeam_QPB = QtWidgets.QPushButton(self.homeTeam_FRM)
                self.homeTeam_QPB.setStyleSheet("color: #FAFAFA")
                self.iconHomeTeam = QtGui.QIcon()
                self.iconHomeTeam.addPixmap(QtGui.QPixmap("./assets/images/teams/ajax.png"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.homeTeam_QPB.setIcon(self.iconHomeTeam)
                self.homeTeam_QPB.setIconSize(QtCore.QSize(32, 32))
                self.homeTeam_QPB.setObjectName(f"{row['match_id']} homeTeam_QPB")
                self.homeTeam_QPB.setText(f"{row['home_team']}")
                # add QPB to HLayout
                self.hLayout_HomeTeam.addWidget(self.homeTeam_QPB)
            
                self.lbl_rate_hometeam = QtWidgets.QLabel(self.homeTeam_FRM)
                self.lbl_rate_hometeam.setStyleSheet("color: #E62641;")
                self.lbl_rate_hometeam.setObjectName(f"{row['match_id']} lbl_rate_hometeam")
                self.lbl_rate_hometeam.setText("1.5")
                # add LBL_RATE to HLayout
                self.hLayout_HomeTeam.addWidget(self.lbl_rate_hometeam)

                self.lbl_score_homeTeam = QtWidgets.QLabel(self.homeTeam_FRM)
                self.lbl_score_homeTeam.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.lbl_score_homeTeam.setStyleSheet("color: #FAFAFA;")
                self.lbl_score_homeTeam.setText("5")
                self.lbl_score_homeTeam.setObjectName(f"{row['match_id']} lbl_score_homeTeam")
                # add LBL_SCORE to HLayout
                self.hLayout_HomeTeam.addWidget(self.lbl_score_homeTeam)
                # add HomeTeam_FRM to Parent Frame
                self.hLayout_LineUpContainer.addWidget(self.homeTeam_FRM)


                # ==== AWAY TEAM ====
                self.awayTeam_FRM = QtWidgets.QFrame(self.lineups_container_FRM)
                self.awayTeam_FRM.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.awayTeam_FRM.setFrameShadow(QtWidgets.QFrame.Raised)
                self.awayTeam_FRM.setObjectName(f"{row['match_id']} awayTeam_FRM")

                self.hLayout_awayTeam = QtWidgets.QHBoxLayout(self.awayTeam_FRM)
                self.hLayout_awayTeam.setObjectName(f"{row['match_id']} hLayout_awayTeam")

                self.lbl_score_awayTeam = QtWidgets.QLabel(self.awayTeam_FRM)
                self.lbl_score_awayTeam.setStyleSheet("color: #FAFAFA;")
                self.lbl_score_awayTeam.setObjectName(f"{row['match_id']} lbl_score_awayTeam")
                self.lbl_score_awayTeam.setText("0")
                self.hLayout_awayTeam.addWidget(self.lbl_score_awayTeam)

                self.lbl_rate_awayTeam = QtWidgets.QLabel(self.awayTeam_FRM)
                self.lbl_rate_awayTeam.setStyleSheet("color: #E62641;")
                self.lbl_rate_awayTeam.setObjectName(f"{row['match_id']} lbl_rate_awayTeam")
                self.lbl_rate_awayTeam.setText("1.5")
                self.hLayout_awayTeam.addWidget(self.lbl_rate_awayTeam)
                
                self.qpb_awayTeam = QtWidgets.QPushButton(self.awayTeam_FRM)
                self.qpb_awayTeam.setLayoutDirection(QtCore.Qt.RightToLeft)
                self.qpb_awayTeam.setStyleSheet("color: #FAFAFA;")
                self.qpb_awayTeam.setText(f"{row['away_team']}")
                self.iconAwayTeam = QtGui.QIcon()
                self.iconAwayTeam.addPixmap(QtGui.QPixmap("./assets/images/teams/fcb.png"),
                                QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.qpb_awayTeam.setIcon(self.iconAwayTeam)
                self.qpb_awayTeam.setIconSize(QtCore.QSize(32, 32))
                self.qpb_awayTeam.setObjectName(f"{row['match_id']} qpb_awayTeam")
                self.hLayout_awayTeam.addWidget(self.qpb_awayTeam)
                # add AwayTeam_FRM to Parent Frame
                self.hLayout_LineUpContainer.addWidget(self.awayTeam_FRM)

                vLayout_LineUp.addWidget(self.lineups_container_FRM)

            # end loop    
            return main_FRM

        # end verification
        return None
    