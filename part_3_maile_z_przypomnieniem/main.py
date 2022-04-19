from sys import argv
from os import environ,  getenv
import os
from dotenv import load_dotenv
import smtplib, ssl
import sqlite3
from datetime import datetime

load_dotenv()

class Database:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE loans
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL,
        email TEXT NOT NULL, 
        book_title TEXT NOT NULL, 
        return_at DATE)''')
        self.connection.commit()

    def insert(self):
        name = input("podaj imie")
        email = input("podaj email")
        book =  input("podaj tytuł książki")
        return_at = input("kiedy ma być zwrócona, format RRRR-MM-DD GG:MM:SS")
        self.cursor.execute(f"INSERT INTO loans (id, name, email, book_title, return_at) VALUES (Null, '{name}', '{email}', '{book}', '{return_at}')")
        self.connection.commit()

    def expired(self):
        date_now = datetime.now()
        return self.cursor.execute(f'SELECT * FROM loans WHERE return_at > {date_now}')

    def get_all(self):
        return self.cursor.execute('SELECT * FROM loans')

    def gives_back(self, id):
        self.cursor.execute(f'DELETE FROM loans WHERE id = {id}')


# if len(argv) > 1 and argv[1] == "setup":
#     """python3 main.py setup"""
if os.path.exists(getenv("DB_NAME")) == False:
    db = Database(getenv("DB_NAME"))
    print("tworzę nową bazę danych")
    db.create_table()

db = Database(getenv("DB_NAME"))
while True:
    print("co chcesz zrobić:")
    print("1. wyświetl rekordy w bazie")
    print("2. dodaj nowy rekord")
    print("3. usuń rekord")
    print("4. wyjście")
    decision = int(input())
    if decision == 1:
        dane = db.get_all()
        for i in dane:
            print(i)
    elif decision == 2:
        db.insert()
    elif decision == 3:
        id = int(input("podaj id rekordu do usunięcia"))
        db.gives_back(id)
    elif decision == 4:
        break




# smtp_server = "smtp.gmail.com"
# port = 465
# sender_email = getenv("EMAIL_PYCAMP")
# password = getenv("PASSWORD_PYCAMP")

# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, sender_email, "kolejny mail z pythona")
