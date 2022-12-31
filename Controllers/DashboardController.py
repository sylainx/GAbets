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

        # get matchs option in DB
        match_ctype = self.priority_model.show()
        self.dashboard_ui.showLeftAside(self, match_ctype)
        # self.dashboard_ui.centerAsideFunc()


        # ======== A C T I O N S  ========
        # self.dashboard_ui.teamQPB.clicked.connect(self.displayTeamsFunc())
        self.dashboard_ui.adminQPB.clicked.connect(lambda: self.callAdminDashboard())
        # END: FUCNTION TO CALL HEADER
        
        
        # ======== L O G O U T  ========
        self.dashboard_ui.logoutQPB.clicked.connect(
            lambda: self.callLogoutFunc())

    # end showDahboardFunc
    def displayTeamsFunc(self):
        print("Teaammmmmms")
    # end showDahboardFunc

    def test(self):
        print("Test")

    def callAdminDashboard(self):
        self.admin_cont_dash.showDashboard()

    
    def callLogoutFunc(self):
        self.dashboard_ui.setVisible(False)
        # DEFINE IN __INIT__ file
        self.parent.connected_user=False
        self.parent.toggleConnection()
        # end __INIT__ file
