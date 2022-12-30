import mysql.connector
from PyQt5.QtWidgets import QMessageBox
import platform


class DBConnection:

    def connection(self):
        host = "localhost"
        db_name = "ag_betssport"
        user = "root"
        if platform.system() == 'Windows':
            pwd = ''
        elif platform.system() == 'Darwin':
            pwd = 'root'
        else:
            pwd= ''

            
        try:
            self.conn = mysql.connector.connect(
                host=host, database=db_name, user=user, password=pwd)
        except mysql.connector.Error as erreur:
            QMessageBox.warning(None, "Erreur de connexion",
                                "Impossible de se connecter a la BD"+str(erreur), QMessageBox.Ok)
        return self.conn
