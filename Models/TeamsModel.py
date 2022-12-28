import bcrypt
import mysql.connector
from PyQt5.QtWidgets import QMessageBox
from Helpers.Helpers import Helpers
#
from Models.dbconnection import DBConnection


class TeamsModel:

    def __init__(self, title=None, level=None, img=None, agent_id=None):
        self.id = int # only to delete and update
        self.title = title
        self.level = level
        self.img = img
        self.agent_id = agent_id
        self.util = Helpers()

    # end init

    def save(self):
        try:
            self.obj = DBConnection()
            self.conn = self.obj.connection()
            # prepare queries
            query = " INSERT INTO `teams`(`id`, `img`, `title`, `level`,`agent_id`, `created_at`,\
            `updated_at`, `deleted_at`) \
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "

            # cursor
            self.cursor = self.conn.cursor(prepared=True)
            # define values
            stmt = [None, self.img, self.title, self.level, self.agent_id, self.util.get_day(),
                    self.util.get_day(), None]

            # execute query
            result = self.cursor.execute(query, stmt)

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

            # fermer le cursor
            self.cursor.close()
            # validate updates
            self.conn.commit()
            return False

        except mysql.connector.Error as erreur:
            QMessageBox.warning(None, "Erreur", "Erreur " +
                                str(erreur), QMessageBox.Ok)
            # fermer le cursor
            self.cursor.close()

        finally:
            # tester si la connexion est ouverte
            if self.conn.is_connected():
                # fermer la connexion
                self.conn.close()

    def show(self):
        try:
            self.obj = DBConnection()
            self.conn = self.obj.connection()
            # requete de selection
            requete = " SELECT * FROM `teams` WHERE `deleted_at` IS NULL "
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
            self.obj = DBConnection()
            self.conn = self.obj.connection()
            requete = " SELECT* FROM `teams` WHERE id=%s "
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

    def update(self, id:int):

        id=int(id)
        print(f"IDs: {id} | type: {type(id)}")
        
        try:
            obj = DBConnection()
            self.conn = obj.connection()
            # UPDATE `teams` SET `id`='[value-1]',`img`='[value-2]',`title`='[value-3]',
            # `level`='[value-4]',`agent_id`='[value-5]',`created_at`='[value-6]',`updated_at`='[value-7]',`deleted_at`='[value-8]' WHERE 1
            requete = " UPDATE `teams` SET title=%s, level=%s, agent_id=%s, updated_at=%s,\
                WHERE id=%s "
            valeurs = (self.title, self.level, self.agent_id,
                       self.util.get_day(), id)
            self.cursor = self.conn.cursor()

            result = self.cursor.execute(requete, valeurs)

            if result:
                # validation du changement au niveau de la table
                self.conn.commit()
                # fermer le cursor
                self.cursor.close()
                # validate updates
                self.conn.commit()
                return True
            else:
                QMessageBox.warning(
                    None, "Error", "Quelque chose s'est mal passé", QMessageBox.Ok)
            # end result

            self.conn.commit()

            return False
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
            self.conn = obj.connection()
            requete = " DELETE FROM `teams` WHERE CODE=%s "
            valeur = (code,)
            self.cursor = self.conn.cursor()
            rep = QMessageBox.question(
                None, "Confirmation", "Voulez-vous supprimer cette equipe", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if rep == QMessageBox.Yes:
                result = self.cursor.execute(requete, valeur)

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

                self.conn.commit()
        except mysql.connector.Error as erreur:
            QMessageBox.warning(
                None, "Erreur", "Impossible de surpprimer cette equipe: " + str(erreur), QMessageBox.Ok)
            # fermer le cursor
            self.cursor.close()
            # tester si la connexion est ouverte
            if self.conn.is_connected():
                # fermer la connexion
                self.conn.close()
