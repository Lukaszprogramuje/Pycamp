from os import getenv
import os
import sqlite3
import smtplib
import ssl
from datetime import datetime
from dotenv import load_dotenv

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
        name = input("podaj imie  ")
        email = input("podaj email  ")
        book =  input("podaj tytuł książki  ")
        return_at = input("kiedy ma być zwrócona, format RRRR-MM-DD  ")
        self.cursor.execute(f"""INSERT INTO loans (id, name, email, book_title, return_at)
        VALUES (Null, '{name}', '{email}', '{book}', '{return_at}')""")
        self.connection.commit()

    def expired(self):
        date_now = datetime.now().strftime('%Y-%m-%d')
        return self.cursor.execute(f"SELECT * FROM loans WHERE return_at < '{date_now}'")

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

smtp_server = "smtp.gmail.com"
port = 465
sender_email = getenv("EMAIL_PYCAMP")
password = getenv("PASSWORD_PYCAMP")
context = ssl.create_default_context()

while True:
    print("co chcesz zrobić:")
    print("1. wyświetl rekordy w bazie")
    print("2. dodaj nowy rekord")
    print("3. usuń rekord")
    print("4. wyślij maile z przypomnieniem")
    print("5. wyjście")
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
        today = db.expired()
        for i in today:
            name = i[1]
            email_to = i[2]
            book_title = i[3]
            message = f"""Subject: Przypomnienie o zwrocie {book_title}\n\n
            hej {name} powinieneś oddać {book_title}"""
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, email_to, message.encode("UTF8"))
                print(f"mail z przypomnieniem wysłany do {name}")
    elif decision == 5:
        break
