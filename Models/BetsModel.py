from Helpers.Helpers import Helpers
from Models.dbconnection import DBConnection
from PyQt5.QtWidgets import QMessageBox
import mysql.connector


class BetsModel:

    def __init__(self, match_id=None, ratio_id=None, user_id=None, amount=None, agent_id=None, status=None):
        self.match_id = match_id
        self.ratio_id = ratio_id
        self.user_id = user_id
        self.amount = amount
        self.agent_id = agent_id
        self.status = status
        self.util = Helpers()

    def save(self):
        try:

            self.obj = DBConnection()
            self.conn = self.obj.connection()
            # creer la chaine de requete
            requete = " INSERT INTO `bets`(`id`, `match_id`, `ratio_id`, `user_id`, `created_at`,\
                 `amount`, `deleted_at`, `agent_id`, `status`)\
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) "

            # definir un cursor
            self.cursor = self.conn.cursor(prepared=True)
            # definir les valeurs
            valeurs = [None, self.match_id, self.ratio_id, self.user_id, self.util.get_day(), 
            self.amount,None, self.agent_id, self.status]

            # executer la requete
            self.cursor.execute(requete, valeurs)
            # validation du changement au niveau de la table
            
            
            # Get the ID of the inserted row
            inserted_id = self.cursor.lastrowid

            # Execute a SELECT statement to retrieve the inserted row
            self.cursor.execute("SELECT * FROM `bets` WHERE id = %s", (inserted_id,))
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
            requete = " SELECT * FROM `bets` "
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
            requete = " SELECT * FROM `bets` WHERE id=%s "
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

    def update(self, id):
        try:
            obj = DBConnection()
            self.conn = obj.connection()
            requete = " UPDATE `bets` SET match_id=%s, ratio_id=%s, user_id=%s, amount=%s,\
                 agent_id=%s, status=%s\
                WHERE id=%s"

            valeurs = (self.match_id, self.ratio_id, self.user_id , self.montant, self.agent_id,
            self.agent_id, self.status, id)

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
            requete = " DELETE FROM `bets` WHERE id=%s "
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
