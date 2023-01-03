
from PyQt5 import QtCore, QtGui, QtWidgets
from Helpers.Helpers import Helpers


class PlaceBetView(QtWidgets.QDialog):

    def __init__(self, parent=None) -> None:
        super().__init__()
        self.setWindowTitle("Matchs")
        self.centerWidget()
        self.setMinimumSize(600,400)

        self.setStyleSheet("background-color: #1E1E1E")

        self.teamCategory_LBL = QtWidgets.QLabel(
            "Veuillez choisir le type de match")
        self.team_on_category_LBL = QtWidgets.QLabel(
            "List des équipes dans ce championnat")

        # call methods
        self.ui()
        self.createView()

    def ui(self):
        mainLayout = QtWidgets.QVBoxLayout()

        # add another widget to contain tabs value
        self.mainContainer_WDG = QtWidgets.QWidget()

        # add mainContainer_WDG to main main widget
        mainLayout.addWidget(self.mainContainer_WDG)
        self.setLayout(mainLayout)

    def centerWidget(self):	
        # Ajout de cette méthode pour centrer la fenêtre        
        frameGm = self.frameGeometry()        
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())        
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()    
        frameGm.moveCenter(centerPoint)    
        self.move(frameGm.topLeft())


    def createView(self):

        self.right_details_WDG = QtWidgets.QWidget()
        self.right_details_WDG.setStyleSheet("background-color: #2C2C2C; padding: 10px")
        self.right_details_WDG.setObjectName("right_details_WDG")

        # ======= Details of match =========
        self.container_details_WDG = QtWidgets.QWidget(self.right_details_WDG)
        self.container_details_WDG.setStyleSheet("background-color: #1E1E1E; margin:10px; ")
        self.container_details_WDG.setObjectName("container_details_WDG")
        self.container_details_WDG.setContentsMargins(10,10,10,10)
        vLayout_maincontainer_details = QtWidgets.QVBoxLayout(
            self.container_details_WDG)
        # vLayout_maincontainer_details.setAlignment(QtCore.Qt.AlignTop)

        # Title
        lbl_info_title = QtWidgets.QLabel("Informations du match")
        lbl_info_title.setStyleSheet("font: 18px; margin: 2px 1px")

        # widget Team
        hLayout_match_info = QtWidgets.QHBoxLayout(self.container_details_WDG)

        self.lbl_home_teams = QtWidgets.QLabel("Real Madrid")
        self.lbl_move_teams = QtWidgets.QLabel("FC Barcelona")


        # Choix pariage
        self.hLayout_bet_choice = QtWidgets.QHBoxLayout()
        self.group_bet_choice = QtWidgets.QButtonGroup()
        
        # add box each team on Layout
        hLayout_match_info.addWidget(
            self.lbl_home_teams, alignment=QtCore.Qt.AlignLeft)
        hLayout_match_info.addWidget(
            self.lbl_move_teams, alignment=QtCore.Qt.AlignRight)

        # amount box
        amount_box_WDG = QtWidgets.QWidget()
        amount_box_WDG.setStyleSheet("background-color: #1E1E1E; ")
        vLyt_amount = QtWidgets.QVBoxLayout()
        lbl_amount_title = QtWidgets.QLabel("Montant du pari:")
        lbl_amount_title.setStyleSheet("margin: 2px")
        self.amount_info_title_QLE = QtWidgets.QLineEdit()
        self.amount_info_title_QLE.setStyleSheet("border: 1px solid #FAFAFA")

        vLyt_amount.addWidget(lbl_amount_title)
        vLyt_amount.addWidget(self.amount_info_title_QLE)

        # add title | match__info_box in  vLayout_maincontainer_details
        vLayout_maincontainer_details.addWidget(
            lbl_info_title, alignment=QtCore.Qt.AlignCenter)
        vLayout_maincontainer_details.addLayout(hLayout_match_info)
        vLayout_maincontainer_details.addLayout(self.hLayout_bet_choice)
        vLayout_maincontainer_details.addLayout(vLyt_amount)

        # end details of match

        # self.hLayout_ListMatchContent_FRM.addWidget(self.right_details_WDG)

        # self.vLayout_ToLineUpContainer.addWidget(self.ListMatchContent_FRM)

        # TODO: end cent

    
    def loadBetChoice(self, list_choice):
        if list_choice:

            for row in list_choice:
                print(f"ROW: {row}")
                id_, title, ratio, visible = row
                self.bet_choice_QPB = QtWidgets.QPushButton()          
                self.bet_choice_QPB.setText(f"{title}")
                self.bet_choice_QPB.setStyleSheet("margin:0.5px; background:red;")
                font = QtGui.QFont()
                font.setFamily("JetBrains Mono")
                font.setPointSize(14)
                font.setWeight(50)
                self.bet_choice_QPB.setFont(font)
                self.bet_choice_QPB.setObjectName(f"betChoice{title}")
                # Add PushButton in Group
                self.group_bet_choice.addButton(self.bet_choice_QPB)
                # Add Checkbox to QVLayout
                self.hLayout_bet_choice.addWidget(self.bet_choice_QPB)
            # end loop
