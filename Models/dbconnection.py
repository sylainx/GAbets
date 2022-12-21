import mysql.connector
from PyQt5.QtWidgets import QMessageBox


class DBConnection:

    def connection(self):
        host = "localhost"
        db_name = "ag_betssport"
        user = "root"
        pwd = ''

        try:
            self.conn = mysql.connector.connect(
                host=host, database=db_name, user=user, password=pwd)
        except mysql.connector.Error as erreur:
            QMessageBox.warning(None, "Erreur de connexion",
                                "Impossible de se connecter a la BD"+str(erreur), QMessageBox.Ok)
        return self.conn
