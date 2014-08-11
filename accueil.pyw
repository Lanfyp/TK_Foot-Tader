# -*- coding:utf-8 -*-
# LANNUZEL YANNICK
# 2014
# FOOT-TRADER V0.1

from tkinter import *
from informations import *
from tkinter.messagebox import *

def accueil(pseudo,mdp):
    #fenetre
    accueil = Tk()
    accueil.configure(bg="white")
    accueil.attributes('-fullscreen', 1)
    accueil.resizable(width=NO, height=NO)
    #frame
    tete=Frame(accueil)
    tete.configure(bg="white")
    centre=Frame(accueil)
    centre.configure(bg="white")
    pied=Frame(accueil)
    pied.configure(bg="white")
    #variables
    nomCoach=pseudo
    niveau="75"
    classement="101"
###############PARCOUR LE FICHIER POUR SAVOIR SI COMPTE EXISTANT#########################
    indice=0#parcour fichier
    donnees=[]#liste pour recuperer valeur
    fichier= open("fichiers\comptes\comptes.txt", "r")#ouverture fichier  
    while indice != 2:
        donnees= fichier.readline().split(';')#decoupe la ligne ne liste (;)
        if donnees[1] == pseudo and donnees[2] == mdp:
            idJoueur= donnees[0]
            connecter=True
            break
        else:
            idJoueur=0
            connecter=False
        indice=indice+1#incremente indice
    fichier.close()#fermeture du fichier
    decoupe=donnees[2].split('\n')#permet de supprimer le retour à la ligne
    donnees[2]=decoupe[0]
#########################################################################################
###############PARCOUR LE FICHIER POUR RECUPERER DONNEES#########################
    if idJoueur!=0:
        donneesJ=[]#liste pour recuperer valeur
        with open("fichiers\clubs\c"+idJoueur+".txt", "r") as fichier:#ouverture fichier
            donneesJ= fichier.read().split("\n")
        indice=5
        while donneesJ[indice]!="":
            indice=indice+1
        indice=indice-5
        nomEquipe=donneesJ[2]
        argent=donneesJ[4]
        effectif=str(indice)
#########################################################################################
    
    if connecter:
        #disposition
        Label(tete, text="Equipe: "+nomEquipe,bg="white").pack(side="left",padx=30)
        Label(tete, text="Coach: "+pseudo.capitalize(),bg="white").pack(side="left",padx=30)
        Label(tete, text="Effectif: "+effectif,bg="white").pack(side="left",padx=30)
        Label(tete, text="Niveau: "+niveau,bg="white").pack(side="left",padx=30)
        Label(tete, text="Argent: "+argent+" €",bg="white").pack(side="left",padx=30)
        Label(tete, text="Classement Club: "+classement,bg="white").pack(side="left",padx=30)

        Button(pied, text="Infos",width=30,relief="raised",borderwidth=5, command=informations).pack(side="left",padx=30)
        Button(pied, text="Quitter",width=30,relief="raised",borderwidth=5, command=accueil.destroy).pack(side="left",padx=30)
        #affichage
        tete.pack()
        centre.pack()
        pied.pack()
        accueil.mainloop()
    else:
        accueil.destroy()
        showwarning("Probléme connection", "Votre pseudo et/ou votre mot de passe est ou sont incorrect(s)")

