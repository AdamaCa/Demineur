from plateau import Plateau

def choix_case():
    x = int(input("Veuillez ecrire la ligne de la case : "))
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
print("lol")

    



    
