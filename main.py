from plateau import Plateau
from fltk import *


#Terminal
"""def choix_case():
1    x = int(input("Veuillez ecrire la ligne de la case : "))
    y = int(input("Veuillez ecrire la colonne de la case :  "))
    return x,y

def choix_action():
    action = input("reveal, flag : ")
    return action
	

plateau = Plateau([5,5])
plateau.affichage()
bombe = False
while plateau.verification_bombe() and bombe == False:  
    x ,y = choix_case()
    print(x,y)
    action = choix_action()
    print(action)
    if action == "reveal":
        plateau.revelation_case((x,y))
        if plateau.plateau[x][y].is_bombe() and not plateau.plateau[x][y].get_flag():
            bombe = True
    if action == "flag":
        plateau.chg_drapeau_case((x,y))
    plateau.affichage()
print("lol")"""""


#Graphique      

taille_fenetre = (1280,720)
cree_fenetre(taille_fenetre[0], taille_fenetre[1])
plateau = Plateau((20,20), taille_fenetre)
bombe = True
mise_a_jour()
while bombe == True: 
    ev = donne_ev()
    tev = type_ev(ev)
    
    
    if tev == "Quitte":
        break
    if tev == "ClicDroit":
        y = int(abscisse_souris()/plateau.get_t_case()[0])
        x = int(ordonnee_souris()/plateau.get_t_case()[1])
        plateau.chg_drapeau_case((x,y))
        
    if tev == "ClicGauche":
        y = int(abscisse_souris()/plateau.get_t_case()[0])
        x= int(ordonnee_souris()/plateau.get_t_case()[1])
        plateau.shine(x, y, True, [])
        
    
    
    bombe = plateau.verification_bombe()    
    mise_a_jour()
    
print(bombe)
ferme_fenetre()


    
