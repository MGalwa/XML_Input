# Magdalena Galwa
# 26/11/2025
# Description:
#Homework:
    # Expand previous Homework 5/6/7/8/9 with additional class, which allow to save records into database:
    # 1. Different types of records require different data tables
    # 2. New record creates new row in data table
    # 3. Implement “no duplicate” check.

import sqlite3

class DBConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name):
        if table_name == 'Feed_News':
            table_sql = '''
            CREATE TABLE IF NOT EXISTS Feed_News (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                city TEXT NOT NULL,
                publish_date DATE NOT NULL
            )
            '''
        elif table_name == 'Feed_Private_Ad':
            table_sql = '''
            CREATE TABLE IF NOT EXISTS Feed_Private_Ad (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                expire_date DATE NOT NULL
            )
            '''
        elif table_name == 'Feed_Book_Review':
            table_sql = '''
            CREATE TABLE IF NOT EXISTS Feed_Book_Review (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                rate INTEGER NOT NULL,
                publish_date DATE NOT NULL
            )
            '''
        else:
            raise ValueError("Unknown table name")
        self.cursor.execute(table_sql)
        self.conn.commit()

    def insert_row(self, table, data):
        if self.is_duplicate(table, data):
            print("Duplicate record detected. Not inserting.")
            return False
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        values = list(data.values())
        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(sql, values)
        self.conn.commit()
        print("Record inserted successfully.")
        return True

    def is_duplicate(self, table, data):
        where_clause = ' AND '.join([f"{k} = ?" for k in data.keys()])
        values = list(data.values())
        sql = f"SELECT COUNT(*) FROM {table} WHERE {where_clause}"
        self.cursor.execute(sql, values)
        count = self.cursor.fetchone()[0]
        return count > 0

    def select_all(self, table):
        sql = f"SELECT * FROM {table}"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def close(self):
        self.cursor.close()
        self.conn.close()