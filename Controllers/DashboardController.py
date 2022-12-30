from PyQt5 import QtWidgets, QtCore, QtGui
import sys
# models
from Models.PriorityModel import PrioritiesModel
from Models.TeamsModel import TeamsModel
from views.Admin.Teams.TeamsView import TeamsView
# views
from views.Dashboard.DashboardView import Ui_DashboardView
from Controllers.AdminDashboardController import AdminDashboardController

class DashboardController():

    def __init__(self, parent) -> None:
        self.parent = parent
        # dashboard admin
        self.admin_cont_dash = AdminDashboardController(parent)
        # dashboard view
        self.dashboard_ui = Ui_DashboardView()
        # teams view
        self.teamView = TeamsView()
        # dashboard model
        self.priority_model = PrioritiesModel()
        # teams model
        self.team_model = TeamsModel()

    def showDashboard(self, ):
        self.dashboard_ui.setupUi(self.parent)
        # TODO: FUCNTION TO CALL HEADER
        self.dashboard_ui.headerContentFunc()
        self.dashboard_ui.teamQPB.clicked.connect(self.displayTeams)
        self.dashboard_ui.adminQPB.clicked.connect(lambda: self.callAdminDashboard())
        # END: FUCNTION TO CALL HEADER
        
        # get matchs option in DB
        match_ctype = self.priority_model.show()
        self.dashboard_ui.showLeftAside(self, match_ctype)
        self.dashboard_ui.match_type_grpe.buttonClicked.connect(
            lambda: self.get_selected_match_option())
        # self.dashboard_ui.showListMatch()
        # show register Widget
        # logout
        self.dashboard_ui.logoutQPB.clicked.connect(
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

        # self.dashboard_ui.match_type_grpe.buttonClicked.connect(
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
            QtWidgets.QMessageBox.warning(None, "Erreur", "Veuillez remplir le formulaire", QtWidgets.QMessageBox.Ok)
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
            team_id =  self.team_model.save()
            
            # SAVE CATEGORY TEAM
            if team_id :
                self.team_model.id = team_id
                for cat_id in self.list_CategoryId:
                    self.team_model.priority_id=cat_id
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
            self.team_model.id=self.teamView.table_WDG.item(index, 0).text()
            self.teamView.title_QLE.setText(str(row[2]))
            self.teamView.level_CBB.setCurrentText(str(row[3]))

        else:
            print("No data found")


    def get_selected_match_option(self):
        # fin
        selected_button= self.dashboard_ui.match_type_grpe.checkedButton()
        if selected_button is not None:
            return selected_button.text()
        else:
            return None

    def associateTeamsXcategories(self):
        list_category = self.get_selected_category()
        self.list_CategoryId= list()
        for row in list_category:
            p_find= self.priority_model.searchByName(row.text())
            if p_find:
                id :int = list(p_find)[0]
                self.list_CategoryId.append(id) 
            


    def get_selected_category(self):
        # fin
         
        selected_items= self.teamView.groupTeamCategory.selectedItems()
        if selected_items is not None:
            for item in selected_items:
                print(item.text())
                
            return selected_items
        else:
            return None


    def test(self):
        print("Test")

    def callAdminDashboard(self):
        self.admin_cont_dash.showDashboard()