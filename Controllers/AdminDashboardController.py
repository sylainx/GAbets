from PyQt5 import QtWidgets, QtCore, QtGui
import sys
# controllers
# from Controllers.DashboardController import DashboardController
from Controllers.AdminMatchsController import AdminMatchsController
#
from Controllers.AdminUsersController import AdminUsersController
from Controllers.UserController import UserController
from Helpers.Helpers import Helpers
from Models.BalanceModel import BalanceModel
from Models.BetsModel import BetsModel
from Models.MatchsModel import MatchsModel
# models
from Models.PriorityModel import PrioritiesModel
from Models.TeamsModel import TeamsModel

# views
from views.Admin.Matchs.MatchsView import MatchsView
from views.Admin.Teams.TeamsView import TeamsView
from views.Admin.Users.AddFundsView import AddFundsView
from views.Admin.Users.UsersView import UsersView

from views.Dashboard.DashboardView import Ui_DashboardView

from views.Dashboard.AdminDashboardView import Ui_AdminDashboardView


class AdminDashboardController(object):

    def __init__(self, parent, user_id) -> None:
        self.parent = parent
        self.user_id = user_id
        # controllers
        self.admin_matchs_controller = AdminMatchsController(
            self, self.user_id)
        self.admin_users_controller = AdminUsersController(self, self.user_id)
        self.users_controller = UserController(self, self.user_id)

        # views
        self.admin_dashboard_ui = Ui_AdminDashboardView()
        self.teamView = TeamsView()
        self.matchView = MatchsView()
        self.userView = UsersView()
        
        self.addFundsView = AddFundsView()
        self.ui_dashboard = Ui_DashboardView()
        # models
        self.priority_model = PrioritiesModel()
        self.team_model = TeamsModel()
        self.bets_model = BetsModel()
        self.matchs_model = MatchsModel()
        self.balance_model = BalanceModel()
        #
        self.util = Helpers()

    def showDashboard(self, ):
        self.admin_dashboard_ui.setupUi(self.parent)

        # TODO: FUCNTION TO CALL HEADER
        self.admin_dashboard_ui.headerContentFunc()
        self.admin_dashboard_ui.teamQPB.clicked.connect(self.displayTeams)

        # get matchs option in DB
        match_type = self.priority_model.show()

        self.admin_dashboard_ui.showLeftAside(match_type)
        self.admin_dashboard_ui.hMainLayout.addWidget(
            self.admin_dashboard_ui.LeftAsideFrame, alignment=QtCore.Qt.AlignLeft)

        self.admin_dashboard_ui.centerAsideFunc()
        self.admin_dashboard_ui.hMainLayout.addWidget(
            self.admin_dashboard_ui.centralAsideFrame, alignment=QtCore.Qt.AlignJustify)

        # get value of child
        self.admin_dashboard_ui.showListBetsFunc()
        # donnees bets pour afficher dans la table
        getBetsData = self.bets_model.show()
        if getBetsData:
            list_info_bet = list()
            # chercher nom equipe:
            for row in getBetsData:
                match_id = self.matchs_model.search(row[1])
                user = self.admin_users_controller.getUserById(row[3])

                if match_id and user:
                    hTm = self.team_model.search(match_id[1])[2]
                    mvTm = self.team_model.search(match_id[2])[2]
                    print(f"LIST INFO: {hTm} \n")
                    print(f"LIST INFO: {mvTm} \n")

                    if hTm and mvTm:
                        dict_info_bet = {
                            'id': row[0],
                            'amount': row[5],
                            'match': f"{hTm} - {mvTm}",
                            'user': f"{user[1]} {user[2]}",
                            'date': row[4],
                        }
                        list_info_bet.append(dict_info_bet)

            # end nom equipe:
            # print(f"LIST INFO: {list_info_bet} ")
            self.admin_dashboard_ui.loadDatas(list_info_bet)
        # end donnees bets table

        # ======== A C T I O N S  ========
        actual_balance = self.users_controller.get_actual_balance()
        self.admin_dashboard_ui.balance.setText(
            f"Balance: {actual_balance} HTG")
        # ACTION ON HEADER BUTTON
        self.admin_dashboard_ui.matchQPB.clicked.connect(
            lambda: self.callMatchController())
        self.admin_dashboard_ui.teamQPB.clicked.connect(
            lambda: self.displayTeams())
        self.admin_dashboard_ui.usersQPB.clicked.connect(
            lambda: self.callUsersController())
        self.admin_dashboard_ui.addFundsQPB.clicked.connect(
            lambda: self.callBackAddFund())
            
        
        # logout
        self.admin_dashboard_ui.logoutQPB.clicked.connect(
            lambda: self.callLogoutFunc())

    # end showDahboardFunc

    def displayTeams(self):
        self.teamView.show()
        self.teamView.listOfDatas
        self.loadFunc()
        self.callTeamFunc()
    # end displayTeams()

    def callTeamFunc(self,):
        self.teamView.listTypeOfMatch(self.priority_model.show())
        self.teamView.saveBtn.clicked.connect(lambda: self.addNewTeam())
        self.teamView.updateBtn.clicked.connect(lambda: self.updateTeam())
        self.teamView.deleteBtn.clicked.connect(lambda: self.deleteTeam())
        self.teamView.table_WDG.clicked.connect(lambda: self.listenTabEvent())

        # self.admin_dashboard_ui.match_type_grpe.buttonClicked.connect(
        # lambda: self.get_selected_match_option())
        self.teamView.groupTeamCategory.itemSelectionChanged.connect(
            lambda: self.associateTeamsXcategories())

        self.teamView.clearFields()
    # end callTeamFunc()

    def callLogoutFunc(self):
        sys.exit()

    def addNewTeam(self,):

        # may be call in the controller
        teamToSave_dic = {
            "img": self.teamView.img_QLB.text(),
            "title": self.teamView.title_QLE.text(),
            'level': self.teamView.level_CBB.currentText()
        }
        img, title, level = teamToSave_dic

        if len(title) == 0 or len(level) == 0:
            QtWidgets.QMessageBox.warning(
                None, "Erreur", "Veuillez remplir le formulaire", QtWidgets.QMessageBox.Ok)
        else:
            agent_id = 1
            # TODO: remove after
            img = "assets/images/teams/fcb.png"

            self.team_model.title = teamToSave_dic['title']
            self.team_model.level = teamToSave_dic["level"]
            # TODO: add correct PATH
            # self.team_model.img = teamToSave_dic["img"]
            self.team_model.img = img
            self.team_model.agent_id = agent_id
            team_id = self.team_model.save()

            # SAVE CATEGORY TEAM
            if team_id:
                self.team_model.id = team_id
                for cat_id in self.list_CategoryId:
                    self.team_model.priority_id = cat_id
                    self.team_model.saveCategoryTeam()
                self.loadFunc()

    def loadFunc(self):
        list_of_teams = self.team_model.show()
        if len(list_of_teams) > 0:
            self.teamView.loadDatas(list_of_teams)

    def updateTeam(self):
        # verifications first
        self.team_model.agent_id = self.user_id
        self.team_model.img = self.teamView.img_QLB.text()
        self.team_model.title = self.teamView.title_QLE.text()
        self.team_model.level = self.teamView.level_CBB.currentText()
        # verifications first

        self.team_model.update(self.team_model.id)
        self.teamView.saveBtn.setEnabled(True)
        self.teamView.updateBtn.setEnabled(False)
        self.teamView.deleteBtn.setEnabled(False)
        self.teamView.clearFields()
        self.loadFunc()

    def deleteTeam(self):
        id = self.txtCode.text()
        # self.team_model.delete(id)
        self.loadDatas()
        self.clearFields()

    def listenTabEvent(self):

        index = self.teamView.table_WDG.currentRow()
        row = self.team_model.search(
            self.teamView.table_WDG.item(index, 0).text())

        if row:
            # fill form
            self.team_model.id = self.teamView.table_WDG.item(index, 0).text()
            self.teamView.title_QLE.setText(str(row[2]))
            self.teamView.level_CBB.setCurrentText(str(row[3]))

        else:
            print("No data found")

    def get_selected_match_option(self):
        # fin
        selected_button = self.admin_dashboard_ui.match_type_grpe.checkedButton()
        if selected_button is not None:
            return selected_button.text()
        else:
            return None

    def associateTeamsXcategories(self):
        list_category = self.get_selected_category()
        self.list_CategoryId = list()
        for row in list_category:
            p_find = self.priority_model.searchByName(row.text())
            if p_find:
                id: int = list(p_find)[0]
                self.list_CategoryId.append(id)

    def get_selected_category(self):
        # fin

        selected_items = self.teamView.groupTeamCategory.selectedItems()
        if selected_items is not None:
            for item in selected_items:
                print(item.text())

            return selected_items
        else:
            return None

    def callMatchController(self):
        # self.matchView.u
        self.admin_matchs_controller.start()

    def callBackAddFund(self):
        self.addFundsView.show()
        self.addFundsView.btn_increase_amount_QPB.clicked.connect(
            lambda: self.callbackButtonAmount())

    def callbackButtonAmount(self):
        code_user = self.addFundsView.code_user_QLE.text()
        amount_increase = self.addFundsView.amount_increase_QLE.text()

        if self.util.valid_str(code_user) and self.util.valid_float(amount_increase):
            amount_increase= float(amount_increase)
            user = self.admin_users_controller.getUserByCode(code_user)

            if amount_increase > 25 and amount_increase < 1000000:
                if user:

                    actn = 1   # add fund
                    self.balance_model.code_user = code_user
                    self.balance_model.action = actn
                    self.balance_model.agent_id = self.user_id
                    self.balance_model.montant = amount_increase
                    # save fund
                    self.balance_model.save()
                    # close QDialog
                    self.addFundsView.clearFields()
                    self.users_controller.get_actual_balance()
                    self.showDashboard()
                    self.addFundsView.accept()
            else:
                QtWidgets.QMessageBox.warning(
                    None, "Error", "La valeur doit etre entre 25 et 1,000,000", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.warning(
                None, "Error", "Veuillez verifier v???os informations", QtWidgets.QMessageBox.Ok)

        # call user controller
    def callUsersController(self):
        # self.matchView.u
        self.admin_users_controller.start()

    def test(self):
        print("Test")

    