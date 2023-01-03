from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from Controllers.AdminMatchsController import AdminMatchsController
from Controllers.PaymentController import PaymentController
from Controllers.UserController import UserController
# models
from Models.PriorityModel import PrioritiesModel
from Models.RatioModel import RatioModel
from Models.TeamsModel import TeamsModel
from Models.UsersModel import UsersModel
from views.Admin.Teams.TeamsView import TeamsView
# views
from views.Dashboard.DashboardView import Ui_DashboardView
from Controllers.AdminDashboardController import AdminDashboardController
from views.Dashboard.PlaceBetView import PlaceBetView


class DashboardController():

    def __init__(self, parent, user_id) -> None:
        self.parent = parent
        self.user_id = user_id

        self.teamView = TeamsView()
        # models
        self.priority_model = PrioritiesModel()
        self.team_model = TeamsModel()
        self.users_model = UsersModel()
        self.ratio_model = RatioModel()
        # controllers
        self.admin_cont_dash = AdminDashboardController(parent, self.user_id)
        self.users_contr = UserController(parent, self.user_id)
        self.match_controller = AdminMatchsController(parent,self.user_id)
        # views
        self.ui_place_bet = PlaceBetView()
        self.ui_dashboard = Ui_DashboardView()

    def showDashboard(self, ):
        self.ui_dashboard.setupUi(self.parent)

        # TODO: FUCNTION TO CALL HEADER
        self.ui_dashboard.headerContentFunc()
        self.ui_dashboard.paymentQPB.clicked.connect(lambda:self.test())

        # get matchs option in DB
        match_type = self.priority_model.show()
        self.ui_dashboard.showLeftAside(match_type)
        self.ui_dashboard.hMainLayout.addWidget(self.ui_dashboard.LeftAsideFrame, alignment=QtCore.Qt.AlignLeft)
        

        self.ui_dashboard.centerAsideFunc()
        self.ui_dashboard.hMainLayout.addWidget(self.ui_dashboard.centralAsideFrame, alignment=QtCore.Qt.AlignJustify)
        

        # get value of child
        getLineUps = self.match_controller.loadLineUpsFunc()
        self.ui_dashboard.showListMatch()
        self.ui_dashboard.vLayoutCenterAside.addWidget(self.ui_dashboard.ListMatchContent_FRM)
        if getLineUps:
            self.ui_dashboard.vLayout_ToLineUpContainer.addChildWidget(getLineUps)
        # self.ui_dashboard.hMainLayout.addWidget()


        # load liste des quotes
        ratios = self.ratio_model.show()
        if ratios:
            self.ui_place_bet.loadBetChoice(ratios)

    
        # ======== A C T I O N S  ========

        # self.ui_dashboard.teamQPB.clicked.connect(self.displayTeamsFunc())
        user = self.users_contr.get_user_datas()
        if user['username']:
            self.ui_dashboard.lbl_user_name.setText(f"{user['username']}")

        if user['is_admin'] == 1:
            self.ui_dashboard.adminQPB.setVisible(True)
            self.ui_dashboard.adminQPB.clicked.connect(
                lambda: self.callAdminDashboard())
        # END: FUCNTION TO CALL HEADER

        actual_balance = self.users_contr.get_actual_balance()
        self.ui_dashboard.balance.setText(f"Balance: {actual_balance} HTG")

        # ****** P A Y M E N T  ******
        self.ui_dashboard.paymentQPB.clicked.connect(
            lambda: self.callPaymentFunc())
        # ****** L O G O U T  ******
        self.ui_dashboard.logoutQPB.clicked.connect(
            lambda: self.callLogoutFunc())

    # end showDahboardFunc
    def callPaymentFunc(self):
        print("Payment")
        paiement = PaymentController(self, self.user_id)

    # end showDahboardFunc

    def test(self):
        print("Test")

    def callAdminDashboard(self):
        self.admin_cont_dash.showDashboard()

    def callLogoutFunc(self):
        self.ui_dashboard.setVisible(False)
        # DEFINE IN __INIT__ file
        self.parent.connected_user = False
        self.parent.toggleConnection()
        # end __INIT__ file
