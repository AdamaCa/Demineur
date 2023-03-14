import os




fichiers = os.listdir("images")
for fichier in fichiers:
    if "_jeu" in fichier:
        os.remove("images/"+fichier)