"""
Module Description: This module imports the 'LifoQueue' data structure from the 'queue' module
and the basic arithmetic operators (+, -, *, /) from the 'operator' module.
"""
from queue import LifoQueue
from operator import add, sub, mul, truediv



class SaisieZarhbic:
    """_summary_
    
    Classe saisie d'une expression d'un calcul zarhbic

    """
    
    def __init__(self):
        self.pileCalcul = LifoQueue()
    

    def SaisieCalcul(self):
        """_summary_
        
        Récupere une chaine dans le fichier calcul.txt, la vérifie puis la stocke dans une pile
        
        Returns:
            _type_: Boleen
        """
        try:
            with open("calcul.txt","r",encoding='UTF-8') as fichier:
                chaineCalcul = fichier.read()
                fichier.close()
        except(FileNotFoundError):
            print("fichier calcul.txt non accessible")
            return False

        return self.VerifSaisie(chaineCalcul)
    
    def VerifSaisie(self, chaineCalcul):
        """_summary_
        
        Verife la chaine récuperer en parametre et la stocke dans une list splitée

        Args:
            chaineCalcul (_type_): string

        Returns:
            _type_: Booleen
        """
        if chaineCalcul[-1] == ' ':
            chaineCalcul = chaineCalcul[:-1]
        tabTemp = chaineCalcul.split(" ")
        nbEntiers = 0
        for element in tabTemp:
            if element.isnumeric():
                nbEntiers += 1
        if (nbEntiers - (len(tabTemp) - nbEntiers)) == 1:
            return self.ConvertToPile(tabTemp)
        print("calcul non valide")
        return False
      
    def ConvertToPile(self, tabTemp):
        """_summary_

        Stock le tableau dans une pile 
        
        Args:
            tabTemp (_type_): list

        Returns:
            _type_: Booleen
        """
        
        for char in tabTemp:
            if char.isnumeric():
                self.pileCalcul.put(int(char))
            else:
                self.pileCalcul.put(char)
        return True
    
    def RemplirPileCalcul(self):
        """_summary_

        Appel de SaisieCalcul + créer un objet CalculZarhbic si la chaine est correcte
    
        Returns:
            _type_: Objet : CalculZarhbic
        """
        
        if(self.SaisieCalcul()):
            return CalculZarhbic(self.pileCalcul)
        return None
        
    
class CalculZarhbic:
    """_summary_
    
    Effectue un calcul zarhbic
    
    """
    def __init__(self,pile):
        self.pileCalcul = pile
        self.tabOperateur = {'+' : add, '-' : sub,
                             '*' : mul, '/' : truediv}
        
    def Calcul(self):
        """_summary_
        
        Lance le calcul de façon récusrsif  + affiche le resultat
        
        """
        
        result = self.CalculRecursif()
        print("Résultat du calcul:", result)

    def CalculRecursif(self):
        """_summary_

        Methode recursive qui effectue le calcul
        
        Returns:
            _type_: float
        """
        
        if self.pileCalcul.empty():
            return None
        
        value = self.pileCalcul.get()
        
        if value in self.tabOperateur:
            operateur = self.tabOperateur[value]
            chiffreDroite = self.CalculRecursif()
            chiffreGauche = self.CalculRecursif()
            
            if chiffreGauche is not None and chiffreDroite is not None:
                return operateur(chiffreGauche, chiffreDroite)
        return value
        
        
saisie = SaisieZarhbic()
calcul = saisie.RemplirPileCalcul()
calcul.Calcul()
