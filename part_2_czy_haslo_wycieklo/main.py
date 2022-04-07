from requests import get
import string
from hashlib import sha1
import logging

logging.basicConfig(filename='log.txt', filemode='w', level=logging.DEBUG)

class Password:
    def __init__(self, password):
        self.password = password
        self.password_hash = sha1(self.password.encode("UTF8")).hexdigest()
        self.prefix = self.password_hash[:5]
        self.suffix = self.password_hash[5:]

    def check_password_difficulty(self):
        self.lower = 0
        self.upper = 0
        self.punct = 0
        self.digit = 0
        for i in self.password:
            if i in string.ascii_lowercase:
                self.lower += 1
            if i in string.ascii_uppercase:
                self.upper += 1
            if i in string.punctuation:
                self.punct += 1
            if i in string.digits:
                self.digit += 1
        if (self.lower * self.upper * self.punct * self.digit != 0) and len(self.password) >= 8:
            logging.info(f'hasło "{self.password}" spełnia wymagania')
            return True
        logging.info(f'hasło "{self.password}" niespełnia wymagań')
        if len(self.password) < 8:
            logging.info("hasło za krótkie")
        if self.lower == 0:
            logging.info("brakuje małych liter")
        if self.upper == 0:
            logging.info("brakuje dużych liter")
        if self.digit == 0:
            logging.info("brakuje cyfr")
        if self.punct == 0:
            logging.info("brakuje znaków specjalnych")
        return False

    def check_in_api(self):
        response = get(f"https://api.pwnedpasswords.com/range/{self.prefix}")
        counter = response.text.splitlines()
        for i in counter:
            if self.suffix in i.lower().split(":"):
                logging.info(f'hasło "{self.password}" wyciekło {i[36]} razy')
                return False
        logging.info(f'hasło "{self.password}" nie wyciekło')
        return True

passwords = []
with open("hasla.txt", encoding="UTF8") as file, open("bezpieczne.txt", mode="w", encoding="UTF8") as out:
    for i in file:
        i = Password(i.strip())
        logging.info(f'sprawdzam hasło "{i.password}"')
        passwords.append(i)
        api = i.check_in_api()
        dif = i.check_password_difficulty()
        if api and dif:
            out.write(str(i.password) + "\n")
