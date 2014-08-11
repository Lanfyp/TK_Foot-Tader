# -*- coding:utf-8 -*-
# LANNUZEL YANNICK
# 2014
# FOOT-TRADER V0.1

from tkinter import *

def informations():
    #fenetre
    info = Tk()
    info.configure(bg="white")
    info.attributes('-fullscreen', 1)
    info.resizable(width=NO, height=NO)
    #frame
    centre=Frame(info)
    centre.configure(bg="white")
    pied=Frame(info)
    #variables
    mdp=StringVar()
    pseudo=StringVar()

    #disposition


    texte="Programme: FOOT TRADE & CASH\nVersion 0.1 2014\nCréateur: Lannuzel Yannick\n\n\
    Le jeu consiste à batir la meilleur équipe possible.\n\
    Pour cela vendez et achetez les joueurs qui vous fairons progresser\n\
    Il vous faut aussi gagner un maximum d'argentpour devenir le numéro un.\nTout cela grace au football trade center."

    texte=Label(centre,text=texte,bg="white").pack(pady=100)

    Button(pied, text="Retour",width=30,relief="raised",borderwidth=5, command=info.destroy).pack()

    #affichage
    centre.pack()
    pied.pack()
    info.mainloop()
