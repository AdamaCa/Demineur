import random
from fltk import *

class Case():
    def __init__(self,X,Y,pos_tab):
        self.X = X
        self.Y = Y
        self.pos_tabx = pos_tab[0]
        self.pos_taby = pos_tab[1]
        self.case = image()
        self.bombe = bool(random.random() < 0.4)
        self.flag = False
        self.elem = "X"
        self.bombe_autour = 0
        self.chiffre = 0
    
    
#Setters

    def set_BombeAutour(self, Ba):
        self.bombe_autour = Ba
        
    
#Setters de test
 
    
    
#Getters
    
    def is_bombe(self):
        print(self.bombe)
        return self.bombe


    def get_elem(self):
        return self.elem
        
    def get_cco(self):
        return self.pos_tabx,self.pos_taby
      
    def get_X(self):
        return self.pos_tabx

    def get_Y(self):
        return self.pos_taby
    
    def get_bombe_autour(self):
        return self.bombe_autour
    
    def get_flag(self):
        return self.flag

        

#Fonctions
    
    def ChgDrapeau(self):
            self.flag = not self.flag
            if self.flag:
                self.elem = "flag"
            else:
                self.elem = "X"
                

            
    def revelation(self):
        if self.elem == "X":
                if self.bombe:
                    self.elem = "bombe"
                else:
                    self.elem = self.bombe_autour
                    efface(self.case)
                    self.case = rectangle(self.X[0],self.X[1],self.Y[0],self.Y[1])          
                    self.chiffre = texte(self.X[0], self.X[1] ,chaine = str(self.bombe_autour))

        