# -*- coding:utf-8 -*-
# LANNUZEL YANNICK
# 2014
# FOOT-TRADER V0.1

##MEMO:
#listeId[0].set(lirefichier()[0]) => Valeur defaut combobox

from tkinter import *    # GUI
from tkinter.ttk    import *    # Widgets avec thèmes
from PIL import Image, ImageTk
from Joueur import *
#fenetre
Mafenetre = Tk()
Mafenetre.title("FOOT-TRADER")
Mafenetre.geometry("1024x768")
Mafenetre.resizable(width=NO, height=NO)

j = Joueur()
a=str(3)
#PORTRAIT
portrait= Image.open('photos/'+a+'.jpg')
logoPhoto= ImageTk.PhotoImage(portrait)

photoLabel= Label(Mafenetre, image= logoPhoto).pack()
nomLabel=Label(Mafenetre, text="NOM: ").pack()
prenomLabel=Label(Mafenetre, text="PRENOM: ").pack()
dateNaissanceLabel=Label(Mafenetre, text="DATE DE NAISSANCE: ").pack()
nationaliteLabel=Label(Mafenetre, text="NATIONALITE: ").pack()
reputationLabel=Label(Mafenetre, text="REPUTATION: ").pack()
posteLabel=Label(Mafenetre, text="POSTE: ").pack()
clubLabel=Label(Mafenetre, text="CLUB: ").pack()
attaqueLabel=Label(Mafenetre, text="ATTAQUE: ").pack()
milieuLabel=Label(Mafenetre, text="MILIEU: ").pack()
defenseLabel=Label(Mafenetre, text="DEFENSE: ").pack()
gardienLabel=Label(Mafenetre, text="GARDIEN: ").pack()
Label(Mafenetre, text="RECUPERATION: ").pack()
recuperationLabel=Label(Mafenetre, textvariable=j.recuperation).pack()
formeLabel=Label(Mafenetre, text="FORME: ").pack()
contratLabel=Label(Mafenetre, text="CONTRAT: ").pack()
valeurLabel=Label(Mafenetre, text="VALEUR: ").pack()
idCarteLabel=Label(Mafenetre, text="ID_CARTE: ").pack()

#BOUTONS
BoutonValider=Button(Mafenetre, text="Valider",width="20" ,command = lambda:j.recherche(a)).pack()
BoutonQuitter=Button(Mafenetre, text="Quitter",width="20" ,command=Mafenetre.destroy).pack()

Mafenetre.mainloop()
