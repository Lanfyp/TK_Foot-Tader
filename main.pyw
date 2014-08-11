# -*- coding:utf-8 -*-
# LANNUZEL YANNICK
# 2014
# FOOT-TRADER V0.1

from tkinter import *
from accueil import *
from informations import *
from PIL import Image, ImageTk


 
#fenetre
root = Tk()
root.configure(bg="white")
root.attributes('-fullscreen', 1)
root.resizable(width=NO, height=NO)
#frame
tete=Frame(root)
tete.configure(bg="white")
centre=Frame(root)
centre.configure(bg="white")
pied=Frame(root)
pied.configure(bg="white")
#variables
mdp=StringVar()
pseudo=StringVar()
#photo
imageLogo= Image.open('photos/logo.jpg')
logo= ImageTk.PhotoImage(imageLogo)
#disposition
Label(tete, text="PSEUDO: ",bg="white").pack(side="left")
Entry(tete,textvariable=pseudo,width=25).pack(side="left",padx=30)
Label(tete, text="MOT DE PASSE: ",bg="white").pack(side="left",padx=30)
Entry(tete,textvariable=mdp,width=25,show="*").pack(side="left",padx=30)
Button(tete, text="Valider",width=25,relief="raised",borderwidth=5, command= lambda : accueil(pseudo.get(),mdp.get())).pack(side="left",padx=30)
Button(tete, text="Créer un compte",width=25,relief="raised",borderwidth=5, command="").pack(side="left")

photoLogo= Label(centre, image= logo).pack(pady=100)

Button(pied, text="Infos",width=30,relief="raised",borderwidth=5, command=informations).pack(side="left",padx=30)
Button(pied, text="Quitter",width=30,relief="raised",borderwidth=5, command=root.destroy).pack(side="left",padx=30)

#affichage
tete.pack()
centre.pack()
pied.pack()
root.mainloop()

