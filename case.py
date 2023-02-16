import random

class Case():
    def __init__(self,X,Y):
      self.X = X
      self.Y = Y
      self.bombe = True #bool(random.random() < 0.4)
      self.flag = False
      self.elem = "X"
      self.bombe_autour = 0
    
    
#Setters

    def set_BombeAutour(self, Ba):
        self.bombe_autour = Ba
        
    
#Setters de test

    def set_bombe(self):
        self.bombe =False
 
    
    
#Getters
    
    def is_bombe(self):
        return self.bombe


    def get_elem(self):
        return self.elem
        
    def get_cco(self):
        return self.X,self.Y
      
    def get_X(self):
        return self.X

    def get_Y(self):
        return self.Y
    
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
        if not self.flag:
            if self.bombe:
                self.elem = "bombe"
            else:
                self.elem = self.bombe_autour           

        