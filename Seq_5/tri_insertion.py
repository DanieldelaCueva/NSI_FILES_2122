def tri_insertion(liste):
    if liste == []:
        return "la liste est vide"
    for i in range(1, len(liste)):
        M = liste[i]
        j = i-1
        while(j >= 0 and M < liste[j]):
            liste[j+1] = liste[j]
            j = j-1
        liste[j+1] = M
    return liste
