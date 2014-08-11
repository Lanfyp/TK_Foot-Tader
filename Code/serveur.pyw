import ftplib as ftp # on importe le module et on la renomme juste pour le script en "ftp"

host = "ftpperso.free.fr" # adresse du serveur FTP
user = "lanfyp" # votre identifiant
password = "france72" # votre mot de passe
connect = (ftp.FTP(host,user,password)) # on se connecte

# Connexion
print ("Connexion a " +host)
etat = connect.getwelcome()
print ("Etat : ",etat)

 
# Ouverture Fichier
fichier="C:/Users/Spycom/Documents/PROG/Python/Fichiers/TK_Foot Tader/fichiers/joueurs/joueurs.txt"
file = open(fichier,'rb')
 
# Envoi Fichier
connect.storbinary('STOR '+'/Python/FootTrader/joueurs/joueurs.txt', file)
connect.retrlines('LIST')

file.close() # on ferme le fichier
connect.quit() #on se deconnecte
