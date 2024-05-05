import re

import mysql.connector
import json

# connect DB
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="audio"
)


def check_table_exists():
    # Create cursor
    mycursor = mydb.cursor()

    # Check if the table exists
    if not table_exists(mycursor, "audio"):
        # Table doesn't exist, create it
        create_table(mycursor)
        print("Table 'audio' created successfully.")
    else:
        print("Table 'audio' already exists.")

def table_exists(cursor, table_name):
    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    return cursor.fetchone() is not None


def create_table(cursor):
    cursor.execute("""
        CREATE TABLE audio (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            content TEXT
        )
    """)

check_table_exists()
class Database():
    def get_all_information(self):
        mycursor = mydb.cursor()
        sql = "SELECT * FROM audio"

        mycursor.execute(sql)
        # Fetch all the results
        results = mycursor.fetchall()
        return results

    def save_word_extraction(self,content):
        mycursor = mydb.cursor()
        sql = "INSERT INTO audio (name, content) VALUES (%s, %s)"
        values = ('test', content)

        mycursor.execute(sql, values)

        # Remember to commit the transaction if you want to make the changes permanent
        mydb.commit()

    def save_audio_name(self,name):
        mycursor = mydb.cursor()
        sql = "INSERT INTO audio (name, content) VALUES (%s, %s)"
        values = (name, 'null')

        mycursor.execute(sql, values)

        # Remember to commit the transaction if you want to make the changes permanent
        mydb.commit()
db = Database()
