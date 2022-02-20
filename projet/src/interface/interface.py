# importation du module externe Tkinter qui nous aide à contruire une interface graphique
from tkinter import (ANCHOR, CENTER, DISABLED, TOP, Button, Label, OptionMenu,
                     Radiobutton, StringVar, Text, Tk)

# importation des fonctions de codage depuis les modules des algorithmes
from ..algorithmes.rot13 import *
from ..algorithmes.cesar import *
from ..algorithmes.vigenere import *
from ..algorithmes.polybe import *


class Interface:
    """
        Classe qui définit les paramètres et la fonctionnalité de l'interface
    """

    # fonction qui affichera dans le champ de sortie le texte traité quand le bouton est actionné 
    def codage(self):
        message = self.champ_entree.get("1.0", "end-1c")
        if self.selection_mode.get() == "1":
            if self.selection_methode == "ROT13":
                return 1
        else: 
            return 2
    
    # contructeur de la classe, exécuté lorsque une instance est crée. Initialise les composants de l'interface
    def __init__(self, fenetre):
        # initialisation de la fenêtre
        self.fenetre = fenetre
        self.fenetre.title("Cryptage")

        # crée le message conteant les instructions
        self.mesage_instructions = Label(fenetre, width=50, height=2, font=("Helvetica", 12), background="#f0f0ed", text="Choisissez la méthode, le mode et le jeu de caractères")

        # place le text à un endroit précis de la fenêtre avec la méthode grid()
        self.mesage_instructions.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # variable qui va contenir le mode de codage selectionnée, 1 (Encoder) est la valeur par défaut
        self.selection_mode = StringVar(fenetre_principale, "1")

        # dicionaire comprenant le texte et le numéro des boutons à générer
        boutons = {
            "Encoder": "1",
            "Décoder": "2"
        }

        # boucle créant les boutons indiqués dans le dictionnaire
        ligne = 1
        for (texte, valeur) in boutons.items():
            Radiobutton(fenetre_principale, text = texte, variable = self.selection_mode, value = valeur).grid(row = ligne, column=0, columnspan=4, padx=10, pady=10)
            ligne += 1

        # variable qui va contenir la méthode de codage selectionnée, ROT13 est la valeur par défaut
        self.selection_methode = StringVar(fenetre_principale, "ROT13")

        methodes = ("ROT13", "CODE DE CÉSAR", "CODE DE VIGNÈRE", "CARRÉ DE POLYBE")
        self.liste_de_methodes = OptionMenu(fenetre_principale, self.selection_methode, *methodes)
        
        # affiche l'outil de sélection de la méthode de codage
        self.liste_de_methodes.grid(row = 3, column=0, columnspan=4, padx=10, pady=10)

        # étiquette et champ de texte pour entrer le message à encoder/décoder
        self.label_entree = Label(fenetre_principale,width=50, height=2, font=("Helvetica", 12), background="#f0f0ed", text="Entrez le message:                                                                         ")
        self.label_entree.grid(row = 4, column=0, columnspan=4, pady=5, sticky="W")

        self.champ_entree = Text(fenetre_principale, font=('Helvetica', 12), height=3, padx=10, pady=10)
        self.champ_entree.grid(row = 5, column=0, columnspan=4, padx=10, pady=2)

        # étiquette et champ de texte où le message encodé/décodé sera affiché
        self.label_sortie = Label(fenetre_principale,width=50, height=2, font=("Helvetica", 12), background="#f0f0ed", text="Le résultat est:                                                                                ")
        self.label_sortie.grid(row = 8, column=0, columnspan=4, pady=5, sticky="W")

        self.champ_sortie = Text(fenetre_principale, font=('Helvetica', 12), height=3, padx=10, pady=10, state=DISABLED)
        self.champ_sortie.grid(row = 11, column=0, columnspan=4, padx=10, pady=2)

        # bouton qui, actionné, appelera la fonction de codage
        self.bouton = Button(fenetre_principale, justify=CENTER, text = "Coder", command=self.codage).grid(row = 12, column=0, columnspan=4, pady=10)




# création d'un objet tk et de l'interface (objet), il sera impossible de changer les dimensions de l'interface
fenetre_principale = Tk()
fenetre_principale.resizable(False, False)
logiciel = Interface(fenetre_principale)

# le script entre dans une boucle infine en attendant que des évènement se produisent
fenetre_principale.mainloop()
