def codage(message):
    """
    Retourne un message reçu en paramètre codé selon la méthode ROT-13.
    Pour cette méthode, l'alphabet utilisable est uniquement l'alphabet en majuscules et dans accentuation, pour conserver la propriété de réversibilité.
    """

    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message_code = "" #initialisation de la variable qui contiendra le message codé

    for lettre in message.upper(): #transforme les lettres minisucules du message en lettres majuscules et parcourt le message à coder caractère par caractère pour les coder
        if lettre in alphabet: #vérifie si le caractère est une lettre pour la coder, ou le laisser inchangé si ce ne l'est pas
            #affectation à de i l'indice de la lettre originale dans l'alphabet utilisé, puis à i_codage de l'indice dans l'alphabet de la lettre codée 
            i = alphabet.index(lettre) 
            i_codage = i+13
            #vérification: le codage se réalise pour des indices de 0 à 25 (26 lettres dans l'alphabet)
            if i_codage > 25:
                i_codage -= 26
            #ajoute la lettre traitée au message final
            message_code += alphabet[i_codage]
        else:
            message_code += lettre

    #retourne un dicionaire contenant les caractéristiques du codage et son résultat pour les montrer sur l'interface
    return {
        "methode": "ROT13",
        "alphabet_base": alphabet,
        "clef": None,
        "message_introduit": message,
        "message_code": message_code
    }

def decodage(message, alphabet):
    """
    Retourne décodé un message préalablement codé selon la méthode ROT-13.
    Le message, ainsi que l'alphabet de base utilisé lors du codage, sont reçus en paramètre.
    """

    message_decode = "" #initialisation de la variable qui contiendra le message décodé

    for lettre in message.upper(): #transforme les lettres minisucules du message en lettres majuscules et parcourt le message à décoder caractère par caractère pour les décoder
        if lettre in alphabet: #vérifie si le caractère est une lettre pour la décoder, ou le laisser inchangé si ce ne l'est pas
            #affectation à de i l'indice de la lettre originale dans l'alphabet utilisé, puis à i_decodage de l'indice dans l'alphabet de la lettre décodée 
            i = alphabet.index(lettre)
            i_decodage = i-13
            #vérification: le codage se réalise pour des indices de 0 à 25 (26 lettres dans l'alphabet)
            if i_decodage < 0:
                i_decodage += 26
            #ajoute la lettre traitée au message final
            message_decode += alphabet[i_decodage]
        else:
            message_decode += lettre

    #retourne un dicionaire contenant les caractéristiques du décodage et son résultat pour les montrer sur l'interface
    return {
        "methode": "ROT13",
        "alphabet_base": alphabet,
        "clef": None,
        "message_introduit": message,
        "message_decode": message_decode
    }