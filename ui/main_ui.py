from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from Helpers.Helpers import Helpers

from list_matchs import Ui_MainWindow



class MainProject(QMainWindow, ):

    def __init__(self):
        super()

        self.setWindowTitle(Helpers().app_name())
        self.setMinimumSize(400, 400)
        self.showMaximized()
        self.setWindowIcon(QWidget.con("./assets/icons/calendar.png"))
        self.creerMenu()


if __name__ == '__main__':
    app = QApplication([])
    window = Ui_MainWindow()
    window.setupUi(app)
    app.exec_()

