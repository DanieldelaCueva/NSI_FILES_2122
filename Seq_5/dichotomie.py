def bien_trieeC(liste, indice):
    trieeC = True
    i = 0
    while trieeC and i < indice:
        if liste[i] >= liste[i+1]:
            trieeC = False
        i = i+1
    return trieeC


def dicho(liste, nbatrouver):
    Trouve = 0
    assert bien_trieeC(liste, len(liste)-1)
    # partie principale de programme dichotomie
    indNB = -1
    a = 0
    b = len(liste)-1
    while Trouve == 0 and a <= b:
        centre = (a+b)//2
        if liste[centre] == nbatrouver:
            Trouve = 1
            indNB = centre
        elif liste[centre] > nbatrouver:
            b = centre-1
        else:
            a = centre+1
    if Trouve == 1:
        return indNB
    else:
        return False
