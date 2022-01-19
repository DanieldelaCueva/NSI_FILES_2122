from rot13 import codage, decodage

string = "Bienvenu au codeur-decodeur"

print(decodage(codage(string)["message_code"].lower(), codage(string)["alphabet_base"])["message_decode"])

