
from PyQt5 import QtCore, QtGui, QtWidgets
from Helpers.Helpers import Helpers


class PlaceBetView(QtWidgets.QDialog):

    def __init__(self, parent=None) -> None:
        super().__init__()
        self.setWindowTitle("Matchs")
        self.centerWidget()
        self.setMinimumSize(600, 400)

        self.setStyleSheet("background-color: #1E1E1E")

        self.teamCategory_LBL = QtWidgets.QLabel(
            "Veuillez choisir le type de match")
        self.team_on_category_LBL = QtWidgets.QLabel(
            "List des équipes dans ce championnat")

        # call methods
        self.ui()
        self.createView()

    def ui(self):
        self.mainLayout = QtWidgets.QVBoxLayout()
        # self.mainLayout.setAlignment(QtCore.Qt.AlignTop)

        # add another widget to contain tabs value
        self.mainContainer_WDG = QtWidgets.QWidget()
        # add mainContainer_WDG to main main widget
        self.mainLayout.addWidget(self.mainContainer_WDG)
        self.setLayout(self.mainLayout)

    def centerWidget(self):
        # Ajout de cette méthode pour centrer la fenêtre
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(
            QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def createView(self):

        # ======= Details of match =========
        self.container_details_WDG = QtWidgets.QWidget(self.mainContainer_WDG)
        self.container_details_WDG.setMinimumSize(400, 350)

        self.container_details_WDG.setStyleSheet(
            "background-color: #2C2C2C; margin:10px; ")
        self.container_details_WDG.setObjectName("container_details_WDG")
        # self.container_details_WDG.setContentsMargins(10,10,10,10)
        vLayout_maincontainer_details = QtWidgets.QVBoxLayout(
            self.container_details_WDG)
        vLayout_maincontainer_details.setAlignment(QtCore.Qt.AlignTop)

        # Title
        lbl_info_title = QtWidgets.QLabel("Informations du match")
        lbl_info_title.setStyleSheet(
            "font: 18px; color: #FAFAFA; margin: 2px 1px")

        # widget Team
        hLayout_match_info = QtWidgets.QHBoxLayout(self.container_details_WDG)

        #
        self.lbl_home_teams = QtWidgets.QLabel()
        self.lbl_move_teams = QtWidgets.QLabel()
        self.lbl_amount_to_win = QtWidgets.QLabel()
        self.lbl_errorMsg = QtWidgets.QLabel()
        self.lbl_errorMsg.setVisible(False)
        doubleValidator = QtGui.QDoubleValidator()

        self.lbl_home_teams.setStyleSheet(
            "font: 18px; color: #FAFAFA; margin: 2px 1px")
        #
        self.lbl_move_teams.setStyleSheet(
            "font: 18px; color: #FAFAFA; margin: 2px 1px")

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
        self.lbl_odd_selected_title = QtWidgets.QLabel()
        self.lbl_odd_selected_title.setStyleSheet("margin: 2px; color: #FAFAFA")
        self.amount_info_title_QLE = QtWidgets.QLineEdit()
        self.amount_info_title_QLE.setValidator(doubleValidator)
        self.amount_info_title_QLE.setStyleSheet(
            "border: 1px solid #FAFAFA; color: #FAFAFA")

        self.btn_place_bet = QtWidgets.QPushButton("Parier")
        self.btn_place_bet.setStyleSheet(
            "color: #FAFAFA; background: #1E1E1E; border-radius:5px; padding:10px;")

        self.lbl_amount_to_win.setStyleSheet("margin: 2px; color: #FAFAFA")
        self.lbl_errorMsg.setStyleSheet("margin: 2px; color: #E62641")

        vLyt_amount.addWidget(self.lbl_odd_selected_title)
        vLyt_amount.addWidget(self.amount_info_title_QLE)
        vLyt_amount.addWidget(self.lbl_amount_to_win)
        vLyt_amount.addWidget(self.lbl_errorMsg)
        vLyt_amount.addWidget(self.btn_place_bet)

        # add title | match__info_box in  vLayout_maincontainer_details
        vLayout_maincontainer_details.addWidget(
            lbl_info_title, alignment=QtCore.Qt.AlignCenter)
        vLayout_maincontainer_details.addLayout(hLayout_match_info)
        vLayout_maincontainer_details.addLayout(self.hLayout_bet_choice)
        vLayout_maincontainer_details.addLayout(vLyt_amount)

        # end details of match

    def loadBetChoice(self, list_choice):
        if list_choice:

            for row in list_choice:
                id_, title, ratio, visible = row
                self.bet_choice_QPB = QtWidgets.QPushButton()
                self.bet_choice_QPB.setText(f"{title}")
                self.bet_choice_QPB.setStyleSheet(
                    "margin:0.5px; background:red;")
                font = QtGui.QFont()
                font.setFamily("JetBrains Mono")
                font.setPointSize(14)
                font.setWeight(50)
                self.bet_choice_QPB.setFont(font)
                self.bet_choice_QPB.setObjectName(f"{title}")
                # Add PushButton in Group
                self.group_bet_choice.addButton(self.bet_choice_QPB)
                # Add Checkbox to QVLayout
                self.hLayout_bet_choice.addWidget(self.bet_choice_QPB)
            # end loop

    def update_match_info(self, dict_match: dict):
        if dict_match:
            self.lbl_home_teams.setText(f"{dict_match['home_team']}")
            self.lbl_move_teams.setText(f"{dict_match['away_team']}")
            # self.lbl_amount_to_win.setText(f"Montant à gagner: {0} HTG")
