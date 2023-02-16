from case import Case

class Plateau():
    
    
    def __init__(self,taille_plateau):
        self.plateau = [[Case(y,x) for x in range(taille_plateau[0])] for y in range(taille_plateau[1])]
        self.pos_autour = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
        self.Bombe_autour()


    def chg_drapeau_case(self,coo_case):
        """Changement drapeau de case"""
        self.plateau[coo_case[0]][coo_case[1]].ChgDrapeau()
    
    def Bombe_autour(self):
        """ donne le nbre de bombe autour de la case """
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
            if self.plateau[coo[0] + coo_a_tester[0]][coo[1] + coo_a_tester[1]].is_bombe():
                print(coo[0]+ coo_a_tester[0], coo[1]+ coo_a_tester[1], "bombe", coo)
                return 1 + self.calcul_BA(coo, liste_coo_a_tester[1:])
        except IndexError:
            pass
        print(coo[0]+ coo_a_tester[0], coo[1]+ coo_a_tester[1], coo)
        return self.calcul_BA(coo, liste_coo_a_tester[1:])

                    
    def revelation_case(self, coo_case):    
        """revele la case et retourne False si la case est saine et inverse"""
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

                



            


