# importation du module externe Tkinter qui nous aide à contruire une interface graphique
from tkinter import (CENTER, RIGHT, Button, Label, OptionMenu,
                     Radiobutton, StringVar, Text, Entry, messagebox)

# from ..algorithmes.rot13 import *

class Interface:
    """
        Classe qui définit les paramètres et la fonctionnalité de l'interface
    """
    
    def __init__(self, fenetre, codage, sauvegarder):

        """
            Contructeur de la classe, exécuté lorsque une instance est crée. Initialise les composants de l'interface
        """

        # initialisation de la fenêtre
        self._fenetre = fenetre
        self._fenetre.title("Cryptage")

        # crée le message conteant les instructions
        self._mesage_instructions = Label(self._fenetre, width=50, height=2, font=("Helvetica", 12), background="#f0f0ed", text="Choisissez la méthode, le mode et le jeu de caractères")

        # place le text à un endroit précis de la fenêtre avec la méthode grid()
        self._mesage_instructions.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # variable qui va contenir le mode de codage selectionnée, 1 (Encoder) est la valeur par défaut
        self._selection_mode = StringVar(self._fenetre, "1")

        # dicionaire comprenant le texte et le numéro des boutons à générer
        boutons = {
            "Encoder": "1",
            "Décoder": "2"
        }

        # boucle créant les boutons indiqués dans le dictionnaire
        ligne = 1
        for (texte, valeur) in boutons.items():
            Radiobutton(self._fenetre, text = texte, variable = self._selection_mode, value = valeur).grid(row = ligne, column=0, columnspan=4, padx=10, pady=10)
            ligne += 1

        # variable qui va contenir la méthode de codage selectionnée, ROT13 est la valeur par défaut
        self._selection_methode = StringVar(self._fenetre, "ROT13")

        methodes = ("ROT13", "CODE DE CÉSAR", "CODE DE VIGENÈRE", "CARRÉ DE POLYBE")
        self._liste_de_methodes = OptionMenu(self._fenetre, self._selection_methode, *methodes)
        
        # affiche l'outil de sélection de la méthode de codage
        self._liste_de_methodes.grid(row = 3, column=0, columnspan=4, padx=10, pady=10)

        # étiquette et champ de texte pour entrer le message à encoder/décoder
        self._label_entree = Label(self._fenetre,width=50, height=2, font=("Helvetica", 12), background="#f0f0ed", text="Entrez le message:                                                                         ")
        self._label_entree.grid(row = 4, column=0, columnspan=4, pady=5, sticky="W")

        self._champ_entree = Text(self._fenetre, font=('Helvetica', 12), height=3, padx=10, pady=10)
        self._champ_entree.grid(row = 5, column=0, columnspan=4, padx=10, pady=2)

        # variable qui contiendra la valeur de la clé
        self._v_cle = StringVar(self._fenetre, "")

        # étiquette et champ de texte pour entrer la clé de codage
        self._label_cle = Label(self._fenetre, width=50, height=2, font=("Helvetica", 12), background="#f0f0ed", text="Entrez la clé de codage:")
        self._label_cle.grid(row = 8, column=0, columnspan=4, pady=5, sticky="W")

        self._entree_cle = Entry(self._fenetre, textvariable=self._v_cle)
        self._entree_cle.grid(row = 8, column=1, columnspan=4, pady=5)

        # étiquette et champ de texte où le message encodé/décodé sera affiché
        self._label_sortie = Label(self._fenetre,width=50, height=2, font=("Helvetica", 12), background="#f0f0ed", text="Le résultat est:                                                                                ")
        self._label_sortie.grid(row = 9, column=0, columnspan=4, pady=5, sticky="W")

        self._champ_sortie = Text(self._fenetre, font=('Helvetica', 12), height=3, padx=10, pady=10, state="disabled")
        self._champ_sortie.grid(row = 12, column=0, columnspan=4, padx=10, pady=2)

        # bouton qui, actionné, appelera la fonction de codage
        self._bouton_coder = Button(self._fenetre, justify=CENTER, text = "Coder", command=codage)
        self._bouton_coder.grid(row = 13, column=0, columnspan=4, pady=10)

        # bouton qui, actionné, sauvegardera le message introduit et le résultat de son encodage/décodage
        self._bouton_sauvegarder = Button(self._fenetre, justify=RIGHT, text = "Sauvegarder", command=sauvegarder)
        self._bouton_sauvegarder.grid(row = 13, column=3, columnspan=4, pady=10)

    # getters pour le message entré, la sortie, le mode, la méthode, et la clé
    def get_entree(self):
        return self._champ_entree.get("1.0", "end-1c")

    def get_sortie(self):
        return self._champ_sortie.get("1.0", "end-1c")

    def get_mode(self):
        return self._selection_mode.get()
    
    def get_methode(self):
        return self._selection_methode.get()

    def get_cle(self):
        return self._v_cle.get()

    def effacer_sortie(self):
        """
            fonction qui efface le champ de sortie
        """
        self._champ_sortie.configure(state="normal")
        self._champ_sortie.delete("1.0", "end-1c")
        self._champ_sortie.configure(state="disabled")


    def afficher_sortie(self, message):
        """
            Fonction qui affiche le message à la sortie
        """
        self._champ_sortie.configure(state="normal")
        self._champ_sortie.insert("1.0", message)
        self._champ_sortie.configure(state="disabled")

 
    def afficher_alerte(self, alerte):
        """
            Fonction qui affiche une alterte avec un message de texte donné
        """
        messagebox.showerror("Erreur", alerte)
    
