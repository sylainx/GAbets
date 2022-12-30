from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from Controllers.DashboardController import DashboardController
from Helpers.Helpers import Helpers
from views.RegisterView import RegisterView
from views.LoginView import LoginView
from PyQt5.QtGui import QIcon
from views.Dashboard.DashboardView import Ui_DashboardView
from views.paymentWidget import Ui_PaymentManageWidget

class MainProject(QMainWindow):

    def __init__(self,parent=None):
        # super().__init__()
        super(MainProject, self).__init__(parent)
        self.setWindowTitle(Helpers().app_name())
        self.setMinimumSize(400, 400)
        self.showMaximized()
        self.setWindowIcon(QIcon("./assets/icons/calendar.png"))
        self.creerMenu()
        self.login = LoginView()

        # self.callAuthenticate()
        self.callDashboard()
        # show payment Widget
        # self.callPaymentLayout()

    def creerMenu(self):
        self.mnBar = self.menuBar()

        # self.mnBar.setStyleSheet("position:absolute;right:0;")
        self.inscriptions = self.mnBar.addMenu("Compte")

        self.account = self.inscriptions.addAction("Connexion")
        # ajouter des evements sur le sous-menu session 1
        self.account.triggered.connect(self.callAuthenticate)
        self.account.setShortcut("CTRL+A")
        self.matchs = self.inscriptions.addAction("Session 2")
        # ajouter des evements sur le sous-menu session 2
        self.matchs.triggered.connect(self.callCourses)
        self.matchs.setShortcut("CTRL+B")

        self.cours = self.mnBar.addMenu("Cours")
        self.notes = self.mnBar.addAction("Notes")
        self.notes.triggered.connect(self.callNotes)
        self.bulletin = self.mnBar.addMenu("Bulletins")

    def showLineUps(self,):
        # self.payScreen = Ui_PaymentManageWidget()
        # self.payScreen.setupUi(self)
        print(" there is NOthing now in LIneups now")

    def callAuthenticate(self):
        login = LoginView(self)
        login.show()

    def callDashboard(self) -> None:
        dashboard = DashboardController(self)
        dashboard.showDashboard()

    def callPaymentLayout(self) -> None:
        pay = Ui_PaymentManageWidget()
        pay.setupUi(self)

    def callNotes(self):
        print("Notes")

    def callCourses(self):
        print("cours")


if __name__ == '__main__':
    app = QApplication([])
    window = MainProject()
    window.show()
    app.exec_()

