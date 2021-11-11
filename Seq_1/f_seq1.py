def est_premier(N):
    i = 2

    while i <= N-1 and N % i != 0:
        i += 1

    if (i == N):
        return True
    else:
        return False


# introduire
#  nombres entiers en arguments, retourne un tableaux avec ceux qui sont premiers
def sont_premiers(*args):
    arguments = list(args)
    premiers = []

    for N in arguments:
        i = 2
        while i <= N-1 and N % i != 0:
            i += 1

        if (i == N):
            premiers.append(N)

    return premiers


def premier_diviseur(N):
    i = 2

    est_premier = False
    # Tant que (i est inférieur à N) ET que (N n'est pas divisible par i), alors )
    while ((i < N) and (N % i != 0)):
        i = i+1
        if (i == N):
            est_premier = True
        else:
            est_premier = False
    # On est sorti de la boucle : soit (i>=N), soit (i est un diviseur de N)

    # On affiche le résultat
    if est_premier == True:
        return 0
    else:
        return i


def nombre_parfait(nombre):
    somme = 0
    for i in range(1, nombre):
        if((nombre % i) == 0):
            somme = somme+i

    if(nombre == somme):
        return True
    else:
        return False


def nombre_de_parfaits(a, b):
    nombres_parfaits = []

    for i in range(a, b):
        somme = 0
        for j in range(1, i):
            if i % j == 0:
                somme = somme+j

        if somme == i:
            nombres_parfaits.append(i)

    return(nombres_parfaits, len(nombres_parfaits))


def premiers_jusqu_a(NB):
    premiers = 0
    est_premier = False

    for N in range(1, NB):
        i = 2
        # Tant que (i est inférieur à N) ET que (N n'est pas divisible par i), alors )
        while ((i < N) and (N % i != 0)):
            i = i + 1            # Ne pas oublier d'incrémenter la variable de boucle i
        if (i == N):
            est_premier = True
        else:
            est_premier = False
        # On est sorti de la boucle : soit (i>=N), soit (i est un diviseur de N)

        # On affiche le résultat
        if est_premier:
            premiers += 1

    return(premiers)


def obtenir_binaire(n):
    quotient = 1
    dividende = n
    reste = 0
    nombre = []
    while quotient != 0:
        quotient = dividende//2
        reste = dividende % 2
        nombre.append(reste)
        dividende = quotient
    nombre.reverse()
    return nombre


def obtenir_decimal(n):
    n = list(n.replace(" ", ""))
    decimal = 0
    puissance = 0
    for i in range(-1, -1*len(n)-1, -1):
        decimal += int(n[i])*(2**puissance)
        puissance += 1
    return decimal

# Si l'utilisateur ne rentre qu'une seule variable, la base sera 2 par defaut.


def decimal_en_base(valeur, base=2):
    nombre = 0
    # Conversion de la valeur du type 'int' au type 'string'
    valeur = str(valeur)
    longueur = len(valeur)   # Récupération de la longueur du mot.
    for i in range(0, longueur):
        # Calcul de la valeur décimale.
        nombre = nombre+int(valeur[longueur-1-i])*(base**i)
    return(nombre)


# SOMME DE DEUX ENTIERS BINAIRES

def conv(n):  # Cette fonction converti un entier en liste de manière à pouvoir utliser chaque bit de manière indépendante.
    n = str(n)
    liste = []
    for i in n:
        liste.append(int(i))
    return(liste)

# -------------------------------------------------------------


def add(a, b):
    ac = conv(a)  # conversion de la valeur a en liste
    bc = conv(b)  # conversion de la valeur b en liste
    ac.reverse()  # Inversion des valeurs dans la liste
    bc.reverse()  # Inversion des valeurs dans la liste
    lena = len(ac)  # Calcul de la longueur de la liste a
    lenb = len(bc)  # Calcul de la longueur de la liste b
    lenmax = max(lena, lenb)  # Calcul de la longueur de la plus grande liste
    if ac < bc:  # si la liste bc est plus longue
        for i in range(lena, lenb):
            ac.append(0)  # Remplissage avec des 0 les bits manquants
            # ac.append(0) ajoute un 0 à la suite de la liste
    else:           # si la liste ac est plus longue
        for i in range(lenb, lena):
            bc.append(0)  # Remplissage avec des 0 les bits manquants

    somme = []           # Création d'une liste vide qui recevra la somme des deux valeurs
    retenue = 0     # Initialisation de la retenue
    for i in range(0, lenmax):
        if i < lena and i < lenb:
            # Ajout du reste de la division euclidienne de la somme des bits + de la retenue par 2 --> bit de poids faible de la somme
            somme.append((ac[i]+bc[i]+retenue) % 2)
            # Mise à jour de la retenue. Si la somme est supérieure à 1 on impose une retenue.
            retenue = (ac[i]+bc[i]+retenue)//2
        elif i >= lena:
            if retenue == 1:
                somme.append((bc[i]+retenue) % 2)
                retenue = (bc[i]+retenue)//2
            else:
                somme.append(bc[i])
        elif i >= lenb:
            if retenue == 1:
                somme.append((ac[i]+retenue) % 2)
                retenue = (ac[i]+retenue)//2
            else:
                somme.append(ac[i])

    if retenue == 1:  # Retenue du dernier bit de poids fort
        somme.append(1)

    somme.reverse()  # Inversion de la liste
    return(somme)

# NOMBRE DE BITS POUR LA SOMME DE DEUX ENTIERS


def nb(dec):
    n = 0
    while dec > 2**(n)-1:
        n = n + 1
    return(n)


def addBin(a, b):
    somme = a+b
    Na = nb(a)
    Nb = nb(b)
    N = max(Na, Nb)   # Calcule le max de Na et Nb
    if somme > (2**N)-1:
        N += 1
    print("nombre de bits nécessaires à l'écriture de la somme de ",
          a, " et ", b, " : ", N)

# MAXIMUM DE A ET B
def maximum(a, b):
    if a > b:
        return(a)
    else:
        return(b)

# MAXIMUM D'UN TABLEAU


def max_liste(tab):
    m = tab[0]
    for i in range(0, len(tab)):
        if tab[i] > m:
            m = tab[i]
    return m

# MOT PALYNDROME


def palyndrome(mot):
    pal = True
    for i in range(0, len(mot)):
        if mot[i] != mot[len(mot)-1-i]:
            pal = False
    return pal
