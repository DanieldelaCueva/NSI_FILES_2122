# importation du module externe Tkinter qui nous aide à contruire une interface graphique
import datetime, os
from tkinter import Tk

# importation de la classe Interface définié dans le module interface du paquet interface
from interface.interface import Interface

from algorithmes.rot13 import *
from algorithmes.cesar import *
from algorithmes.vigenere import *
from algorithmes.polybe import *
 
def codage():

    """
        Fonction qui affichera dans le champ de sortie le texte traité quand le bouton est actionné
    """

    interface.effacer_sortie()

    message = interface.get_entree()
    cle = interface.get_cle()

    try:
        if interface.get_mode() == "1":
            if interface.get_methode() == "ROT13":
                message_code = rot13_c(message)['message_code']
                interface.afficher_sortie(message_code)

            elif interface.get_methode() == "CODE DE CÉSAR":
                message_code = cesar_c(message, int(cle))['message_code']
                interface.afficher_sortie(message_code)

            elif interface.get_methode() == "CODE DE VIGENÈRE":
                message_code = vigenere_c(message, cle)['message_code']
                interface.afficher_sortie(message_code)

            elif interface.get_methode() == "CARRÉ DE POLYBE":
                message_code = polybe_c(message)['message_code']
                interface.afficher_sortie(message_code)

            else:
                interface.afficher_sortie("")
        else: 
            if interface.get_methode() == "ROT13":
                message_decode = rot13_d(message)['message_decode']
                interface.afficher_sortie(message_decode)

            elif interface.get_methode() == "CODE DE CÉSAR":
                message_decode = cesar_d(message, int(cle))['message_decode']
                interface.afficher_sortie(message_decode)

            elif interface.get_methode() == "CODE DE VIGENÈRE":
                message_decode = vigenere_d(message, cle)['message_decode']
                interface.afficher_sortie(message_decode)

            elif interface.get_methode() == "CARRÉ DE POLYBE":
                message_decode = polybe_d(message)['message_decode']
                interface.afficher_sortie(message_decode)
    # affiche une erreur si elle se produit
    except ValueError as error:
        interface.afficher_alerte(error)

def sauvegarder():

    """
        Fonction qui crée un fichier texte avec les données de l'opération
    """

    date = datetime.datetime.now().strftime('%Y-%m-%d-%Hh%Mmin%Ss')
    adresse_fichier = os.getcwd() +  "\projet\output\\" + date + ".txt"
    
    with open(adresse_fichier, 'x', encoding='utf8') as f:
        f.write('Date: ' + date)
        f.write("\n")
        if interface.get_mode() == "1":
            f.write('Opération: Encodage')
            f.write("\n")
        else:
            f.write('Opération: Décodage')
            f.write("\n")

        f.write("Méthode: " + interface.get_methode())
        f.write("\n")
        if interface.get_methode() == "CODE DE VIGENÈRE" or interface.get_methode() == "CODE DE CÉSAR":
            f.write('Clé: ' + interface.get_cle())
            f.write("\n")
        f.write('Message introduit: ' + interface.get_entree())
        f.write("\n")
        f.write('Message résultant: ' + interface.get_sortie())


# création d'un objet tk et de l'interface (objet), il sera impossible de changer les dimensions de l'interface
fenetre_principale = Tk()
fenetre_principale.resizable(False, False)
interface = Interface(fenetre_principale, codage, sauvegarder)

# le script entre dans une boucle infine en attendant que des évènement se produisent
fenetre_principale.mainloop()