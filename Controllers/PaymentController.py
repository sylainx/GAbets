from PyQt5 import QtWidgets, QtCore, QtGui
import sys
# models
from Models.BalanceModel import BalanceModel
from Models.TeamsModel import TeamsModel
from Models.UsersModel import UsersModel
# views


class PaymentController():

    def __init__(self, parent, user_id) -> None:
        self.parent = parent
        self.user_id = user_id
        # models
        self.team_model = TeamsModel()
        self.users_model = UsersModel()
        self.balance_model = BalanceModel()
        # views
        self.get_payments_datas()

    def start(self, ):
        self.dashboard_ui.setupUi(self.parent)
        # TODO: FUCNTION TO CALL HEADER
        self.dashboard_ui.headerContentFunc()

    # end start

    def test(self):
        print("Test")

    def get_payments_datas(self):
        # if self.user_id:
        #     user = self.users_model.search(self.user_id)
        #     if user:
        #         return {
        #             'id': user[0],
        #             'firstname': user[1],
        #             'lastname': user[2],
        #             'email': user[3],
        #             'tel': user[4],
        #             'code_user': user[5],
        #             'address': user[6],
        #             'username': user[7],
        #             'nif': user[8],
        #             'sexe': user[9],
        #             'dataNais': user[10],
        #             'created_at': user[12],
        #             'is_admin': user[15],
        #         }

        # return {
        #     'id': None,
        #     'firstname': None,
        #     'lastname': None,
        #     'email': None,
        #     'tel': None,
        #     'code_user': None,
        #     'address': None,
        #     'username': None,
        #     'nif': None,
        #     'sexe': None,
        #     'dataNais': None,
        #     'created_at': None,
        #     'is_admin': None,
        # }
        pass
