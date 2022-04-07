"""program sprawdzający czy hasła z pliku hasla.txt są hasłami bezpiecznymi
 i czy kiedykolwiek wyciekły do sieci

"""
import logging
from hashlib import sha1
import string
from requests import get

logging.basicConfig(filename='log.txt', filemode='w', level=logging.DEBUG)

class Password:
    """klasa przetrzymująca dane hasła"""
    def __init__(self, password):
        self.password = password
        self.password_hash = sha1(self.password.encode("UTF8")).hexdigest()
        self.prefix = self.password_hash[:5]
        self.suffix = self.password_hash[5:]

    def check_password_difficulty(self):
        """funkcja sprawdzająca złożoność hasła"""
        lower = 0
        upper = 0
        punct = 0
        digit = 0
        for item in self.password:
            if item in string.ascii_lowercase:
                lower += 1
            if item in string.ascii_uppercase:
                upper += 1
            if item in string.punctuation:
                punct += 1
            if item in string.digits:
                digit += 1
        if (lower * upper * punct * digit != 0) and len(self.password) >= 8:
            logging.info(f'hasło "{self.password}" spełnia wymagania')
            return True
        logging.info(f'hasło "{self.password}" niespełnia wymagań')
        if len(self.password) < 8:
            logging.info("hasło za krótkie")
        if lower == 0:
            logging.info("brakuje małych liter")
        if upper == 0:
            logging.info("brakuje dużych liter")
        if digit == 0:
            logging.info("brakuje cyfr")
        if punct == 0:
            logging.info("brakuje znaków specjalnych")
        return False

    def check_in_api(self):
        """funkcja sprawdzająca czy dane hasło wyciekło sieci"""
        response = get(f"https://api.pwnedpasswords.com/range/{self.prefix}")
        counter = response.text.splitlines()
        for item in counter:
            if self.suffix in item.lower().split(":"):
                logging.info(f'hasło "{self.password}" wyciekło {item[36]} razy')
                return False
        logging.info(f'hasło "{self.password}" nie wyciekło')
        return True

if __name__ == "__main__":
    passwords = []
    with open("hasla.txt", encoding="UTF8") as file:
        for i in file:
            i = Password(i.strip())
            logging.info(f'sprawdzam hasło "{i.password}"')
            passwords.append(i)
            API = i.check_in_api()
            DIF = i.check_password_difficulty()
            if API and DIF:
                with open("bezpieczne.txt", mode="w", encoding="UTF8") as out:
                    out.write(str(i.password) + "\n")
