alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffres="0123456789"

def cesar_c(message, decalage=3):

    """
    Retourne un message reçu en paramètre codé selon la méthode du code de César.
    """

    message_code = "" #initialisation de la variable qui contiendra le message codé

    for caractere in message.upper(): #transforme les lettres minisucules du message en lettres majuscules et parcourt le message à coder caractère par caractère pour les coder
        if caractere in alphabet: #vérifie si le caractère est une lettre pour la coder, ou le laisser inchangé si ce ne l'est pas
            #affectation à i de l'indice de la lettre originale dans l'alphabet utilisé, puis à i_codage de l'indice dans l'alphabet de la lettre codée 
            i = alphabet.index(caractere) 
            i_codage = (i+decalage)%26
            #ajoute la lettre codée au message final
            message_code += alphabet[i_codage]
        elif caractere in chiffres:
            #affectation à i de l'indice du chiffre original dans les chiffres utilisés, puis à i_codage de l'indice dans les chiffres du chiffre codé
            i = chiffres.index(caractere)
            i_codage = (i+decalage)%10
            #ajoute le chiffre codé au message final
            message_code += chiffres[i_codage]
        else:
            message_code += caractere

    #retourne un dicionaire contenant les caractéristiques du codage et son résultat pour les montrer sur l'interface
    return {
        "methode": "César",
        "alphabet_base": alphabet,
        "chiffres_base": chiffres,
        "clef": decalage,
        "message_introduit": message,
        "message_code": message_code
    }

def cesar_d(message, decalage=3):
    """
    Retourne décodé un message préalablement codé selon la méthode de César.
    Le message, ainsi que l'alphabet et les chiffres de base utilisés lors du codage, sont reçus en paramètre.
    """

    message_decode = "" #initialisation de la variable qui contiendra le message décodé

    for caractere in message.upper(): #transforme les lettres minisucules du message en lettres majuscules et parcourt le message à décoder caractère par caractère pour les décoder
        if caractere in alphabet: #vérifie si le caractère est une lettre pour la décoder
            #affectation à de i l'indice de la lettre originale dans l'alphabet utilisé, puis à i_decodage de l'indice dans l'alphabet de la lettre décodée 
            i = alphabet.index(caractere)
            i_decodage = i-decalage
            #vérification: le codage se réalise pour des indices de 0 à 25 (26 lettres dans l'alphabet)
            if i_decodage < 0:
                i_decodage += 26
            #ajoute la lettre décodée au message final
            message_decode += alphabet[i_decodage]
        elif caractere in chiffres: #vérifie si le caractère est un chiffre pour le décoder
            #affectation à de i l'indice du chiffre original dans les chiffres utilisés, puis à i_decodage de l'indice dans les chiffres du chiffre décodé
            i = chiffres.index(caractere)
            i_decodage = i-decalage
            #vérification: le codage se réalise pour des indices de 0 à 9 (10 chiffres de base)
            if i_decodage < 0:
                i_decodage += 10
            #ajoute le chiffre décodé au message final
            message_decode += chiffres[i_decodage]
        else:
            message_decode += caractere

    #retourne un dicionaire contenant les caractéristiques du décodage et son résultat pour les montrer sur l'interface
    return {
        "methode": "César",
        "alphabet_base": alphabet,
        "chiffres_base": chiffres,
        "clef": decalage,
        "message_introduit": message,
        "message_decode": message_decode
    }