from Helpers.Helpers import Helpers
from Models.dbconnection import DBConnection
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
from datetime import date


class PlayMatchModel:

    def __init__(self, match_id=None, score_1=None, score_2=None, status=None, agent_id=None):
        self.match_id = match_id
        self.score_1 = score_1
        self.score_2 = score_2
        self.status = status
        self.agent_id = agent_id
        self.util = Helpers()


    def save(self):
        try:
            code_user = 1
            self.obj = DBConnection()
            self.conn = self.obj.connection()
            
            # creer la chaine de requete
            requete = " INSERT INTO `play_match`(`id`, `match_id`, `score_1`, `score_2`, `status`, `agent_id`, `created_at`, `updated_at`, `deleted_at`) \
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) "

            # definir un cursor
            self.cursor = self.conn.cursor(prepared=True)
            # definir les valeurs
            valeurs = [None, self.match_id, self.score_1, self.score_2,self.status, self.agent_id, self.util.get_day(), self.util.get_day() , None]

            # executer la requete
            self.cursor.execute(requete, valeurs)
            
            # Get the ID of the inserted row
            inserted_id = self.cursor.lastrowid

            # Execute a SELECT statement to retrieve the inserted row
            self.cursor.execute("SELECT * FROM `play_match` WHERE id = %s", (inserted_id,))
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
            requete = " SELECT * FROM `play_match` WHERE `deleted_at` IS NULL "
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
            requete = " SELECT* FROM `play_match` WHERE CODE=%s "
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
