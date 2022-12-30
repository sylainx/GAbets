from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QRadioButton, QTableWidgetItem, QTableWidget, QTextEdit, QComboBox, QDateEdit, QPushButton, QVBoxLayout, QFormLayout, QGridLayout, QTabWidget, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt
from Models.RegisterModel import RegisterModel
from datetime import date


def creerOnglet(self):

    rightside_layout = QHBoxLayout()
    content_rightside = QWidget()
    content_rightside.setStyleSheet(
        "background-color: #f9fbfc;"
        "border-radius: 10px;"
    )
    content_rightside.setLayout(rightside_layout)

    # 2e ligne, 3e colon
    self.gridLayout.addWidget(content_rightside, 1, 2)


    # radioButton Layouts
    q_gender_LYT = QHBoxLayout()
    have_account_LYT = QHBoxLayout()
    # creating a form self.gridLayout
    form_layout = QVBoxLayout()
    self.loginbtn = QPushButton("Sign Up")
    self.loginbtn.setCursor(Qt.PointingHandCursor)
    self.loginbtn.setStyleSheet("color: white;\n"
                                "    margin-top:5px;\n"
                                "    height:30px;\n"
                                "    width:100px;\n"
                                "color:white;\n"
                                "text-align:center;\n"
                                "background-color:blue;\n"
                                "border-radius:10px;\n"
                                "font-size:15px;\n"
                                )
    self.have_account = QLabel("have an account?")
    self.have_account.setAlignment(QtCore.Qt.AlignCenter);
    self.have_account.setStyleSheet("font-size: 12px;\n"
                                    "    margin-top:5px;\n"
                                    "    color:1E1E1E;\n"
                                    "    text-align:center;\n")

    self.inviteSignUpBtn = QPushButton("Login to account")
    self.inviteSignUpBtn.setCursor(Qt.PointingHandCursor)
    self.inviteSignUpBtn.setStyleSheet("font-size: 12px;\n"
                                        "    margin-top:5px;\n"
                                        "    text-align:center;\n"
                                        "    color: blue;\n")

    self.inviteSignUpBtn.clicked.connect(lambda: self.clallSignUpFunc())
    form_layout.setAlignment(Qt.AlignTop)
    self.label_title = QLabel("Sign Up Page")
    self.label_title.setAlignment(QtCore.Qt.AlignCenter);
    self.label_title.setStyleSheet("    font-size: 15px;\n"
                                    "    font-weight:bold;\n"
                                    "    margin-top:5px;\n"
                                    "    text-align:center;\n"
                                    "    color:blue;\n"
                                    )
    # create link back to login
    have_account_LYT.addWidget(self.have_account)
    have_account_LYT.addWidget(self.inviteSignUpBtn)
    # add radioButton to Widget
    self.rdMale = QRadioButton("Masculin")
    self.rdFemale = QRadioButton("Feminin")
    q_gender_LYT.addWidget(self.rdFemale)
    q_gender_LYT.addWidget(self.rdMale)
    # Create date
    self.txtDateOfBirth = QDateEdit()
    self.txtDateOfBirth.setDisplayFormat("dd/MM/yyyy")
    self.txtDateOfBirth.setCalendarPopup(True)
    self.txtDateOfBirth.setStyleSheet(
                                    "    color:#1E1E1E;\n"
                                    )

    self.txtFirstName = QLineEdit()
    self.txtLastName = QLineEdit()
    self.txtUserName = QLineEdit()
    self.txtAdress = QLineEdit()
    self.txtEmail = QLineEdit()
    self.txtPhone = QLineEdit()
    self.txtNif = QLineEdit()
    self.txtPassword = QLineEdit()
    self.txtConfirmPassword = QLineEdit()
    self.txtConfirmPassword.setEchoMode(QLineEdit.Password)
    self.txtPassword.setEchoMode(QLineEdit.Password)

    # adding rows
    # for name and adding input text
    form_layout.addWidget(self.label_title)
    form_layout.addWidget(QLabel(" First name"))
    form_layout.addWidget(self.txtFirstName)
    form_layout.addWidget(QLabel("Last name"))
    form_layout.addWidget(self.txtLastName)
    form_layout.addWidget(QLabel("User name"))
    form_layout.addWidget(self.txtUserName)
    form_layout.addWidget(QLabel("User Email"))
    form_layout.addWidget(self.txtEmail)
    form_layout.addWidget(QLabel("user Adress"))
    form_layout.addWidget(self.txtAdress)

    form_layout.addWidget(QLabel("Sexe"))
    form_layout.addLayout(q_gender_LYT)

    form_layout.addWidget(QLabel("Date of birth"))
    form_layout.addWidget(self.txtDateOfBirth)

    form_layout.addWidget(QLabel("user Nif"))
    form_layout.addWidget(self.txtNif)
    form_layout.addWidget(QLabel("Password"))
    form_layout.addWidget(self.txtPassword)
    form_layout.addWidget(QLabel("confirm Password"))
    form_layout.addWidget(self.txtConfirmPassword)
    form_layout.addWidget(self.loginbtn)

    form_layout.addLayout(have_account_LYT)


    #     Setting self.gridLayout
    form_layout.addLayout(q_gender_LYT)
    rightside_layout.addLayout(form_layout)
    #
    self.content.setLayout(self.gridLayout)

    