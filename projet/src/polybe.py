chiffres="0123456789"

def polybe_c(message_clair, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXY"):
    # vérifie que l'alphabet introduit a bien une longeur de 25, arrete l'exécution sdu programme et affiche une erreur sinon
    if len(alphabet) != 25:
        raise ValueError("L'alphabet doit comporter 25 lettres")

    # construit la grille de codage (matrice) a partir de l'alphabet de 25 lettres donné
    grille = list()
    for i in range(1, 6):
        ligne = alphabet[5*(i-1) : (5*i)]
        grille.append(list(ligne))

    message_code = ""

    for caractere in message_clair.upper():
        if caractere in alphabet:
            codage = ""
            # cherche dans quelle ligne de la matrice de codage se trouve le caractère à coder, joint sa ligne et colonne au message
            for ligne in grille:
                if caractere in ligne:
                    codage += str(grille.index(ligne) + 1)
                    codage += str(ligne.index(caractere) + 1)
                    message_code += codage
        elif caractere in chiffres:
            # affiche une erreur si le caractère à coder est un chiffre
            raise ValueError("Les chiffres ne peuvent pas être codés avec Polybe")
        else:
            message_code += caractere

    # retourne un dicionaire contenant les caractéristiques du codage et son résultat pour les montrer sur l'interface
    return {
        "methode": "Polybe",
        "alphabet_base": alphabet,
        "chiffres_base": chiffres,
        "cle": None,
        "message_clair": message_clair,
        "message_code": message_code
    }