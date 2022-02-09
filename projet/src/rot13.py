from cesar import cesar_c, cesar_d

def rot13_c(message_clair):
    """
    Retourne un message reçu en paramètre codé selon la méthode ROT-13.
    """

    #rot13 est le code de césar avec un décalage de 13
    resultats = cesar_c(message_clair, 13)

    #retourne un dicionaire contenant les caractéristiques du codage et son résultat pour les montrer sur l'interface
    return {
        "methode": "ROT13",
        "alphabet_base": resultats["alphabet_base"],
        "chiffres_base": resultats["chiffres_base"],
        "cle": None,
        "message_clair": message_clair,
        "message_code": resultats["message_code"]
    }

def rot13_d(message_code):
    """
    Retourne décodé un message préalablement codé selon la méthode ROT-13.
    Le message, ainsi que l'alphabet de base utilisé lors du codage, sont reçus en paramètre.
    """

    #rot13 est le code de césar avec un décalage de 13
    resultats = cesar_d(message_code, 13)

    #retourne un dicionaire contenant les caractéristiques du décodage et son résultat pour les montrer sur l'interface
    return {
        "methode": "ROT13",
        "alphabet_base": resultats["alphabet_base"],
        "chiffres_base": resultats["chiffres_base"],
        "cle": None,
        "message_code": message_code,
        "message_decode": resultats["message_decode"]
    }