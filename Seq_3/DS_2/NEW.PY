def somme_ligne(carre, k):
    """
    Fonction renvoyant la somme des nombres de la ligne d'indice 
    k d'un carré pris en paramètre
    """
    somme = 0
    for nombre in carre[k]:
        somme += int(nombre)
    return somme

def somme_lignes_egales(carre):
    """
    Fonction renvoyant True si les sommes de toutes les lignes
    sont égales et False le cas échéant
    """
    #Affecte à la variable valeur_lignes la valeur de la somme de 
    #la première ligne du carré, comme valeur de référence
    valeur_lignes = somme_ligne(carre, 0)
    
    #compare la valeur des sommes du reste des lignes du carré à 
    #la valeur de référence valeur_lignes
    for ligne in range(1,len(carre)):
        if somme_ligne(carre, ligne) != valeur_lignes:
            return False
    return True

def somme_colonne(carre, k):
    """
    Fonction qui renvoie la somme des nombres d'une colonne k
    d'un carré pris en paramètre
    """
    somme = 0
    for ligne in carre:
        somme += int(ligne[k])
    return somme