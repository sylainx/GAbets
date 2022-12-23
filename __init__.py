from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from views.RegisterView import RegisterView
from views.LoginView import LoginView
from PyQt5.QtGui import QIcon
import sys

from views.paymentWidget import Ui_PaymentManageWidget


class MainProject(QMainWindow, Ui_PaymentManageWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("AG BETS SPORTS")
        self.setMinimumSize(400, 400)
        self.showMaximized()
        self.setWindowIcon(QIcon("./assets/icons/calendar.png"))
        # self.setStyleSheet("background-color:#a45378")
        self.creerMenu()
        self.setupUi(self)

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
        self.payScreen = Ui_PaymentManageWidget()
        self.payScreen.setupUi(self)

    def callAuthenticate(self):
        login = LoginView(self)
        login.show()

    def callNotes(self):
        print("Notes")

    def callCourses(self):
        print("cours")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainProject()
    window.show()
    sys.exit(app.exec_())

# app = QApplication([])
# mv = MainView()
# mv.show()
# app.exec()
