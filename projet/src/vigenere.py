def vigenere_c(message_clair, cle_orig, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """
        Code un message selon le chiffrement de Vigenère
    """

    message_code = ""

    cle = cle_orig.replace(" ", "") # supprime les espaces dans la clé

    # s'assure que la clé est assez longue pour coder le message en la répétant autat de fois que nécéssaire
    while len(cle) < len(message_clair):
        cle += cle

    k = 0

    for caractere in message_clair.upper():
        if caractere in alphabet:
            # somme des indices dans l'alphabet introduit du caractère et du caractère de la clé correspondant
            i = ( alphabet.index(caractere) + alphabet.index(cle.upper()[k]) ) % 26
            k += 1

            message_code += alphabet[i]
        # code uniquement les caractères présents dans l'alphabet indiqué en paramètre
        else:
            message_code += caractere
    
    # retourne un dicionaire contenant les caractéristiques du codage et son résultat pour les montrer sur l'interface
    return {
        "methode": "Vigenère",
        "alphabet_base": alphabet,
        "chiffres_base": None,
        "cle": cle_orig,
        "message_clair": message_clair,
        "message_code": message_code
    }

def vigenere_d(message_code, cle_orig, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """
        Décode un message selon le chiffrement de Vigenère
    """

    message_decode = ""

    cle = cle_orig.replace(" ", "") # supprime les espaces dans la clé

    # s'assure que la clé est assez longue pour décoder le message en la répétant autat de fois que nécéssaire
    while len(cle) < len(message_code):
        cle += cle

    k = 0

    for caractere in message_code.upper():
        if caractere in alphabet:
            # différence des indices dans l'alphabet introduit du caractère et du caractère de la clé correspondant
            i = ( alphabet.index(caractere) - alphabet.index(cle.upper()[k]) )
            print(i)
            if i < 0:
                i += 26
            k += 1

            message_decode += alphabet[i]
        # décode uniquement les caractères présents dans l'alphabet indiqué en paramètre
        else:
            message_decode += caractere
    
    # retourne un dicionaire contenant les caractéristiques du décodage et son résultat pour les montrer sur l'interface
    return {
        "methode": "Vigenère",
        "alphabet_base": alphabet,
        "chiffres_base": None,
        "cle": cle_orig,
        "message_code": message_code,
        "message_decode": message_decode
    }

test = "Message de test"
cle_t = "test"

print(vigenere_d(vigenere_c(test, cle_t)["message_code"], cle_t))