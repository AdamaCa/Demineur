import random
from fltk import *
from PIL import Image

class Case():
    def __init__(self,X,Y,pos_tab):
        self.X = X
        self.Y = Y
        self.pos_tabx = pos_tab[0]
        self.pos_taby = pos_tab[1]
        self.case =  image(self.X[0], self.X[1], "images/case_jeu.png", hauteur = int(self.Y[1]-self.X[1]), largeur=int(self.Y[0]-self.X[0]), ancrage="nw")
        self.bombe = bool(random.random() < 0.2)
        self.perdu = False
        self.flag = False
        self.img_flag = "images/flag_jeu.png"
        self.image = ''
        self.bombe_autour = 0
        self.affiche_bombe()

    
#Test

    def affiche_bombe(self):
        if self.is_bombe():
            efface(self.case)
            self.case = image(self.X[0], self.X[1], "images/bombe_jeu.png", hauteur = int(self.Y[1]-self.X[1]), largeur=int(self.Y[0]-self.X[0]), ancrage="nw")

        
#Setters
 
    def set_BombeAutour(self, Ba):
        self.bombe_autour = Ba
        self.image = "images/{}_jeu.png".format(Ba)
        
    
#Setters de test

    
    
#Getters

    def get_perdu(self):
        return self.perdu
    
    
    def is_bombe(self):
        return self.bombe

        
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
            self.img_flag = image(self.X[0], self.X[1], "images/flag_jeu.png", hauteur = int(self.Y[1]-self.X[1]), largeur=int(self.Y[0]-self.X[0]), ancrage="nw")
        else:
            efface(self.case)
            self.case = rectangle(self.X[0], self.X[1], self.Y[0],self.Y[1], couleur="white", remplissage="green")
       

            
    def revelation(self):
        if not self.flag:
                efface(self.case)
                if self.bombe: 
                    print("fzeiojnfozfiznfoznf", self.perdu)
                    self.case = image(self.X[0], self.X[1], "images/bombe_jeu.png", hauteur = int(self.Y[1]-self.X[1]), largeur=int(self.Y[0]-self.X[0]), ancrage="nw")
                    self.perdu = True
                else:
                    self.case = image(self.X[0], self.X[1], self.image, hauteur = int(self.Y[1]-self.X[1]), largeur=int(self.Y[0]-self.X[0]), ancrage="nw")


        