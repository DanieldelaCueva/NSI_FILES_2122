def trouve_min(liste, ind_depart):
    """Renvoie l'indice du minimum des elements d'une liste entre ind_depart et la fin de la liste"""
    # on s'assure que la liste n'est pas vide
    if liste == []:
        return "la liste est vide"
    # recheche de l'indice du minimum
    ind_min = ind_depart
    elt_min = liste[ind_min:]
    for element in elt_min:
        if element < liste[ind_min]:
            ind_min = liste.index(element)
    return ind_min


def tri_selection(liste):
    if liste == []:
        return "la liste est vide"
    for i in range(len(liste)-1):
        indicemini = trouve_min(liste, i)
    # echange le terme de rang i et le terme de rang indicemini
        liste[i], liste[indicemini] = liste[indicemini], liste[i]
    # A COMPLETER
    return liste
