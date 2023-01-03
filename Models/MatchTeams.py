import bcrypt
import mysql.connector
from PyQt5.QtWidgets import QMessageBox
from Helpers.Helpers import Helpers
#
from Models.dbconnection import DBConnection


class MatchTeams:

    def __init__(self, match_id=None, home_team_id=None, away_team_id=None,):
        
        self.match_id = match_id
        self.home_team_id = home_team_id
        self.away_team_id = away_team_id
        
    # end init

    def save(self):
        try:
            self.obj = DBConnection()
            self.conn = self.obj.connection()
            # prepare queries
            query = " INSERT INTO `match_teams`(`match_id`, \
                `home_team_id`, `away_team_id`) \
            VALUES (%s,%s,%s) "

            # cursor
            self.cursor = self.conn.cursor(prepared=True)
            # define values
            stmt = [self.match_id, self.home_team_id, self.away_team_id]

            # execute query
            self.cursor.execute(query, stmt)
            

            # Execute a SELECT statement to retrieve the inserted row
            self.cursor.execute("SELECT * FROM `match_teams` WHERE match_id = %s", (self.match_id,))
            # Fetch the inserted row
            inserted_row = self.cursor.fetchone()

            # Check the inserted row
            if inserted_row:
                # Data has been inserted successfully                
                self.cursor.close()
                # validate updates
                self.conn.commit()
                return inserted_row

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
            requete = " SELECT * FROM `match_teams` "
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

    def searchByHomeTeamID(self, id):
        try:
            self.obj = DBConnection()
            self.conn = self.obj.connection()
            requete = " SELECT* FROM `match_teams` WHERE home_team_id=%s "
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

    def searchByMatchId(self, title:str):
        try:
            self.obj = DBConnection()
            self.conn = self.obj.connection()
            requete = " SELECT * FROM `match_teams` WHERE match_id=%s "
            self.cursor = self.conn.cursor()
            valeur = (title,)
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

