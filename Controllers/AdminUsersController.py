from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import random
from views.Admin.Users.UsersView import UsersView
from Models.UsersModel import UsersModel
# views


class AdminUsersController(object):

    def __init__(self, parent, user_id) -> None:
        self.parent = parent
        self.user_id = user_id
        super().__init__()
         # controllers

        # views
        self.usersView = UsersView(self.parent)
        # models
        self.users_model = UsersModel()

    def start(self, ):
      # Option to show widget
      self.usersView.show()
      list_users = self.users_model.show()
      if list_users:
        self.usersView.loadDatas(list_users)
      # end  