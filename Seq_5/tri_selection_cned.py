def trouve_min(liste, ind_depart):
    """Renvoie le tupple : l'indice du minimum"""
    if liste == []:
        return "la liste est vide"
    ind_min = ind_depart
    elt_min = liste[ind_min]
    for i in range(ind_depart, len(liste)):
        # on rappelle que len(liste) donne la longeur de la  liste
        if liste[i] < elt_min:
            elt_min = liste[i]
            ind_min = i
    return ind_min


def tri_selection(liste):
    if liste == []:
        return "la liste est vide"
    for i in range(len(liste)-1):
        indicemini = trouve_min(liste, i)
        if indicemini != i:
            liste[i], liste[indicemini] = liste[indicemini], liste[i]
    return liste
