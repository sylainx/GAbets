from Helpers.Helpers import Helpers
from Models.dbconnection import DBConnection
from PyQt5.QtWidgets import QMessageBox
import mysql.connector


class BalanceModel:

    def __init__(self, code_user=None, action=None, montant=None, agent_id=None, ):
        self.code_user = code_user
        self.action = action
        self.montant = montant
        self.agent_id = agent_id
        
        self.util= Helpers()

    def save(self):
        try:
            
            self.obj = DBConnection()
            self.conn = self.obj.connection()
            # creer la chaine de requete
            
            requete = " INSERT INTO `solde`(`id`, `code_user`, `action`, `montant`, `created_at`, \
                `updated_at`, `deleted_at`, `agent_id`)\
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "

            # definir un cursor
            self.cursor = self.conn.cursor(prepared=True)
            # definir les valeurs
            valeurs = [None, self.code_user, self.action, self.montant, self.util.get_day(), self.util.get_day(),
            None, self.agent_id]

            # executer la requete
            self.cursor.execute(requete, valeurs)
            
            # Get the ID of the inserted row
            inserted_id = self.cursor.lastrowid

            # Execute a SELECT statement to retrieve the inserted row
            self.cursor.execute("SELECT * FROM `solde` WHERE id = %s", (inserted_id,))
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
                    None, "Confirmation - balance", "Enregistrement reussi", QMessageBox.Ok)
                return inserted_id

            else:
                QMessageBox.warning(
                    None, "Error - balance", "BLC- Quelque chose s'est mal passé", QMessageBox.Ok)
            
            # validation du changement au niveau de la table
            self.cursor.close()
            self.conn.commit()
            
        except mysql.connector.Error as erreur:
            QMessageBox.warning(None, "Erreur - balance", "BLC- Erreur " +
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
            requete = " SELECT * FROM `solde` "
            self.cursor = self.conn.cursor()
            self.cursor.execute(requete)
            self.liste = self.cursor.fetchall()

        except mysql.connector.Error as erreur:
            QMessageBox.warning(
                None, "Erreur - balance", "BLC- Impossible d'acceder a la BD " + str(erreur), QMessageBox.Ok)
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
            requete = " SELECT * FROM `solde` WHERE id=%s "
            self.cursor = self.conn.cursor()
            valeur = (id,)
            self.cursor.execute(requete, valeur)
            self.liste = self.cursor.fetchone()

        except mysql.connector.Error as erreur:
            QMessageBox.warning(
                None, "Erreur - balance", "BLC- Impossible de se connecter a la BD " + str(erreur), QMessageBox.Ok)
            # fermer le cursor
            self.cursor.close()
            # tester si la connexion est ouverte
            if self.conn.is_connected():
                # fermer la connexion
                self.conn.close()
        return self.liste


    def searchForUser(self, code_user, action=None):
        try:
            obj = DBConnection()
            self.conn = obj.connection()
            requete = " SELECT montant,action,code_user FROM `solde` WHERE code_user=%s "
            if action and action == 1 or action== 2:
                requete += "AND action= %s"
            else:
                requete += ""   # empty but necessary
            
            self.cursor = self.conn.cursor()
            valeur = (code_user,action)
            self.cursor.execute(requete, valeur)
            self.liste = self.cursor.fetchall()

        except mysql.connector.Error as erreur:
            QMessageBox.warning(
                None, "Erreur - balance", "BLC- Impossible de se connecter a la BD " + str(erreur), QMessageBox.Ok)
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
            requete = " UPDATE `solde` SET code_user=%s, montant=%s, agent_id=%s,\
                WHERE id=%s"
            valeurs = (self.code_user, self.montant, self.agent_id, id)

            self.cursor = self.conn.cursor()
            self.cursor.execute(requete, valeurs)
            self.conn.commit()
            QMessageBox.information(
                None, "Confirmation - balance", "BLC- Modification reussie", QMessageBox.Ok)
        except mysql.connector.Error as erreur:
            QMessageBox.warning(
                None, "Erreur - balance", "BLC- Impossible d'acceder a la BD " + str(erreur), QMessageBox.Ok)
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
            requete = " DELETE FROM `solde` WHERE id=%s "
            valeur = (id,)
            self.cursor = self.conn.cursor()
            rep = QMessageBox.question(
                None, "Confirmation - balance", "BLC- Voulez-vous supprimer cette inscription", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if rep == QMessageBox.Yes:
                self.cursor.execute(requete, valeur)
                self.conn.commit()
        except mysql.connector.Error as erreur:
            QMessageBox.warning(
                None, "Erreur - balance", "BLC- Impossible de surpprimer cett inscription: " + str(erreur), QMessageBox.Ok)
            # fermer le cursor
            self.cursor.close()
            # tester si la connexion est ouverte
            if self.conn.is_connected():
                # fermer la connexion
                self.conn.close()
