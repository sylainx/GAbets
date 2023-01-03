from PyQt5 import QtWidgets, QtCore, QtGui
import sys
# controllers
# from Controllers.DashboardController import DashboardController
from Controllers.AdminMatchsController import AdminMatchsController
# 
from Controllers.AdminUsersController import AdminUsersController
# models
from Models.PriorityModel import PrioritiesModel
from Models.TeamsModel import TeamsModel

# views
from views.Admin.Matchs.MatchsView import MatchsView
from views.Admin.Teams.TeamsView import TeamsView
from views.Admin.Users.UsersView import UsersView

from views.Dashboard.AdminDashboardView import Ui_AdminDashboardView


class AdminDashboardController(object):

    def __init__(self, parent,user_id) -> None:
        self.parent = parent
        self.user_id = user_id
        # controllers
        self.admin_matchs_controller = AdminMatchsController(self,self.user_id)
        self.admin_users_controller = AdminUsersController(self,self.user_id)
        # views
        self.admin_dashboard_ui = Ui_AdminDashboardView()
        self.teamView = TeamsView()
        self.matchView = MatchsView()
        self.userView = UsersView()
        # models
        self.priority_model = PrioritiesModel()
        self.team_model = TeamsModel()
        


    def showDashboard(self, ):
        self.admin_dashboard_ui.setupUi(self.parent)

        # TODO: FUCNTION TO CALL HEADER
        self.admin_dashboard_ui.headerContentFunc()
        self.admin_dashboard_ui.teamQPB.clicked.connect(self.displayTeams)
        
        # get matchs option in DB
        match_type = self.priority_model.show()
        
        self.admin_dashboard_ui.showLeftAside(match_type)
        self.admin_dashboard_ui.hMainLayout.addWidget(self.admin_dashboard_ui.LeftAsideFrame, alignment=QtCore.Qt.AlignLeft)
        
        self.admin_dashboard_ui.centerAsideFunc()
        self.admin_dashboard_ui.hMainLayout.addWidget(self.admin_dashboard_ui.centralAsideFrame, alignment=QtCore.Qt.AlignJustify)
        
        # get value of child
        getLineUps = self.admin_matchs_controller.loadLineUpsFunc()
        self.admin_dashboard_ui.showListMatch()
        self.admin_dashboard_ui.vLayoutCenterAside.addWidget(self.admin_dashboard_ui.ListMatchContent_FRM)
        if getLineUps:
            self.admin_dashboard_ui.vLayout_ToLineUpContainer.addChildWidget(getLineUps)
        # self.admin_dashboard_ui.hMainLayout.addWidget()



        # ======== A C T I O N S  ========

        # ACTION ON HEADER BUTTON
        self.admin_dashboard_ui.matchQPB.clicked.connect(
            lambda: self.callMatchController())
        self.admin_dashboard_ui.teamQPB.clicked.connect(
            lambda: self.displayTeams())
        self.admin_dashboard_ui.usersQPB.clicked.connect(
            lambda: self.callUsersController())    
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
        self.team_model.agent_id = 1
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

        # call user controller
    def callUsersController(self):
        # self.matchView.u
        self.admin_users_controller.start()    

    def test(self):
        print("Test")
