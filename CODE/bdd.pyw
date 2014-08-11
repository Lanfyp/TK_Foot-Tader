import sqlite3 #bibliotheque

fichierDonnees = 'bd_test.sq3' #bdd
connexion = sqlite3.connect(fichierDonnees) #connexion à bdd
tampon =connexion.cursor()#creation memoire tampon
##tampon.execute("CREATE TABLE membres (id INTEGER NOT NULL PRIMARY KEY,age INTEGER, nom TEXT, taille REAL)")#création de la table
##tampon.execute("INSERT INTO membres(age,nom,taille) VALUES(12,'Flora',1.35)")#ajout de données 
##tampon.execute("INSERT INTO membres(age,nom,taille) VALUES(10,'Perrine',1.20)")#ajout de données 
##tampon.execute("INSERT Into membres(age,nom,taille) VALUES(4,'Joan',1.05)")#ajout de données
##connexion.commit()#enregistrement du tampon dans la bdd
tampon.execute("SELECT * FROM membres")
for l in tampon:
    print(l)
    
tampon.close()#fermeture du tampon
connexion.close()#fermeture de la connexion
