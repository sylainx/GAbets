from PyQt5 import QtCore, QtGui, QtWidgets
from Helpers.Helpers import Helpers
from PyQt5.QtWidgets import QLabel, QRadioButton, QDateEdit, QLineEdit,QWidget


class BetView(QtWidgets.QDialog):

    def __init__(self, parent=None) -> None:
        super().__init__()
        self.setWindowTitle("Users")
        self.setMinimumSize(100, 600)
        self.setMaximumSize(600, 640)
        self.centerWidget()
        # self.move(parent.rect().center())
        self.setGeometry(
            QtCore.QRect(0, 96, 16777214, 16777214))
        # self.setModal(True)
        self.setStyleSheet("background-color: #1E1E1E"
        "QLabel{\n"
            " \"JetBrains Mono\";\n"
            "    color: #1E1E1E\n"
            "}\n"
            "\n"
            "QLineEdit{\n"
            "    border: 1px solid white;\n"
            "}\n"
            "QLineEdit:focus{\n"
            "    border:0px solid white\n"
            "}\n")
        
        # self.imgText_QLB = QtWidgets.QLabel()
        # self.img_QLB = QtWidgets.QLabel()
        # self.title_LBL = QtWidgets.QLabel()
        # self.title_QLE = QtWidgets.QLineEdit()    
        # self.level_LBL = QtWidgets.QLabel()
        # self.level_CBB = QtWidgets.QComboBox()
        # self.teamCategory_LBL = QtWidgets.QLabel()
        # self.teamCategory_CHB = QtWidgets.QCheckBox()

        # call methods
        self.ui()
        # self.createFormRegister()
        self.listOfDatas()


    def centerWidget(self):	
        # Ajout de cette méthode pour centrer la fenêtre        
        frameGm = self.frameGeometry()        
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())        
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()        
        frameGm.moveCenter(centerPoint)        
        self.move(frameGm.topLeft())
    # end centerWidget


    def ui(self):
        mainLayout = QtWidgets.QVBoxLayout()

        # add another widget to contain tabs value
        self.mainContainer_WDG = QtWidgets.QTabWidget()

        # add mainContainer_WDG to main main widget
        mainLayout.addWidget(self.mainContainer_WDG)
        self.setLayout(mainLayout)

        



    def listOfDatas(self):
        
        self.table_WDG = QtWidgets.QTableWidget()
        header=("ID","match ID","ratio ID","User ID","Created At", "amount","Agent ID","Status")
        
        self.table_WDG.setColumnCount(len(header))
        self.table_WDG.setHorizontalHeaderLabels(header)
        # add a signal on the QTableWidget
        # self.table_WDG.cellClicked.connect(lambda:self.eventOnTable())
        # self.formLayout.addWidget(self.table_WDG)

    
    def loadDatas(self,list):

        # image to load
        imgTable_LBL = QtWidgets.QLabel()
        # end image to load
        self.table_WDG.setRowCount(len(list))
        self.table_WDG.setStyleSheet(
          "background-color: #2C2C2C;\n"
           "color: #42b883;\n"
           
        )
        row=0
        for i in list:
            # imgTable_LBL.setPixmap(QtGui.QPixmap(str(i[1])))
            # self.table_WDG.setItem(row,0,QtWidgets.QTableWidgetItem(imgTable_LBL))
            self.table_WDG.setItem(row, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.table_WDG.setItem(row, 1, QtWidgets.QTableWidgetItem(str(i[1])))
            self.table_WDG.setItem(row, 2, QtWidgets.QTableWidgetItem(str(i[2])))         
            self.table_WDG.setItem(row, 3, QtWidgets.QTableWidgetItem(str(i[3])))         
            self.table_WDG.setItem(row, 4, QtWidgets.QTableWidgetItem(str(i[4])))         
            self.table_WDG.setItem(row, 5, QtWidgets.QTableWidgetItem(str(i[5])))         
            # self.table_WDG.setItem(row, 6, QtWidgets.QTableWidgetItem(str(i[6])))         
            self.table_WDG.setItem(row, 7, QtWidgets.QTableWidgetItem(str(i[7])))         
            self.table_WDG.setItem(row, 8, QtWidgets.QTableWidgetItem(str(i[8])))                 
            row+=1


