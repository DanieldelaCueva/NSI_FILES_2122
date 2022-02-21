from cesar import cesar_c, cesar_d
from rot13 import rot13_c, rot13_d
from vigenere import vigenere_c, vigenere_d
from polybe import polybe_c, polybe_d

import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXY #$%&'()*+,-./"

erreurs=[]
reussis = 0
total = 0

for i in range(100000):
    mot=""
    for i in range(random.randint(1, 20)):
        mot += alphabet[random.randint(0,24)]

    if rot13_d(rot13_c(mot)["message_code"])["message_decode"]:
        reussis += 1
        total += 1
    else:
        erreurs.append(["rot13", mot])
        total += 1

    if cesar_d(cesar_c(mot)["message_code"])["message_decode"]:
        reussis += 1
        total += 1
    else:
        erreurs.append(["cesar", mot])
        total += 1

    if vigenere_d(vigenere_c(mot, "cleparfaite")["message_code"], "cleparfaite")["message_decode"]:
        reussis += 1
        total += 1
    else:
        erreurs.append(["vigenere", mot])
        total += 1

    if polybe_d(polybe_c(mot)["message_code"])["message_decode"]:
        reussis += 1
        total += 1
    else:
        erreurs.append(["polybe", mot])
        total += 1


taux = (reussis / total)*100

print("Taux de réuissite: " + str(taux) + "%")
print(erreurs)