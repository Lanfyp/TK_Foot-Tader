class Joueur:
    """Classe définissant une personne caractérisée par :
       nom
       prenom
       dateNaissance
       nationalite
       reputation
       poste
       club
       attaque
       milieu
       defense
       gardien
       recuperation
       forme
       contrat
       valeur
       idCarte"""

    
    def __init__(self):
        """Constructeur de notre classe"""
        self.nomPrenom = ""
        self.prenom = ""
        self.dateNaissance = ""
        self.nationalite = ""
        self.reputation = ""
        self.poste = ""
        self.club = ""
        self.attaque = ""
        self.milieu = ""
        self.defense = ""
        self.gardien = ""
        self.recuperation = ""
        self.forme = ""
        self.contrat = ""
        self.valeur = ""
        self.idCarte = ""

    def recherche(self,idSearch):
        """Lit un fichier et retourne son contenu dans une liste"""
        indice=0#parcour fichier
        donnees=[]#liste pour recuperer valeur
        fichier= open("fichiers\joueurs\joueurs.txt", "r")#ouverture fichier
        while indice != int(idSearch):
            donnees= fichier.readline().split(';')#decoupe la ligne ne liste (;)
            indice=indice+1#incremente indice
        fichier.close()#fermeture du fichier
        decoupe=donnees[15].split('\n')#permet de supprimer le retour à la ligne
        donnees[15]=decoupe[0]
        # affectation des valeurs
        self.idCarte = donnees[0]
        self.nom = donnees[1]
        self.prenom = donnees[2]
        self.dateNaissance = donnees[3]
        self.nationalite = donnees[4]
        self.reputation = donnees[5]
        self.poste = donnees[6]
        self.club = donnees[7]
        self.attaque = donnees[8]
        self.milieu = donnees[9]
        self.defense = donnees[10]
        self.gardien = donnees[11]
        self.recuperation = donnees[12]
        self.forme = donnees[13]
        self.contrat = donnees[14]
        self.valeur = donnees[15]
        

