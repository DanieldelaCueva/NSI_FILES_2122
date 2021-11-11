#minimum et maximum d'une tuple
def min_max(Mytuple):
  min=Mytuple[0]
  max=Mytuple[0]
  for element in Mytuple:
    if min > element:
      min = element
    elif max < element:
      max = element
  return(min,max)


#nombre de 0 et 1 dans un tuple
def nb_0_et_1(t):
    nb0 = 0
    nb1 = 1

    for e in t:
        if int(e) == 0:
            nb0 += 1
        elif int(e) == 1:
            nb1 +=1
    return (nb0, nb1)

#somme des éléments d'une tuple
def SommeTuple(Mytuple):
  somme= 0
  n=len(Mytuple)
  i=0
  while (i<n):
    somme = somme + Mytuple[i]
    i += 1
  return(somme)


#calcul des coordonnes du milieu d'un segment
from collections import namedtuple

AA=(1,2)
BB=(3,6)

def CoordonneeMilieu(AA,BB):
  II=((AA[0]+BB[0])/2,(AA[1]+BB[1])/2)
  coord = namedtuple("Milieu",["x","y"])
  M = coord(II[0],II[1])
  return(M)

#somme des carres inférieurs à n
def somme_carres_inferieurs_a(n):
    L=[0]*n
    i = 0

    while i<n:
        L[i] = i**2
        i = i +1

    n = len(L)
    S = 0

    for i in range(n):
        S = S + L[i]

    print('La somme des carrés des entiers strictement inférieurs à',n,'est',S)

