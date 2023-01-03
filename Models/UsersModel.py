from Models.dbconnection import DBConnection
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
from datetime import date


class UsersModel:

    def __init__(self, lastname=None, firstname=None, email=None, sexe=None, date_nais=None, tel=None, password=None,
                 address=None, agent_id=None, username=None, nif=None, is_admin=None):
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
        self.agent_id = agent_id
        self.is_admin = is_admin

    def save(self):
        try:
            code_user = 1
            self.obj = DBConnection()
            self.conn = self.obj.connection()
            # creer la chaine de requete
            requete = " INSERT INTO `users`(`id`, `firstname`, `lastname`, `email`, `tel`, `code_user`, `address`, `username`, `nif`, \
                `sexe`, `dataNais`, `password`, `created_at`, `updated_at`, `deleted_at`,`is_admin`) \
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "

            # definir un cursor
            self.cursor = self.conn.cursor(prepared=True)
            # definir les valeurs
            valeurs = [None, self.firstname, self.lastname, self.email, self.tel, code_user,
                       self.address, self.username, self.nif, self.sexe, self.date_nais, self.password, self.get_day, self.get_day, None, self.is_admin]

            # executer la requete
            self.cursor.execute(requete, valeurs)
            
            
            # Get the ID of the inserted row
            inserted_id = self.cursor.lastrowid

            # Execute a SELECT statement to retrieve the inserted row
            self.cursor.execute("SELECT * FROM `users` WHERE id = %s", (inserted_id,))
            # Fetch the inserted row
            inserted_row = self.cursor.fetchone()

            # Check the inserted row
            if inserted_row:
                # Data has been inserted successfully                
                self.cursor.close()
                # validate updates
                self.conn.commit()
                # retourne le nombre de ligne affecte
                QMessageBox.information(
                    None, "Confirmation", "Enregistrement reussi", QMessageBox.Ok)
                return inserted_id

            else:
                QMessageBox.warning(
                    None, "Error", "Quelque chose s'est mal passé", QMessageBox.Ok)
            
        except mysql.connector.Error as erreur:
            QMessageBox.warning(None, "Erreur", "Erreur " +
                                str(erreur), QMessageBox.Ok)
            # fermer le cursor
            self.cursor.close()
            # tester si la connexion est ouverte
            if self.conn.is_connected():
                # fermer la connexion
                self.conn.close()

    def show(self):
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

    def search(self, code):
        try:
            obj = DBConnection()
            self.conn = obj.connection()
            requete = " SELECT * FROM `USERS` WHERE id=%s "
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

    def update(self):
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

    def delete(self, code):

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
