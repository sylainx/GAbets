import mysql.connector

from Models.dbconnection import DBConnection


class Controller:
    def __init__(self, db_path):
        self.conn = self.obj = DBConnection()
        self.conn = self.obj.connection()
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        
        if self.is_table_exist(table_name):
            return  # La table est déja là, on ne fait rien

        # Générer la commande SQL pour créer la table
        column_defs = ", ".join([f"{name} {datatype}" for name, datatype in columns])
        sql = f"CREATE TABLE {table_name} ({column_defs})"
    
        # Exécuter la commande SQL
        self.cursor.execute(sql)
        self.conn.commit()

        # Vérifier si la table a été créée
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        if self.cursor.fetchone():
            return True # La table est créée, 
        return False # Un probleme est survenu, 

    def insert(self, table_name, values):

        if not self.is_table_exist(table_name):
            return  # La table n'est pas presente, on ne fait rien

        # Générer la commande SQL pour insérer un enregistrement
        column_names = ", ".join([name for name, _ in values])
        placeholders = ", ".join(["?" for _, _ in values])
        sql = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"

        # Exécuter la commande SQL avec les valeurs
        self.cursor.execute(sql, [value for _, value in values])
        
        # Get the ID of the inserted row
        inserted_id = self.cursor.lastrowid
        # Execute a SELECT statement to retrieve the inserted row
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE id = {inserted_id}")
        self.conn.commit()

        # Fetch the inserted row
        inserted_row = self.cursor.fetchone()

        # Check the inserted row
        if inserted_row:
            # Data has been inserted successfully
            return inserted_id
        else:
            return False

    def select(self, table_name, where=None, order_by=None):

        if not self.is_table_exist(table_name):
            return  # La table n'est pas presente, on ne fait rien
            
        # Générer la commande SQL pour sélectionner des enregistrements
        sql = f"SELECT * FROM {table_name}"
        if where:
            sql += f" WHERE {where}"
        if order_by:
            sql += f" ORDER BY {order_by}"
        # Exécuter la commande SQL et récupérer les résultats
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update(self, table_name, values, where):
        # Générer la commande SQL pour mettre à jour un enregistrement
        updates = ", ".join([f"{name} = ?" for name, _ in values])
        sql = f"UPDATE {table_name} SET {updates} WHERE {where}"

        # Exécuter la commande SQL avec les valeurs
        self.cursor.execute(sql, [value for _, value in values])
        self.conn.commit()

    def delete(self, table_name, where):
        # Générer la commande SQL pour supprimer un enregistrement
        sql = f"DELETE FROM {table_name} WHERE {where}"
        # Exécuter la commande SQL
        self.cursor.execute(sql)
        self.conn.commit()

    def drop(self, table_name):

        if not self.is_table_exist(table_name):
            return  # La table n'est pas presente, on ne fait rien

        # Générer la commande SQL pour supprimer un enregistrement
        sql = f"DROP TABLE {table_name} "
        # Exécuter la commande SQL
        self.cursor.execute(sql)
        self.conn.commit()

    def is_table_exist(self, table_name):
        # Vérifier l'existence de la table
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        if self.cursor.fetchone():
            return True  # La table est presente
        return False