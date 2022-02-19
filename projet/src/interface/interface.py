# importation du module externe Tkinter qui nous aide à contruire une interface graphique
from tkinter import Tk, Label, Button, StringVar, Radiobutton, TOP, OptionMenu

class Interface:
    """
        Classe qui définit les paramètres et la fonctionnalité de l'interface
    """
    def __init__(self, fenetre):
        # initialisation de la fenêtre
        self.fenetre = fenetre
        self.fenetre.title("Cryptage")

        # crée le message conteant les instructions
        self.mesage_instructions = Label(fenetre, width=50, height=2, font=("Helvetica", 12), background="#f0f0ed", text="Choisissez la méthode, le mode et le jeu de caractères")

        # place le text à un endroit précis de la fenêtre avec la méthode grid()
        self.mesage_instructions.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        v = StringVar(fenetre_principale, "1")

        # dicionaire comprenant le texte et le numéro des boutons à générer
        boutons = {
            "Encoder": "1",
            "Décoder": "2"
        }

        # boucle créant les boutons indiqués dans le dictionnaire
        ligne = 1
        for (texte, valeur) in boutons.items():
            Radiobutton(fenetre_principale, text = texte, variable = v, value = valeur).grid(row = ligne, column=0, columnspan=4, padx=10, pady=10)
            ligne += 1

        # variable qui va contenir la méthode de codage selectionnée
        options = StringVar(fenetre_principale)

        methodes = ("ROT13", "CODE DE CÉSAR", "CODE DE VIGNÈRE", "CARRÉ DE POLYBE")
        liste_de_methodes = OptionMenu(fenetre_principale, options, *methodes)
        
        # affiche l'outil de sélection de la méthode de codage
        liste_de_methodes.grid(row = 3, column=0, columnspan=4, padx=10, pady=10)




# création d'un objet tk et de l'interface (objet)
fenetre_principale = Tk()
logiciel = Interface(fenetre_principale)

# le script entre dans une boucle infine en attendant que des évènement se produisent
fenetre_principale.mainloop()