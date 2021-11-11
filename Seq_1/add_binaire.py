## PAGE 8/20 SÉANCE 10
def conv(n): ### Cette fonction converti un entier en liste de manière à pouvoir utliser chaque bit de manière indépendante.
  n=str(n)
  liste=[]
  for i in n:
    liste.append(int(i))
  return(liste)

# -------------------------------------------------------------
def add(a,b):
  ac=conv(a) # conversion de la valeur a en liste
  bc=conv(b) # conversion de la valeur b en liste
  ac.reverse() # Inversion des valeurs dans la liste
  bc.reverse() # Inversion des valeurs dans la liste
  lena=len(ac) # Calcul de la longueur de la liste a
  lenb=len(bc) # Calcul de la longueur de la liste b
  lenmax=max(lena,lenb) # Calcul de la longueur de la plus grande liste
  if ac < bc: # si la liste bc est plus longue
    for i in range(lena,lenb):
      ac.append(0) # Remplissage avec des 0 les bits manquants
                # ac.append(0) ajoute un 0 à la suite de la liste
  else:           # si la liste ac est plus longue
    for i in range(lenb,lena):
      bc.append(0) # Remplissage avec des 0 les bits manquants

  somme=[]           # Création d'une liste vide qui recevra la somme des deux valeurs
  retenue = 0     # Initialisation de la retenue
  for i in range(0,lenmax):
    if i < lena and i< lenb:
        somme.append((ac[i]+bc[i]+retenue)%2)  # Ajout du reste de la division euclidienne de la somme des bits + de la retenue par 2 --> bit de poids faible de la somme
        retenue = (ac[i]+bc[i]+retenue)//2 # Mise à jour de la retenue. Si la somme est supérieure à 1 on impose une retenue.
    elif i >= lena: # Les lignes 32 à 43 résolvent le problème d'addition lorsque les binaires sont de longeurs différentes, et donc la plus longue des deux listes à un "index out of range" quand i >= len() de l'autre
        if retenue == 1:
            somme.append((bc[i]+retenue)%2)
            retenue = (bc[i]+retenue)//2
        else:
            somme.append(bc[i])
    elif i >= lenb:
        if retenue == 1:
            somme.append((ac[i]+retenue)%2)
            retenue = (ac[i]+retenue)//2
        else: 
            somme.append(ac[i])


  if retenue == 1: # Retenue du dernier bit de poids fort
    somme.append(1)

  somme.reverse() # Inversion de la liste
  return(somme)

print(add(11111,11111))