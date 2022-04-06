from requests import get
import string
from hashlib import sha1


hasla = []
with open("hasla.txt") as file:
    for i in file:
        hasla.append(i.strip())

# string.ascii_lowercase
# string.ascii_uppercase
# string.punctuation
# string.digits
for haslo in hasla:
    lower = 0
    upper = 0
    punct = 0
    digit = 0
    print(haslo)
    print(f"dlugosc hasla {len(haslo)}")
    for i in haslo:
        if i in string.ascii_lowercase:
            lower += 1
        if i in string.ascii_uppercase:
            upper += 1
        if i in string.punctuation:
            punct += 1
        if i in string.digits:
            digit += 1
    if lower * upper * punct * digit != 0:
        print("haslo mocne")
    else:
        print("haslo slabe")
    if lower == 0:
        print("brakuje malych liter")
    if upper == 0:
        print("brakuje duzych liter")
    if digit == 0:
        print("brakuje cyfr")
    if punct == 0:
        print("brakuje znakow specjalnych")
    hashowane = sha1(haslo.encode("UTF8"))
    print(hashowane.hexdigest())
    print()






