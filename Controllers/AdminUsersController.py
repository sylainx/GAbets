from pydoc import Helper
import sys
import random
from datetime import date
from Helpers.Helpers import Helpers
from views.Admin.Users.AddFundsView import AddFundsView
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
        self.addFundView = AddFundsView(self.parent)
        # models
        self.users_model = UsersModel()
        # helpers
        self.util = Helpers()

    def start(self, ):
        # Option to show widget
        self.usersView.show()
        list_users = self.users_model.show()
        if list_users:
            self.usersView.loadDatas(list_users)
        self.usersView.table_WDG.cellClicked.connect(
            lambda: self.listenTabEvent())

        
        # to delete user
        self.usersView.deleteBtn.clicked.connect(
            lambda: self.deleteElementEvent())
        self.usersView.updateBtn.clicked.connect(lambda:self.updateUserFunc())
        # end
        #
        #

    def updateUserFunc(self,):
        self.usersView.changeBtnColor()
        print("Update")

    def deleteElementEvent(self,):
        self.usersView.changeBtnColor()
        index = self.usersView.table_WDG.currentRow()
        id = self.usersView.table_WDG.item(index, 0).text()
        code_id = int(id)
        if code_id :
          list_users = self.users_model.search(code_id)
          self.users_model.delete(id)
        if list_users:
            self.usersView.loadDatas(list_users)

    def listenTabEvent(self):

        index = self.usersView.table_WDG.currentRow()

        self.usersView.saveBtn.setEnabled(False)
        self.usersView.updateBtn.setEnabled(True)
        self.usersView.deleteBtn.setEnabled(True)
        # self.usersView.addFundBtn.setEnabled(True)

        row = self.users_model.search(
            self.usersView.table_WDG.item(index, 0).text())

        if row:

            # fill form
            self.users_model.id = self.usersView.table_WDG.item(
                index, 0).text()
            self.usersView.txtFirstName.setText(str(row[1]))
            self.usersView.txtLastName.setText(str(row[2]))
            self.usersView.txtEmail.setText(str(row[3]))
            self.usersView.txtPhone.setText(str(row[4]))
            self.usersView.txtAdress.setText(str(row[6]))
            self.usersView.txtUsername.setText(str(row[7]))
            self.usersView.txtNif.setText(str(row[8]))
            if row[9] == "Masculin":
                self.usersView.rdMale.setChecked(True)
            else:
                self.usersView.rdFemale.setChecked(True)
            # self.usersView.txtDateOfBirth.setDate(
            #     date.fromisoformat(str(row[10])))
        else:
            print("No data found")

    def getUserById(self, usr_id):
        user = self.users_model.search(usr_id)
        if user:
            return user
        return None

    def getUserByCode(self, code_user):
        user = self.users_model.searchUserByCode(code_user)
        if user:
            return user
        return None

    
