alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffres="0123456789"

def cesar_c(message_clair, decalage=3):

    """
    Retourne un message reçu en paramètre codé selon la méthode du code de César.
    """

    message_code = ""

    for caractere in message_clair.upper():
        if caractere in alphabet: # vérifie si le caractère est une lettre pour la coder, ou le laisser inchangé si ce ne l'est pas
            i = alphabet.index(caractere) 
            i_codage = (i+decalage)%26 # codage de la lettre avec le décalage indiqué
            
            message_code += alphabet[i_codage]

        elif caractere in chiffres:
            i = chiffres.index(caractere)
            i_codage = (i+decalage)%10 # codage d'un chiffre avec le décalage indiqué
            
            message_code += chiffres[i_codage]
        else:
            message_code += caractere

    # retourne un dicionaire contenant les caractéristiques du codage et son résultat pour les montrer sur l'interface
    return {
        "methode": "César",
        "alphabet_base": alphabet,
        "chiffres_base": chiffres,
        "cle": decalage,
        "message_clair": message_clair,
        "message_code": message_code
    }

def cesar_d(message_code, decalage=3):
    """
    Retourne décodé un message préalablement codé selon la méthode de César.
    Le message, ainsi que l'alphabet et les chiffres de base utilisés lors du codage, sont reçus en paramètre.
    """

    message_decode = ""

    for caractere in message_code.upper():
        if caractere in alphabet: # vérifie si le caractère est une lettre pour la décoder
            i = alphabet.index(caractere)
            i_decodage = i - decalage

            # vérification: le codage se réalise pour des indices de 0 à 25 (26 lettres dans l'alphabet)
            if i_decodage < 0:
                i_decodage += 26

            message_decode += alphabet[i_decodage]

        elif caractere in chiffres: #vérifie si le caractère est un chiffre pour le décoder
            i = chiffres.index(caractere)
            i_decodage = i-decalage

            # vérification: le codage se réalise pour des indices de 0 à 9 (10 chiffres de base)
            if i_decodage < 0:
                i_decodage += 10
                
            message_decode += chiffres[i_decodage]
        else:
            message_decode += caractere

    #retourne un dicionaire contenant les caractéristiques du décodage et son résultat pour les montrer sur l'interface
    return {
        "methode": "César",
        "alphabet_base": alphabet,
        "chiffres_base": chiffres,
        "cle": decalage,
        "message_code": message_code,
        "message_decode": message_decode
    }