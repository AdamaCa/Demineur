from case import Case
from fltk import cree_fenetre, mise_a_jour

class Plateau():
    
    
    def __init__(self,taille_plateau,taille_fenetre):
        self.t_case = (taille_fenetre[0]/taille_plateau[0], taille_fenetre[1]/taille_plateau[1])
        self.plateau = [[Case((y*self.t_case[0],x*self.t_case[1]),((y+1)*self.t_case[0],(x+1)*self.t_case[1]),(y,x)) for x in range(taille_plateau[0])] for y in range(taille_plateau[1])]
        self.pos_autour = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
        self.Bombe_autour()
        

    #getters
    def get_t_case(self):
        return self.t_case
        
    
    
    #Fonctions
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
        try:
            print(coo[0] ,coo_a_tester[0],coo[1] ,coo_a_tester[1],"errrrrrrrrrrrrrrrrrrr")
            if self.plateau[coo[0] + coo_a_tester[0]][coo[1] + coo_a_tester[1]].is_bombe():
                return 1 + self.calcul_BA(coo, liste_coo_a_tester[1:])
        except IndexError:
            pass
        print(coo[0]+ coo_a_tester[0], coo[1]+ coo_a_tester[1], coo)
        return self.calcul_BA(coo, liste_coo_a_tester[1:])

                    
    def revelation_case(self, coo_case):    
        """revele la case et retourne False si la case est saine et inversemzn"""  
        self.plateau[coo_case[0]][coo_case[1]].revelation()
        
    def verification_bombe(self):
        """ Verifie si il reste des bombes sans drapeau"""
        nbre = 0
        for ligne in self.plateau:
            for case in ligne:
                if case.is_bombe() and not case.get_flag():
                    nbre += 1
        return bool(nbre)
    
    
# Terminal 
    def affichage(self):
        for i in self.plateau:
            print([case.get_elem() for case in i ])
            
    def affichage_graphique(self):
        mise_a_jour()

                



            


