from Models.dbconnection import DBConnection
from PyQt5.QtWidgets import QMessageBox
import mysql.connector


class RatioModel:

    def __init__(self, title=None, ratio=None, visible=None, ):
        self.title = title
        self.ratio = ratio
        self.visible = visible
        

    def enregistrer(self):
        try:
            code_user = 1
            self.obj = DBConnection()
            self.conn = self.obj.connection()
            # creer la chaine de requete
            requete = "INSERT INTO `ratios`(`id`, `title`, `ratio`, `visible`)\
                VALUES (%s,%s,%s,%s) "

            # definir un cursor
            self.cursor = self.conn.cursor(prepared=True)
            # definir les valeurs
            valeurs = [None, self.title, self.ratio, self.visible]

            # executer la requete
            self.cursor.execute(requete, valeurs)
            
            
            # Get the ID of the inserted row
            inserted_id = self.cursor.lastrowid

            # Execute a SELECT statement to retrieve the inserted row
            self.cursor.execute("SELECT * FROM `ratios` WHERE id = %s", (inserted_id,))
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
            requete = " SELECT * FROM `ratios` "
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



    def search(self, id):
        try:
            obj = DBConnection()
            self.conn = obj.connection()
            requete = " SELECT * FROM `ratios` WHERE id=%s "
            self.cursor = self.conn.cursor()
            valeur = (id,)
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



    def update(self,id):
        try:
            obj = DBConnection()
            self.conn = obj.connection()
            requete = " UPDATE `ratios` SET title=%s, ratio=%s, visible=%s,\
                WHERE id=%s"
            valeurs = (self.title, self.ratio, self.visible, id)

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


    def delete(self, id):

        try:
            obj = DBConnection()
            conn = obj.connection()
            requete = " DELETE FROM `ratios` WHERE id=%s "
            valeur = (id,)
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
