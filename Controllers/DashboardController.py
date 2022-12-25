from PyQt5 import QtWidgets, QtCore, QtGui
# models
from Models.PriorityModel import PrioritiesModel
from Models.TeamsModel import TeamsModel
# views
from views.Dashboard.DashboardView import Ui_DashboardView


class DashboardController():

    def __init__(self) -> None:

        # dashboard view
        self.dashboard_ui = Ui_DashboardView()
        # dashboard model
        self.priority_model = PrioritiesModel()
        # teams model
        self.team_model = TeamsModel()

    def showDashboard(self, parent):
        self.dashboard_ui.setupUi(parent)
        match_ctype =self.priority_model.show()
        self.dashboard_ui.showLeftAside(self,match_ctype)
        self.dashboard_ui.match_type_grpe.buttonClicked.connect(lambda:self.get_selected_option())
        # self.get_selected_option()
    
    def get_selected_option(self):
        # Récupération du bouton sélectionné dans le groupe
        
        selected_button = self.dashboard_ui.match_type_grpe.checkedButton()
        if selected_button is not None:
            print( selected_button.text())
            return selected_button.text()
        else:
            return print("Aucune option sélectionnée")
