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
cree_fenetre(1280,720)
plateau = Plateau([30,30], taille_fenetre)
bombe = False
mise_a_jour()
while not bombe: 
    ev = donne_ev()
    tev = type_ev(ev)
    
    
    if tev == "Quitte":
        bombe = True
        break
    
    if tev == "ClicGauche":
        y = int(abscisse_souris()/plateau.get_t_case()[0])
        x= int(ordonnee_souris()/plateau.get_t_case()[1])
        print(y,x)
        plateau.revelation_case((y,x))
        print("wsh")
        
    mise_a_jour()
    
ferme_fenetre()


    
