from Models.dbconnection import DBConnection
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
from datetime import date


class MatchsModel:

    def __init__(self, home_team_id=None, move_team_id=None, priority_id=None,  country=None, agent_id=None):
        self.home_team_id = home_team_id
        self.move_team_id = move_team_id
        self.priority_id = priority_id
        self.country = country
        self.agent_id = agent_id

    def enregistrer(self):
        try:
            code_user = 1
            self.obj = DBConnection()
            self.conn = self.obj.connection()
            # creer la chaine de requete
            requete = " INSERT INTO `matchs`(`id`, `home_team_id`, `move_team_id`, `priority_id`, `created_at`, `updated_at`,\
                 `deleted_at`, `agent_id`, `country`)\
                VALUES (%s,%s,%s,%s,%s) "

            # definir un cursor
            self.cursor = self.conn.cursor(prepared=True)
            # definir les valeurs
            valeurs = [None, self.home_team_id, self.move_team_id, self.priority_id, self.get_day, self.get_day, None,
                       self.agent_id, self.country]

            # executer la requete
            self.cursor.execute(requete, valeurs)
            # validation du changement au niveau de la table
            self.conn.commit()
            # retourne le nombre de ligne affecte
            QMessageBox.information(
                None, "Confirmation", "Enregistrement reussi", QMessageBox.Ok)

        except mysql.connector.Error as erreur:
            QMessageBox.warning(None, "Erreur", "Erreur " +
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
            requete = " SELECT * FROM `MATCHS` WHERE `deleted_at` IS NULL "
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

    def rechercher(self, id):
        try:
            obj = DBConnection()
            self.conn = obj.connection()
            requete = " SELECT * FROM `MATCHS` WHERE id=%s "
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

    def modifier(self,id):
        try:
            obj = DBConnection()
            self.conn = obj.connection()
            requete = " UPDATE `MATCHS` SET home_team_id=%s, move_team_id=%s, priority_id=%s, agent_id=%s, country=%s, \
            updated_at=%s WHERE id=%s"
            valeurs = (self.home_team_id, self.move_team_id, self.priority_id, self.agent_id, self.country,
                    self.get_day, id)
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

    def supprimer(self, id):

        try:
            obj = DBConnection()
            conn = obj.connection()
            requete = " DELETE FROM `MATCHS` WHERE id=%s "
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

    def get_day(self,):
        return date.today()
