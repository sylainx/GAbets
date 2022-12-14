from PyQt5.QtWidgets import QApplication, QMainWindow
from views.RegisterView import RegisterView
from views.LoginView import LoginView
from PyQt5.QtGui import QIcon
import sys


class MainView(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("BETS SPORTS")
        self.setMinimumSize(400, 400)
        self.showMaximized()
        self.setWindowIcon(QIcon("./assets/icons/calendar.png"))
        # self.setStyleSheet("background-color:#a45378")
        self.creerMenu()

    def creerMenu(self):
        self.mnBar = self.menuBar()
        # self.mnBar.setStyleSheet("position:absolute;right:0;")
        self.inscriptions = self.mnBar.addMenu("Inscription")
        self.session1 = self.inscriptions.addAction("Session 1")
        # ajouter des evements sur le sous-menu session 1
        self.session1.triggered.connect(self.callLogin)
        self.session1.setShortcut("CTRL+A")
        self.session2 = self.inscriptions.addAction("Session 2")
        # ajouter des evements sur le sous-menu session 2
        self.session2.triggered.connect(self.callCourses)
        self.session2.setShortcut("CTRL+B")
        self.cours = self.mnBar.addMenu("Cours")
        self.notes = self.mnBar.addAction("Notes")
        self.notes.triggered.connect(self.callNotes)
        self.bulletin = self.mnBar.addMenu("Bulletins")

    def callLogin(self):
        login = LoginView(self)
        login.show()

    def callNotes(self):
        print("Notes")

    def callCourses(self):
        print("cours")


app = QApplication([])
mv = MainView()
mv.show()
app.exec()
