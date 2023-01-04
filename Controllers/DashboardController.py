from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from Controllers.AdminMatchsController import AdminMatchsController
from Controllers.PaymentController import PaymentController
from Controllers.UserController import UserController
from Models.BetsModel import BetsModel
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
        self.bets_model = BetsModel()
        # controllers
        self.admin_cont_dash = AdminDashboardController(parent, self.user_id)
        self.users_contr = UserController(parent, self.user_id)
        self.match_controller = AdminMatchsController(parent, self.user_id)
        # views
        self.ui_place_bet = PlaceBetView()
        self.ui_dashboard = Ui_DashboardView()
        # properties
        self.coef = 0

    def showDashboard(self, ):
        self.ui_dashboard.setupUi(self.parent)

        # TODO: FUCNTION TO CALL HEADER
        self.ui_dashboard.headerContentFunc()
        self.ui_dashboard.paymentQPB.clicked.connect(lambda: self.test())

        # get matchs option in DB
        match_type = self.priority_model.show()
        self.ui_dashboard.showLeftAside(match_type)
        self.ui_dashboard.hMainLayout.addWidget(
            self.ui_dashboard.LeftAsideFrame, alignment=QtCore.Qt.AlignLeft)

        self.ui_dashboard.centerAsideFunc()
        self.ui_dashboard.hMainLayout.addWidget(
            self.ui_dashboard.centralAsideFrame, alignment=QtCore.Qt.AlignJustify)

        # get value of child
        getLineUps = self.match_controller.loadLineUpsFunc()
        self.ui_dashboard.showListMatch()
        self.ui_dashboard.vLayoutCenterAside.addWidget(
            self.ui_dashboard.ListMatchContent_FRM)
        if getLineUps:
            self.ui_dashboard.vLayout_ToLineUpContainer.addChildWidget(
                getLineUps)
        # self.ui_dashboard.hMainLayout.addWidget()
        self.match_controller.matchView.group_btn_bets.buttonClicked.connect(
            lambda x: self.matchCallBack(x))

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

    def matchCallBack(self, btn: QtWidgets.QPushButton):
        self.find_match_id = btn.objectName()
        if self.find_match_id:
            list_matchs = self.match_controller.loadMatchsFunc()

            self.dict_matchSelected = self.match_controller.get_match_by_id(
                self.find_match_id)

            if self.dict_matchSelected:
                self.ui_place_bet.show()
                self.ui_place_bet.update_match_info(self.dict_matchSelected)
                # press one odd button
                self.ui_place_bet.group_bet_choice.buttonClicked.connect(lambda x:self.changeOddValue(x))
                # gggg                
                self.ui_place_bet.amount_info_title_QLE.textChanged.connect(lambda:self.get_bet_amount())
                self.ui_place_bet.btn_place_bet.clicked.connect(lambda:self.makeBetFunc())

    def changeOddValue(self, btn: QtWidgets.QPushButton):
        self.ui_place_bet.lbl_errorMsg.setVisible(False)
        self.get_bet_amount()
        # valeur cote(odd)
        self.selectedOdd= btn.text()
        
        if self.selectedOdd and self.dict_matchSelected:
            self.coef = self.dict_matchSelected[self.selectedOdd]
            self.ui_place_bet.lbl_odd_selected_title.setText(f"Coef: {self.coef}")
            
    
    def get_bet_amount(self):
        # montant a gagner
        self.ui_place_bet.lbl_errorMsg.setVisible(False)

        amount_enter = self.ui_place_bet.amount_info_title_QLE.text()
        if len(amount_enter) > 0 :
            if self.coef:
                _usr_mt = float(amount_enter) or 0
                _coef = float(self.coef) or 0
                self.montTotal = _coef * _usr_mt                
                self.ui_place_bet.lbl_amount_to_win.setText(f"Montant à gagner: {self.montTotal} HTG")
                return self.montTotal
            else:
                self.ui_place_bet.lbl_errorMsg.setVisible(True)
                self.ui_place_bet.lbl_errorMsg.setText(f"Veuillez selectionner un cote!")
        else: 
            self.montTotal=0
            self.ui_place_bet.lbl_errorMsg.setVisible(True)
            self.ui_place_bet.lbl_errorMsg.setText(f"Veuillez entrer une valeur!")
            
        return None


    def makeBetFunc(self):
        amountToBet = self.get_bet_amount()
        if amountToBet :
            self.bets_model.match_id= self.find_match_id
            self.bets_model.ratio_id = self.coef
            self.bets_model.amount=amountToBet        
            self.bets_model.user_id= self.user_id
            self.bets_model.status= 1
            self.bets_model.save()
            self.ui_place_bet.accept()

    
    def callAdminDashboard(self):
        self.admin_cont_dash.showDashboard()



    def callLogoutFunc(self):
        self.ui_dashboard.setVisible(False)
        # DEFINE IN __INIT__ file
        self.parent.connected_user = False
        self.parent.toggleConnection()
        # end __INIT__ file
