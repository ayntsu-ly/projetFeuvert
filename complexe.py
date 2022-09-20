
from math import pow as puissance,sqrt as racine,atan as arctan
 
class Complexe:
    def __init__(self,a=0,b=0):
        try:
            self._a = int(a)
            self._b = int(b)
            self._c= int(c)
        except ValueError as erreurValeur:
            print("Erreur: {0}, format non conforme".format(erreurValeur))
            print("Erreur: {1}, format non".format(erreurValeur))
        else:
            if self._a == 0 and self._b == 0:
              print("ERREUR! Aucun traitement car la partie imaginaire et réelle vaut: 0")
            else:
              print(self.__str__())

    def __str__(self):
        b = self._b if self._b < 0 else "+"+str(self._b)
        return "Nombre complexe: Z= {0}{1}i\nModule: {2}\nArgument: {3}\nCoordonnée polaire: {4}\nConjuguée du nombre complexe :{5}\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n".format(self._a,b,self.module(),self.argument(),self.coordonneePolaire(),self.conjugue())


    def module(self):
        return racine(puissance(self.a,2)+puissance(self.b,2))

    def argument(self):
        return 2*arctan(self._b/(self._a+self.module()))

    def coordonneePolaire(self):
        return "[{0},{1}]".format(self.module(),self.argument())

    def conjugue(self):
        c = self._b
        c *= -1
        b = c if c < 0 else "+"+str(c)
        return "{0}{1}i".format(self._a,b)


    def __add__(self, other):
        a = self._a+other.a
        b = self._b+other.b
        nouvelleObjet = Complexe(a,b)
        return nouvelleObjet

    def __sub__(self, other):
        a = self._a-other.a
        b = self._b-other.b
        nouvelleObjet = Complexe(a, b)
        return nouvelleObjet

    def __mul__(self, other):
        a = self._a*other.a+self._b*other.b*-1
        b = self._a*other.b+self._b*other.a
        nouvelleObjet = Complexe(a, b)
        return nouvelleObjet


    def _getA(self):
        return self._a
    def _getB(self):
        return self._b

    def _setA(self,nvA):
        self._a = nvA
    def _setB(self,nvB):
        self._b = nvB

    a = property(_getA,_setA)
    b = property(_getB,_setB)
    Complexe = complex(2,2)