from PyQt5.QtWidgets import QMessageBox
import mysql.connector
import secrets
from datetime import date
from Models.dbconnection import DBConnection
from Helpers.Helpers import Helpers


class RegisterModel:
    # util = Helpers()

    def __init__(self, lastname=None, firstname=None, email=None, sexe=None, date_nais=None, tel=None, password=None,
                 address=None, username=None, nif=None):
        self.lastname = lastname
        self.firstname = firstname
        self.username = username
        self.email = email
        self.sexe = sexe
        self.date_nais = date_nais
        self.tel = tel
        self.password = password
        self.address = address
        self.nif = nif
        self.util = Helpers()

# fonction permettant de generer un code d'utilisateur unique
    def generer_code(self) -> str:
    # generate 1 secure random numbers between 10 and 500
        for x in range(0, 1):
            self.secret_code = "CODE_" + (10 + secrets.randbelow(500)).__str__()
            self.verify_code(self.secret_code)
        # recursive function : get unique ID in all_commandes
        return self.secret_code

# fonction permettant de verifier si le code n'existe pas 
    def verify_code(self,secret_code):
        
        self.obj_con = DBConnection()
        self.conn = self.obj_con.connection()
        # prepare
        query = " SELECT `code_user` FROM `users` WHERE code_user=%s "
        self.cursor = self.conn.cursor(prepared=True)
        # define values
        statement = [secret_code]
        # execute query
        self.cursor.execute(query, statement)
        # return nb line
        data_found = self.cursor.fetchone()
        if data_found == True:
            self.generer_code()

    

    def enregistrer(self):
        try:
            code_user = self.generer_code()

            self.obj = DBConnection()
            self.conn = self.obj.connection()

            # hash password
            pwd_hashed = self.util.hash_password(self.password)

            # creer la chaine de requete
            
            requete = " INSERT INTO `users` (`id`, `firstname`, `lastname`, `email`, `tel`, `code_user`, `address`,\
                 `username`, `nif`, `sexe`, `dataNais`, `password`, `created_at`, `updated_at`, `deleted_at`) \
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "

            # definir un cursor
            self.cursor = self.conn.cursor(prepared=True)
            # definir les valeurs
            valeurs = ["None", self.firstname, self.lastname, self.email, self.tel, code_user,
                       self.address, self.username, self.nif, self.sexe, self.date_nais, pwd_hashed, self.util.get_day(), 
                       self.util.get_day(), None]
            print(f'Valeurs: {valeurs} ')
            # executer la requete
            result = self.cursor.execute(requete, valeurs)

            if result:
                # fermer le cursor
                self.cursor.close()
                # validate updates
                self.conn.commit()
                return True
            else:
                QMessageBox.warning(
                    None, "Error", "Quelque chose s'est mal passé", QMessageBox.Ok)
            # end result

            # validation du changement au niveau de la table
            self.conn.commit()
            # retourne le nombre de ligne affecte

        except mysql.connector.Error as erreur:
            QMessageBox.warning(None, "Erreur", "Erreur - " +
                                str(erreur), QMessageBox.Ok)
            # fermer le cursor
            self.cursor.close()
            # tester si la connexion est ouverte
            if self.conn.is_connected():
                # fermer la connexion
                self.conn.close()

    def afficher(self):
        try:
            self.obj = DBConnection()
            self.conn = self.obj.connection()
            # requete de selection
            requete = " SELECT * FROM USERS WHERE `deleted_at` IS NULL "
            self.cursor = self.conn.cursor()
            self.cursor.execute(requete)
            self.liste = self.cursor.fetchall()
        except mysql.connector.Error as erreur:
            QMessageBox.warning(
                None, "Erreur", "Impossible d'acceder a la BD " + str(erreur), QMessageBox.Ok)
            # fermer le cursor
            self.cursor.close()
            # tester si la connexion est ouverte
            if self.conn.is_connected():
                # fermer la connexion
                self.conn.close()
        return self.liste

    def rechercher(self, code):
        try:
            obj = DBConnection()
            self.conn = obj.connection()
            requete = " SELECT* FROM USERS WHERE CODE=%s "
            self.cursor = self.conn.cursor()
            valeur = (code,)
            self.cursor.execute(requete, valeur)
            self.liste = self.cursor.fetchone()

        except mysql.connector.Error as erreur:
            QMessageBox.warning(
                None, "Erreur", "Impossible de se connecter a la BD " + str(erreur), QMessageBox.Ok)
            # fermer le cursor
            self.cursor.close()
            # tester si la connexion est ouverte
            if self.conn.is_connected():
                # fermer la connexion
                self.conn.close()
        return self.liste

    def modifier(self):
        try:
            obj = DBConnection()
            self.conn = obj.connection()
            requete = " UPDATE USERS SET firstname=%s, lastname=%s, username=%s, email=%s, sexe=%s, datenais=%s, tel=%s, \
                address=%s, nif=%s, updated_at=%s,\
             WHERE CODE=%s"
            valeurs = (self.firstname, self.lastname, self.username, self.email, self.sexe, self.date_nais,
                       self.tel, self.address, self.nif, self.get_day)
            self.cursor = self.conn.cursor()
            self.cursor.execute(requete, valeurs)
            self.conn.commit()
            QMessageBox.information(
                None, "Confirmation", "Modification reussie", QMessageBox.Ok)
        except mysql.connector.Error as erreur:
            QMessageBox.warning(
                None, "Erreur", "Impossible d'acceder a la BD " + str(erreur), QMessageBox.Ok)
            # fermer le cursor
            self.cursor.close()
            # tester si la connexion est ouverte
            if self.conn.is_connected():
                # fermer la connexion
                self.conn.close()

    def supprimer(self, code):

        try:
            obj = DBConnection()
            conn = obj.connection()
            requete = " DELETE FROM USERS WHERE CODE=%s "
            valeur = (code,)
            self.cursor = self.conn.cursor()
            rep = QMessageBox.question(
                None, "Confirmation", "Voulez-vous supprimer cette inscription", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if rep == QMessageBox.Yes:
                self.cursor.execute(requete, valeur)
                self.conn.commit()
        except mysql.connector.Error as erreur:
            QMessageBox.warning(
                None, "Erreur", "Impossible de surpprimer cett inscription: " + str(erreur), QMessageBox.Ok)
            # fermer le cursor
            self.cursor.close()
            # tester si la connexion est ouverte
            if self.conn.is_connected():
                # fermer la connexion
                self.conn.close()

    def get_day(self,):
        return date.today()
