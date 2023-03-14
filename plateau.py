from tkinter.tix import IMAGE
from case import Case
from fltk import cree_fenetre, mise_a_jour
import os
from skimage import io, transform

class Plateau():
    
    
    def __init__(self,taille_plateau,taille_fenetre):
        self.Supression_image()
        
        self.t_case = (taille_fenetre[0]/taille_plateau[0], taille_fenetre[1]/taille_plateau[1])
        self.Chargement_image()
        print(taille_plateau[0])
        self.plateau = [[Case((x*self.t_case[0], y*self.t_case[1]), ((x+1)*self.t_case[0], (y+1)*self.t_case[1] ),(y,x)) for x in range(taille_plateau[0])] for y in range(taille_plateau[1])]
        print(len(self.plateau))
        self.pos_autour = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
        
        self.Bombe_autour()
        

    #getters
    def get_t_case(self):
        return self.t_case
    
    
    
    #Fonctions
    
    def Supression_image(self):
        fichiers = os.listdir("images")
        for fichier in fichiers:
            if "_jeu" in fichier:
                os.remove("images/"+fichier)
    
    def Chargement_image(self):
        fichiers = os.listdir("images")
        for fichier in fichiers:
            if fichier.endswith(".png"):
                img = io.imread("images/" + fichier)
                img1 = transform.resize(img, self.t_case)
                io.imsave("images/"+fichier.split(".")[0]+"_jeu.png",img1)
                
    def chg_drapeau_case(self,coo_case):
        """Changement drapeau de case"""
        self.plateau[coo_case[0]][coo_case[1]].ChgDrapeau()
    
    def Bombe_autour(self):
        """  """
        for ligne in self.plateau:
            for case in ligne:
                if not case.is_bombe():
                    case.set_BombeAutour(self.calcul_BA(case.get_cco(), self.pos_autour))

    
    def calcul_BA(self,coo, liste_coo):
        """ calcul le nbre de bombe autour de la case """

        if len(liste_coo) == 0:# condition d'arret
            return 0
        liste_coo_a_tester = liste_coo
        coo_a_tester = liste_coo_a_tester[0]
        if coo[0] + coo_a_tester[0] >= 0 and coo[1] + coo_a_tester[1] >= 0 :
            try:
                
                if self.plateau[coo[0] + coo_a_tester[0]][coo[1] + coo_a_tester[1]].is_bombe():
                    return 1 + self.calcul_BA(coo, liste_coo_a_tester[1:])
            except IndexError:
                pass
        return self.calcul_BA(coo, liste_coo_a_tester[1:])

                    
    def revelation_case(self, coo_case):    
        """revele la case et retourne False si la case est saine et inversemzn"""  
        self.plateau[coo_case[0]][coo_case[1]].revelation()
        print(self.plateau[coo_case[0]][coo_case[1]].get_perdu(),"fefefefefefefefefefeZF")
        
    def verification_bombe(self):
        """ Verifie si il reste des bombes sans drapeau et si es bombes decouvertes"""
        nbre = 0
        for ligne in self.plateau:
            for case in ligne:
                if not case.get_perdu():
                    if case.is_bombe() and not case.get_flag():
                        nbre = 1
                else:
                    return "perdu"
        if nbre == 1:
            return True        
        return "win"
        
    def shine(self, x, y, premier_clicque, decouvertes):
        try:
            if (x,y) in decouvertes:
                    return None
            decouvertes.append((x,y))
            if self.plateau[x][y].is_bombe():
                if premier_clicque:
                    self.plateau[x][y].revelation()
                return None
            if self.plateau[x][y].get_bombe_autour() != 0:
                self.plateau[x][y].revelation()
                return None
        except IndexError:
            return None
        self.plateau[x][y].revelation()
        for i in self.pos_autour:
            if x+i[0] >= 0 and y+i[1] >= 0:
                self.shine(x+i[0], y+i[1], False, decouvertes)
    
                
        
    
    
# Terminal 


                



            


