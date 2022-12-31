from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

# controllers
from Controllers.AuthController import AuthController
from Controllers.DashboardController import DashboardController
from Helpers.Helpers import Helpers
# views
from PyQt5.QtGui import QIcon
from views.AuthView import AuthView
from views.paymentWidget import Ui_PaymentManageWidget


class MainProject(QMainWindow):

    def __init__(self, parent=None):
        # super().__init__()
        super(MainProject, self).__init__(parent)
        self.setWindowTitle(Helpers().app_name())
        self.setMinimumSize(1250, 600)
        self.showMaximized()
        self.setWindowIcon(QIcon("./assets/icons/calendar.png"))
        self.creerMenu()
        # properties
        # TODO: PASS false FALSE show login form
        # self.connected_user = False
        self.connected_user = True
        self.agent_id = None
        # initiate
        self.auth = AuthController(self)
        self.toggleConnection()
        
    
    def toggleConnection(self):
        
        if(self.connected_user):
            self.dashboard = DashboardController(self)
            self.dashboard.showDashboard()
            
        else:
            self.auth.start()



    def creerMenu(self):
        self.mnBar = self.menuBar()
        
        # self.mnBar.setStyleSheet("position:absolute;right:0;")
        self.menu = self.mnBar.addMenu("Compte")

        self.account = self.menu.addAction("Connexion")
        # ajouter des evements sur le sous-menu session 1
        self.account.triggered.connect(self.callAuthenticate)
        self.account.setShortcut("CTRL+A")
       

        self.cours = self.mnBar.addMenu("Cours")
        self.bulletin = self.mnBar.addMenu("Bulletins")


    def callAuthenticate(self):
        login = AuthView(self)
        login.show()

if __name__ == '__main__':
    app = QApplication([])
    window = MainProject()
    window.show()
    app.exec_()
