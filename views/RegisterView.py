from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QRadioButton, QTableWidgetItem, QTableWidget, QTextEdit, QComboBox, QDateEdit, QPushButton, QVBoxLayout, QFormLayout, QGridLayout, QTabWidget, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt
from Models.RegisterModel import RegisterModel
from datetime import date


class RegisterView(QDialog):
    insc = RegisterModel()

    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Register")
        self.setMinimumSize(600, 600)
        self.setMaximumSize(600, 600)
        self.setModal(True)
        self.creerOnglet()
        self.creerFormInscription()
        self.creertableau()
        self.loadDatas()

    def creerOnglet(self):
        mainLayout = QHBoxLayout()
        
        # table widget
        self.tabWidget = QTabWidget()
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)
        # widget
        self.inscriptions = QWidget()
        self.paiements = QWidget()
        self.admissions = QWidget()
        # ajouter les widgets dans les Tab
        
        self.tabWidget.addTab(self.inscriptions, "Inscriptions")
        self.tabWidget.addTab(self.paiements, "Paiements")
        self.tabWidget.addTab(self.admissions, "Admissions")
        mainLayout.addWidget(self.tabWidget)
        self.setLayout(mainLayout)

    def creerFormInscription(self):
        # creer un QGridLayout
        layoutprincipal = QVBoxLayout()
        # creer un QFormLayout
        self.form = QFormLayout()
        self.form.setAlignment(Qt.AlignTop)
        qSexe = QHBoxLayout()
        hbBouton = QHBoxLayout()
        hbBouton.setAlignment(Qt.AlignTop)
       
       # hbBouton.addStretch(0)
        self.btNew = QPushButton("Nouveau")
        self.btNew.clicked.connect(self.nouveau)

        self.btSave = QPushButton("Save")
        self.btSave.clicked.connect(self.enregistrer)
        
        self.btUpdate = QPushButton("Update")
        self.btUpdate.clicked.connect(self.modifier)
        
        self.btDelete = QPushButton("Delete")
        self.btDelete.clicked.connect(self.supprimer)
        
        self.btDelete.setEnabled(False)
        self.btUpdate.setEnabled(False)
        
        hbBouton.addWidget(self.btNew)
        hbBouton.addWidget(self.btSave)
        hbBouton.addWidget(self.btUpdate)
        hbBouton.addWidget(self.btDelete)

        self.rdMasculin = QRadioButton("Masculin")
        self.rdFeminin = QRadioButton("Feminin")
        qSexe.addWidget(self.rdMasculin)
        qSexe.addWidget(self.rdFeminin)

        self.txtDateNais = QDateEdit()
        self.txtDateNais.setDisplayFormat("dd/MM/yyyy")
        self.txtDateNais.setCalendarPopup(True)
        
        self.txtAdresse = QLineEdit()
        self.txtUsername = QLineEdit()
        self.txtLastname = QLineEdit()
        self.txtFirstname = QLineEdit()
        self.txtEmail = QLineEdit()
        self.txtTel = QLineEdit()
        self.txtNif = QLineEdit()
        self.txtAgentID = QLineEdit()


        # ajouter des Widgets
        self.form.addRow("Username", self.txtUsername)
        self.form.addRow("Lastname", self.txtLastname)
        self.form.addRow("Firstname", self.txtFirstname)
        self.form.addRow("email", self.txtEmail)
        self.form.addRow("Sexe", qSexe)
        self.form.addRow("Date Nais.", self.txtDateNais)
        self.form.addRow("Adresse", self.txtAdresse)
        self.form.addRow("", hbBouton)
        layoutprincipal.addLayout(self.form)
        self.inscriptions.setLayout(layoutprincipal)

    def nouveau(self):
        self.txtUsername.clear()
        self.txtLastname.clear()
        self.txtFirstname.clear()
        self.txtEmail.clear()
        self.txtAdresse.clear()
        self.txtDateNais.setDate(date.today())
        self.rdMasculin.setChecked(False)
        self.rdFeminin.setChecked(False)
        # btn
        self.btDelete.setEnabled(False)
        self.btUpdate.setEnabled(False)
        self.btSave.setEnabled(True)

    def enregistrer(self):
        self.insc.code = None
        # self.insc.nomComplet = self.txtNom.text()
        # sexe = None
        # if self.rdFeminin.isChecked():
        #     sexe = self.rdFeminin.text()
        # else:
        #     sexe = self.rdMasculin.text()
        # self.insc.sexe = sexe
        # self.insc.dateNais = self.txtDateNais.date().toPyDate()
        # self.insc.faculte = self.cbFaculte.currentText()
        # self.insc.adresse = self.txtAdresse.text()
        # self.insc.enregistrer()
        # self.nouveau()
        # self.loadDatas()

    def modifier(self):
        self.insc.code = self.txtCode.text()
        # self.insc.nomComplet = self.txtNom.text()
        # sexe = None
        # if self.rdFeminin.isChecked():
        #     sexe = self.rdFeminin.text()
        # else:
        #     sexe = self.rdMasculin.text()
        # self.insc.sexe = sexe
        # self.insc.dateNais = self.txtDateNais.date().toPyDate()
        # self.insc.faculte = self.cbFaculte.currentText()
        # self.insc.adresse = self.txtAdresse.text()
        # self.insc.modifier()
        # self.btSave.setEnabled(False)
        # self.nouveau()
        # self.loadDatas()

    def creertableau(self):
        self.table = QTableWidget()
        header = ("Code", "Nom complet", "Sexe",
                  "Date nais.", "Faculte", "Adresse")
        self.table.setColumnCount(len(header))
        self.table.setHorizontalHeaderLabels(header)
        # ajouter un signal sur le QTableWidget
        self.table.cellClicked.connect(self.myTableEvent)
        self.form.addWidget(self.table)

    def loadDatas(self):
        ligne = self.insc.afficher()
        self.table.setRowCount(len(ligne))
        row = 0
        for l in ligne:
            self.table.setItem(row, 0, QTableWidgetItem(str(l[0])))
            self.table.setItem(row, 1, QTableWidgetItem(str(l[1])))
            self.table.setItem(row, 2, QTableWidgetItem(str(l[2])))
            self.table.setItem(row, 3, QTableWidgetItem(str(l[3])))
            self.table.setItem(row, 4, QTableWidgetItem(str(l[4])))
            self.table.setItem(row, 5, QTableWidgetItem(str(l[5])))
            row += 1

    def myTableEvent(self):
        index = self.table.currentRow()
        self.btUpdate.setEnabled(True)
        self.btDelete.setEnabled(True)
        self.btSave.setEnabled(False)
        ligne = self.insc.rechercher(self.table.item(index, 0).text())
        self.txtCode.setText(str(ligne[0]))
        self.txtNom.setText(str(ligne[1]))
        if ligne[2] == "Masculin":
            self.rdMasculin.setChecked(True)
        else:
            self.rdFeminin.setChecked(True)
        self.txtDateNais.setDate(date.fromisoformat(str(ligne[3])))
        self.cbFaculte.setCurrentText(str(ligne[4]))
        self.txtAdresse.setText(str(ligne[5]))

    def supprimer(self):
        id_to_delete = self.txtCode.text()
        self.insc.supprimer(id_to_delete)
        self.loadDatas()
        self.nouveau()
