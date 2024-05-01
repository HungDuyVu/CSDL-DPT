import re

import mysql.connector
import json

# connect DB
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="audio"
)

class Database():
    def save_word_extraction(self):
        print(1)

db = Database()