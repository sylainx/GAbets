from datetime import date
import mysql.connector
from PyQt5.QtWidgets import QMessageBox
from Helpers.Helpers import Helpers
#
from Models.dbconnection import DBConnection


class LoginModel:

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.util = Helpers()

    # end init

    def check_user_connect(self):
        try:
            self.obj_con = DBConnection()
            self.conn = self.obj_con.connection()

            # prepare
            query = " SELECT `password`, `id` FROM `users` WHERE username=%s "

            self.cursor = self.conn.cursor(prepared=True)
            # define values
            statement = [self.username]

            # execute query
            self.cursor.execute(query, statement)
            # return nb line
            self.data_found = self.cursor.fetchone()

            if self.data_found and type(self.data_found) is tuple:

                if (self.util.verify_password(self.password, self.data_found[0])):
                    # retourne le nombre de ligne affecte
                    QMessageBox.information(
                        None, "Confirmation", "Connexion reussi", QMessageBox.Ok)
                    # close cursor
                    self.cursor.close()
                    # test to close connection
                    if self.conn.is_connected():
                        self.conn.close()

                    return self.data_found[1]
                else:
                    QMessageBox.warning(
                        None, "Error", "Mot de passe incorrect", QMessageBox.Ok)
                # end clause hash_password
            else:
                QMessageBox.warning(
                    None, "Error", "Nom d'utilisateur incorrect", QMessageBox.Ok)

            # end clause data_found
            # close cursor
            self.cursor.close()
            # test to close connection
            if self.conn.is_connected():
                self.conn.close()

            return False

        except mysql.connector.Error as error:
            QMessageBox.warning(None, "Error", "Error " +
                                str(error), QMessageBox.Ok)
            # close cursor
            self.cursor.close()
            # test to close connection
            if self.conn.is_connected():
                self.conn.close()

    # end function check_user_connection


    
    def enregistrer(self):
        try:
            code_user = 1

            self.obj = DBConnection()
            self.conn = self.obj.connection()

            # hash password
            pwd_hashed = self.util.hash_password(self.password)

            # creer la chaine de requete
            requete = " INSERT INTO `users`(`id`, `firstname`, `lastname`, `email`, `tel`, `code_user`, `address`, `username`, `nif`, \
                `sexe`, `dataNais`, `password`, `created_at`, `updated_at`, `deleted_at`) \
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)) "

            # definir un cursor
            self.cursor = self.conn.cursor(prepared=True)
            # definir les valeurs
            valeurs = [None, self.firstname, self.lastname, self.email, self.tel, code_user,
                       self.address, self.username, self.nif, self.sexe, self.date_nais, pwd_hashed, self.get_day, self.get_day, None]

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
            QMessageBox.warning(None, "Erreur", "Erreur " +
                                str(erreur), QMessageBox.Ok)
            # fermer le cursor
            self.cursor.close()
            # tester si la connexion est ouverte
            if self.conn.is_connected():
                # fermer la connexion
                self.conn.close()
